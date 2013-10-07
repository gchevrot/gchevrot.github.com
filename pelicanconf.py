# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# ===============
# Basic settings
# ===============
AUTHOR = u'gchevrot'
SITENAME = u'Guillaume Chevrot'
USE_FOLDER_AS_CATEGORY = 'True'
STATIC_PATHS = ['images', 'pdfs']
SITEURL = 'http://gchevrot.github.io/home'
#SITEURL = '/Users/guillaume/Documents/WebSite/Pelican/gchevrot/output'

# Posts
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/post.html'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

OUTPUT_PATH = 'home'

# =======
# Theming
# =======
THEME = 'theme'

GITHUB_URL = 'http://github.com/gchevrot/'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/gchevrot'),
          ('LinkedIn', 'http://fr.linkedin.com/pub/guillaume-chevrot/58/35a/701'))
TWITTER_URL = 'http://twitter.com/gchevrot'
LINKEDIN_URL = 'http://fr.linkedin.com/pub/guillaume-chevrot/58/35a/701'


DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
