#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: how2decode-fw.py
Purpose: Decode data with fullwidth.
Description: Script Based on script CAL9000 by Chris Loomis from OWASP Project, posted at:
                     <https://www.owasp.org/index.php/Category:OWASP_CAL9000_Project>
Version: 1.0B
Licence: GNU3
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
from fullwidth1 import CodingFW1
from fullwidth2 import CodingFW2
from fullwidth3 import CodingFW3
from fullwidth4 import CodingFW4
from colors import *

def main():
    
    usage = '''%(prog)s [-t type_encode] [--str="data"]'''
    
    parser = argparse.ArgumentParser(usage=usage)
    
    parser.add_argument( '-t', '--type', action='store', type=str, choices=['fw1', 'fw2', 'fw3', 'fw4'], default='fw1', dest='enc', help='Type of Decode strings. Select [fw1 => Fullwidth 1] or [fw2 => Fullwidth 2] or [fw3 => Fullwidth 3] '
            'or [fwd4 => Fullwidth 4]')
    parser.add_argument('--str', action='store', type=str, dest='txt', help='The String Decode')
    parser.add_argument("--version", action="version", version="%(prog)s 1.0b")
    
    args = parser.parse_args()
    
    enc = args.enc
    txt = args.txt

    if len(sys.argv) < 3:
        parser.print_help()
        sys.exet(1)
    
    try:
        if (enc == 'fw1'):
            msg = CodingFW1(txt.lower())
            print(color("[+] Fullwidth 1: ", 2, 1) + "%s" % msg.decoded())
        elif (enc == 'fw2'):
            msg = CodingFW2(txt.lower())
            print(color("[+] Fullwidth 2: ", 2, 1) + "%s" % msg.decoded())
        elif (enc == 'fw3'):
            msg = CodingFW3(txt.lower())
            print(color("[+] Fullwidth 3: ", 2, 1) + "%s" % msg.decoded())
        elif (enc == 'fw4'):
            msg = CodingFW4(txt.lower())
            print(color("[+] Fullwidth 4: ", 2, 1) + "%s" % msg.decoded())
    except AttributeError:
        print(color("\n[!] This data non-fullwidth", 1, 1))
        print(color("[*] Please try usage data with how2decoded-brute-force.py\n", 3, 1))
        sys.exit(1)

if __name__ == "__main__":
    main()
