from tkinter import *
from tkinter.ttk import *
import requests

def showWeather(event):  # 下拉選單選取選項後執行的程式
    city = cbVar.get()  # 使用者選取的選項
    if city != '請選擇:':  # 選擇縣市
        try:
            report = requests.get(f'https://Heroku網址/weather/{city}').text  # 取得Web API資料
            jsondata = eval(report)  # 將回傳的資料轉換為字典格式
            showdata = f"{city} 天氣資料:\n"
            showdata += f"天氣狀況: {jsondata['天氣狀況']}\n"
            showdata += f"最高溫: {jsondata['最高溫']}\n"
            showdata += f"最低溫: {jsondata['最低溫']}\n"
            showdata += f"舒適度: {jsondata['舒適度']}\n"
            showdata += f"降雨機率: {jsondata['降雨機率']}\n"
            labelVar.set(showdata)
        except Exception as e:
            labelVar.set(f"取得天氣資料時出錯: {e}")
    else:
        labelVar.set('請選擇縣市!')

# 建立主視窗
win = Tk()
win.title('縣市天氣資料')
win.geometry('300x350')

# 下拉選單
cbVar = StringVar()
cb = Combobox(win, textvariable=cbVar)  # 下拉選單元件
cb['values'] = (
    "請選擇:", "臺北", "新北", "桃園", "臺中", "臺南", "高雄",
    "基隆", "新竹", "嘉義", "苗栗", "彰化", "南投", "雲林",
    "屏東", "宜蘭", "花蓮", "臺東", "澎湖", "金門", "連江"
)  # 設定選項
cb.current(0)  # 預設第一個選項
cb.bind('<<ComboboxSelected>>', showWeather)  # 設定選取選項後執行的程式
cb.place(x=70, y=15)

# 顯示天氣資料的標籤
labelVar = StringVar()
labelShow = Label(
    win, foreground='red', justify='left', textvariable=labelVar
)  # 標籤元件
labelVar.set('尚未選定縣市')
labelShow.place(x=80, y=220)

# 執行主程式
win.mainloop()
