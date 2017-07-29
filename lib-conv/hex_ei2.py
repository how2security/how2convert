#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: hex_ei2.py
Purpose: Class Encode/Decode with Hexadecimal EI2.
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

class CodingHexEI2:
    def __init__(self, mystring):
        self.mystring = mystring
	# Encode Hexadecimal EI2
        self.hex_ei2 = { r'\x0000' : '', r'\x0020' : ' ', r'\x0021' : '!', r'\x0022' : '"', r'\x0023' : '#', r'\x0024' : '$', r'\x0025' : '%', r'\x0026' : '&', r'\x0027' : "'", r'\x0028' : '(', r'\x0029' : ')', r'\x002a' : '*', r'\x002b' : '+', r'\x002c' : ',', r'\x002d' : '-', r'\x002e' : '.', r'\x002f' : '/', r'\x0030' : '0', r'\x0031' : '1', r'\x0032' : '2', r'\x0033' : '3', r'\x0034' : '4', r'\x0035' : '5', r'\x0036' : '6', r'\x0037' : '7', r'\x0038' : '8', r'\x0039' : '9', r'\x003a' : ':', r'\x003b' : ';', r'\x003c' : '<', r'\x003d' : '=', r'\x003e' : '>', r'\x003f' : '?', r'\x0040' : '@', r'\x0041' : 'A', r'\x0042' : 'B', r'\x0043' : 'C', r'\x0044' : 'D', r'\x0045' : 'E', r'\x0046' : 'F', r'\x0047' : 'G', r'\x0048' : 'H', r'\x0049' : 'I', r'\x004a' : 'J', r'\x004b' : 'K', r'\x004c' : 'L', r'\x004d' : 'M', r'\x004e' : 'N', r'\x004f' : 'O', r'\x0050' : 'P', r'\x0051' : 'Q', r'\x0052' : 'R', r'\x0053' : 'S', r'\x0054' : 'T', r'\x0055' : 'U', r'\x0056' : 'V', r'\x0057' : 'W', r'\x0058' : 'X', r'\x0059' : 'Y', r'\x005a' : 'Z', r'\x005b' : '[', r'\x005c' : '\\', r'\x005d' : '[', r'\x005e' : '^', r'\x005f' : '_', r'\x0060' : '`', r'\x0061' : 'a', r'\x0062' : 'b', r'\x0063' : 'c', r'\x0064' : 'd', r'\x0065' : 'e', r'\x0066' : 'f', r'\x0067' : 'g', r'\x0068' : 'h', r'\x0069' : 'i', r'\x006a' : 'j', r'\x006b' : 'k', r'\x006c' : 'l', r'\x006d' : 'm', r'\x006e' : 'n', r'\x006f' : 'o', r'\x0070' : 'p', r'\x0071' : 'q', r'\x0072' : 'r', r'\x0073' : 's', r'\x0074' : 't', r'\x0075' : 'u', r'\x0076' : 'v', r'\x0077' : 'w', r'\x0078' : 'x', r'\x0079' : 'y', r'\x007a' : 'z', r'\x007b' : '{', r'\x007c' : '|', r'\x007d' : '}', r'\x007e' : '~', r'\x00a0' : ' ', r'\x00a1' : '¡', r'\x00a2' : '¢', r'\x00a3' : '£', r'\x00a4' : '¤', r'\x00a5' : '¥', r'\x00a6' : '¦', r'\x00a7' : '§', r'\x00a8' : '¨', r'\x00a9' : '©', r'\x00aa' : 'ª', r'\x00ab' : '«', r'\x00ac' : '¬', r'\x00ad' : '­', r'\x00ae' : '®', r'\x00af' : '¯', r'\x00b0' : '°', r'\x00b1' : '±', r'\x00b2' : '²', r'\x00b3' : '³', r'\x00b4' : '´', r'\x00b5' : 'µ', r'\x00b6' : '¶', r'\x00b7' : '·', r'\x00b8' : '¸', r'\x00b9' : '¹', r'\x00ba' : 'º', r'\x00bb' : '»', r'\x00bc' : '¼', r'\x00bd' : '½', r'\x00be' : '¾', r'\x00bf' : '¿', r'\x00c0' : 'À', r'\x00c1' : 'Á', r'\x00c2' : 'Â', r'\x00c3' : 'Ã', r'\x00c4' : 'Ä', r'\x00c5' : 'Å', r'\x00c6' : 'Æ', r'\x00c7' : 'Ç', r'\x00c8' : 'È', r'\x00c9' : 'É', r'\x00ca' : 'Ê', r'\x00cb' : 'Ë', r'\x00cc' : 'Ì', r'\x00cd' : 'Í', r'\x00ce' : 'Î', r'\x00cf' : 'Ï', r'\x00d0' : 'Ð', r'\x00d1' : 'Ñ', r'\x00d2' : 'Ò', r'\x00d3' : 'Ó', r'\x00d4' : 'Ô', r'\x00d5' : 'Õ', r'\x00d6' : 'Ö', r'\x00d7' : '×', r'\x00d8' : 'Ø', r'\x00d9' : 'Ù', r'\x00da' : 'Ú', r'\x00db' : 'Û', r'\x00dc' : 'Ü', r'\x00dd' : 'Ý', r'\x00de' : 'Þ', r'\x00df' : 'ß', r'\x00e0' : 'à', r'\x00e1' : 'á', r'\x00e2' : 'â', r'\x00e3' : 'ã', r'\x00e4' : 'ä', r'\x00e5' : 'å', r'\x00e6' : 'æ', r'\x00e7' : 'ç', r'\x00e8' : 'è', r'\x00e9' : 'é', r'\x00ea' : 'ê', r'\x00eb' : 'ë', r'\x00ec' : 'ì', r'\x00ed' : 'í', r'\x00ee' : 'î', r'\x00ef' : 'ï', r'\x00f0' : 'ð', r'\x00f1' : 'ñ', r'\x00f2' : 'ò', r'\x00f3' : 'ó', r'\x00f4' : 'ô', r'\x00f5' : 'õ', r'\x00f6' : 'ö', r'\x00f7' : '÷', r'\x00f8' : 'ø', r'\x00f9' : 'ù', r'\x00fa' : 'ú', r'\x00fb' : 'û', r'\x00fc' : 'ü', r'\x00fd' : 'ý', r'\x00fe' : 'þ', r'\x00ff' : 'ÿ' }

    def decoded(self):
        answer = self.mystring
        for i in self.mystring:
            for i, j in self.hex_ei2.iteritems():
                answer = answer.replace(i, j)
        return answer

    def encoded(self):
        answer = ''
        for i in self.mystring:
            for k in self.hex_ei2:
                if i in self.hex_ei2[k]:
                    answer += k
                    break
            else:
                answer += i
        return answer
