#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: hex_standard.py
Purpose: Class Encode/Decode with Hexadecimal Standard.
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

class CodingHexStd:
    def __init__(self, mystring):
        self.mystring = mystring
	# Encode Hexadecimal Standard
        self.hex_std = { '0x00' : '', '0x20' : ' ', '0x21' : '!', '0x22' : '"', '0x23' : '#', '0x24' : '$', '0x25' : '%', '0x26' : '&', '0x27' : "'", '0x28' : '(', '0x29' : ')', '0x2a' : '*', '0x2b' : '+', '0x2c' : ',', '0x2d' : '-', '0x2e' : '.', '0x2f' : '/', '0x30' : '0', '0x31' : '1', '0x32' : '2', '0x33' : '3', '0x34' : '4', '0x35' : '5', '0x36' : '6', '0x37' : '7', '0x38' : '8', '0x39' : '9', '0x3a' : ':', '0x3b' : ';', '0x3c' : '<', '0x3d' : '=', '0x3e' : '>', '0x3f' : '?', '0x40' : '@', '0x41' : 'A', '0x42' : 'B', '0x43' : 'C', '0x44' : 'D', '0x45' : 'E', '0x46' : 'F', '0x47' : 'G', '0x48' : 'H', '0x49' : 'I', '0x4a' : 'J', '0x4b' : 'K', '0x4c' : 'L', '0x4d' : 'M', '0x4e' : 'N', '0x4f' : 'O', '0x50' : 'P', '0x51' : 'Q', '0x52' : 'R', '0x53' : 'S', '0x54' : 'T', '0x55' : 'U', '0x56' : 'V', '0x57' : 'W', '0x58' : 'X', '0x59' : 'Y', '0x5a' : 'Z', '0x5b' : '[', '0x5c' : '\\', '0x5d' : '[', '0x5e' : '^', '0x5f' : '_', '0x60' : '`', '0x61' : 'a', '0x62' : 'b', '0x63' : 'c', '0x64' : 'd', '0x65' : 'e', '0x66' : 'f', '0x67' : 'g', '0x68' : 'h', '0x69' : 'i', '0x6a' : 'j', '0x6b' : 'k', '0x6c' : 'l', '0x6d' : 'm', '0x6e' : 'n', '0x6f' : 'o', '0x70' : 'p', '0x71' : 'q', '0x72' : 'r', '0x73' : 's', '0x74' : 't', '0x75' : 'u', '0x76' : 'v', '0x77' : 'w', '0x78' : 'x', '0x79' : 'y', '0x7a' : 'z', '0x7b' : '{', '0x7c' : '|', '0x7d' : '}', '0x7e' : '~', '0xa0' : ' ', '0xa1' : '¡', '0xa2' : '¢', '0xa3' : '£', '0xa4' : '¤', '0xa5' : '¥', '0xa6' : '¦', '0xa7' : '§', '0xa8' : '¨', '0xa9' : '©', '0xaa' : 'ª', '0xab' : '«', '0xac' : '¬', '0xad' : '­', '0xae' : '®', '0xaf' : '¯', '0xb0' : '°', '0xb1' : '±', '0xb2' : '²', '0xb3' : '³', '0xb4' : '´', '0xb5' : 'µ', '0xb6' : '¶', '0xb7' : '·', '0xb8' : '¸', '0xb9' : '¹', '0xba' : 'º', '0xbb' : '»', '0xbc' : '¼', '0xbd' : '½', '0xbe' : '¾', '0xbf' : '¿', '0xc0' : 'À', '0xc1' : 'Á', '0xc2' : 'Â', '0xc3' : 'Ã', '0xc4' : 'Ä', '0xc5' : 'Å', '0xc6' : 'Æ', '0xc7' : 'Ç', '0xc8' : 'È', '0xc9' : 'É', '0xca' : 'Ê', '0xcb' : 'Ë', '0xcc' : 'Ì', '0xcd' : 'Í', '0xce' : 'Î', '0xcf' : 'Ï', '0xd0' : 'Ð', '0xd1' : 'Ñ', '0xd2' : 'Ò', '0xd3' : 'Ó', '0xd4' : 'Ô', '0xd5' : 'Õ', '0xd6' : 'Ö', '0xd7' : '×', '0xd8' : 'Ø', '0xd9' : 'Ù', '0xda' : 'Ú', '0xdb' : 'Û', '0xdc' : 'Ü', '0xdd' : 'Ý', '0xde' : 'Þ', '0xdf' : 'ß', '0xe0' : 'à', '0xe1' : 'á', '0xe2' : 'â', '0xe3' : 'ã', '0xe4' : 'ä', '0xe5' : 'å', '0xe6' : 'æ', '0xe7' : 'ç', '0xe8' : 'è', '0xe9' : 'é', '0xea' : 'ê', '0xeb' : 'ë', '0xec' : 'ì', '0xed' : 'í', '0xee' : 'î', '0xef' : 'ï', '0xf0' : 'ð', '0xf1' : 'ñ', '0xf2' : 'ò', '0xf3' : 'ó', '0xf4' : 'ô', '0xf5' : 'õ', '0xf6' : 'ö', '0xf7' : '÷', '0xf8' : 'ø', '0xf9' : 'ù', '0xfa' : 'ú', '0xfb' : 'û', '0xfc' : 'ü', '0xfd' : 'ý', '0xfe' : 'þ', '0xff' : 'ÿ' }

    def decoded(self):
        answer = self.mystring
        for i in self.mystring:
            for i, j in self.hex_std.iteritems():
                answer = answer.replace(i, j)
        return answer

    def encoded(self):
        answer = ''
        for i in self.mystring:
            for k in self.hex_std:
                if i in self.hex_std[k]:
                    answer += k
                    break
            else:
                answer += i
        return answer
