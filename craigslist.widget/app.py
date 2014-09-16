#!/usr/bin/python

import sys
import json
import urllib
from xml.dom import minidom
from urlparse import urlparse
from datetime import datetime

arg = sys.argv[1]
url = "%s&format=rss" % arg
dom = minidom.parse(urllib.urlopen(url))
items = []

# http://stackoverflow.com/a/1551394
def pretty_date(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    from datetime import datetime
    now = datetime.now()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time,datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return str(second_diff) + " seconds ago"
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return str(second_diff / 60) + " minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return str(second_diff / 3600) + " hours ago"
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 31:
        return str(day_diff / 7) + " weeks ago"
    if day_diff < 365:
        return str(day_diff / 30) + " months ago"
    return str(day_diff / 365) + " years ago"

# https://developer.yahoo.com/python/python-xml.html#mini

for node in dom.getElementsByTagName('item')[0:5]:

    image_node = node.getElementsByTagName('enc:enclosure')
    if image_node:
        image = image_node[0].getAttribute('resource')
    else:
        image = 'http://www.craigslist.org/images/peace.jpg'

    date_node = node.getElementsByTagName('dc:date')[0].firstChild.data

    # 2014-09-15T15:52:38-07:00

    # t = time.mktime(time.strptime(date_node, "%Y-%m-%dT%H:%M:%S-%h:%M"));

    t = datetime.strptime(date_node, "%Y-%m-%dT%H:%M:%S-%I:00")


    items.append({
        'title': node.getElementsByTagName('title')[0].firstChild.data,
        'link': node.getElementsByTagName('link')[0].firstChild.data,
        'description': node.getElementsByTagName('description')[0].firstChild.data,
        'image': image,
        'date': pretty_date(t)
    })

print json.dumps(items)

sys.exit()