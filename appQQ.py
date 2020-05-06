import json
import os
from selenium import webdriver
def get_image_link(search_query):
    img_urls = []
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.getenv('GOOGLE_CHROME_BIN',None)
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    ## 方案A
    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=os.getenv('CHROMEDRIVER_PATH',None))
   
    # driver = webdriver.Chrome(executable_path='/app/.chromedriver/bin/chromedriver')
    
    ## 方案B
    # driver = webdriver.Chrome(executable_path='chromedriver')

    t = search_query[:-4]+'餐點價格'
    url = 'https://www.google.com/search?q=' + t 
    driver.get(url)
    return url
################################
################################
################################



# from flask import Flask, request, abort
# from flask import jsonify,url_for , redirect
# import requests


## 設置 #############################
# from flask import Flask, session ; import os ;  import flask
from flask import Flask   ;     import os
app = Flask(__name__)
# app.config['SECRET_KEY'] = os.urandom(24)
# #########################################
# app.secret_key = os.urandom(24)


##
## http://127.0.0.1:5000/  
## ,'POST'
## https://moon5566.herokuapp.com/
@app.route('/', methods=['GET'])  
def index():
    return "GO :"+get_image_link("COCO")

@app.route('/CMD/<string:SS>', methods=['GET'])  
def QQS(SS):
    SS =SS.replace('+','/')
    SSQ= os.popen(SS).read()   ## <str>
    print(SSQ)
    SSQ =SSQ.replace('\n','</br>')
    return SSQ

    SS=SS.replace("\n","</br>")
    SS=SS.replace("+","/")

    SSQ= os.popen(SS).read()   ## <str>
    return SSQ


if __name__ == "__main__":
    app.run(port=80)
    # print( Ghh(B)  )


