#!/usr/bin/env python

import time
from pprint import pprint
from zapv2 import ZAPv2

target = 'https://pentestcloud.io'
zap = ZAPv2(apikey="1234", proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})


# print(dir(zap.pscan.scanners))
# print("=====================")
# print(dir(zap.pscan.scanners[0]))

print 'Accessing target %s' % target
zap.urlopen(target)
time.sleep(2)

print 'Spidering target %s' % target
scanid = zap.spider.scan(target)
time.sleep(2)

while (int(zap.spider.status(scanid)) < 100):
    print 'Spider progress %: ' + zap.spider.status(scanid)
    if int(zap.spider.status(scanid)) > 2:
        zap.spider.stop()

    time.sleep(2)

print 'Spider completed'
time.sleep(5)

print 'Scanning target %s' % target
# zap.ascan.disable_all_scanners()
# zap.ascan.enable_scanners([6])
zap.ascan.enable_all_scanners()

scanid = zap.ascan.scan(target)
while (int(zap.ascan.status(scanid)) < 100):
    print 'Scan progress %: ' + zap.ascan.status(scanid)
    time.sleep(5)
print 'Scan completed'

# Report the results

print 'Hosts: ' + ', '.join(zap.core.hosts)
print 'Alerts: '
pprint (zap.core.alerts())
