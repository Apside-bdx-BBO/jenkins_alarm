#!/usr/bin/python
import codecs
import json
import sys
import time
import urllib
import urllib.request

print("******************************************************")
print("* Script for Arduino should work                     *")
print("******************************************************")

# Configurations
ping_server = 30
jenkins_jobs = ["samsung-retail", "samsung-evollis-sdk-test"]
# ser = serial.Serial('COM6', 9600)

# Arduino Configuration
SUCCESS = b'b'
FAILURE = b'r'
BUILDING = b'a'
UNSTABLE = b'y'

time.sleep(5)


def get_status(jobName):
    global buildStatusJson
    jenkinsUrl = "http://jenkins-server-1.preprod:8080/job/"
    jenkinsStream = urllib.request.Request(jenkinsUrl + jobName + "/lastBuild/api/json")
    try:
        urllib.request.urlopen(jenkinsStream)
    except urllib.error.URLError as e:
        print("URL Error: " + str(e.reason))
        print("      (job name [" + jobName + "] probably wrong)")
        # sys.exit(2)

    buildStatusJson = None
    reader = codecs.getreader("utf-8")
    try:
        buildStatusJson = json.load(reader(jenkinsStream))
        # buildStatusJson = json.load(jenkinsStream)
    except:
        print("Failed to parse json")
        #sys.exit(3)

    if buildStatusJson is not None:
        return jobName, buildStatusJson["timestamp"], buildStatusJson["result"],

while 1:
    for job in jenkins_jobs:
        status = get_status(job)
        if status is not None:
            print(status[0], status[2])
            if status[2] == "UNSTABLE":
                time.sleep(ping_server)
        else:
            print('NO JOB')
