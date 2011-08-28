# CSS Property Sorter Script

## Setup for Vim

1. Create `~/.vim/ftplugin/css.vim` if it's not existed yet.
2. Open `~/.vim/ftplugin/css.vim` and add new lines below:

```vim
" CSS Property Sorter Script (:SortCSS to run)
command! -range=% SortCSS :<line1>,<line2>!python /path/to/css_prop_sorter.py
```

## Usage in Vim

1. Open a CSS file in Vim.
2. Turn in to Visual mode.
3. Select CSS definition(s). At least 1 set of `{` to `}`.
4. Type `:SortCSS` and return.

This will automatically sort your CSS properties. You can just type `:SortCSS` so that entire properties will be sorted in a file.

## Credits

You can find more information about the script below:  
http://lab.youck.org/css-property-order.html

This script is based on Kyo Nagashima's Perl script:  
http://hail2u.net/blog/coding/perl-sort-css-properties.html

* Author: Yu I. <Twitter @japboy>
* Original author: Kyo Nagashima <kyo@hail2u.net>, http://hail2u.net/ xaicron, http://blog.livedoor.jp/xaicron/
* License: MIT license (http://opensource.org/licenses/mit-license.php)
