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

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

ARTICLE_PATHS = ['']
STATIC_PATHS = [
    'images',
    'CNAME',
    'favicons/favicon.ico',
    'favicons/apple-touch-icon.png',
    'favicons/apple-touch-icon-57x57.png',
    'favicons/apple-touch-icon-72x72.png',
    'favicons/apple-touch-icon-76x76.png',
    'favicons/apple-touch-icon-114x114.png',
    'favicons/apple-touch-icon-120x120.png',
    'favicons/apple-touch-icon-144x144.png',
    'favicons/apple-touch-icon-152x152.png',
]

EXTRA_PATH_METADATA = {
    'favicons/favicon.ico': {'path': 'favicon.ico'},
    'favicons/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'favicons/apple-touch-icon-57x57.png': {'path': 'apple-touch-icon-57x57.png'},
    'favicons/apple-touch-icon-72x72.png': {'path': 'apple-touch-icon-72x72.png'},
    'favicons/apple-touch-icon-76x76.png': {'path': 'apple-touch-icon-76x76.png'},
    'favicons/apple-touch-icon-114x114.png': {'path': 'apple-touch-icon-114x114.png'},
    'favicons/apple-touch-icon-120x120.png': {'path': 'apple-touch-icon-120x120.png'},
    'favicons/apple-touch-icon-144x144.png': {'path': 'apple-touch-icon-144x144.png'},
    'favicons/apple-touch-icon-152x152.png': {'path': 'apple-touch-icon-152x152.png'},
}

THEME = 'themes/thatjohnmartin'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'