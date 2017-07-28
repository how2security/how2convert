#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: how2decode-dec.py
Purpose: Decode data with decimal.
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
from dec_eid import CodingDecEId
from dec_long import CodingDecLong
from dec_straigth import CodingDecStr
from colors import *

def main():
    
    usage = '''%(prog)s [-t type_encode] [--str="data"]'''
    
    parser = argparse.ArgumentParser(usage=usage)
    
    parser.add_argument( '-t', '--type', action='store', type=str, choices=['dec1', 'dec2', 'dec3'], default='dec1', dest='enc', help='Type of Decode strings. Select [dec1 => Straigth] or [dec2 => Long] or [dec3 => EId]')
    parser.add_argument('--str', action='store', type=str, dest='txt', help='The String Decode')
    parser.add_argument("--version", action="version", version="%(prog)s 1.0b")
    
    args = parser.parse_args()
    
    enc = args.enc
    txt = args.txt
    
    if len(sys.argv) < 3:
        parser.print_help()
        sys.exit(1)
        
    try:
        if (enc == 'dec1'):
            msg = CodingDecStr(txt.lower())
            print(color("[+] DEC Straigth: ", 2, 1) + "%s" % msg.decoded())
            print(color("[*] Removing dot...", 4, 1))
            msg_notdot = msg.decoded()
            msg_notdot = msg_notdot.replace('..','++++++++++')
            msg_notdot = msg_notdot.replace('.', '')
            msg_notdot = msg_notdot.replace('++++++++++','.')
            print(color("[+] DEC Straigth without dot: ", 2, 1) + "%s" % msg_notdot)
        elif (enc == 'dec2'):
            msg = CodingDecLong(txt.lower())
            print(color("[+] DEC Long: ", 2, 1) + "%s" % msg.decoded())
        elif (enc == 'dec3'):
            msg = CodingDecEId(txt.lower())
            print(color("[+] DEC EId: ", 2, 1) + "%s" % msg.decoded())
    except AttributeError:
        print(color("\n[!] This data non-decimal", 1, 1))
        print(color("[*] Please try usage data with how2decoded-brute-force.py\n", 3, 1))
        sys.exit(1)

if __name__ == "__main__":
    main()
