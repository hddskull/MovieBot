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
# options.add_argument('headless')
browser = webdriver.Chrome(executable_path=chromedriver, options=options)


def findCinemaByName(CinemaName):
    varToBot = ""
    errorText = "Такой кинотеатр не найден"
    CinemaName.lower()
    url = "https://www.afisha.ru/search/?query="
    url += CinemaName
    browser.get(url)
    # нашли кнопку с лупой и кликнули
    # searchButton = browser.find_element_by_class_name('.//div[@class="ui-button"]')
    # searchButton.click()
    # searchInput = browser.find_element_by_class_name("page-search__form-input")
    # searchInput.send_keys(CinemaName)
    # searchInput.send_keys(Keys.ENTER)
    sections = browser.find_element_by_xpath('.//ul[@class="page-search__results"]')
    section = sections.find_element_by_xpath('.//h3').text
    if section != "Кинотеатры":
        return errorText

    movieUrl = sections.find_element_by_tag_name("a").get_attribute("href")
    # print(movieUrl)

    # открываем новую вкладку и переключаемся на неё
    browser.execute_script("window.open();")
    browser.switch_to.window(browser.window_handles[1])
    # и переходим по ссылке
    browser.get(movieUrl)

    listOfMovies = browser.find_elements_by_class_name("_1aOCt")

    for li in listOfMovies:
        movieData = li.find_element_by_class_name("_1WdLJ")

        name = movieData.find_element_by_xpath('.//h3').text
        # print(name)
        varToBot += "Название: "
        varToBot += name
        varToBot += "\n"

        genre = movieData.find_element_by_xpath('.//a[@class="LfTHA"]').text
        # print(genre)
        varToBot += "Жанр: "
        varToBot += genre
        varToBot += "\n"

        desription = movieData.find_element_by_xpath('.//div[@class="tWnyM"]').text
        # print(desription)
        varToBot += "Описание: "
        varToBot += desription
        varToBot += "\n"

        movieTimes = li.find_element_by_xpath('.//ul[@class="MRsbh"]')
        times = movieTimes.find_elements_by_xpath('.//li')

        varToBot += "Сеансы: \n "
        for el in times:
            # print(el.text)
            varToBot += el.text
            varToBot += "\n"

        varToBot += "------------\n"
    browser.quit()
    return varToBot
    # print(varToBot)



# Возвращает переменную varToBot, которую нужно выводить в боте

CinemaName = 'Балтика'
print(findCinemaByName(CinemaName))

