from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

chromedriver = '/usr/bin/chromedriver'
options = webdriver.ChromeOptions()
# options.add_argument('headless')
browser = webdriver.Chrome(executable_path=chromedriver, options=options)


def findMoviePage(moviename):
    browser.get("https://www.afisha.ru/msk/schedule_cinema/")
    # нашли кнопку с лупой и кликнули
    searchButton = browser.find_element_by_class_name("menu-item-link")
    searchButton.click()
    # берем поле ввода, вводим в него и имметируем нажатие энтер
    searchInput = browser.find_element_by_class_name("search__input")
    searchInput.send_keys(moviename)
    searchInput.send_keys(Keys.ENTER)
    # проверяем что h3 == фильмы, потом берем первый элемент и на нем кликаем кнопку раписания
    title = browser.find_element_by_class_name("page-search__results-section-title")
    if title.text == "Фильмы":
        movieList = browser.find_element_by_class_name("new-list__item-ticket")
        linkToMoviePage = movieList.find_elements_by_xpath(".//a")[0].get_attribute('href')
    else:
        print("Movie not found")
    # Получив ссылку переходим на страницу фильма
    # открываем новую вкладку и переключаемся на неё
    browser.execute_script("window.open();")
    browser.switch_to.window(browser.window_handles[1])
    browser.get(linkToMoviePage)
    # берем элемент страницы в котором у нас расписание
    mainDiv = browser.find_element_by_id("widget-content")
    movieSchedule = mainDiv.find_elements_by_xpath(".//li")
    return movieSchedule


def showSchedule(movieschedule):
    for li in movieschedule:
        movieTheatreSc = li.text.split("\n")

        if len(movieTheatreSc) > 2:
            for text in movieTheatreSc:
                print(text)
            print("-------------------")

            # Попытки красивого вывода
            # # если у кинотеатра нет рейтинга то проверяем 4 элемент
            # if ":" in movieTheatreSc[2]:
            #     countNoRate += 1
            #     if "от" in movieTheatreSc[3]:
            # # если у кинотеатра есть рейтинг то проверяем 5 элемент
            # else:
            #     countWRate += 1


def findMovie(moviename):
    mc = findMoviePage(moviename)
    showSchedule(mc)


#findMovie("батя")