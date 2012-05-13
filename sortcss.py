#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''CSS Property Sorter Script
This script will sort CSS properties by defined rule.

WEBSITE
https://github.com/livibetter/css-prop-sorter

CREDITS
This script is based on Kyo Nagashima's Perl script:
http://hail2u.net/blog/coding/perl-sort-css-properties.html

Author: Yu-Jie Lin <livibetter@gmail.com>, http://yjl.im
Author: Yu I. <Twitter @japboy>
Original author: Kyo Nagashima <kyo@hail2u.net>, http://hail2u.net/
                 xaicron, http://blog.livedoor.jp/xaicron/
License: MIT license, see COPYING
'''

__program__     = 'sortcss.py'
__version__     = '0.1.0'
__license__     = 'MIT'
__description__ = 'CSS Property Sorter Script'
__website__     = 'https://github.com/livibetter/css-prop-sorter'

__author__  = 'Yu-Jie Lin'
__email__   = 'livibetter@gmail.com'
__credits__ = ['Yu-Jie Lin', 'Yu I.', 'Kyo Nagashima', 'xaicron']

import argparse
import itertools
import sys
import re

CSS_PROPS_TEXT = '''
# CSS 2.1
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

# CSS 3 2D Transforms Module
transform
-moz-transform
-o-transform
-webkit-transform
transform-origin
-moz-transform-origin
-webkit-transform-origin

# CSS 3 3D Transforms Module
perspective
-webkit-perspective
perspective-origin
-webkit-perspective-origin
backface-visibility
-webkit-backface-visibility

# CSS 3 Animations Module
animation-name
-webkit-animation-name
animation-duration
-webkit-animation-duration
animation-timing-function
-webkit-animation-timing-function
animation-iteration-count
-webkit-animation-iteration-count
animation-direction
-webkit-animation-direction
animation-play-state
-webkit-animation-play-state
animation-delay
-webkit-animation-delay
animation
-webkit-animation

# CSS 3 Backgrounds and Borders Module
background-clip
-moz-background-clip
-webkit-background-clip
background-origin
-moz-background-origin
-webkit-background-origin
background-size
-moz-background-size
-o-background-size
-webkit-background-size
border-top-right-radius
border-bottom-right-radius
border-bottom-left-radius
border-top-left-radius
border-radius
-moz-border-radius
-webkit-border-radius
border-image-source
border-image-slice
border-image-width
border-image-outset
border-image-repeat
border-image
-moz-border-image
-webkit-border-image
box-decoration-break
box-shadow
-moz-box-shadow
-webkit-box-shadow

# CSS 3 Basic Box Model Module
overflow-x
-ms-overflow-x
overflow-y
-ms-overflow-y
overflow-style
marquee-style
-webkit-marquee-style
marquee-loop
marquee-direction
-webkit-marquee-direction
marquee-speed
-webkit-marquee-speed
-webkit-marquee
rotation
rotation-point

# CSS 3 Basic User Interface Module
appearance
-moz-appearance
-webkit-appearance
icon
box-sizing
-moz-box-sizing
-webkit-box-sizing
outline-offset
resize
nav-index

# CSS 3 Color Module
opacity

# CSS 3 Fonts Module
font-stretch
font-size-adjust
src
unicode-range

# CSS 3 Generated Content for Paged Media Module
string-set
bookmark-level
bookmark-label
bookmark-target
bookmark-state

# CSS 3 Grid Positioning Module
grid-columns
grid-rows

# CSS 3 Hyperlink Presentation Module
target-name
target-new
target-position
target

# CSS 3 Image Values and Replaced Content Module
linear-gradient
-moz-linear-gradient
-webkit-gradient
image-resolution

# CSS 3 Line Box Module
line-stacking-strategy
line-stacking-ruby
line-stacking-shift
line-stacking
alignment-baseline
alignment-adjust
baseline-shift
inline-box-align
drop-initial-size
drop-initial-value
drop-initial-before-align
drop-initial-before-adjust
drop-initial-after-align
drop-initial-after-adjust

# CSS 3 Multi-column Layout Module
column-width
-moz-column-width
-webkit-column-width
column-count
-moz-column-count
-webkit-column-count
columns
-webkit-columns
column-gap
-moz-column-gap
-webkit-column-gap
column-rule-color
-moz-column-rule-color
-webkit-column-rule-color
column-rule-style
-moz-column-rule-style
-webkit-column-rule-style
column-rule-width
-moz-column-rule-width
-webkit-column-rule-width
column-rule
-moz-column-rule
-webkit-column-rule
column-span
column-fill

# CSS 3 Paged Media Module
size
page
image-orientation
fit
fit-position

# CSS 3 Presentation Levels Module
presentation-level

# CSS 3 Ruby Module
ruby-position
ruby-align
ruby-overhang
ruby-span

