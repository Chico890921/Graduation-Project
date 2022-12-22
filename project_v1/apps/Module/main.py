# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print_hi("PyCharm")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# -*- coding: utf-8 -*-

import json
import random
import re
import time

import pandas as pd
import requests

# selenium，2022/9/17 將套件更新到4.4.3版本，因此寫法全部都更新過
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

keyword = "adidas"
page = 184
ecode = "utf-8-sig"
my_headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "cookie": '__LOCALE__null=TW; SPC_T_ID=wxv+iSLj3O7H6qDOQhZiKAuNxFL3vCIzSNxPKjyp/e3aZkOyOpXUx36SHoJElA90C3p7uOlJ+TBB3Ec0C9CKh3JR6cSyqr2sA0D6bae/+ChxDOtnsqCGB9rZNANBtHsYUbMMuDUc5wDyh0fS1tPw8F3riR7+kTzgYmFs0FOwQzg=; SPC_T_IV=R3RvOFZPUXk0MEU5UEwzRQ==; SPC_F=06HnjeBKD6QfQaxu2WzZe0oWe46Q6le8; REC_T_ID=1c06438a-364c-11ed-b2f3-ee7c6594edb5; csrftoken=iIITffWMfgRQP8g0FHTBLJ2r4Ko1Otw6; _gcl_au=1.1.1251735121.1663393609; SPC_IA=-1; SPC_EC=-; SPC_T_ID="wxv+iSLj3O7H6qDOQhZiKAuNxFL3vCIzSNxPKjyp/e3aZkOyOpXUx36SHoJElA90C3p7uOlJ+TBB3Ec0C9CKh3JR6cSyqr2sA0D6bae/+ChxDOtnsqCGB9rZNANBtHsYUbMMuDUc5wDyh0fS1tPw8F3riR7+kTzgYmFs0FOwQzg="; SPC_U=-; SPC_T_IV="R3RvOFZPUXk0MEU5UEwzRQ=="; SPC_SI=WpwhYwAAAABvVTNObFBDMJ22HAAAAAAAOEFWSThOaVQ=; SPC_R_T_ID=wxv+iSLj3O7H6qDOQhZiKAuNxFL3vCIzSNxPKjyp/e3aZkOyOpXUx36SHoJElA90C3p7uOlJ+TBB3Ec0C9CKh3JR6cSyqr2sA0D6bae/+ChxDOtnsqCGB9rZNANBtHsYUbMMuDUc5wDyh0fS1tPw8F3riR7+kTzgYmFs0FOwQzg=; SPC_R_T_IV=R3RvOFZPUXk0MEU5UEwzRQ==; _fbp=fb.1.1663393614946.166652952; _QPWSDCXHZQA=58608429-1742-4d4b-b700-1610287752ea; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.900060094.1663393617; _ga=GA1.1.1772813716.1663393612; shopee_webUnique_ccd=ZLvsf7u90HavJpxcPjL1MA%3D%3D%7CQcr1Rvv7VsFJ7%2FBK9LzI9kg79UDWk6hFShOyEvvca2mBD900Mr3ck1TCP6RzCXel622tEqXT7%2F1%2FZGmH9kyAbaHYSCHiVmGouQ%3D%3D%7CpPquNK0ZO5EnPU1J%7C06%7C3; ds=c635d5e472189f9285afa538288e5acb; cto_bundle=XQYXsF80c2hvSDRIMElWRXd3ejVKY3hIanZSTXVQRlZIR0VCYXdMb0QlMkJMWmE2Tm5NbTBGWFpQdjFMNmszMHY5dW1QMkltdERWJTJGWlJNMVljRklrTURLb0tWNGFZYktSWUV5YUdMTThKT2dSemtlWTgxd3JuN0h2MngxTVAwVDklMkJGT2tzWlZ4YmlUdFU0Unc5Y3FIamo5OGJ1TEElM0QlM0Q; _ga_RPSBE3TQZZ=GS1.1.1663393612.1.1.1663395067.60.0.0',
    "if-none-match-": "55b03-9e2557dfd0e772de9f277b50d1165cc2",
    "referer": "https://shopee.tw/%E8%8A%B1%E8%A5%AF%E8%A1%AB-50%E6%AC%BE%E5%8F%AF%E9%81%B8-%E9%96%8B%E8%A1%AB-%E8%A5%AF%E8%A1%AB-%E7%94%B7%E7%94%9F%E5%A4%8F%E5%A8%81%E5%A4%B7%E7%9F%AD%E8%A2%96%E8%A5%AF%E8%A1%AB-%E5%BA%A6%E5%81%87%E9%A2%A8%E8%A5%AF%E8%A1%AB-%E7%9F%AD%E8%A2%96%E8%A5%AF%E8%A1%AB-%E4%BA%94%E5%88%86%E8%A2%96%E8%A5%AF%E8%A1%AB-%E7%94%B7%E7%94%9F%E4%B8%8A%E8%A1%A3-%E5%AF%AC%E9%AC%86%E8%8A%B1%E8%A5%AF%E8%A1%AB-%E8%A5%AF%E8%A1%AB-%E6%BC%94%E5%87%BA%E6%9C%8D-i.5695643.16302986550?sp_atk=8d962fa5-d6ce-48ee-b150-79d3d469d3e2&xptdk=8d962fa5-d6ce-48ee-b150-79d3d469d3e2",
    "sec-ch-ua": '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "x-api-source": "pc",
    "x-requested-with": "XMLHttpRequest",
    "x-shopee-language": "zh-Hant",
}
# https://shopee.tw/api/v4/seller_operation/get_shop_ratings?limit=6&offset=0&replied=false&shop_id=2833326&user_id=2834618

