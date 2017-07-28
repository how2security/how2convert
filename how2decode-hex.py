#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: how2decode-hex.py
Purpose: Decode data with hexadecimal.
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
from hex_standard import CodingHexStd
from hex_straigth import CodingHexStr
from hex4_entity import CodingHex4Ent
from hex_entity import CodingHexEnt
from hex_ei0 import CodingHexEI0
from hex_ei1 import CodingHexEI1
from hex_ei2 import CodingHexEI2
from hex_ei3 import CodingHexEI3
from hex_ei4 import CodingHexEI4
from hex_ei5 import CodingHexEI5
from hex_url import CodingHexURL
from colors import *

def main():
    
    usage = '''%(prog)s [-t type_encode] [--str="data"]'''
    
    parser = argparse.ArgumentParser(usage=usage)
    
    parser.add_argument( '-t', '--type', action='store', type=str, choices=['hex0', 'hex1', 'hex2', 'hex3', 'hex4', 'hex5', 'hex6', 'hex7', 'hex8', 'hex9', 'hex10'], default='hex0', dest='enc', help='Type of Decode strings. Select '
    '[hex0 => Standard] or [hex1 => Straintg] or [hex2 => EI0] or [hex3 => EI1] or [hex4 => EI2] or [hex5 => EI3] '
    'or [hex6 => EI4] or [hex7 => EI5] or [hex8 => Entity] or [hex9 => Entity4] or [hex10 => URL')
    parser.add_argument('--str', action='store', type=str, dest='txt', help='The String Decode')
    parser.add_argument("--version", action="version", version="%(prog)s 1.0b")
    
    args = parser.parse_args()
    
    enc = args.enc
    txt = args.txt

    if len(sys.argv) < 3:
        parser.print_help()
        sys.exit(1)
    
    try:
        if (enc == 'hex0'):
            msg = CodingHexStd(txt.lower())
            print(color("[+] HEXA Standard: ", 2, 1) + "%s" % msg.decoded())
        elif (enc == 'hex1'):
            msg = CodingHexStr(txt.lower())
            print(color("[+] HEXA Straigth: ", 2, 1) + "%s" % msg.decoded())
        elif (enc == 'hex2'):
            msg = CodingHexEI0(txt.lower())
            print(color("[+] HEXA EI0: ", 2, 1) + "%s" % msg.decoded())
        elif (enc == 'hex3'):
            msg = CodingHexEI1(txt.lower())
            print(color("[+] HEXA EI1: ", 2, 1) + "%s" % msg.decoded())
        elif (enc == 'hex4'):
            msg = CodingHexEI2(txt.lower())
            print(color("[+] HEXA EI2: ", 2, 1) + "%s" % msg.decoded())
        elif (enc == 'hex5'):
            msg = CodingHexEI3(txt.lower())
            print(color("[+] HEXA EI3: ", 2, 1) + "%s" % msg.decoded())
        elif (enc == 'hex6'):
            msg = CodingHexEI4(txt.lower())
            print(color("[+] HEXA EI4: ", 2, 1) + "%s" % msg.decoded())
        elif (enc == 'hex7'):
            msg = CodingHexEI5(txt.lower())
            print(color("[+] HEXA EI5: ", 2, 1) + "%s" % msg.decoded())
        elif (enc == 'hex8'):
            msg = CodingHexEnt(txt.lower())
            print(color("[+] HEXA Entity: ", 2, 1) + "%s" % msg.decoded())
        elif (enc == 'hex9'):
            msg = CodingHex4Ent(txt.lower())
            print(color("[+] HEXA4 Entity: ", 2, 1) + "%s" % msg.decoded())
        elif (enc == 'hex10'):
            msg = CodingHexURL(txt.lower())
            print(color("[+] HEXA URL: ", 2, 1) + "%s" % msg.decoded())
    except AttributeError:
        print(color("\n[!] This data non-hexadecimal", 1, 1))
        print(color("[*] Please try usage data with how2decoded-brute-force.py\n", 3, 1))
        sys.exit(1)

if __name__ == "__main__":
    main()
