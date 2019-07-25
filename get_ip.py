# coding=UTF-8
import requests
import json
import time
import os

#cd work dir
os.system("cd /home/pi/Documents/github-pi/pi")
response = requests.get("http://ip-api.com/json")
ip_json = json.loads(response.text)
for line in open("/home/pi/Documents/github-pi/pi/address.txt"):
    line = line.strip()
    if line != ip_json["query"]:
        print "need change the ip"
        os.system("echo %s > address.txt" % ip_json["query"])
        os.system("git add address.txt")
        os.system("git commit -m '%s ip update'" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        os.system("git push")
print "Date:%s ip:%s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), ip_json["query"])
