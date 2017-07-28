#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: uni_standard.py
Purpose: Class Encode/Decode with Unicode Standard.
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

class CodingUniStd:
    def __init__(self, mystring):
        self.mystring = mystring
	# Encode Unicode Standard
        self.unicode_std= { 'u0000' : '', 'u0020' : ' ', 'u0021' : '!', 'u0022' : '"', 'u0023' : '#', 'u0024' : '$', 'u0025' : '%', 'u0026' : '&', 'u0027' : "'", 'u0028' : '(', 'u0029' : ')', 'u002a' : '*', 'u002b' : '+', 'u002c' : ',', 'u002d' : '-', 'u002e' : '.', 'u002f' : '/', 'u0030' : '0', 'u0031' : '1', 'u0032' : '2', 'u0033' : '3', 'u0034' : '4', 'u0035' : '5', 'u0036' : '6', 'u0037' : '7', 'u0038' : '8', 'u0039' : '9', 'u003a' : ':', 'u003b' : ';', 'u003c' : '<', 'u003d' : '=', 'u003e' : '>', 'u003f' : '?', 'u0040' : '@', 'u0041' : 'A', 'u0042' : 'B', 'u0043' : 'C', 'u0044' : 'D', 'u0045' : 'E', 'u0046' : 'F', 'u0047' : 'G', 'u0048' : 'H', 'u0049' : 'I', 'u004a' : 'J', 'u004b' : 'K', 'u004c' : 'L', 'u004d' : 'M', 'u004e' : 'N', 'u004f' : 'O', 'u0050' : 'P', 'u0051' : 'Q', 'u0052' : 'R', 'u0053' : 'S', 'u0054' : 'T', 'u0055' : 'U', 'u0056' : 'V', 'u0057' : 'W', 'u0058' : 'X', 'u0059' : 'Y', 'u005a' : 'Z', 'u005b' : '[', 'u005c' : '\\', 'u005d' : '[', 'u005e' : '^', 'u005f' : '_', 'u0060' : '`', 'u0061' : 'a', 'u0062' : 'b', 'u0063' : 'c', 'u0064' : 'd', 'u0065' : 'e', 'u0066' : 'f', 'u0067' : 'g', 'u0068' : 'h', 'u0069' : 'i', 'u006a' : 'j', 'u006b' : 'k', 'u006c' : 'l', 'u006d' : 'm', 'u006e' : 'n', 'u006f' : 'o', 'u0070' : 'p', 'u0071' : 'q', 'u0072' : 'r', 'u0073' : 's', 'u0074' : 't', 'u0075' : 'u', 'u0076' : 'v', 'u0077' : 'w', 'u0078' : 'x', 'u0079' : 'y', 'u007a' : 'z', 'u007b' : '{', 'u007c' : '|', 'u007d' : '}', 'u007e' : '~', 'u00a0' : ' ', 'u00a1' : '¡', 'u00a2' : '¢', 'u00a3' : '£', 'u00a4' : '¤', 'u00a5' : '¥', 'u00a6' : '¦', 'u00a7' : '§', 'u00a8' : '¨', 'u00a9' : '©', 'u00aa' : 'ª', 'u00ab' : '«', 'u00ac' : '¬', 'u00ad' : '­', 'u00ae' : '®', 'u00af' : '¯', 'u00b0' : '°', 'u00b1' : '±', 'u00b2' : '²', 'u00b3' : '³', 'u00b4' : '´', 'u00b5' : 'µ', 'u00b6' : '¶', 'u00b7' : '·', 'u00b8' : '¸', 'u00b9' : '¹', 'u00ba' : 'º', 'u00bb' : '»', 'u00bc' : '¼', 'u00bd' : '½', 'u00be' : '¾', 'u00bf' : '¿', 'u00c0' : 'À', 'u00c1' : 'Á', 'u00c2' : 'Â', 'u00c3' : 'Ã', 'u00c4' : 'Ä', 'u00c5' : 'Å', 'u00c6' : 'Æ', 'u00c7' : 'Ç', 'u00c8' : 'È', 'u00c9' : 'É', 'u00ca' : 'Ê', 'u00cb' : 'Ë', 'u00cc' : 'Ì', 'u00cd' : 'Í', 'u00ce' : 'Î', 'u00cf' : 'Ï', 'u00d0' : 'Ð', 'u00d1' : 'Ñ', 'u00d2' : 'Ò', 'u00d3' : 'Ó', 'u00d4' : 'Ô', 'u00d5' : 'Õ', 'u00d6' : 'Ö', 'u00d7' : '×', 'u00d8' : 'Ø', 'u00d9' : 'Ù', 'u00da' : 'Ú', 'u00db' : 'Û', 'u00dc' : 'Ü', 'u00dd' : 'Ý', 'u00de' : 'Þ', 'u00df' : 'ß', 'u00e0' : 'à', 'u00e1' : 'á', 'u00e2' : 'â', 'u00e3' : 'ã', 'u00e4' : 'ä', 'u00e5' : 'å', 'u00e6' : 'æ', 'u00e7' : 'ç', 'u00e8' : 'è', 'u00e9' : 'é', 'u00ea' : 'ê', 'u00eb' : 'ë', 'u00ec' : 'ì', 'u00ed' : 'í', 'u00ee' : 'î', 'u00ef' : 'ï', 'u00f0' : 'ð', 'u00f1' : 'ñ', 'u00f2' : 'ò', 'u00f3' : 'ó', 'u00f4' : 'ô', 'u00f5' : 'õ', 'u00f6' : 'ö', 'u00f7' : '÷', 'u00f8' : 'ø', 'u00f9' : 'ù', 'u00fa' : 'ú', 'u00fb' : 'û', 'u00fc' : 'ü', 'u00fd' : 'ý', 'u00fe' : 'þ', 'u00ff' : 'ÿ' }

    def decoded(self):
        answer = self.mystring
        for i in self.mystring:
            for i, j in self.unicode_std.iteritems():
                answer = answer.replace(i, j)
        return answer

    def encoded(self):
        answer = ''
        for i in self.mystring:
            for k in self.unicode_std:
                if i in self.unicode_std[k]:
                    answer += k
                    break
            else:
                answer += i
        return answer
