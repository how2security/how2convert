#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: how2decode-uni.py
Purpose: Decode data with Unicode.
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
from uni_eiu import CodingUniEIu
from uni_standard import CodingUniStd
from uni_straigth import CodingUniStr
from uni_url import CodingUniURL
from colors import *

def main():
    
    usage = '''%(prog)s [-t type_encode] [--str="data"]'''
    
    parser = argparse.ArgumentParser(usage=usage)
    
    parser.add_argument('-t', '--type', action='store', type=str, choices=['uni0', 'uni1', 'uni2', 'uni3'], default='uni0', dest='enc', help='Type of Decode strings. Select [uni0 => Standard] or [uni1 => Straigth] or [uni2 => EIu] '
    'or [uni3 => URL]')
    parser.add_argument('--str', action='store', type=str, dest='txt', help='The String Decode')
    parser.add_argument("--version", action="version", version="%(prog)s 1.0b")
    
    args = parser.parse_args()
    
    enc = args.enc
    txt = args.txt

    if len(sys.argv) < 3:
        parser.print_help()
        sys.exit(1)
    
    try:
        if (enc == 'uni0'):
            msg = CodingUniStd(txt.lower())
            print(color("[+] Unicode Standard: ", 2, 1) + "%s" % msg.decoded())
        elif (enc == 'uni1'):
            msg = CodingUniStr(txt.lower())
            print(color("[+] Unicode Straigth: ", 2, 1) + "%s" % msg.decoded())
        elif (enc == 'uni2'):
            msg = CodingUniEIu(txt.lower())
            print(color("[+] Unicode EIu: ", 2, 1) + "%s" % msg.decoded())
        elif (enc == 'uni3'):
            msg = CodingUniURL(txt.lower())
            print(color("[+] Unicode URL: ", 2, 1) + "%s" % msg.decoded())
    except AttributeError:
        print(color("\n[!] This data non-unicode", 1, 1))
        print(color("[*] Please try usage data with how2decoded-brute-force.py\n", 3, 1))
        sys.exit(1)

if __name__ == "__main__":
    main()
