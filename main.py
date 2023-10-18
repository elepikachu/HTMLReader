import requests
from bs4 import BeautifulSoup
import  pyttsx3


def get_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


def parse_page(soup):
    article = soup.find_all('p')
    text = ''
    for para in article:
        text += para.get_text()
    return text


def html_reader(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    url = input("input the link to read: \n")
    print(url)
    soup = get_page(url)
    text = parse_page(soup)
    html_reader(text)