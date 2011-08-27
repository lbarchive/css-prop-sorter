#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''CSS Property Sorter Script
This script will sort CSS properties by defined rule. Script reads standard
input and sort it by lines if the lines are CSS property, and write them to
standard output.

CREDITS
This script is based on Kyo Nagashima's Perl script:
http://hail2u.net/blog/coding/perl-sort-css-properties.html

Author: Yu I. <Twitter @japboy>
Original author: Kyo Nagashima <kyo@hail2u.net>, http://hail2u.net/
                 xaicron, http://blog.livedoor.jp/xaicron/
License: MIT license (http://opensource.org/licenses/mit-license.php)
'''

import sys
import re

css_properties = []

# CSS 2.1 core properties
css_properties += '''
margin-top
margin-right
margin-bottom
margin-left
margin
padding-top
padding-right
padding-bottom
padding-left
padding
border-top-width
border-right-width
border-bottom-width
border-left-width
border-width
border-top-color
border-right-color
border-bottom-color
border-left-color
border-color
border-top-style
border-right-style
border-bottom-style
border-left-style
border-style
border-top
border-right
border-bottom
border-left
border
display
position
top
right
bottom
left
float
clear
z-index
direction
unicode-bidi
width
min-width
max-width
height
min-height
max-height
line-height
vertical-align
overflow
clip
visibility
content
quotes
counter-reset
counter-increment
list-style-type
list-style-image
list-style-position
list-style
page-break-before
page-break-after
page-break-inside
orphans
widows
color
background-color
background-image
background-repeat
background-attachment
background-position
background
font-family
font-style
font-variant
font-weight
font-size
font
text-indent
text-align
text-decoration
letter-spacing
word-spacing
text-transform
white-space
caption-side
table-layout
border-collapse
border-spacing
empty-cells
cursor
outline
outline-width
outline-style
outline-color
volume
speak
pause-before
pause-after
pause
cue-before
cue-after
cue
play-during
azimuth
elevation
speech-rate
voice-family
pitch
pitch-range
stress
richness
speak-punctuation
speak-numeral
speak-header
'''.lstrip('\n').splitlines()

def prioritify(line_buffer):
    '''Prioritizer Function
    This function will return argument's priority. Priority will be integer and
    smaller number will be higher priority.
    '''

    priority = 9999

    for css_property in css_properties:
        if line_buffer.find(css_property) != -1:
            priority = css_properties.index(css_property)
            break

    return priority

def sort_properties(stdin_buffer):
    '''CSS Property Sorter Function
    This function will read buffer argument, split it to a list by lines,
    sort it by defined rule, and return sorted buffer if it's CSS property.
    This function depends on 'prioritify' function.
    '''

    pattern = re.compile(r'(.*{\r?\n?)(.*)(}.*)', re.DOTALL + re.MULTILINE)
    matched_patterns = pattern.findall(stdin_buffer)
    sorted_patterns = []
    sorted_buffer = stdin_buffer

    if len(matched_patterns) != 0:
        for matched_groups in matched_patterns:
            sorted_patterns += matched_groups[0].splitlines(True)
            sorted_patterns += sorted(matched_groups[1].splitlines(True),
                                      key=prioritify)
            sorted_patterns += matched_groups[2].splitlines(True)

        sorted_buffer = ''.join(sorted_patterns)

    return sorted_buffer

if __name__ == '__main__':
    sorted_buffer = sort_properties(sys.stdin.read())

    if not isinstance(sorted_buffer, str):
        sys.stderr.write('Error')
        sys.exit(2)

    sys.stdout.write(sorted_buffer)