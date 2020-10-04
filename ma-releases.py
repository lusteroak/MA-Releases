import re
import requests

#Header for MetalArchives, without this don't work
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

# Crawleable URL from MetalArchives
url = 'https://www.metal-archives.com/band/discography/id/3540384034/tab/all'

def scrapper():
    r = requests.get(url, headers=headers)
    findi = r.text
    #Enter a year which an Artist releases something
    year = input('Enter a year: \n')
    #Regex matching 'year'
    findYear = re.compile(r'\b' + year + r'\b')
    mo = findYear.findall(findi)
    #print the quantity of releases in 'year'
    print(f"Buckethead Releases: {len(mo)} records in {year}")

scrapper()


