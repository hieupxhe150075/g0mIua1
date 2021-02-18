import os,sys
from time import sleep
from bs4 import BeautifulSoup
import requests
from colorama import Fore
#Màu:
app_token=input("NHẬP TOKEN:")
cookie_fb=input("NHẬP COOKIE FB:")
red='\u001b[31;1m'

green='\u001b[32;1m'
blue='\u001b[34;1m'
yellow='\u001b[33;1m'
reset='\u001b[0m'

#Nền:
back_red='\u001b[41m'
back_green='\u001b[42m'
back_yellow='\u001b[43m'
back_blue='\u001b[44m'
url_login="https://gomlua.com/user/info?os=web"
url ="https://gomlua.com/cpi/listCampaignFacebook?os=web&type=like_post"
head_gomlua={
  'Host':'gomlua.com',
  'Accept':'application/json, text/plain, */*',
  'app_token':app_token,
  'User-Agent':'Mozilla/5.0 (Linux; Android 10; RMX1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36',
  }
head_fb={
  'Host':'mbasic.facebook.com',
  'user-agent':'Mozilla/5.0 (Linux; Android 10; RMX1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36',
  'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'cookie':cookie_fb,
}
login =requests.get(url_login,headers=head_gomlua)
tên =login.json()["data"]["username"]
dn=login.json()["message"]
tiền =login.json()["data"]["current_paddy"]
đô =str(tiền)
if dn=="Thanh cong":
  sleep(1)
  print (green+"ĐĂNG NHẬP THÀNH CÔNG❤️")
  sleep(1)
  os.system("clear")
  print (green+"Bản Quyền:CB TOOL")
  print (yellow+"USERNAME:",red+tên)
  print (yellow+"Ví:",red+đô)
  h =int(input(Fore.GREEN+"Nhập Time:"))
  print ("\n")
  while True:
    try:
      web =requests.get(url, headers=head_gomlua)
      pa=web.json()["data"]["list"]
      if pa==[]:
        print (green+"HẾT JOB",end=" \r")
      checklogin=web.json()["message"]
      job=web.json()['data']['list'][0]['campaign_url']
      link_id =web.json()['data']['list'][0]["link_id"]
      id_nhan=str(link_id)
      type =web.json()["data"]["list"][0]["react_type"]
      content =web.json()["data"]["list"][0]["link_title"]
      url_nhan="https://gomlua.com/likeToken/checkLikeToken?os=web&link_id="+id_nhan
      checkjob=requests.get(url_nhan,headers=head_gomlua)
      if checklogin=="Thanh cong":
        if checkjob=="Thanh cong":
          print (green+"LẤY JOB THÀNH CÔNG")
        if type=="LIKE":
          web2=requests.get(job,headers=head_fb,allow_redirects=True)
          sop =BeautifulSoup(web2.text,"html.parser")
          p =sop.find_all("a",href=True)
          for i in p:
            link=i["href"]
            if "/a/like.php?" in link:
              requests.get("https://mbasic.facebook.com" + link, headers=head_fb, allow_redirects=True)
          nhan_tien=f"https://gomlua.com/likeToken/likeSuccess?os=web&link_id={id_nhan}&like_count=1"
          tien =requests.get(nhan_tien,headers=head_gomlua)
          success=tien.json()["message"]
          if "Chúc mừng" in success:
            login =requests.get(url_login,headers=head_gomlua)
            tiền =login.json()["data"]["current_paddy"]
            print(green+"==============================")
            print (yellow+"BẠN NHẬN ĐƯỢC 35 LÚA","|Ví:",tiền)
            print(green+"==============================")
          if 'lại' in success:
            i=0
            for restart in range(10):
              i=i+1
              print("ĐANG NHẬN LẠI😭",end=" \r")
              tien =requests.get(nhan_tien,headers=head_gomlua)
              success=tien.json()["message"]
              if "Chúc mừng" in success:
                login =requests.get(url_login,headers=head_gomlua)
                tiền =login.json()["data"]["current_paddy"]
                print(green+"==============================")
                print (yellow+"BẠN NHẬN ĐƯỢC 35 LÚA","|Ví:",tiền)
                print(green+"==============================")
          for time in range(h,-1,-1):
            sleep(1)
            print (Fore.YELLOW+"ĐANG LỌC JOB",time,"GIÂY",end=" \r")
        
    except:
      print("",end=" \r")
else:
  print ("Vui Lòng Đăng Nhập Lại!!")
   
   
    