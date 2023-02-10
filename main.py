from pprint import pprint
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import json

def get_headers():
    headers = Headers(browser='firefox', os='win')
    return headers.generate()

#HOST = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
HOST = 'https://spb.hh.ru/search/vacancy?area=1&area=2&search_field=description&only_with_salary=true&text=Python+django+flask&from=suggest_post&ored_clusters=true&enable_snippets=true'


if __name__ == '__main__':

    response = requests.get(HOST, headers=get_headers())
    hh_main = response.text
    print(response)
    soup = BeautifulSoup(hh_main, features='lxml')

    vacancy_list = soup.find_all(attrs={'data-qa': "vacancy-serp__results"})

    link = soup.findAll('a',{'class': 'serp-item__title', 'data-qa': 'serp-item__title', 'target': '_blank'})
    # for l in link:
    #     pprint(l.attrs['href'])

    company = soup.findAll('a', {'data-qa': "vacancy-serp__vacancy-employer"})
    # for c in company:
    #     pprint(c.text)

    adress = soup.find_all(attrs={'class': "bloko-text", 'data-qa': "vacancy-serp__vacancy-address"})
    # for a in adress:
    #     pprint(a.text)

    salary = soup.find_all(attrs={'data-qa':"vacancy-serp__vacancy-compensation"})
    # for s in salary:
    #     pprint(s.text)

    finish_list = list()
    for (l,a,s,c) in zip(link, adress, salary, company):
        finish_list.append(
            {
                'link' : l['href'],
                'adress' : a.text,
                'sallary': s.text,
                'company' : c.text
            }
        )
    pprint(finish_list)

    with open("data.json", 'w', encoding='utf-8') as file:
        json.dump(finish_list, file, ensure_ascii=False, indent=3)











    # link = soup.find_all(class_="serp-item__title")
    # city = soup.find_all(attrs={'class': "bloko-text", 'data-qa': "vacancy-serp__vacancy-address"})
    # salary = soup.find_all(attrs={'data-qa': "vacancy-serp__vacancy-compensation"})
    # company = soup.find_all(attrs={'data-qa': "vacancy-serp__vacancy-employer"})

    #pprint(link)