#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: uni_eiu.py
Purpose: Class Encode/Decode with Unicode EIu.
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

class CodingUniEIu:
    def __init__(self, mystring):
        self.mystring = mystring
	# Encode Unicode EIu
        self.unicode_eiu= { r'\u0000' : '', r'\u0020' : ' ', r'\u0021' : '!', r'\u0022' : '"', r'\u0023' : '#', r'\u0024' : '$', r'\u0025' : '%', r'\u0026' : '&', r'\u0027' : "'", r'\u0028' : '(', r'\u0029' : ')', r'\u002a' : '*', r'\u002b' : '+', r'\u002c' : ',', r'\u002d' : '-', r'\u002e' : '.', r'\u002f' : '/', r'\u0030' : '0', r'\u0031' : '1', r'\u0032' : '2', r'\u0033' : '3', r'\u0034' : '4', r'\u0035' : '5', r'\u0036' : '6', r'\u0037' : '7', r'\u0038' : '8', r'\u0039' : '9', r'\u003a' : ':', r'\u003b' : ';', r'\u003c' : '<', r'\u003d' : '=', r'\u003e' : '>', r'\u003f' : '?', r'\u0040' : '@', r'\u0041' : 'A', r'\u0042' : 'B', r'\u0043' : 'C', r'\u0044' : 'D', r'\u0045' : 'E', r'\u0046' : 'F', r'\u0047' : 'G', r'\u0048' : 'H', r'\u0049' : 'I', r'\u004a' : 'J', r'\u004b' : 'K', r'\u004c' : 'L', r'\u004d' : 'M', r'\u004e' : 'N', r'\u004f' : 'O', r'\u0050' : 'P', r'\u0051' : 'Q', r'\u0052' : 'R', r'\u0053' : 'S', r'\u0054' : 'T', r'\u0055' : 'U', r'\u0056' : 'V', r'\u0057' : 'W', r'\u0058' : 'X', r'\u0059' : 'Y', r'\u005a' : 'Z', r'\u005b' : '[', r'\u005c' : '\\', r'\u005d' : '[', r'\u005e' : '^', r'\u005f' : '_', r'\u0060' : '`', r'\u0061' : 'a', r'\u0062' : 'b', r'\u0063' : 'c', r'\u0064' : 'd', r'\u0065' : 'e', r'\u0066' : 'f', r'\u0067' : 'g', r'\u0068' : 'h', r'\u0069' : 'i', r'\u006a' : 'j', r'\u006b' : 'k', r'\u006c' : 'l', r'\u006d' : 'm', r'\u006e' : 'n', r'\u006f' : 'o', r'\u0070' : 'p', r'\u0071' : 'q', r'\u0072' : 'r', r'\u0073' : 's', r'\u0074' : 't', r'\u0075' : 'u', r'\u0076' : 'v', r'\u0077' : 'w', r'\u0078' : 'x', r'\u0079' : 'y', r'\u007a' : 'z', r'\u007b' : '{', r'\u007c' : '|', r'\u007d' : '}', r'\u007e' : '~', r'\u00a0' : ' ', r'\u00a1' : '¡', r'\u00a2' : '¢', r'\u00a3' : '£', r'\u00a4' : '¤', r'\u00a5' : '¥', r'\u00a6' : '¦', r'\u00a7' : '§', r'\u00a8' : '¨', r'\u00a9' : '©', r'\u00aa' : 'ª', r'\u00ab' : '«', r'\u00ac' : '¬', r'\u00ad' : '­', r'\u00ae' : '®', r'\u00af' : '¯', r'\u00b0' : '°', r'\u00b1' : '±', r'\u00b2' : '²', r'\u00b3' : '³', r'\u00b4' : '´', r'\u00b5' : 'µ', r'\u00b6' : '¶', r'\u00b7' : '·', r'\u00b8' : '¸', r'\u00b9' : '¹', r'\u00ba' : 'º', r'\u00bb' : '»', r'\u00bc' : '¼', r'\u00bd' : '½', r'\u00be' : '¾', r'\u00bf' : '¿', r'\u00c0' : 'À', r'\u00c1' : 'Á', r'\u00c2' : 'Â', r'\u00c3' : 'Ã', r'\u00c4' : 'Ä', r'\u00c5' : 'Å', r'\u00c6' : 'Æ', r'\u00c7' : 'Ç', r'\u00c8' : 'È', r'\u00c9' : 'É', r'\u00ca' : 'Ê', r'\u00cb' : 'Ë', r'\u00cc' : 'Ì', r'\u00cd' : 'Í', r'\u00ce' : 'Î', r'\u00cf' : 'Ï', r'\u00d0' : 'Ð', r'\u00d1' : 'Ñ', r'\u00d2' : 'Ò', r'\u00d3' : 'Ó', r'\u00d4' : 'Ô', r'\u00d5' : 'Õ', r'\u00d6' : 'Ö', r'\u00d7' : '×', r'\u00d8' : 'Ø', r'\u00d9' : 'Ù', r'\u00da' : 'Ú', r'\u00db' : 'Û', r'\u00dc' : 'Ü', r'\u00dd' : 'Ý', r'\u00de' : 'Þ', r'\u00df' : 'ß', r'\u00e0' : 'à', r'\u00e1' : 'á', r'\u00e2' : 'â', r'\u00e3' : 'ã', r'\u00e4' : 'ä', r'\u00e5' : 'å', r'\u00e6' : 'æ', r'\u00e7' : 'ç', r'\u00e8' : 'è', r'\u00e9' : 'é', r'\u00ea' : 'ê', r'\u00eb' : 'ë', r'\u00ec' : 'ì', r'\u00ed' : 'í', r'\u00ee' : 'î', r'\u00ef' : 'ï', r'\u00f0' : 'ð', r'\u00f1' : 'ñ', r'\u00f2' : 'ò', r'\u00f3' : 'ó', r'\u00f4' : 'ô', r'\u00f5' : 'õ', r'\u00f6' : 'ö', r'\u00f7' : '÷', r'\u00f8' : 'ø', r'\u00f9' : 'ù', r'\u00fa' : 'ú', r'\u00fb' : 'û', r'\u00fc' : 'ü', r'\u00fd' : 'ý', r'\u00fe' : 'þ', r'\u00ff' : 'ÿ' }

    def decoded(self):
        answer = self.mystring
        for i in self.mystring:
            for i, j in self.unicode_eiu.iteritems():
                answer = answer.replace(i, j)
        return answer

    def encoded(self):
        answer = ''
        for i in self.mystring:
            for k in self.unicode_eiu:
                if i in self.unicode_eiu[k]:
                    answer += k
                    break
            else:
                answer += i
        return answer
