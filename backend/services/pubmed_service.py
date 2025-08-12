# PubMed research service using Entrez E-utilities API (NCBI)
import requests

def search_pubmed(term: str):
    # Refined: Use real API and handle errors gracefully
    try:
        url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={term}&retmax=5&retmode=json"
        resp = requests.get(url)
        resp.raise_for_status()
        ids = resp.json().get('esearchresult', {}).get('idlist', [])
        links = [f"https://pubmed.ncbi.nlm.nih.gov/{id}/" for id in ids]
        return links
    except Exception as e:
        return [f"Error fetching PubMed results: {e}"]