# 進入每個商品，抓取買家留言
def goods_comments(item_id, shop_id):
    # url = 'https://shopee.tw/api/v2/item/get_ratings?itemid='+ str(item_id) + '&shop_id=' + str(shop_id) + '&offset=0&limit=200&flag=1&filter=0'
    url = (
        "https://shopee.tw/api/v2/item/get_ratings?filter=0&flag=1&itemid="
        + str(item_id)
        + "&limit=50&offset=0&shopid="
        + str(shop_id)
        + "&type=0"
    )
    r = requests.get(url, headers=my_headers)
    st = r.text.replace("\\n", "^n")
    st = st.replace("\\t", "^t")
    st = st.replace("\\r", "^r")

    gj = json.loads(st)
    return gj["data"]["ratings"]


# 自動下載ChromeDriver
service = ChromeService(executable_path=ChromeDriverManager().install())

# 關閉通知提醒
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# 開啟瀏覽器
driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
time.sleep(5)

print("---------- 開始進行爬蟲 ----------")
tStart = time.time()  # 計時開始

container_product = pd.DataFrame()
container_comment = pd.DataFrame()


print("url: ")
url = input()

for i in range(int(page)):

    # 準備用來存放資料的陣列
    itemid = []
    shopid = []
    name = []
    brand = []
    stock = []
    price = []
    discount = []
    cmt_count = []
    five_star = []
    four_star = []
    three_star = []
    two_star = []
    one_star = []
    rating_star = []

    # driver.get('https://shopee.tw/search?keyword=' + keyword + '&page=' + str(i)) /////////
    driver.get(url + "?page=" + str(i) + "&sortBy=pop")
    # driver.get('https://shopee.tw/long09800?page='+str(i)+'&smtt=0.169154739-1671513159.4&sortBy=pop')

    # 滾動頁面
    for scroll in range(6):
        driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(2)

    # 取得商品內容
    for item, thename in zip(
        driver.find_elements(by=By.XPATH, value='//*[@data-sqe="link"]'),
        driver.find_elements(by=By.XPATH, value='//*[@data-sqe="name"]'),
    ):
        # 商品ID、商家ID
        getID = item.get_attribute("href")
        theitemid = int((getID[getID.rfind(".") + 1 : getID.rfind("?")]))
        theshopid = int(
            getID[getID[: getID.rfind(".")].rfind(".") + 1 : getID.rfind(".")]
        )
        itemid.append(theitemid)
        shopid.append(theshopid)

        # 商品名稱

        getname = thename.text.split("\n")[0]
        print("抓取： " + getname)
        name.append(getname)

        # 消費者評論詳細資料
        iteComment = goods_comments(item_id=theitemid, shop_id=theshopid)
        # print(iteComment)

        userid = []  # 使用者ID
        comment_rating_star = []  # 給星
        comment = []  # 留言內容

        if iteComment is not None:
            for comm in iteComment:
                userid.append(comm["userid"])
                comment_rating_star.append(comm["rating_star"])
                try:
                    comment.append(comm["comment"])
                except:
                    a = 1
                    # comment.append(None)

        f = open(r"apps/data/text.txt", "a", encoding="UTF-8")
        # result = list(map(str, iteComment))
        # result ='in(iteComment)

        # iteComment.join(iteComment)

        result = ""
        for element in comment:
            # result = result.join(element)
            result += element
            if element != "":
                f.write(element + "\n" + "\n")
                print("element:", element)

        # f.write(result)
        f.close()


tEnd = time.time()  # 計時結束
