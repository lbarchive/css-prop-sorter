#!/usr/bin/env python

from setuptools import setup

script_name = 'sortcss.py'

with open(script_name) as f:
  meta = dict(
    (k.strip(' _'), eval(v)) for k, v in
      # There will be a '\n', with eval(), it's safe to ignore
      (line.split('=') for line in f if line.startswith('__'))
    )

classifiers = [
  'Development Status :: 3 - Alpha',
  'Environment :: Console',
  'Intended Audience :: Developers',
  'License :: OSI Approved :: MIT License',
  'Natural Language :: English',
  'Operating System :: POSIX',
  'Programming Language :: Python :: 2.7',
  'Programming Language :: Python :: 3',
  'Topic :: Utilities',
  ]

setup_d = dict(
  name        = meta['program'],
  version     = meta['version'],
  license     = meta['license'],
  url         = meta['website'],

  description = meta['description'],

  classifiers = classifiers,

  author       = meta['author'],
  author_email = meta['email'],
  
  scripts = [script_name],

  install_requires = ['distribute'],
  )

if __name__ == '__main__':
  setup(**setup_d)
