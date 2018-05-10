# -*- coding: utf-8 -*-

"""
Copyright (c) 2018 hackbox developers (http://hackbox.io)
See the file 'LICENSE' for copying permission
"""

import requests
import sys

import error_based
from tools.sqlbuster.utils import sql_erros


def run(url):
    """check SQL injection vulnerability"""
    error_based.identify(url, sql_erros.errors)


run("https://hackyourselffirst.troyhunt.com/Make/3?orderby=3")
