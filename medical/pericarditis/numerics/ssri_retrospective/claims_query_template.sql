
-- SSRI-Pericarditis Retrospective Cohort Study
-- Target: Optum Clinformatics Extended Data / IBM MarketScan
-- Analyst: [Name], [Institution]

-- Step 1: Index pericarditis encounters
WITH index_pericarditis AS (
    SELECT DISTINCT
        patid,
        MIN(clm_from_dt) AS index_date
    FROM medical_claims
    WHERE
        dx1 IN ('I30.0','I30.1','I30.8','I30.9','I31.0')
        AND clm_from_dt BETWEEN '2010-01-01' AND '2022-06-30'
    GROUP BY patid
),

-- Step 2: Exclude prior pericarditis (washout)
prior_pericarditis AS (
    SELECT DISTINCT mc.patid
    FROM medical_claims mc
    INNER JOIN index_pericarditis ip ON mc.patid = ip.patid
    WHERE
        mc.dx1 IN ('I30.0','I30.1','I30.8','I30.9','I31.0')
        AND mc.clm_from_dt BETWEEN DATEADD(day, -365, ip.index_date)
                                AND DATEADD(day, -1,   ip.index_date)
),

-- Step 3: Continuous enrollment check
enrolled AS (
    SELECT patid
    FROM enrollment
    GROUP BY patid
    HAVING MIN(enroll_start) <= DATEADD(day, -365, (SELECT MIN(index_date) FROM index_pericarditis ip2 WHERE ip2.patid = enrollment.patid))
       AND MAX(enroll_end)   >= DATEADD(month, 18, (SELECT MIN(index_date) FROM index_pericarditis ip3 WHERE ip3.patid = enrollment.patid))
),

-- Step 4: Cohort
cohort AS (
    SELECT ip.patid, ip.index_date
    FROM index_pericarditis ip
    INNER JOIN enrolled e ON ip.patid = e.patid
    WHERE ip.patid NOT IN (SELECT patid FROM prior_pericarditis)
      AND DATEDIFF(year, dob, ip.index_date) BETWEEN 18 AND 75
),

-- Step 5: Fluoxetine exposure (within 30 days of index)
fluoxetine_exposure AS (
    SELECT DISTINCT c.patid, 1 AS fluoxetine_exposed
    FROM cohort c
    INNER JOIN pharmacy_claims rx ON c.patid = rx.patid
    WHERE
        rx.ndc IN (/* fluoxetine NDC codes */ '00777310502','00093081401')
        AND rx.fill_dt BETWEEN c.index_date AND DATEADD(day, 30, c.index_date)
        AND rx.days_supply >= 30
),

-- Step 6: Confounders (colchicine, NSAIDs, steroids)
confounders AS (
    SELECT
        c.patid,
        MAX(CASE WHEN rx.ndc IN (/* colchicine */ '00603133321') THEN 1 ELSE 0 END) AS colchicine,
        MAX(CASE WHEN rx.ndc IN (/* NSAIDs */    '00591243305','00054491925') THEN 1 ELSE 0 END) AS nsaid,
        MAX(CASE WHEN rx.ndc IN (/* steroids */  '54569136200')  THEN 1 ELSE 0 END) AS steroid,
        MAX(CASE WHEN mc.dx1 LIKE 'F3%' THEN 1 ELSE 0 END) AS depression
    FROM cohort c
    LEFT JOIN pharmacy_claims rx ON c.patid = rx.patid
        AND rx.fill_dt BETWEEN DATEADD(day,-30,c.index_date) AND DATEADD(day,30,c.index_date)
    LEFT JOIN medical_claims mc ON c.patid = mc.patid
        AND mc.clm_from_dt BETWEEN DATEADD(day,-365,c.index_date) AND c.index_date
    GROUP BY c.patid
),

-- Step 7: Outcome (recurrent pericarditis within 18 months)
outcome AS (
    SELECT DISTINCT c.patid, 1 AS recurrence
    FROM cohort c
    INNER JOIN medical_claims mc ON c.patid = mc.patid
    WHERE
        mc.dx1 IN ('I30.0','I30.1','I30.8','I30.9')
        AND mc.clm_from_dt BETWEEN DATEADD(day, 28,  c.index_date)
                               AND DATEADD(month, 18, c.index_date)
)

-- Final analytic dataset
SELECT
    c.patid,
    c.index_date,
    COALESCE(fe.fluoxetine_exposed, 0) AS fluoxetine,
    COALESCE(o.recurrence, 0)          AS recurrence_18mo,
    conf.colchicine,
    conf.nsaid,
    conf.steroid,
    conf.depression
FROM cohort c
LEFT JOIN fluoxetine_exposure fe ON c.patid = fe.patid
LEFT JOIN confounders conf       ON c.patid = conf.patid
LEFT JOIN outcome o              ON c.patid = o.patid
ORDER BY c.patid;
