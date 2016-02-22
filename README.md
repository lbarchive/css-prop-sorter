# CSS Property Sorter Script

## Installation

    pip install sortcss.py

### Setup for Vim

1. Create `~/.vim/ftplugin/css.vim` if it's not existed yet.
2. Open `~/.vim/ftplugin/css.vim` and add new lines below:

```vim
" CSS Property Sorter Script (:SortCSS to run)
command! -range=% -nargs=* SortCSS :<line1>,<line2>!python /path/to/sortcss.py <f-args>
```

## Usage

### Command-line options

    usage: sortcss.py [-h] [-g] [--css-props-file [CSS_PROPS_FILE]]
                      [INFILE] [OUTFILE]

    positional arguments:
      INFILE                Input file
      OUTFILE               Output file

    optional arguments:
      -h, --help            show this help message and exit
      -g, --group           group properties
      --css-props-file [CSS_PROPS_FILE]
                            use custom CSS properties list file

#### CSS properties list file

You can use custom list by supplying the file to `sortcss.py`, the basic format is:

    # comment
    margin
    padding

    background
    color

The order of properties is the order that`sortcss.py` sort by and the blank line also indicates separate groups. If you have `-g`, then `sortcss.py` will insert a blank line between the groups.

### Usage in Vim

1. Open a CSS file in Vim.
2. Turn in to Visual mode.
3. Select CSS definition(s). At least 1 set of `{` to `}`.
4. Type `:SortCSS` and return.

This will automatically sort your CSS properties.

#### Notes

* You can just type `:SortCSS` so that entire properties will be sorted in a file.
* You can also append arguments as if using `sortcss.py` directly, e.g. `:SortCSS -g` for grouping.

## Credits

You can find more information about the script below:
http://lab.youck.org/css-property-order.html

This script is based on Kyo Nagashima's Perl script:
http://hail2u.net/blog/coding/perl-sort-css-properties.html

* Yu-Jie Lin, http://yjl.im
* Yu I., Twitter @japboy
* Kyo Nagashima <kyo@hail2u.net>, http://hail2u.net/
* xaicron, http://blog.livedoor.jp/xaicron/

## License

    MIT License, see COPYING
