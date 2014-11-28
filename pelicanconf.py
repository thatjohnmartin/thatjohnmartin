#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'John Martin'
SITENAME = u'That John Martin'
SITEURL = 'http://thatjohnmartin.com'

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

FEED_RSS = 'rss.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
	('About', 'pages/about.html'),
    # ('Email', 'john@lonepixel.com'),
	('@johnm', 'http://twitter.com/johnm'),
    # ('LinkedIn', 'http://www.linkedin.com/in/thatjohnmartin'),
    # ('Github', 'http://github.com/thatjohnmartin'),
)

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

ARTICLE_PATHS = ['']
STATIC_PATHS = ['images', 'css', 'CNAME']
THEME = 'themes/thatjohnmartin'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'