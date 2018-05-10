#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2018 hackbox.io developers (http://hackbox.io)
See the file 'LICENSE' for copying permission
"""

from bs4 import BeautifulSoup
import requests
import re
from urlparse import urljoin


stack = []
domain = None
count = 0


def run(target, **kwargs):
    """
    Map a website using recursive crawling method
    """

    global stack, domain, count

    stack.append(target)
    domain = target.split("://")[1].split("/")[0]
    count = 0
    start(**kwargs)
    return stack


def start(**options):
    """
    Start recursive crawling
    """

    global stack, domain, count

    if options["verbose"]:
        print("+| {}".format(stack[count]))
    res = requests.get(stack[count])

    if res.ok:
        links = crawl_links(res.content)
        for link in links:
            if not link.startswith("http"):
                link = urljoin(res.url, link)
            if link.endswith("/"):
                link = link[:-1]

            if link not in stack and (re.compile(r'://' + domain).search(link) or
                                      re.compile(r'://www.' + domain).search(link)):
                if options["verbose"]:
                    print("+|    | {}".format(link))
                stack.append(link)

    count += 1
    if count < len(stack) <= options["max_links"]:
        start(**options)


def crawl_links(content):
    """
    Crawl all the links from given page content
    """

    soup = BeautifulSoup(content, "lxml")
    a_tags = soup.find_all("a")
    links = []

    for a_tag in a_tags:
        try:
            if is_valid_url(a_tag["href"]):
                links.append(a_tag["href"])
        except KeyError:
            pass

    return links


def is_valid_url(url):
    """
    Check if the href URL is valid
    """

    return (
        url != "#" and
        url != "" and
        url[0] != "?" and
        url[0] != "#" and
        not url.startswith("tel:") and
        not url.startswith("javascript:") and
        not url.startswith("mailto:")
    )
