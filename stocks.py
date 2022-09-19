'''
#pesquisar: como preencher tabelas no google sheets
#pesquisar: como rodar o script de tempos em tempos (provavelmente com timer)

'''
import requests
import pandas as pd
from bs4 import BeautifulSoup
import schedule
import time

url_list = [
'https://www.google.com/search?client=opera-gx&q=CACR11&sourceid=opera&ie=UTF-8&oe=UTF-8',
'https://www.google.com/search?client=opera-gx&q=OUJP11&sourceid=opera&ie=UTF-8&oe=UTF-8',
'https://www.google.com/search?client=opera-gx&q=PLCR11&sourceid=opera&ie=UTF-8&oe=UTF-8',
'https://www.google.com/search?client=opera-gx&q=RBHG11&sourceid=opera&ie=UTF-8&oe=UTF-8',
'https://www.google.com/search?client=opera-gx&q=IRBR3&sourceid=opera&ie=UTF-8&oe=UTF-8',
'https://www.google.com/search?client=opera-gx&q=KLBN4F&sourceid=opera&ie=UTF-8&oe=UTF-8'
 ]
price_list = []
stock_list = ['CACR11', 'OUJP11', 'PLCR11','RBHG11','IRBR3', 'KLBN4F']
date_list = []

def stock(elemento):
    html = requests.get(elemento)
    soup = BeautifulSoup(html.text, 'html.parser')
    
    date = soup.find(class_="nXE3Ob")
    date_list.append(date.text[0:20])
    
    price = soup.find(class_="BNeawe iBp4i AP7Wnd")
    price_list.append(price.text)


def job():
    for i in url_list:
        stock(i)
        if i == 'https://www.google.com/search?client=opera-gx&q=KLBN4F&sourceid=opera&ie=UTF-8&oe=UTF-8':
            information = pd.DataFrame({'Acao':stock_list, 'Preço':price_list, 'Data':date_list})
            print(information)

            result = information.to_html(classes='table table-striped')

            text_file = open("index.html", "w")
            text_file.write(result)
            text_file.close()
            
            del information
            date_list.clear()
            price_list.clear()



schedule.every(30).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)




