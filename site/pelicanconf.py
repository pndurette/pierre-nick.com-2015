#!/usr/bin/env python
# -*- coding: utf-8 -*- #
#from __future__ import unicode_literals

AUTHOR = u'Pierre Nicolas Durette'
SITENAME = u'Pierre Nick Durette'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'America/Toronto'
DEFAULT_LANG = u'en'
THEME = '../../pelican-pn2015'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# pelican-pn2015 theme-specific
# SECTIONS = ['section_intro', 'section_projects', 'section_blog']
SECTIONS = ['section_intro']

QUOTES = [
  "I'll create a <a href='https://www.youtube.com/watch?v=hkDD03yeLnU'>GUI interface using visual basic</a> see if I can track an IP address.",
  "It's a UNIX system! I know this!",
  "<a href='https://www.youtube.com/watch?v=LhF_56SxrGk'>ENHANCE</a>!"
]

TAGLINE = "Hello! Toronto guy from Montreal here. Tech, things, city, code, travel, <a href='https://instagram.com/p/ulZ56MwWf9/'>schnauzer</a>."

# Icon row links
# Font-Awesome icon names. e.g. <i class="fa fa-<NAME>"></i>
LINK_ICONS = [
  {'name': 'github', 'href': 'https://github.com/pndurette'},
  {'name': 'twitter', 'href': 'https://twitter.com/PierreNick'},
  {'name': 'instagram', 'href': 'https://instagram.com/PierreNick'},
  {'name': 'linkedin', 'href': 'https://ca.linkedin.com/in/pndurette'}
]
