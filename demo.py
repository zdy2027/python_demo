#!/usr/bin/env python

import jenkins
server = jenkins.Jenkins('http://172.29.152.184:8080')
version = server.get_version()
print version
