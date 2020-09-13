import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')

print(results.prettify())

job_elems = results.find_all('section', class_='card-content')

print('Printing job elem')
for job_elem in job_elems:
    print(job_elem, end='\n'*2)

