import requests
import fake_useragent
import random
import hashlib
import json
import os




class Netschool:
  def __init__(self,un,password, path):
    self.un = un
    self.password = password
    self.path = path
    self.checkLogin()
  def Create(self):
#
  def get_name(self):
    self.checkLogin()
    res = requests.get('https://net-school.cap.ru/webapi/context', headers={
      'At': config['NET-SCHOOL']['at'],
    },
    cookies=json.loads(config['NET-SCHOOL']['cookie'].replace("'",'"'))
    )
    return res.json()["user"]["name"]
  def work(self):
    self.checkLogin()
    res = requests.get('https://net-school.cap.ru/webapi/student/diary?schoolId=518&studentId=823977&vers=1724407067334&weekEnd=2023-10-22&weekStart=2023-10-16&withLaAssigns=false&yearId=161853', headers={
      'At': config['NET-SCHOOL']['at'],
    },
    cookies=json.loads(config['NET-SCHOOL']['cookie'].replace("'",'"'))
    )
    x = json.loads(res.text)
    print(json.dumps(x,indent=4,ensure_ascii=False))



