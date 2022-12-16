import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By #新版selenium這個是必要的
import time

def button_event():
    #driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) 
    driver = webdriver.Chrome(options=options)  # 這三行是因為小黑窗會跳奇怪的訊息，加後就不會

    driver.get("https://web085004.adm.ncyu.edu.tw/NewSite/Login.aspx?Language=zh-TW")
    time.sleep(1)
    account = driver.find_element(By.NAME,"TbxAccountId")
    ssid=sid.get()
    account.send_keys(ssid)
    password = driver.find_element(By.NAME,"TbxPassword")
    sspw=spw.get()
    password.send_keys(sspw)#your password
    login = driver.find_element(By.NAME,"BtnPreLogin")
    login.click()
    time.sleep(2)
    menu = driver.find_element(By.NAME,"BtnMenu")
    menu.click()
    time.sleep(2)
    menu1 = driver.find_element(By.LINK_TEXT,"教學意見調查作業")
    menu1.click()
    time.sleep(2)
    driver.switch_to.frame("application-frame-main") #switch frame
    menu2 = driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_BtnEntAns")
    menu2.click()
    time.sleep(2)
    driver.switch_to.default_content()
    driver.switch_to.frame("application-frame-main")
    
    driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_BtnSure").click()
    
    for ii in range(1,50):   #假設有50個意見調查'
        flag=1
        for i in range(1,40):
            try:
                browser=driver
                browser.find_element(By.ID,"ctl00_ContentPlaceHolder1_RBAns"+str(i)+"_0") #找到這個問卷確切有幾題
                flag+=1
            except:
                break

        for i in range(1,flag): #開始填 從1到flag-1，所以flag我預設是1
            driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_RBAns"+str(i)+"_"+str(degree)).click()
            driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$BtnSave").click()    

        driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_BtnEntAns").click()    
        driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_BtnSure").click()
                  

def choose(): #取得大家想填的滿意度
    global degree
    degree=choice.get()    

        

win=tk.Tk()  #介面的部分
win.geometry("350x200")
win.title("Teaching_evaluation_auto_fill")
sid=tk.StringVar()
spw=tk.StringVar()

label=tk.Label(win,text="請輸入學號")
label.grid(row=0,column=1,padx=10,pady=5)
label2=tk.Label(win,text="請輸入密碼")
label2.grid(row=1,column=1,padx=10,pady=5)

sID=tk.Entry(win,textvariable=sid)
sID.grid(row=0,column=2,padx=5,pady=5)
sPW=tk.Entry(win,textvariable=spw,show='*')
sPW.grid(row=1,column=2,padx=5,pady=5)


choice=tk.StringVar()
label3=tk.Label(win,text="請選擇滿意度")
label3.grid(row=3,column=2,padx=5,pady=5)

item1=tk.Radiobutton(win,text="非常同意",variable=choice,value="0",command=choose,cursor="heart")
item1.grid(row=4,column=1,pady=5)
item2=tk.Radiobutton(win,text="同意",variable=choice,value="1",command=choose,cursor="star")
item2.grid(row=4,column=2,pady=5)
item3=tk.Radiobutton(win,text="普通",variable=choice,value="2",command=choose,cursor="target")
item3.grid(row=4,column=3,pady=5)
item4=tk.Radiobutton(win,text="不同意",variable=choice,value="3",command=choose,cursor="spider")
item4.grid(row=5,column=1,pady=5)
item5=tk.Radiobutton(win,text="非常不同意",variable=choice,value="4",command=choose,cursor="pirate")
item5.grid(row=5,column=3,pady=5)

button=tk.Button(win,text="開始填寫",command=button_event) #讓上面的selenium開始做事
button.grid(row=6,column=2,pady=5)

win.mainloop()


    
