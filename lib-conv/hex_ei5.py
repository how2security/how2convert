#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: hex_ei5.py
Purpose: Class Encode/Decode with Hexadecimal EI5.
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

class CodingHexEI5:
    def __init__(self, mystring):
        self.mystring = mystring
	# Encode Hexadecimal EI5
        self.hex_ei5 = { r'\x0000000' : '', r'\x0000020' : ' ', r'\x0000021' : '!', r'\x0000022' : '"', r'\x0000023' : '#', r'\x0000024' : '$', r'\x0000025' : '%', r'\x0000026' : '&', r'\x0000027' : "'", r'\x0000028' : '(', r'\x0000029' : ')', r'\x000002a' : '*', r'\x000002b' : '+', r'\x000002c' : ',', r'\x000002d' : '-', r'\x000002e' : '.', r'\x000002f' : '/', r'\x0000030' : '0', r'\x0000031' : '1', r'\x0000032' : '2', r'\x0000033' : '3', r'\x0000034' : '4', r'\x0000035' : '5', r'\x0000036' : '6', r'\x0000037' : '7', r'\x0000038' : '8', r'\x0000039' : '9', r'\x000003a' : ':', r'\x000003b' : ';', r'\x000003c' : '<', r'\x000003d' : '=', r'\x000003e' : '>', r'\x000003f' : '?', r'\x0000040' : '@', r'\x0000041' : 'A', r'\x0000042' : 'B', r'\x0000043' : 'C', r'\x0000044' : 'D', r'\x0000045' : 'E', r'\x0000046' : 'F', r'\x0000047' : 'G', r'\x0000048' : 'H', r'\x0000049' : 'I', r'\x000004a' : 'J', r'\x000004b' : 'K', r'\x000004c' : 'L', r'\x000004d' : 'M', r'\x000004e' : 'N', r'\x000004f' : 'O', r'\x0000050' : 'P', r'\x0000051' : 'Q', r'\x0000052' : 'R', r'\x0000053' : 'S', r'\x0000054' : 'T', r'\x0000055' : 'U', r'\x0000056' : 'V', r'\x0000057' : 'W', r'\x0000058' : 'X', r'\x0000059' : 'Y', r'\x000005a' : 'Z', r'\x000005b' : '[', r'\x000005c' : '\\', r'\x000005d' : '[', r'\x000005e' : '^', r'\x000005f' : '_', r'\x0000060' : '`', r'\x0000061' : 'a', r'\x0000062' : 'b', r'\x0000063' : 'c', r'\x0000064' : 'd', r'\x0000065' : 'e', r'\x0000066' : 'f', r'\x0000067' : 'g', r'\x0000068' : 'h', r'\x0000069' : 'i', r'\x000006a' : 'j', r'\x000006b' : 'k', r'\x000006c' : 'l', r'\x000006d' : 'm', r'\x000006e' : 'n', r'\x000006f' : 'o', r'\x0000070' : 'p', r'\x0000071' : 'q', r'\x0000072' : 'r', r'\x0000073' : 's', r'\x0000074' : 't', r'\x0000075' : 'u', r'\x0000076' : 'v', r'\x0000077' : 'w', r'\x0000078' : 'x', r'\x0000079' : 'y', r'\x000007a' : 'z', r'\x000007b' : '{', r'\x000007c' : '|', r'\x000007d' : '}', r'\x000007e' : '~', r'\x00000a0' : ' ', r'\x00000a1' : '¡', r'\x00000a2' : '¢', r'\x00000a3' : '£', r'\x00000a4' : '¤', r'\x00000a5' : '¥', r'\x00000a6' : '¦', r'\x00000a7' : '§', r'\x00000a8' : '¨', r'\x00000a9' : '©', r'\x00000aa' : 'ª', r'\x00000ab' : '«', r'\x00000ac' : '¬', r'\x00000ad' : '­', r'\x00000ae' : '®', r'\x00000af' : '¯', r'\x00000b0' : '°', r'\x00000b1' : '±', r'\x00000b2' : '²', r'\x00000b3' : '³', r'\x00000b4' : '´', r'\x00000b5' : 'µ', r'\x00000b6' : '¶', r'\x00000b7' : '·', r'\x00000b8' : '¸', r'\x00000b9' : '¹', r'\x00000ba' : 'º', r'\x00000bb' : '»', r'\x00000bc' : '¼', r'\x00000bd' : '½', r'\x00000be' : '¾', r'\x00000bf' : '¿', r'\x00000c0' : 'À', r'\x00000c1' : 'Á', r'\x00000c2' : 'Â', r'\x00000c3' : 'Ã', r'\x00000c4' : 'Ä', r'\x00000c5' : 'Å', r'\x00000c6' : 'Æ', r'\x00000c7' : 'Ç', r'\x00000c8' : 'È', r'\x00000c9' : 'É', r'\x00000ca' : 'Ê', r'\x00000cb' : 'Ë', r'\x00000cc' : 'Ì', r'\x00000cd' : 'Í', r'\x00000ce' : 'Î', r'\x00000cf' : 'Ï', r'\x00000d0' : 'Ð', r'\x00000d1' : 'Ñ', r'\x00000d2' : 'Ò', r'\x00000d3' : 'Ó', r'\x00000d4' : 'Ô', r'\x00000d5' : 'Õ', r'\x00000d6' : 'Ö', r'\x00000d7' : '×', r'\x00000d8' : 'Ø', r'\x00000d9' : 'Ù', r'\x00000da' : 'Ú', r'\x00000db' : 'Û', r'\x00000dc' : 'Ü', r'\x00000dd' : 'Ý', r'\x00000de' : 'Þ', r'\x00000df' : 'ß', r'\x00000e0' : 'à', r'\x00000e1' : 'á', r'\x00000e2' : 'â', r'\x00000e3' : 'ã', r'\x00000e4' : 'ä', r'\x00000e5' : 'å', r'\x00000e6' : 'æ', r'\x00000e7' : 'ç', r'\x00000e8' : 'è', r'\x00000e9' : 'é', r'\x00000ea' : 'ê', r'\x00000eb' : 'ë', r'\x00000ec' : 'ì', r'\x00000ed' : 'í', r'\x00000ee' : 'î', r'\x00000ef' : 'ï', r'\x00000f0' : 'ð', r'\x00000f1' : 'ñ', r'\x00000f2' : 'ò', r'\x00000f3' : 'ó', r'\x00000f4' : 'ô', r'\x00000f5' : 'õ', r'\x00000f6' : 'ö', r'\x00000f7' : '÷', r'\x00000f8' : 'ø', r'\x00000f9' : 'ù', r'\x00000fa' : 'ú', r'\x00000fb' : 'û', r'\x00000fc' : 'ü', r'\x00000fd' : 'ý', r'\x00000fe' : 'þ', r'\x00000ff' : 'ÿ' }

    def decoded(self):
        answer = self.mystring
        for i in self.mystring:
            for i, j in self.hex_ei5.iteritems():
                answer = answer.replace(i, j)
        return answer

    def encoded(self):
        answer = ''
        for i in self.mystring:
            for k in self.hex_ei5:
                if i in self.hex_ei5[k]:
                    answer += k
                    break
            else:
                answer += i
        return answer
