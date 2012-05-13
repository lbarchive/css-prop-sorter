#!/usr/bin/env python

'''CSS Property Sorter Script Unittest

Copyright (c) 2012 Yu-Jie Lin

Author: Yu-Jie Lin <livibetter@gmail.com>, http://yjl.im
License: MIT license (http://opensource.org/licenses/mit-license.php)
'''


from __future__ import print_function
import glob
import os.path
import unittest
import sys

sys.path.append('..')
sys.dont_write_bytecode = True
from sortcss import make_parser, sort_properties as SP
sys.dont_write_bytecode = False


def F(filename):

    with open(filename) as f:
        return f.read()


class TestFile(unittest.TestCase):

    def __init__(self, basename, n, args_line, args, methodName='runTest'):

        super(TestFile, self).__init__(methodName)
        self.basename = basename
        self.n = n
        self.args_line = args_line
        self.args = args

        self.source = basename + '-0.css'
        self.expect = '%s-%s.css' % (basename, n)
        # For appending text after default error message
        self.longMessage = True

    def runTest(self):
        
        err_msg = '\n' \
            '* Source  : %s\n' \
            '* Expect  : %s\n' \
            '* Arg line: %s\n' \
            '* Argparse: %s' \
            % (self.source, self.expect, self.args_line, self.args)
        self.assertMultiLineEqual(SP(F(self.source), self.args),
                                  F(self.expect),
                                  err_msg)
        

if __name__ == '__main__':

    parser = make_parser()
    suite = unittest.TestSuite()
    for src in glob.glob('case/test-????-0.css'):
        basename = src.replace('-0.css', '')
        arg = basename + '.arg'
        add_one = True
        if os.path.exists(arg):
            with open(arg) as f:
                for line in f:
                    n, args_line = line.rstrip('\n').split(' ', 1)
                    if n == '1':
                        add_one = False
                    args = parser.parse_args(args_line.split())
                    testcase = TestFile(basename, n, args_line, args)
                    suite.addTest(testcase)
        if add_one:
          suite.addTest(TestFile(basename, '1', '', parser.parse_args('')))
    unittest.TextTestRunner().run(suite)
