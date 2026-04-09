#!/usr/bin/env python3
"""
GEO + SRA search for cardiac CVB datasets.
Searches the four required queries and downloads expression data.
"""

import json
import os
import time
import gzip
import shutil
import urllib.request
from Bio import Entrez

Entrez.email = 'noreply@example.com'
Entrez.tool  = 'cardiac_cvb_search'

TRANSCRIPTOMICS_DIR = '/home/jb/medical_problems/numerics/transcriptomics'
os.makedirs(TRANSCRIPTOMICS_DIR, exist_ok=True)

# ── helpers ──────────────────────────────────────────────────────────────────

def search_geo(query, db='gds', retmax=50):
    time.sleep(0.4)
    handle = Entrez.esearch(db=db, term=query, retmax=retmax)
    rec    = Entrez.read(handle)
    handle.close()
    return rec

def fetch_gds_summary(uid_list):
    if not uid_list:
        return []
    time.sleep(0.4)
    handle = Entrez.esummary(db='gds', id=','.join(uid_list))
    records = Entrez.read(handle)
    handle.close()
    return records

def fetch_sra_summary(uid_list):
    if not uid_list:
        return []
    time.sleep(0.4)
    handle = Entrez.esummary(db='sra', id=','.join(uid_list))
    records = Entrez.read(handle)
    handle.close()
    return records

def parse_gds_record(rec):
    acc  = rec.get('Accession', '')
    title = rec.get('title', rec.get('Title', ''))
    gtype = rec.get('gdsType', rec.get('Type', ''))
    n_samples = int(rec.get('n_samples', rec.get('Samples', 0)))
    organism  = rec.get('taxon', rec.get('Organism', ''))
    return dict(accession=acc, title=title, type=gtype,
                samples=n_samples, organism=organism)

def build_geo_soft_url(accession):
    """Return FTP URL for a GEO dataset's series matrix file."""
    # GSE accessions
    if accession.startswith('GSE'):
        stub = accession[:-3] + 'nnn'
        return (
            f'https://ftp.ncbi.nlm.nih.gov/geo/series/{stub}/{accession}'
            f'/matrix/{accession}_series_matrix.txt.gz'
        )
    return None

def download_file(url, dest_path):
    """Download url → dest_path; return True on success."""
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=120) as resp, \
             open(dest_path, 'wb') as out:
            shutil.copyfileobj(resp, out)
        return True
    except Exception as e:
        print(f'  Download failed: {e}')
        if os.path.exists(dest_path):
            os.remove(dest_path)
        return False

