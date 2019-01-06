import requests
import bs4


def find_weather(city):
    URL = 'https://ua.sinoptik.ua/погода-'
    url = URL + city
    r = requests.get(url)
    b = bs4.BeautifulSoup(r.text, 'html.parser')
    """p3 = b.select('.temperature .p3')
    morning_w1 = p3[0].getText()
    p4 = b.select('.temperature .p4')
    morning_w2 = p4[0].getText()
    p5 = b.select('.temperature .p5')
    lunch_w1 = p5[0].getText()
    p6 = b.select('.temperature .p6')
    lunch_w2 = p6[0].getText()
    p7 = b.select('.temperature .p7')
    afternun_w1 = p7[0].getText()
    p8 = b.select('.temperature .p8')
    afternun_w2 = p8[0].getText()
    p = b.select('.rSide .description')

    return 'Ранок: {}, {}\nДень: {}, {}\nВечір: {}, {}\n{}'.format(morning_w1, morning_w2, lunch_w1, lunch_w2,
                                                                  afternun_w1, afternun_w2, p[1].getText())"""
    return b.select('.today-temp')[0].getText()

