from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# хромдрайвер для винды
# chromedriver = 'chromedriver.exe'

# хромдрайвер для убунты
chromedriver = '/usr/bin/chromedriver'
options = webdriver.ChromeOptions()
# закомментить строку ниже чтоб отображала графически браузер
options.add_argument('headless')
browser = webdriver.Chrome(executable_path=chromedriver, options=options)


def findMoviePage(moviename):
    varToBot = ""
    errorText = "Такой фильм не найден"
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
        # print("here")
        movieList = browser.find_elements_by_xpath('.//div[@data-test="LIST"]')
        linksToMoviePage = browser.find_elements_by_class_name('new-list__item-link')
        for link in linksToMoviePage:
            if link.text.lower() == moviename.lower():
                linkToMoviePage = link.get_attribute('href')
    else:
        return errorText
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
    varToBot = ""
    for li in movieschedule:
        movieTheatreSc = li.text.split("\n")

        if len(movieTheatreSc) > 2:
            for text in movieTheatreSc:
                # print(text)
                varToBot += text
                varToBot += "\n"
            # print("----------")
            varToBot += "----------\n"
    return varToBot


def findMovie(moviename):
    mc = findMoviePage(moviename)
    varToBot = showSchedule(mc)
    # print(varToBot)
    browser.quit()
    return varToBot

# findMovie("Отец")
