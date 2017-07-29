#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: how2decode-js.py
Purpose: Decode data with JavaScript Escape.
Description: Script Based on script CAL9000 by Chris Loomis from OWASP Project, posted at:
                     <https://www.owasp.org/index.php/Category:OWASP_CAL9000_Project>
Version: 1.0B
Licence: GPLv3
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.

Other itens: Copyright (c) 2017, How2Security All rights reserved.
'''

import sys
import string
import argparse
sys.path.append('lib-conv')
from js_esc import CodingJSEsc
from colors import *

def main():
    
    usage = '''%(prog)s [--str="data"]'''
    
    parser = argparse.ArgumentParser(usage=usage)
    
    parser.add_argument('--str', action='store', type=str, dest='txt', help='The String Decode')
    parser.add_argument("--version", action="version", version="%(prog)s 1.0b")
    
    args = parser.parse_args()
    
    txt = args.txt

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    try:  
        msg = CodingJSEsc(txt.lower())
        print(color("[+] JavaScript Escape: ", 2, 1) + "%s" % msg.decoded())
    except AttributeError:
        print(color("\n[!] This data non-javascript", 1, 1))
        print(color("[*] Please try usage data with how2decoded-brute-force.py\n", 3, 1))
        sys.exit(1)

if __name__ == "__main__":
    main()