# CSS 3 Speech Module
voice-volume
voice-balance
rest-before
rest-after
rest
voice-rate
voice-pitch
voice-range
voice-stress
voice-duration

# CSS 3 Text Module
bikeshedding
word-break
-ms-word-break
hyphens
hyphenate-character
hyphenate-resource
text-wrap
word-wrap
-ms-word-wrap
text-align-last
-ms-text-align-last
text-justify
-ms-text-justify
text-shadow
text-indent
hanging-punctuation
text-emphasis
text-shadow
text-outline

# CSS 3 Transitions Module
transition-property
-webkit-transition-property
transition-duration
-webkit-transition-duration
transition-timing-function
-webkit-transition-timing-function
transition-delay
-webkit-transition-delay
transition
-webkit-transition
'''

def compile_props(props_text, grouped=False):

    props = props_text.splitlines()
    props = filter(lambda line: not line.startswith('#'), props)
    if not grouped:
        props = list(filter(None, props))
        return props, [0]*len(props)

    g_id = 0
    final_props = []
    groups = []
    for prop in props:
      if prop.strip():
        final_props.append(prop)
        groups.append(g_id)
      else:
        g_id += 1
    return final_props, groups

def prioritify(line_buffer, pgs):
    '''Prioritizer Function
    This function will return argument's priority. Priority will be integer and
    smaller number will be higher priority.
    '''
    props, groups = pgs

    priority = 9999
    group = 0

    for css_property in props:
        if line_buffer.find(css_property + ':') != -1:
            priority = props.index(css_property)
            group = groups[priority]
            break

    return priority, group

def props_grouper(props, pgs):

    if not props:
        return props
    # zip prop with priority and group_id
    props_pg = zip(map(lambda prop: prioritify(prop, pgs), props), props)
    # sort by group id
    props_pg = sorted(props_pg, key=lambda item: item[0][1])
    # group by group id
    props_by_groups = map(lambda item: list(item[1]), itertools.groupby(props_pg, key=lambda item: item[0][1]))
    # sort each group
    props_by_groups = map(lambda item: sorted(item, key=lambda item: item[0][0]), props_by_groups)
    props = []
    for group in props_by_groups:
        # drop pg
        group = map(lambda item: item[1], group)
        props += group
        props += ['\n']
    props.pop()
    return props

def sort_properties(stdin_buffer, args):
    '''CSS Property Sorter Function
    This function will read buffer argument, split it to a list by lines,
    sort it by defined rule, and return sorted buffer if it's CSS property.
    This function depends on 'prioritify' function.
    '''
    # Initializing
    if 'css_props_text' not in args:
        args.css_props_text = CSS_PROPS_TEXT
    css_pgs = compile_props(args.css_props_text, args.group)

    pattern = re.compile(r'(.*?{\r?\n?)(.*?)(}.*?)|(.*)', re.DOTALL + re.MULTILINE)
    matched_patterns = pattern.findall(stdin_buffer)
    sorted_patterns = []
    sorted_buffer = stdin_buffer

    RE_prop = re.compile(r'((?:.*?)(?:;)(?:.*?\n)|(?:.*))', re.DOTALL + re.MULTILINE)

    if len(matched_patterns) != 0:
        for matched_groups in matched_patterns:
            sorted_patterns += matched_groups[0].splitlines(True)
            props = map(lambda line: line.lstrip('\n'),
                        RE_prop.findall(matched_groups[1]))
            props = list(filter(lambda line: line.strip('\n '), props))
            props = props_grouper(props, css_pgs)
            sorted_patterns += props
            sorted_patterns += matched_groups[2].splitlines(True)
            sorted_patterns += matched_groups[3].splitlines(True)

        sorted_buffer = ''.join(sorted_patterns)

    return sorted_buffer

def make_parser():

    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--group',
                        action='store_true',
                        default=False,
                        help='group properties')
    return parser

if __name__ == '__main__':

    parser = make_parser()
    parser.add_argument('--css-props-file',
                        nargs='?',
                        type=argparse.FileType('r'),
                        help='use custom CSS properties list file')
    if sys.stdin.isatty():
        parser.add_argument('infile',
                            nargs='?',
                            default=sys.stdin,
                            type=argparse.FileType('r'),
                            help='Input file',
                            metavar='INFILE')
    parser.add_argument('outfile',
                        nargs='?',
                        default=sys.stdout,
                        type=argparse.FileType('w'),
                        help='Output file',
                        metavar='OUTFILE')
    args = parser.parse_args()
    if not sys.stdin.isatty():
        args.infile = sys.stdin

    if args.css_props_file:
        args.css_props_text = args.css_props_file.read()

    sorted_buffer = sort_properties(args.infile.read(), args)

    if not isinstance(sorted_buffer, str):
        sys.stderr.write('Error')
        sys.exit(2)

    args.outfile.write(sorted_buffer)
