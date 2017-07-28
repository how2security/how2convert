#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: hex_ei3.py
Purpose: Class Encode/Decode with Hexadecimal EI3.
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

class CodingHexEI3:
    def __init__(self, mystring):
        self.mystring = mystring
	# Encode Hexadecimal EI3
        self.hex_ei3 = { r'\x00000' : '', r'\x00020' : ' ', r'\x00021' : '!', r'\x00022' : '"', r'\x00023' : '#', r'\x00024' : '$', r'\x00025' : '%', r'\x00026' : '&', r'\x00027' : "'", r'\x00028' : '(', r'\x00029' : ')', r'\x0002a' : '*', r'\x0002b' : '+', r'\x0002c' : ',', r'\x0002d' : '-', r'\x0002e' : '.', r'\x0002f' : '/', r'\x00030' : '0', r'\x00031' : '1', r'\x00032' : '2', r'\x00033' : '3', r'\x00034' : '4', r'\x00035' : '5', r'\x00036' : '6', r'\x00037' : '7', r'\x00038' : '8', r'\x00039' : '9', r'\x0003a' : ':', r'\x0003b' : ';', r'\x0003c' : '<', r'\x0003d' : '=', r'\x0003e' : '>', r'\x0003f' : '?', r'\x00040' : '@', r'\x00041' : 'A', r'\x00042' : 'B', r'\x00043' : 'C', r'\x00044' : 'D', r'\x00045' : 'E', r'\x00046' : 'F', r'\x00047' : 'G', r'\x00048' : 'H', r'\x00049' : 'I', r'\x0004a' : 'J', r'\x0004b' : 'K', r'\x0004c' : 'L', r'\x0004d' : 'M', r'\x0004e' : 'N', r'\x0004f' : 'O', r'\x00050' : 'P', r'\x00051' : 'Q', r'\x00052' : 'R', r'\x00053' : 'S', r'\x00054' : 'T', r'\x00055' : 'U', r'\x00056' : 'V', r'\x00057' : 'W', r'\x00058' : 'X', r'\x00059' : 'Y', r'\x0005a' : 'Z', r'\x0005b' : '[', r'\x0005c' : '\\', r'\x0005d' : '[', r'\x0005e' : '^', r'\x0005f' : '_', r'\x00060' : '`', r'\x00061' : 'a', r'\x00062' : 'b', r'\x00063' : 'c', r'\x00064' : 'd', r'\x00065' : 'e', r'\x00066' : 'f', r'\x00067' : 'g', r'\x00068' : 'h', r'\x00069' : 'i', r'\x0006a' : 'j', r'\x0006b' : 'k', r'\x0006c' : 'l', r'\x0006d' : 'm', r'\x0006e' : 'n', r'\x0006f' : 'o', r'\x00070' : 'p', r'\x00071' : 'q', r'\x00072' : 'r', r'\x00073' : 's', r'\x00074' : 't', r'\x00075' : 'u', r'\x00076' : 'v', r'\x00077' : 'w', r'\x00078' : 'x', r'\x00079' : 'y', r'\x0007a' : 'z', r'\x0007b' : '{', r'\x0007c' : '|', r'\x0007d' : '}', r'\x0007e' : '~', r'\x000a0' : ' ', r'\x000a1' : '¡', r'\x000a2' : '¢', r'\x000a3' : '£', r'\x000a4' : '¤', r'\x000a5' : '¥', r'\x000a6' : '¦', r'\x000a7' : '§', r'\x000a8' : '¨', r'\x000a9' : '©', r'\x000aa' : 'ª', r'\x000ab' : '«', r'\x000ac' : '¬', r'\x000ad' : '­', r'\x000ae' : '®', r'\x000af' : '¯', r'\x000b0' : '°', r'\x000b1' : '±', r'\x000b2' : '²', r'\x000b3' : '³', r'\x000b4' : '´', r'\x000b5' : 'µ', r'\x000b6' : '¶', r'\x000b7' : '·', r'\x000b8' : '¸', r'\x000b9' : '¹', r'\x000ba' : 'º', r'\x000bb' : '»', r'\x000bc' : '¼', r'\x000bd' : '½', r'\x000be' : '¾', r'\x000bf' : '¿', r'\x000c0' : 'À', r'\x000c1' : 'Á', r'\x000c2' : 'Â', r'\x000c3' : 'Ã', r'\x000c4' : 'Ä', r'\x000c5' : 'Å', r'\x000c6' : 'Æ', r'\x000c7' : 'Ç', r'\x000c8' : 'È', r'\x000c9' : 'É', r'\x000ca' : 'Ê', r'\x000cb' : 'Ë', r'\x000cc' : 'Ì', r'\x000cd' : 'Í', r'\x000ce' : 'Î', r'\x000cf' : 'Ï', r'\x000d0' : 'Ð', r'\x000d1' : 'Ñ', r'\x000d2' : 'Ò', r'\x000d3' : 'Ó', r'\x000d4' : 'Ô', r'\x000d5' : 'Õ', r'\x000d6' : 'Ö', r'\x000d7' : '×', r'\x000d8' : 'Ø', r'\x000d9' : 'Ù', r'\x000da' : 'Ú', r'\x000db' : 'Û', r'\x000dc' : 'Ü', r'\x000dd' : 'Ý', r'\x000de' : 'Þ', r'\x000df' : 'ß', r'\x000e0' : 'à', r'\x000e1' : 'á', r'\x000e2' : 'â', r'\x000e3' : 'ã', r'\x000e4' : 'ä', r'\x000e5' : 'å', r'\x000e6' : 'æ', r'\x000e7' : 'ç', r'\x000e8' : 'è', r'\x000e9' : 'é', r'\x000ea' : 'ê', r'\x000eb' : 'ë', r'\x000ec' : 'ì', r'\x000ed' : 'í', r'\x000ee' : 'î', r'\x000ef' : 'ï', r'\x000f0' : 'ð', r'\x000f1' : 'ñ', r'\x000f2' : 'ò', r'\x000f3' : 'ó', r'\x000f4' : 'ô', r'\x000f5' : 'õ', r'\x000f6' : 'ö', r'\x000f7' : '÷', r'\x000f8' : 'ø', r'\x000f9' : 'ù', r'\x000fa' : 'ú', r'\x000fb' : 'û', r'\x000fc' : 'ü', r'\x000fd' : 'ý', r'\x000fe' : 'þ', r'\x000ff' : 'ÿ' }

    def decoded(self):
        answer = self.mystring
        for i in self.mystring:
            for i, j in self.hex_ei3.iteritems():
                answer = answer.replace(i, j)
        return answer

    def encoded(self):
        answer = ''
        for i in self.mystring:
            for k in self.hex_ei3:
                if i in self.hex_ei3[k]:
                    answer += k
                    break
            else:
                answer += i
        return answer
