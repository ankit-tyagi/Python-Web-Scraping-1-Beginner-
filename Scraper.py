import requests
from bs4 import BeautifulSoup
import smtplib
import time


url = 'https://www.amazon.in/Reebok-Mens-Rush-Running-Shoes/dp/B07FKFXNTH?pf_rd_p=694b9d36-2eb6-4ee4-8d67-51e8321505be&pd_rd_wg=AUmDX&pf_rd_r=FZ74W7SSSB5158P31JW8&ref_=pd_gw_unk&pd_rd_w=Qy7kc&pd_rd_r=0a466d21-02e2-43da-bf61-40f3ce4f16c3&th=1&psc=1'

headers = {"user-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

def checkprice():
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    price = price.replace(",","")
    cprice = float(price[2:7])

    if(cprice < 1500):
        sendmail()

    print(cprice)
    print(title.strip())

    if(cprice > 1500):
        sendmail()
    #print(soup.prettify())


def sendmail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('ankit7tyagi@gmail.com','Enter your password here before the bracket is closed') 
    #'Enter your password here before the bracket is closed')
    subject = 'Price fell down'
    body = 'Check the amazon link https://www.amazon.in/Reebok-Mens-Rush-Running-Shoes/dp/B07FKFXNTH?pf_rd_p=694b9d36-2eb6-4ee4-8d67-51e8321505be&pd_rd_wg=AUmDX&pf_rd_r=FZ74W7SSSB5158P31JW8&ref_=pd_gw_unk&pd_rd_w=Qy7kc&pd_rd_r=0a466d21-02e2-43da-bf61-40f3ce4f16c3&th=1&psc=1'

    msg = f"subject: {subject}\n\n{body}"
    server.sendmail(
        'ankit7tyagi@gmail.com',
        'ankit7tyagi@gmail.com',
        msg
    )

    print('Email has been sent  ')
    server.quit()

num = 2
while(True and num>0):
    checkprice()
    time.sleep(5)
    num = num-1
    print(time.strftime("%H:%M:%S", time.gmtime())) # time.localtime))