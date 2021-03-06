#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 ~ 2012 Deepin, Inc.
#               2011 ~ 2012 Wang Yong
#
# Author:     Wang Yong <lazycat.manatee@gmail.com>
# Maintainer: Wang Yong <lazycat.manatee@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# To test other language, use below method:
#       env LANG=zh_CN LANGUAGE=zh_CN foo.py

from deepin_utils.file import get_parent_dir
import gettext
import os

LOCALE_DIR=os.path.join(get_parent_dir(__file__, 2), "locale")
PROJECT_NAME = "deepin-software-center"
if not os.path.exists(LOCALE_DIR):
    LOCALE_DIR="/usr/share/locale"

_ = None
try:
    _ = gettext.translation(PROJECT_NAME, LOCALE_DIR).gettext
except Exception, e:
    try:
        _ = gettext.translation(PROJECT_NAME, LOCALE_DIR, ['en_US']).gettext
    except Exception, e:
        _ = lambda i : i

def get_locale_code():
    try:
        return gettext.find(PROJECT_NAME, LOCALE_DIR).split(LOCALE_DIR)[1].split('/')[1]
    except:
        return "en_US"
