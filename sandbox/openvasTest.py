#!/usr/bin/env python
# -*- coding:utf-8 -*-

import openvas_lib


print(dir(openvas_lib.VulnscanManager))


scanner = openvas_lib.VulnscanManager("localhost", "admin", "rockjeev8194@", 9390, 903)

print("================================")
print(scanner.get_report_html("8ac4da9c-a1aa-4b44-a02c-cda5722c43c8"))

# scan_id, target_id = scanner.launch_scan(target = "127.0.0.1", # Target to scan
                                        #  profile = "SimpleScan")
