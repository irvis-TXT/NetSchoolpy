import requests
import hashlib
import json


class NetSchool:
  def __init__(self,un,password):
    self.un = un
    self.password = password
    self.at = None
    self.cookies = None
  def login(self):
    global ses
    ses = requests.Session()
    user_agent = "NetScooPY by irvisTXT"
    response = ses.post('https://net-school.cap.ru/webapi/auth/getdata')
    lt = str(response.json()['lt'])
    ver = str(response.json()['ver'])
    salt = str(response.json()['salt'])
    pw = salt + hashlib.md5(self.password.encode('utf-8')).hexdigest()
    pw2 = hashlib.md5(pw.encode('utf-8')).hexdigest()
    response = ses.post(
        'https://net-school.cap.ru/webapi/auth/login', 
        
        data={
        'loginType': '1',
        'lt': lt,
        'pw2': pw2,
        'scid': '514',
        'un': self.un,
        'ver': ver,
      },
        headers={
        'Origin': 'https://net-school.cap.ru',
        'Referer': 'https://net-school.cap.ru/authorize/login'
      }
      )
    self.at = str(response.json()['at'])
    self.cookie =  json.loads(str(ses.cookies.get_dict()).replace("'",'"'))
    return str(response.json()['at'])
  
  
  def logout(self):
    res = requests.post('https://net-school.cap.ru/webapi/auth/logout',
      data={
        "at":"02872638704874641346969371",
        "VER":"1734880036083"
      }, 
      headers={
        "At": self.at,
        "Origin": "https://net-school.cap.ru",
        "Referer": "https://net-school.cap.ru/app/school/main/"
      }, 
      cookies=self.cookie)
    res1 = requests.get('https://net-school.cap.ru/webapi/auth/logout', 
      headers={
        "At": self.at,
        "Origin": "https://net-school.cap.ru",
        "Referer": "https://net-school.cap.ru/app/school/main/"
      }, 
      cookies=self.cookie)
    
    
  def get_name(self):
    res = requests.get('https://net-school.cap.ru/webapi/context', headers={
      'At': self.at,
    },
    cookies=self.cookie
    )
    return res.json()["user"]["name"]
  def work(self):
    res = requests.get('https://net-school.cap.ru/webapi/student/diary?schoolId=514&studentId=823976&vers=1733153515912&weekStart=2024-12-23&weekEnd=2024-12-23&withLaAssigns=false&yearId=162614', headers={
      'At': self.at,
    },
    cookies=self.cookie
    )
    return json.dumps(json.loads(res.text),indent=4,ensure_ascii=False)

