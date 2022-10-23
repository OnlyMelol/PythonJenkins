# coding=utf-8
"""
@Project: PythonJenkins
@File: /job.py
@Author: Dustin Lin
@Created on: 2022/10/23 20:03:56
"""
import jenkins

server = jenkins.Jenkins("http://127.0.0.1:8080", "dustin", "pwd")
print(server.get_whoami())
