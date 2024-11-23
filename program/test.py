import random,requests
from lxml import etree


def get_weather(times,time):
    '''
    date:传入纯数字日期 --'20240320'
    time:传入时间(小时) --'18'
    '''
    time=int(time)
    if time >= 12:
        time-=12
        i=1-time/12
    
    elif time < 12:
        i=time/12
    
    weather_url=f'https://datashareclub.com/weather/%E5%B9%BF%E4%B8%9C/%E9%9F%B6%E5%85%B3/101280209.html'
    heads={"UserAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"}
    #获取页面数据
    response=requests.get(url=weather_url,headers=heads).text
    tree=etree.HTML(response)
    temperature_max=tree.xpath(f'/html/body/div/div/main/div[2]/div[2]/div/table/tbody/tr[{times}]/td[2]/text()')
    temperature_min=tree.xpath(f'/html/body/div/div/main/div[2]/div[2]/div/table/tbody/tr[{times}]/td[3]/text()')
    #difference=int(temperature_max[0])-int(temperature_min[0])
    humidity= str(random.randint(60, 80))+'%'
    
    return float(temperature_max[0][:-1]),temperature_max

d,h=get_weather(2,18)
print(d)
print(h)