#!/usr/bin/env python

import jenkins
server = jenkins.Jenkins('http://172.29.152.183:31749')
version = server.get_version()
print version
