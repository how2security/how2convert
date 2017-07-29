#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: how2encode.py
Purpose: Criate data encoded with varius type encode.
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

import base64
import sys
import argparse
#sys.path.append('/root/devel/convert/lib-conv')
sys.path.append('lib-conv')
from dec_eid import CodingDecEId
from dec_long import CodingDecLong
from dec_straigth import CodingDecStr
from fullwidth1 import CodingFW1
from fullwidth2 import CodingFW2
from fullwidth3 import CodingFW3
from fullwidth4 import CodingFW4
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
from uni_eiu import CodingUniEIu
from uni_standard import CodingUniStd
from uni_straigth import CodingUniStr
from uni_url import CodingUniURL
from js_esc import CodingJSEsc
from html_esc import CodingHTMLEsc
from colors import *

def main():
    
    usage = '''%(prog)s [-t type_encode] [--str="data"]'''
    
    parser = argparse.ArgumentParser(usage=usage)
    
    parser.add_argument( '-t', '--type', action='store', type=str, choices=['hex', 'uni', 'dec', 'fwd', 'html', 'js', 'b64', 'b32', 'b16', 'full'], default='hex', dest='enc', help='Type of Encode strings. Select [hex => Hexadecimal] or '
                                                          '[uni => Unicode] or [dec => Decimal] or [fwd => Fullwidth]' 
                                                          'or [html => escape javascript] or [b64 => base64] or '
                                                          '[full => envery encode]')
    parser.add_argument('--str', action='store', type=str, dest='txt', help='The String Encode/Decode')
    parser.add_argument("--version", action="version", version="%(prog)s 1.0b")
    
    args = parser.parse_args()
    
    enc = args.enc
    txt = args.txt
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    try:
        if (enc == 'hex'):
            msg = CodingHexStd(txt)
            print(color("[+] HEXA Standard: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingHexStr(txt)
            print(color("[+] HEXA Straigth: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingHexEI0(txt)
            print(color("[+] HEXA EI0:", 2, 1) + "%s" % msg.encoded())
            msg = CodingHexEI1(txt)
            print(color("[+] HEXA EI1: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingHexEI2(txt)
            print(color("[+] HEXA EI2: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingHexEI3(txt)
            print(color("[+] HEXA EI3: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingHexEI4(txt)
            print(color("[+] HEXA EI4: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingHexEI5(txt)
            print(color("[+] HEXA EI5: ", 2,1) + "%s" % msg.encoded())
            msg = CodingHexEnt(txt)
            print(color("[+] HEXA Entity: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingHex4Ent(txt)
            print(color("[+] HEXA4 Entity: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingHexURL(txt)
            print(color("[+] HEXA URL: ", 2, 1) + "%s" % msg.encoded())
        elif (enc == 'dec'):
            msg = CodingDecStr(txt)
            print(color("[+] DEC Straigth: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingDecLong(txt)
            print(color("[+] DEC Long: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingDecEId(txt)
            print(color("[+] DEC EId: ", 2, 1) + "%s" % msg.encoded())
        elif (enc == 'uni'):
            msg = CodingUniStd(txt)
            print(color("[+] Unicode Standard: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingUniStr(txt)
            print(color("[+] Unicode Straigth: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingUniEIu(txt)
            print(color("[+] Unicode EIu: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingUniURL(txt)
            print(color("[+] Unicode URL: ", 2, 1) + "%s" % msg.encoded())
        elif (enc == 'fwd'):
            msg = CodingFW1(txt)
            print(color("[+] Fullwidth 1: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingFW2(txt)
            print(color("[+] Fullwidth 2: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingFW3(txt)
            print(color("[+] Fullwidth 3: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingFW4(txt)
            print(color("[+] Fullwidth 4: ", 2, 1) + "%s" % msg.encoded())
        elif (enc == 'js'):
            msg = CodingJSEsc(txt)
            print(color("[+] JavaScript Escape: ", 2, 1) + "%s" % msg.encoded())
        elif (enc == 'html'):
            msg = CodingHTMLEsc(txt)
            print(color("[+] HTML Escape: ", 2, 1) + "%s" % msg.encoded())
        elif (enc == 'b16'):
            msg = base64.b16encode(txt)
            print(color("[+] Base16: ", 2, 1) + "%s" % msg)
        elif (enc == 'b32'):
            msg = base64.b32encode(txt)
            print(color("[+] Base32: ", 2, 1) + "%s" % msg)
        elif (enc == 'b64'):
            msg = base64.b64encode(txt)
            print(color("[+] Base64: ", 2, 1) + "%s" % msg)
        elif (enc == 'full'):
            msg = CodingHexStd(txt)
            print(color("[+] HEXA Standard: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingHexStr(txt)
            print(color("[+] HEXA Straigth: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingHexEI0(txt)
            print(color("[+] HEXA EI0: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingHexEI1(txt)
            print(color("[+] HEXA EI1: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingHexEI2(txt)
            print(color("[+] HEXA EI2: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingHexEI3(txt)
            print(color("[+] HEXA EI3: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingHexEI4(txt)
            print(color("[+] HEXA EI4: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingHexEI5(txt)
            print(color("[+] HEXA EI5: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingHexEnt(txt)
            print(color("[+] HEXA Entity: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingHex4Ent(txt)
            print(color("[+] HEXA4 Entity: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingHexURL(txt)
            print(color("[+] HEXA URL: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingDecStr(txt)
            print(color("[+] DEC Straigth: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingDecLong(txt)
            print(color("[+] DEC Long: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingDecEId(txt)
            print(color("[+] DEC EId: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingUniStd(txt)
            print(color("[+] Unicode Standard: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingUniStr(txt)
            print(color("[+] Unicode Straigth: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingUniEIu(txt)
            print(color("[+] Unicode EIu: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingUniURL(txt)
            print(color("[+] Unicode URL: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingFW1(txt)
            print(color("[+] Fullwidth 1: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingFW2(txt)
            print(color("[+] Fullwidth 2: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingFW3(txt)
            print(color("[+] Fullwidth 3: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingFW4(txt)
            print(color("[+] Fullwidth 4: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingJSEsc(txt)
            print(color("[+] JavaScript Escape: ", 2, 1) + "%s" % msg.encoded())
            msg = CodingHTMLEsc(txt)
            print(color("[+] HTML Escape: ", 2, 1) + "%s" % msg.encoded())
            msg = base64.b16encode(txt)
            print(color("[+] Base16: ", 2, 1) + "%s" % msg)
            msg = base64.b32encode(txt)
            print(color("[+] Base32: ", 2, 1) + "%s" % msg)
            msg = base64.b64encode(txt)
            print(color("[+] Base64: ", 2, 1) + "%s" % msg)
    except AttributeError:
        print(color("\n[!] This data not valid", 1, 1))
        parser.print_help()
        sys.exit(1)
    except TypeError:
        print(color("\n[!] This data non base[16|32|64]", 1, 1))
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()

