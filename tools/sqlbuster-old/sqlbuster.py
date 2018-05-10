#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from urlparse import urlparse

import sqlerrors
import web


def run(url):
    """check SQL injection vulnerability"""

    print("+ Testing SQL injection: {}".format(url))

    domain = url.split("?")[0]  # domain with path without queries
    queries = urlparse(url).query.split("&")
    # no queries in url
    if not any(queries):
        return False, None

    payloads = ("'", "')", "';", '"', '")', '";', '`', '`)', '`;', '\\', "%27", "%%2727", "%25%27", "%60", "%5C")
    res = None
    for payload in payloads:
        website = domain + "?" + ("&".join([param + payload for param in queries]))
        res = requests.get(website)

        print("+ Trying new payload...")

        if res.text:
            vulnerable, db = sqlerrors.check(res.text)
            if vulnerable and db is not None:
                print("+ URL is vulnerable to SQL injection")
                print("+ Database: {}".format(db))
                print("+ Language: {}".format(res.headers.get("x-powered-by", "null")))
                print("+ Server: {}".format(res.headers.get("server", "null")))
                return True, db

    print("- URL is not vulnerable to SQL injection")
    print("+ Language: {}".format(res.headers.get("x-powered-by", "null")))
    print("+ Server: {}".format(res.headers.get("server", "null")))
    return False, None
