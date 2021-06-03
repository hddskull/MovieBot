import time
import selenium
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup

# хромдрайвер для винды
# chromedriver = 'chromedriver.exe'

# хромдрайвер для убунты
chromedriver = '/usr/bin/chromedriver'

options = webdriver.ChromeOptions()
# закомментить строку ниже чтоб отображала графически браузер
options.add_argument('headless')
browser = webdriver.Chrome(executable_path=chromedriver, options=options)


def findCinemaByMetro(metroName):
    varToBot = ""
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
        varToBot += "На данной станции нет ближайших кинотеатров"
        return varToBot

    time.sleep(1)
    # -----------------------------------------------------------
    # получаем массив дивов с кинотеатрами, которые нужно запарсить
    divOfCinemas = browser.find_element_by_id("widget-content")
    Infos = divOfCinemas.find_elements_by_xpath('.//div[@data-test="ITEM"]')

    for div in Infos:
        lefty = div.find_element_by_xpath('.//div[@class="new-list__item-info"]')
        righty = div.find_element_by_xpath('.//div[@class="new-list__item-content"]')
        # print("lefty", lefty.text)
        # print("righty:", righty.text)

        name = lefty.find_element_by_xpath('.//h3').text
        # print("Название: ", name)
        varToBot += "Название: "
        varToBot += name
        varToBot += "\n"

        try:
            rating = lefty.find_element_by_xpath('.//div[@class="rating-static"]').text
            print("Рейтинг: ", rating)
            varToBot += "Рейтинг: "
            varToBot += rating
            varToBot += "\n"

        except:
            print("Рейтинга нет")
            varToBot.join("Рейтинга нет", "\n")
        address = righty.find_element_by_xpath('.//div[@class="new-list__item-record-value"]').text
        # print("Адрес: ", address)
        varToBot += "Адрес: "
        varToBot += address
        varToBot += "\n"


        # print("----------------")
        varToBot += "----------------"
        varToBot += "\n"
    browser.quit()
    return varToBot

# Возвращает переменную varToBot, которую нужно выводить в боте

# metroName = 'Шипиловская'
# print(findCinemaByMetro(metroName))
# browser.quit()