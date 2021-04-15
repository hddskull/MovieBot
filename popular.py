import time
from selenium import webdriver
from bs4 import BeautifulSoup

chromedriver = 'chromedriver.exe'
options = webdriver.ChromeOptions()
# options.add_argument('headless')
browser = webdriver.Chrome(executable_path=chromedriver, options=options)

browser.get("https://www.afisha.ru/msk/schedule_cinema/")
mainDiv = browser.find_element_by_id("widget-content")
arr = mainDiv.find_elements_by_xpath(".//li")


# print(type(arr))
# print(arr[0])
def desc_pop(x):
    x = x.text.split("\n")
    # если рейтинга нет, то длина не равна 4
    # а у всех остальных элементов индекс-1

    try:
        if len(x) == 4:
            return 'Название: {}\n' \
                   'Короткое описание: {}\n' \
                   'Рейтинг: {}\n' \
                   'Жанр: {}'.format(x[2], x[3], x[1], x[0])
        else:
            return 'Название: {}\n' \
                   'Короткое описание: {}\n' \
                   'Жанр: {}'.format(x[1], x[2], x[0])
    except:
        return 'none'


def gettt(li):
    link = li.find_elements_by_xpath(".//a")[-1].get_attribute('href')
    # print(link)

    # открываем новую вкладку и переключаемся на неё
    browser.execute_script("window.open();")
    browser.switch_to.window(browser.window_handles[1])
    # и переходим по ссылке
    browser.get(link)
    # если что-то вылетает, раскомментируй
    # time.sleep(3)
    result = []
    try:
        txt = browser.find_elements_by_xpath("//h2")[0].text.split("IMDb:")
        if len(txt) == 2:
            result.append(txt[1])
        # завершающая конструкция, закрываем вкладку и идём назад
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
    except:
        browser.close()
        browser.switch_to.window(browser.window_handles[0])

    return tuple(result)


def popular():
    for li in arr:
        result = desc_pop(li)
        imdb = gettt(li)
        if imdb:
            imdb = imdb[0]
        else:
            imdb = 'none'
        yield result, imdb