def try_download_geo_matrix(accession):
    """Try to download series_matrix for a GSE accession."""
    dest_gz   = os.path.join(TRANSCRIPTOMICS_DIR, f'{accession}_series_matrix.txt.gz')
    dest_txt  = os.path.join(TRANSCRIPTOMICS_DIR, f'{accession}_series_matrix.txt')

    if os.path.exists(dest_txt):
        print(f'  Already have {accession}_series_matrix.txt')
        return dest_txt

    url = build_geo_soft_url(accession)
    if not url:
        return None
    print(f'  Downloading {accession} from {url}')
    if download_file(url, dest_gz):
        # decompress
        with gzip.open(dest_gz, 'rb') as f_in, open(dest_txt, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
        print(f'  Saved → {dest_txt} ({os.path.getsize(dest_txt)//1024} KB)')
        return dest_txt
    return None

# ── GEO searches ─────────────────────────────────────────────────────────────

CARDIAC_GEO_QUERIES = [
    ('cvb_myocarditis',         '"coxsackievirus" AND "myocarditis"'),
    ('cvb_cardiomyopathy',      '"coxsackievirus" AND "cardiomyopathy"'),
    ('cvb_b3_heart',            '"coxsackievirus B3" AND "heart"'),
    ('viral_myocarditis_tx',    '"viral myocarditis" AND "transcriptome"'),
]

all_results = {}
seen_accessions = set()

for key, query in CARDIAC_GEO_QUERIES:
    print(f'\n=== GEO search: {query} ===')
    result = search_geo(query, db='gds', retmax=50)
    ids    = result.get('IdList', [])
    count  = int(result.get('Count', 0))
    print(f'  Total hits: {count}  |  Retrieved IDs: {len(ids)}')

    datasets = []
    if ids:
        summaries = fetch_gds_summary(ids)
        for rec in summaries:
            parsed = parse_gds_record(rec)
            datasets.append(parsed)
            print(f'  {parsed["accession"]:15s}  {parsed["samples"]:4d} samples  {parsed["title"][:80]}')

    all_results[key] = {
        'query': query,
        'total_count': count,
        'retrieved': len(ids),
        'datasets': datasets
    }

# ── also search db=gse directly for cardiac-specific terms ───────────────────

EXTRA_GEO_QUERIES = [
    ('dcm_viral_expression',    '"dilated cardiomyopathy" AND ("virus" OR "viral") AND "expression"'),
    ('pericarditis_expression',  '"pericarditis" AND "expression"'),
    ('cvb3_cardiomyocyte',      '"coxsackievirus B3" AND ("cardiomyocyte" OR "cardiac")'),
]

for key, query in EXTRA_GEO_QUERIES:
    print(f'\n=== GEO search (GSE): {query} ===')
    result = search_geo(query, db='gds', retmax=50)
    ids    = result.get('IdList', [])
    count  = int(result.get('Count', 0))
    print(f'  Total hits: {count}  |  Retrieved IDs: {len(ids)}')

    datasets = []
    if ids:
        summaries = fetch_gds_summary(ids)
        for rec in summaries:
            parsed = parse_gds_record(rec)
            datasets.append(parsed)
            print(f'  {parsed["accession"]:15s}  {parsed["samples"]:4d} samples  {parsed["title"][:80]}')

    all_results[key] = {
        'query': query,
        'total_count': count,
        'retrieved': len(ids),
        'datasets': datasets
    }

# ── collect unique cardiac-relevant accessions for download ──────────────────

CARDIAC_KEYWORDS = {
    'myocarditis', 'cardiomyopathy', 'cardiac', 'heart',
    'cardiomyocyte', 'pericarditis', 'DCM', 'ventricular',
}

downloadable = []
for key, data in all_results.items():
    for ds in data['datasets']:
        acc = ds['accession']
        if not acc.startswith('GSE'):
            continue
        if acc in seen_accessions:
            continue
        title_lower = ds['title'].lower()
        if any(kw.lower() in title_lower for kw in CARDIAC_KEYWORDS):
            seen_accessions.add(acc)
            downloadable.append(ds)
            continue
        # also include datasets from CVB queries regardless of title
        if key in ('cvb_myocarditis', 'cvb_cardiomyopathy',
                   'cvb_b3_heart', 'viral_myocarditis_tx', 'cvb3_cardiomyocyte'):
            seen_accessions.add(acc)
            downloadable.append(ds)

print(f'\n\n=== Cardiac-relevant GSE datasets to attempt download: {len(downloadable)} ===')
for ds in downloadable:
    print(f'  {ds["accession"]}  {ds["title"][:80]}')

# ── SRA search ────────────────────────────────────────────────────────────────

SRA_QUERY = '"coxsackievirus B3" AND "heart" AND "RNA-Seq"'
print(f'\n\n=== SRA search: {SRA_QUERY} ===')
sra_result = search_geo(SRA_QUERY, db='sra', retmax=100)
sra_ids    = sra_result.get('IdList', [])
sra_count  = int(sra_result.get('Count', 0))
print(f'  Total SRA hits: {sra_count}  |  Retrieved: {len(sra_ids)}')

sra_runs = []
if sra_ids:
    sra_summaries = fetch_sra_summary(sra_ids)
    for rec in sra_summaries:
        uid   = rec.get('Id', '')
        title = rec.get('Title', '')
        expxml = rec.get('ExpXml', '')
        runs_xml = rec.get('Runs', '')
        # Parse run accessions from XML snippet
        import re
        run_accs = re.findall(r'acc="(SRR\d+)"', str(runs_xml))
        exp_accs = re.findall(r'acc="(SRX\d+)"', str(expxml))
        sra_entry = {
            'uid': uid,
            'title': title,
            'experiment': exp_accs,
            'runs': run_accs,
        }
        sra_runs.append(sra_entry)
        print(f'  UID={uid}  runs={run_accs}  {title[:80]}')

# broader SRA search
SRA_QUERY2 = '"coxsackievirus" AND "myocarditis" AND "RNA-Seq"'
print(f'\n=== SRA search: {SRA_QUERY2} ===')
sra2 = search_geo(SRA_QUERY2, db='sra', retmax=100)
sra2_ids = sra2.get('IdList', [])
print(f'  Total hits: {sra2.get("Count",0)}  |  Retrieved: {len(sra2_ids)}')
if sra2_ids:
    s2 = fetch_sra_summary(sra2_ids)
    for rec in s2:
        import re
        runs_xml = rec.get('Runs', '')
        run_accs = re.findall(r'acc="(SRR\d+)"', str(runs_xml))
        sra_entry = {
            'uid': rec.get('Id',''),
            'title': rec.get('Title',''),
            'runs': run_accs,
        }
        if rec.get('Id','') not in [x['uid'] for x in sra_runs]:
            sra_runs.append(sra_entry)
            print(f'  {run_accs}  {rec.get("Title","")[:80]}')

# ── Download matrix files ─────────────────────────────────────────────────────

download_log = {}
for ds in downloadable:
    acc = ds['accession']
    print(f'\nAttempting download: {acc} — {ds["title"][:60]}')
    dest = try_download_geo_matrix(acc)
    download_log[acc] = {
        'title': ds['title'],
        'downloaded': dest is not None,
        'path': dest,
    }

# ── Save results ──────────────────────────────────────────────────────────────

OUTPUT = '/home/jb/medical_problems/results/geo_cardiac_cvb_search.json'
final = {
    'geo_searches': all_results,
    'downloadable_datasets': downloadable,
    'sra_runs': sra_runs,
    'download_log': download_log,
}
with open(OUTPUT, 'w') as f:
    json.dump(final, f, indent=2)

print(f'\n\nResults saved → {OUTPUT}')
print(f'Downloads: {sum(1 for v in download_log.values() if v["downloaded"])}/{len(download_log)} succeeded')
