import threading
import time
import requests


def download_page(url):
    response = requests.get(url)
    print(f'Requête à {url}, code statut={response.status_code}')
    #time.sleep(5)


t = threading.Thread(target=download_page, args={'https://makina-corpus.com/'})
t.start() # démarrage thread
time.sleep(2) # mise en attente n s
t.join() # attente fin du thread
