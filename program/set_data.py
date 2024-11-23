# set_data.py - By: Sakiri - Sat Mar 23 2024
# version: 0.3

import json
import sys
import os

def set_data(name,journey,speed,school,time,mode,start_time):
    '''
    保存用户配置
    '''
    user_data={'user_name':name,'school':school,'journey':journey,'speed':speed,'time':time,'times':int(times),'mode':mode,'start_time':start_time}
    with open('./data/user_data.json','w')as f:
        json.dump(user_data,f)

def open_json():
    #打开json
    with open('./data/user_data.json','r',encoding='utf-8') as f:
        load_data=json.load(f)
    return load_data

if __name__=='__main__':
    #检测和创建user_data.json
    file_path='./data/user_data.json'
    if os.path.exists(file_path):
        print('\033[96m存在user_data.json\033[0m')
    else:
        #创建文件
        with open(file_path,'w') as file:
            file.write('')
        print('\033[96m自动创建了user_data.json\033[0m')
        print('\033[91m跑步信息为空，接下来请选择“重新创建信息文件”\033[0m')

    print(
        '📚                                             \033[1;35;46m   --使用须知--   \033[0m\n'
        '\n📗1，日期将默认设置为当前日期，然后向后递减，(如果创建两张图片，那么跑步日期将会是当前日期已及当前日期的前一天)\n     \033[91m如果需要自定义日期，可以在后面的选项更改\033[0m'
        '\n📓2，时间设置格式为hour:min，程序将会随机设定分钟，前后差值为一小时 例：你输入18:20，程序将在17:50~18:50范围内随机取值\n     \033[91m注意!!时间的 : 符号必须在英文输入法下输入,不然会报错!!\033[0m'
        '\n📕3，路程同理，向后差值0.3km，保留后两位小数 例: 你输入2，程序将在2~2.3的范围随机取值'
        '\n📙4，启动脚本后，需保持流畅的网络连接及版本较新的Microsoft Edge浏览器(Windows 10/11系统自带)，用于获取天气数据和跑步图像'
        '\n📘5，如果第一次使用此脚本，需要选择“重新创建配置文件”'
        '\n📗6，此脚本具有时效性，随着目标网址的更改可能会随时失效(应该没那么快😅)，或者其他问题。')
    input('\033[96m了解“使用须知”的内容后，按下回车键开始创建/修改跑步信息\033[0m')

    print('📚                                          \033[1;35;46m   --开始创建/修改跑步信息--   \033[0m\n')
    modes=input('🔨重新创建信息文件(\033[96m输入d\033[0m) or 🔧只修改某个值(\033[96m输入r\033[0m)')
    while True:
        if modes == "d" or modes == "r":
            break
        else:
            modes=input("\n\033[91m错误的输入，请重新输入有效的选项：\033[0m")

    if modes == 'd':
        #重新创建配置文件
        print("\033[1;35;46m --重新创建配置文件-- \033[0m")
        name=input('输入用户名(你在keep应用的昵称)：')
        journey=input('输入路程：(生成截图上跑步的路程，输入整数，程序会在一定范围内随机取值)')
        speed=input('输入配速(菜鸡一般在7-10,业余在5-7,有跑步基础4-5,高手3-4):')
        time=input('输入时间(跑步截图上显示开始跑步的时间。详细参见“使用须知2”)：')
        school=input('输入学校名称(地名)：')
        times=input('创建图片张数：')
        mode=input('是否需要自动设置起点日期？详细参见“使用须知1”(\033[96m🤖需要输入y or 🧐不需要输入n\033[0m)')

        while True:
            if mode =='y':
                start_time=input('请输入起点日期(年月日，例：2024-01-01)')
                break
            elif mode == 'n':
                start_time=0
                break
            else:
                mode=input("\n\033[91m错误的输入，请重新输入有效的选项：\033[0m")
                continue
        set_data(name,journey,speed,school,time,mode,start_time)
        print('保存用户配置成功 Ciallo~(∠・ω< )⌒☆ 按下任意键退出')

    elif modes == 'r':
        #修改某个数组
        print("\033[1;35;46m --修改一个或多个值-- \033[0m")
        #确认json文件是否有内容
        try:
            load_data=open_json()
        except json.decoder.JSONDecodeError:
            print('\n\033[91m当前用户数据为空，请重新执行此脚本，并选择"重新创建配置文件"\033[0m')
            sys.exit(1)
        i=0
        while i == 0:
            print('\n\033[96m当前的数据内容：\033[0m')
            #输出信息内容
            for key,value in dict.items(load_data):
                if key == 'user_name':
                    print(f'keep昵称:{str(value)}------------输入{key}来更改这个值')
                elif key == 'school':
                    print(f'\n学校名称:{str(value)}------------输入{key}来更改这个值')
                elif key == 'journey':
                    print(f'\n路程:{str(value)}------------输入{key}来更改这个值')
                elif key == 'speed':
                    print(f'\n配速:{str(value)}------------输入{key}来更改这个值')
                elif key == 'time':
                    print(f'\n跑步开始时间:{str(value)}------------输入{key}来更改这个值')
                elif key == 'times':
                    print(f'\n创建图像张数:{str(value)}------------输入{key}来更改这个值')
                elif key == 'mode':
                    mode_value=[key,value]
                    if value=='y':
                        print('\n当前自动计算起点日期',end=' ')
                    else :
                        print('\n当前关闭自动计算起点日期',end=' ')
                    print('------------输入mode以开关这个设置')
            #修改内容
            in_key=input('\n输入需要修改的数据：')
            if in_key == 'mode':
                if mode_value[1] == 'y':
                    load_data[in_key]='n'
                    in_value=input('起点日期(年-月-日格式):')
                    load_data['start_time']=in_value
                    print('自动计算起点日期已关闭')
                else :
                    load_data[in_key]='y'
                    load_data['start_time']=0
                    print('自动计算起点日期已打开')
            else :
                in_value=input('输入'+in_key+'的新值：')
                load_data[in_key]=in_value

            #保存修改
            i=input('保存成功,输入\033[91m1\033[0m以退出修改脚本,输入\033[91m0\033[0m则继续修改内容\n')
            i=int(i)
        with open("./data/user_data.json",'w',encoding='utf-8') as f:
            json.dump(load_data,f,ensure_ascii=False)
        print('保存用户配置成功 Ciallo~(∠・ω< )⌒☆ 按下任意键退出')