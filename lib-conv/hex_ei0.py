#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: hex_ei0.py
Purpose: Class Encode/Decode with Hexadecimal EI0.
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

class CodingHexEI0:
    def __init__(self, mystring):
        self.mystring = mystring
	# Encode Hexadecimal EI0
        self.hex_ei0 = { r'\x00' : '', r'\x20' : ' ', r'\x21' : '!', r'\x22' : '"', r'\x23' : '#', r'\x24' : '$', r'\x25' : '%', r'\x26' : '&', r'\x27' : "'", r'\x28' : '(', r'\x29' : ')', r'\x2a' : '*', r'\x2b' : '+', r'\x2c' : ',', r'\x2d' : '-', r'\x2e' : '.', r'\x2f' : '/', r'\x30' : '0', r'\x31' : '1', r'\x32' : '2', r'\x33' : '3', r'\x34' : '4', r'\x35' : '5', r'\x36' : '6', r'\x37' : '7', r'\x38' : '8', r'\x39' : '9', r'\x3a' : ':', r'\x3b' : ';', r'\x3c' : '<', r'\x3d' : '=', r'\x3e' : '>', r'\x3f' : '?', r'\x40' : '@', r'\x41' : 'A', r'\x42' : 'B', r'\x43' : 'C', r'\x44' : 'D', r'\x45' : 'E', r'\x46' : 'F', r'\x47' : 'G', r'\x48' : 'H', r'\x49' : 'I', r'\x4a' : 'J', r'\x4b' : 'K', r'\x4c' : 'L', r'\x4d' : 'M', r'\x4e' : 'N', r'\x4f' : 'O', r'\x50' : 'P', r'\x51' : 'Q', r'\x52' : 'R', r'\x53' : 'S', r'\x54' : 'T', r'\x55' : 'U', r'\x56' : 'V', r'\x57' : 'W', r'\x58' : 'X', r'\x59' : 'Y', r'\x5a' : 'Z', r'\x5b' : '[', r'\x5c' : '\\', r'\x5d' : '[', r'\x5e' : '^', r'\x5f' : '_', r'\x60' : '`', r'\x61' : 'a', r'\x62' : 'b', r'\x63' : 'c', r'\x64' : 'd', r'\x65' : 'e', r'\x66' : 'f', r'\x67' : 'g', r'\x68' : 'h', r'\x69' : 'i', r'\x6a' : 'j', r'\x6b' : 'k', r'\x6c' : 'l', r'\x6d' : 'm', r'\x6e' : 'n', r'\x6f' : 'o', r'\x70' : 'p', r'\x71' : 'q', r'\x72' : 'r', r'\x73' : 's', r'\x74' : 't', r'\x75' : 'u', r'\x76' : 'v', r'\x77' : 'w', r'\x78' : 'x', r'\x79' : 'y', r'\x7a' : 'z', r'\x7b' : '{', r'\x7c' : '|', r'\x7d' : '}', r'\x7e' : '~', r'\xa0' : ' ', r'\xa1' : '¡', r'\xa2' : '¢', r'\xa3' : '£', r'\xa4' : '¤', r'\xa5' : '¥', r'\xa6' : '¦', r'\xa7' : '§', r'\xa8' : '¨', r'\xa9' : '©', r'\xaa' : 'ª', r'\xab' : '«', r'\xac' : '¬', r'\xad' : '­', r'\xae' : '®', r'\xaf' : '¯', r'\xb0' : '°', r'\xb1' : '±', r'\xb2' : '²', r'\xb3' : '³', r'\xb4' : '´', r'\xb5' : 'µ', r'\xb6' : '¶', r'\xb7' : '·', r'\xb8' : '¸', r'\xb9' : '¹', r'\xba' : 'º', r'\xbb' : '»', r'\xbc' : '¼', r'\xbd' : '½', r'\xbe' : '¾', r'\xbf' : '¿', r'\xc0' : 'À', r'\xc1' : 'Á', r'\xc2' : 'Â', r'\xc3' : 'Ã', r'\xc4' : 'Ä', r'\xc5' : 'Å', r'\xc6' : 'Æ', r'\xc7' : 'Ç', r'\xc8' : 'È', r'\xc9' : 'É', r'\xca' : 'Ê', r'\xcb' : 'Ë', r'\xcc' : 'Ì', r'\xcd' : 'Í', r'\xce' : 'Î', r'\xcf' : 'Ï', r'\xd0' : 'Ð', r'\xd1' : 'Ñ', r'\xd2' : 'Ò', r'\xd3' : 'Ó', r'\xd4' : 'Ô', r'\xd5' : 'Õ', r'\xd6' : 'Ö', r'\xd7' : '×', r'\xd8' : 'Ø', r'\xd9' : 'Ù', r'\xda' : 'Ú', r'\xdb' : 'Û', r'\xdc' : 'Ü', r'\xdd' : 'Ý', r'\xde' : 'Þ', r'\xdf' : 'ß', r'\xe0' : 'à', r'\xe1' : 'á', r'\xe2' : 'â', r'\xe3' : 'ã', r'\xe4' : 'ä', r'\xe5' : 'å', r'\xe6' : 'æ', r'\xe7' : 'ç', r'\xe8' : 'è', r'\xe9' : 'é', r'\xea' : 'ê', r'\xeb' : 'ë', r'\xec' : 'ì', r'\xed' : 'í', r'\xee' : 'î', r'\xef' : 'ï', r'\xf0' : 'ð', r'\xf1' : 'ñ', r'\xf2' : 'ò', r'\xf3' : 'ó', r'\xf4' : 'ô', r'\xf5' : 'õ', r'\xf6' : 'ö', r'\xf7' : '÷', r'\xf8' : 'ø', r'\xf9' : 'ù', r'\xfa' : 'ú', r'\xfb' : 'û', r'\xfc' : 'ü', r'\xfd' : 'ý', r'\xfe' : 'þ', r'\xff' : 'ÿ' }

    def decoded(self):
        answer = self.mystring
        for i in self.mystring:
            for i, j in self.hex_ei0.iteritems():
                answer = answer.replace(i, j)
        return answer

    def encoded(self):
        answer = ''
        for i in self.mystring:
            for k in self.hex_ei0:
                if i in self.hex_ei0[k]:
                    answer += k
                    break
            else:
                answer += i
        return answer
