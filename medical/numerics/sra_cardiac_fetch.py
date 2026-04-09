#!/usr/bin/env python3
"""
Fetch SRA run accessions for CVB3 cardiac RNA-seq experiments.
Uses efetch with proper XML parsing.
"""

import json
import time
import xml.etree.ElementTree as ET
from Bio import Entrez

Entrez.email = 'noreply@example.com'
Entrez.tool  = 'sra_cardiac_cvb3_fetch'

def search_sra(query, retmax=100):
    time.sleep(0.4)
    handle = Entrez.esearch(db='sra', term=query, retmax=retmax)
    rec    = Entrez.read(handle)
    handle.close()
    return rec

def efetch_sra_xml(uid_list):
    time.sleep(0.4)
    handle = Entrez.efetch(db='sra', id=','.join(uid_list), rettype='full', retmode='xml')
    raw    = handle.read()
    handle.close()
    return raw

def parse_sra_xml(xml_bytes):
    runs = []
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return runs

    for pkg in root.iter('EXPERIMENT_PACKAGE'):
        exp   = pkg.find('.//EXPERIMENT')
        study = pkg.find('.//STUDY')
        smp   = pkg.find('.//SAMPLE')

        exp_acc   = exp.get('accession', '') if exp is not None else ''
        exp_title = ''
        if exp is not None:
            t = exp.find('.//TITLE')
            if t is not None:
                exp_title = t.text or ''

        study_acc = ''
        study_title = ''
        if study is not None:
            study_acc = study.get('accession', '')
            t = study.find('.//TITLE')
            if t is not None:
                study_title = t.text or ''

        organism = ''
        if smp is not None:
            o = smp.find('.//SCIENTIFIC_NAME')
            if o is not None:
                organism = o.text or ''

        for run_set in pkg.iter('RUN_SET'):
            for run in run_set.iter('RUN'):
                run_acc    = run.get('accession', '')
                spots      = run.get('total_spots', '')
                bases      = run.get('total_bases', '')
                size       = run.get('size', '')
                published  = run.get('published', '')
                runs.append({
                    'run_accession':    run_acc,
                    'experiment':       exp_acc,
                    'experiment_title': exp_title,
                    'study':            study_acc,
                    'study_title':      study_title,
                    'organism':         organism,
                    'spots':            spots,
                    'bases':            bases,
                    'size_bytes':       size,
                    'published':        published,
                })
    return runs

# ── Main searches ─────────────────────────────────────────────────────────────

queries = [
    '"coxsackievirus B3" AND "heart" AND "RNA-Seq"',
    '"coxsackievirus B3" AND "myocarditis"',
    '"coxsackievirus" AND "myocarditis" AND "RNA-Seq"',
    '"coxsackievirus" AND "cardiomyopathy" AND "RNA-Seq"',
    '"viral myocarditis" AND "RNA-Seq"',
]

all_runs = []
seen_runs = set()
query_summary = []

for q in queries:
    print(f'\n=== SRA: {q} ===')
    result = search_sra(q, retmax=200)
    ids    = result.get('IdList', [])
    count  = int(result.get('Count', 0))
    print(f'  Count={count}  IDs={len(ids)}')

    if ids:
        xml_data = efetch_sra_xml(ids)
        runs     = parse_sra_xml(xml_data)
        new_runs = []
        for r in runs:
            if r['run_accession'] and r['run_accession'] not in seen_runs:
                seen_runs.add(r['run_accession'])
                all_runs.append(r)
                new_runs.append(r)
                print(f'  {r["run_accession"]:12s}  {r["organism"]:20s}  {r["experiment_title"][:60]}')

        query_summary.append({
            'query':       q,
            'total_count': count,
            'retrieved':   len(ids),
            'new_runs':    len(new_runs),
        })
    else:
        query_summary.append({'query': q, 'total_count': count, 'retrieved': 0, 'new_runs': 0})

print(f'\n\nTotal unique SRA runs: {len(all_runs)}')

output = {
    'query_summary': query_summary,
    'total_unique_runs': len(all_runs),
    'runs': all_runs,
}

out_path = '/home/jb/medical_problems/results/sra_cardiac_cvb_runs.json'
with open(out_path, 'w') as f:
    json.dump(output, f, indent=2)
print(f'Saved → {out_path}')
