#!/usr/bin/env python
# PyVisiLibity: a Python binding of VisiLibity1
# Copyright (C) 2018 Yu Cao < University of Southampton> Yu.Cao at soton.ac.uk
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or 
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details. 
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

from distutils.core import setup, Extension

module = Extension('_visilibity',sources = ['visilibity.i'],
		   swig_opts=['-c++'])

setup (name = 'PyVisiLibity',
       version = '1.0',
       author = 'Yu Cao',
       author_email = 'yu.cao@soton.ac.uk',
       url = 'https://github.com/tsaoyu/VisiLibity1',
       description = 'Python bindings of VisiLibity1',
       ext_modules = [module])
