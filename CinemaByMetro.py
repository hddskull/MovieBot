import time
import selenium
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup

# хромдрайвер для винды
# chromedriver = 'chromedriver.exe'

# хромдрайвер для убунты
chromedriver = '/usr/bin/chromedriver'

options = webdriver.ChromeOptions()
# закомментить строку ниже чтоб отображала графически браузер
# options.add_argument('headless')
browser = webdriver.Chrome(executable_path=chromedriver, options=options)


def findCinemaByMetro(metroName):
    metroName.lower()
    browser.get("https://www.afisha.ru/msk/cinema/cinema_list/")
    # нашли кнопку с лупой и кликнули
    searchButton = browser.find_element_by_xpath("//span[.='Станция метро']")
    searchButton.click()
    searchInput = browser.find_element_by_class_name("_3_S5H")
    searchInput.send_keys(metroName)
    searchInput.send_keys(Keys.ENTER)
    suggestion = browser.find_element_by_class_name("_2Q_r1")
    # Если по данной станции не будет кинотеатра то будет выведен текст
    try:
        suggestion.click()
    except WebDriverException:
        print("На данной станции нет ближайших кинотеатров")
    # получаем массив дивов с кинотеатрами, которые нужно запарсить
    divOfCinemas = browser.find_element_by_class_name("new-list list-place")


# metroName = 'ФИЛИ'
# findCinemaByMetro(metroName)
# browser.quit()
