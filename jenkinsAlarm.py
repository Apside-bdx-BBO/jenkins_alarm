#!/usr/bin/python
import jenkinsapi
from jenkinsapi.jenkins import Jenkins

import codecs
import json
import sys
import time

jenkins_url = 'http://jenkins-server-1.preprod:8080/'

print("******************************************************")
print("* Script for Arduino should work                     *")
print("******************************************************")

# Configurations
ping_server = 30
# jenkinsHome = Jenkins('http://localhost:8080', username = None, password = None)
jenkins_jobs = ["samsung-retail", "samsung-evollis-sdk-test"]
# ser = serial.Serial('COM6', 9600)

# Arduino Configuration
SUCCESS = b'b'
FAILURE = b'r'
BUILDING = b'a'
UNSTABLE = b'y'

time.sleep(5)

def get_server_instance():
    return Jenkins(jenkins_url, username = None, password = None)

def get_job_details():
    # Refer Example #1 for definition of function 'get_server_instance'
    server = get_server_instance()
    for j in server.get_jobs():
        job_instance = server.get_job(j[0])
        if job_instance.name in jenkins_jobs:
            print('Job Name:%s' % (job_instance.name))
            print('Job Description:%s' % (job_instance.get_description()))
            print('Is Job running:%s' % (job_instance.is_running()))
            print('Is Job enabled:%s' % (job_instance.is_enabled()))


# def getSCMInfroFromLatestGoodBuild(jenkinsHome, jobName):
#     job = jenkinsHome[jobName]
#     lgb = job.get_latest_build()
#     return lgb.get_revision()

get_job_details()
# for job in jenkins_jobs:
#     pass