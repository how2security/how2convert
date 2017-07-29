#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: uni_straigth.py
Purpose: Class Encode/Decode with Unicode Straigth.
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

class CodingUniStr:
    def __init__(self, mystring):
        self.mystring = mystring
	# Encode Unicode Straigth
        self.unicode_str= { '0000' : '', '0020' : ' ', '0021' : '!', '0022' : '"', '0023' : '#', '0024' : '$', '0025' : '%', '0026' : '&', '0027' : "'", '0028' : '(', '0029' : ')', '002a' : '*', '002b' : '+', '002c' : ',', '002d' : '-', '002e' : '.', '002f' : '/', '0030' : '0', '0031' : '1', '0032' : '2', '0033' : '3', '0034' : '4', '0035' : '5', '0036' : '6', '0037' : '7', '0038' : '8', '0039' : '9', '003a' : ':', '003b' : ';', '003c' : '<', '003d' : '=', '003e' : '>', '003f' : '?', '0040' : '@', '0041' : 'A', '0042' : 'B', '0043' : 'C', '0044' : 'D', '0045' : 'E', '0046' : 'F', '0047' : 'G', '0048' : 'H', '0049' : 'I', '004a' : 'J', '004b' : 'K', '004c' : 'L', '004d' : 'M', '004e' : 'N', '004f' : 'O', '0050' : 'P', '0051' : 'Q', '0052' : 'R', '0053' : 'S', '0054' : 'T', '0055' : 'U', '0056' : 'V', '0057' : 'W', '0058' : 'X', '0059' : 'Y', '005a' : 'Z', '005b' : '[', '005c' : '\\', '005d' : '[', '005e' : '^', '005f' : '_', '0060' : '`', '0061' : 'a', '0062' : 'b', '0063' : 'c', '0064' : 'd', '0065' : 'e', '0066' : 'f', '0067' : 'g', '0068' : 'h', '0069' : 'i', '006a' : 'j', '006b' : 'k', '006c' : 'l', '006d' : 'm', '006e' : 'n', '006f' : 'o', '0070' : 'p', '0071' : 'q', '0072' : 'r', '0073' : 's', '0074' : 't', '0075' : 'u', '0076' : 'v', '0077' : 'w', '0078' : 'x', '0079' : 'y', '007a' : 'z', '007b' : '{', '007c' : '|', '007d' : '}', '007e' : '~', '00a0' : ' ', '00a1' : '¡', '00a2' : '¢', '00a3' : '£', '00a4' : '¤', '00a5' : '¥', '00a6' : '¦', '00a7' : '§', '00a8' : '¨', '00a9' : '©', '00aa' : 'ª', '00ab' : '«', '00ac' : '¬', '00ad' : '­', '00ae' : '®', '00af' : '¯', '00b0' : '°', '00b1' : '±', '00b2' : '²', '00b3' : '³', '00b4' : '´', '00b5' : 'µ', '00b6' : '¶', '00b7' : '·', '00b8' : '¸', '00b9' : '¹', '00ba' : 'º', '00bb' : '»', '00bc' : '¼', '00bd' : '½', '00be' : '¾', '00bf' : '¿', '00c0' : 'À', '00c1' : 'Á', '00c2' : 'Â', '00c3' : 'Ã', '00c4' : 'Ä', '00c5' : 'Å', '00c6' : 'Æ', '00c7' : 'Ç', '00c8' : 'È', '00c9' : 'É', '00ca' : 'Ê', '00cb' : 'Ë', '00cc' : 'Ì', '00cd' : 'Í', '00ce' : 'Î', '00cf' : 'Ï', '00d0' : 'Ð', '00d1' : 'Ñ', '00d2' : 'Ò', '00d3' : 'Ó', '00d4' : 'Ô', '00d5' : 'Õ', '00d6' : 'Ö', '00d7' : '×', '00d8' : 'Ø', '00d9' : 'Ù', '00da' : 'Ú', '00db' : 'Û', '00dc' : 'Ü', '00dd' : 'Ý', '00de' : 'Þ', '00df' : 'ß', '00e0' : 'à', '00e1' : 'á', '00e2' : 'â', '00e3' : 'ã', '00e4' : 'ä', '00e5' : 'å', '00e6' : 'æ', '00e7' : 'ç', '00e8' : 'è', '00e9' : 'é', '00ea' : 'ê', '00eb' : 'ë', '00ec' : 'ì', '00ed' : 'í', '00ee' : 'î', '00ef' : 'ï', '00f0' : 'ð', '00f1' : 'ñ', '00f2' : 'ò', '00f3' : 'ó', '00f4' : 'ô', '00f5' : 'õ', '00f6' : 'ö', '00f7' : '÷', '00f8' : 'ø', '00f9' : 'ù', '00fa' : 'ú', '00fb' : 'û', '00fc' : 'ü', '00fd' : 'ý', '00fe' : 'þ', '00ff' : 'ÿ' }

    def decoded(self):
        answer = self.mystring
        for i in self.mystring:
            for i, j in self.unicode_str.iteritems():
                answer = answer.replace(i, j)
        return answer

    def encoded(self):
        answer = ''
        for i in self.mystring:
            for k in self.unicode_str:
                if i in self.unicode_str[k]:
                    answer += k
                    break
            else:
                answer += i
        return answer
