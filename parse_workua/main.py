from pdb import set_trace
from bs4 import BeautifulSoup
from random import randint
import requests

ROOT_URL = 'https://www.work.ua/ru/jobs/'

def random_sleep():
    sleep(random.randint(2 ,4))
page = 0
with open ('./workua.txt', 'w') as the_file:
    # while True:
    while page != 4:
        page += 1
        response = requests.get(ROOT_URL, params={'page': page})
        random_sleep()
        assert response.status_code == 200
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        job_list = soup.find('div', {'id': 'pjax-job-list'})

        if job_list is None:
            break

        cards = job_list.findAll('div', {'class': 'card-hover'})
        for card in cards:
            a = card.find_all('a', href=True)[0]
            href = a['href']
            id_ = href.split('/')[-2]
            title = a['title']
            card_result = {
                'href': href,
                'id': id_,
                'title': title,
            }

        the_file.write(f'id:{id_};href:{href};title:{title}\n')

