# -*- coding: utf-8 -*-

"""
Copyright (c) 2018 hackbox developers (http://hackbox.io)
See the file 'LICENSE' for copying permission
"""

import requests
import re

from tools.sqlbuster.utils import user_agents


def identify(url, sql_errors):
    print("+ Testing error based SQL injection")
    print("+ URL: {}".format(url))

    res = requests.get("{}'".format(url), headers={"User-Agent": user_agents.get()})

    for db, errors in sql_errors.items():
        for error in errors:
            if re.compile(error).search(res.content):
                print("+ Injectable {} detected".format(db))
                return

    print "- Not Injectable"
