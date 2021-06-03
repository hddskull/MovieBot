import time
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


browser.get("https://www.afisha.ru/msk/schedule_cinema/")
mainDiv = browser.find_element_by_id("widget-content")
arr = mainDiv.find_elements_by_xpath(".//li")
# print(type(arr))
# print(arr[0])

def show_desc_pop(x):
    x = x.text.split("\n")
    varToBot = ""
    # если рейтинга нет, то длина не равна 4
    # а у всех остальных элементов индекс-1
    if (len(x) == 4):
        # print("название:          ", x[2])
        # print("короткое описание: ", x[3])
        # print("рейтинг:           ", x[1])
        # print("жанр:              ", x[0])

        varToBot += "название:          " + x[2]
        varToBot += "\nкороткое описание: " + x[3]
        varToBot += "\nрейтинг:           " + x[1]
        varToBot += "\nжанр:              " + x[0]


    elif(len(x) == 3):
        # print("название:          ", x[1])
        # print("короткое описание: ", x[2])
        # print("жанр:              ", x[0])

        varToBot += "название:          " + x[1]
        varToBot += "\nкороткое описание: " + x[2]
        varToBot += "\nжанр:              " + x[0]
    elif(len(x) == 2):
        # print("название:          ", x[1])
        # print("жанр:              ", x[0])

        varToBot += "название:          " + x[1]
        varToBot += "\nжанр:              "+ x[0]
    else:
        print("название:          ", x[1])
        varToBot += "название:          " + x[1] + "\n"
    return varToBot

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
    try:
        txt = browser.find_elements_by_xpath("//h2")[0].text.split("IMDb:")
        if len(txt) == 2:
            print("рейтинг IMDb: ", txt[1])
        # завершающая конструкция, закрываем вкладку и идём назад
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
    except:
        browser.close()
        browser.switch_to.window(browser.window_handles[0])

def popular():
    varToBot = ""
    for li in arr:
        varToBot += show_desc_pop(li)
# раскомментить строку ниже чтоб отображать imdb оценку, но займет времени п*здец как много
#         gettt(li)
#         print("\n--------------------------------------\n")
        varToBot +=" \n---------------\n"
    print(varToBot)
    browser.quit()
    return varToBot

# popular()