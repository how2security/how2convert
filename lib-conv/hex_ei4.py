#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: hex_ei4.py
Purpose: Class Encode/Decode with Hexadecimal EI4.
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

class CodingHexEI4:
    def __init__(self, mystring):
        self.mystring = mystring
	# Encode Hexadecimal EI4
        self.hex_ei4 = { r'\x000000' : '', r'\x000020' : ' ', r'\x000021' : '!', r'\x000022' : '"', r'\x000023' : '#', r'\x000024' : '$', r'\x000025' : '%', r'\x000026' : '&', r'\x000027' : "'", r'\x000028' : '(', r'\x000029' : ')', r'\x00002a' : '*', r'\x00002b' : '+', r'\x00002c' : ',', r'\x00002d' : '-', r'\x00002e' : '.', r'\x00002f' : '/', r'\x000030' : '0', r'\x000031' : '1', r'\x000032' : '2', r'\x000033' : '3', r'\x000034' : '4', r'\x000035' : '5', r'\x000036' : '6', r'\x000037' : '7', r'\x000038' : '8', r'\x000039' : '9', r'\x00003a' : ':', r'\x00003b' : ';', r'\x00003c' : '<', r'\x00003d' : '=', r'\x00003e' : '>', r'\x00003f' : '?', r'\x000040' : '@', r'\x000041' : 'A', r'\x000042' : 'B', r'\x000043' : 'C', r'\x000044' : 'D', r'\x000045' : 'E', r'\x000046' : 'F', r'\x000047' : 'G', r'\x000048' : 'H', r'\x000049' : 'I', r'\x00004a' : 'J', r'\x00004b' : 'K', r'\x00004c' : 'L', r'\x00004d' : 'M', r'\x00004e' : 'N', r'\x00004f' : 'O', r'\x000050' : 'P', r'\x000051' : 'Q', r'\x000052' : 'R', r'\x000053' : 'S', r'\x000054' : 'T', r'\x000055' : 'U', r'\x000056' : 'V', r'\x000057' : 'W', r'\x000058' : 'X', r'\x000059' : 'Y', r'\x00005a' : 'Z', r'\x00005b' : '[', r'\x00005c' : '\\', r'\x00005d' : '[', r'\x00005e' : '^', r'\x00005f' : '_', r'\x000060' : '`', r'\x000061' : 'a', r'\x000062' : 'b', r'\x000063' : 'c', r'\x000064' : 'd', r'\x000065' : 'e', r'\x000066' : 'f', r'\x000067' : 'g', r'\x000068' : 'h', r'\x000069' : 'i', r'\x00006a' : 'j', r'\x00006b' : 'k', r'\x00006c' : 'l', r'\x00006d' : 'm', r'\x00006e' : 'n', r'\x00006f' : 'o', r'\x000070' : 'p', r'\x000071' : 'q', r'\x000072' : 'r', r'\x000073' : 's', r'\x000074' : 't', r'\x000075' : 'u', r'\x000076' : 'v', r'\x000077' : 'w', r'\x000078' : 'x', r'\x000079' : 'y', r'\x00007a' : 'z', r'\x00007b' : '{', r'\x00007c' : '|', r'\x00007d' : '}', r'\x00007e' : '~', r'\x0000a0' : ' ', r'\x0000a1' : '¡', r'\x0000a2' : '¢', r'\x0000a3' : '£', r'\x0000a4' : '¤', r'\x0000a5' : '¥', r'\x0000a6' : '¦', r'\x0000a7' : '§', r'\x0000a8' : '¨', r'\x0000a9' : '©', r'\x0000aa' : 'ª', r'\x0000ab' : '«', r'\x0000ac' : '¬', r'\x0000ad' : '­', r'\x0000ae' : '®', r'\x0000af' : '¯', r'\x0000b0' : '°', r'\x0000b1' : '±', r'\x0000b2' : '²', r'\x0000b3' : '³', r'\x0000b4' : '´', r'\x0000b5' : 'µ', r'\x0000b6' : '¶', r'\x0000b7' : '·', r'\x0000b8' : '¸', r'\x0000b9' : '¹', r'\x0000ba' : 'º', r'\x0000bb' : '»', r'\x0000bc' : '¼', r'\x0000bd' : '½', r'\x0000be' : '¾', r'\x0000bf' : '¿', r'\x0000c0' : 'À', r'\x0000c1' : 'Á', r'\x0000c2' : 'Â', r'\x0000c3' : 'Ã', r'\x0000c4' : 'Ä', r'\x0000c5' : 'Å', r'\x0000c6' : 'Æ', r'\x0000c7' : 'Ç', r'\x0000c8' : 'È', r'\x0000c9' : 'É', r'\x0000ca' : 'Ê', r'\x0000cb' : 'Ë', r'\x0000cc' : 'Ì', r'\x0000cd' : 'Í', r'\x0000ce' : 'Î', r'\x0000cf' : 'Ï', r'\x0000d0' : 'Ð', r'\x0000d1' : 'Ñ', r'\x0000d2' : 'Ò', r'\x0000d3' : 'Ó', r'\x0000d4' : 'Ô', r'\x0000d5' : 'Õ', r'\x0000d6' : 'Ö', r'\x0000d7' : '×', r'\x0000d8' : 'Ø', r'\x0000d9' : 'Ù', r'\x0000da' : 'Ú', r'\x0000db' : 'Û', r'\x0000dc' : 'Ü', r'\x0000dd' : 'Ý', r'\x0000de' : 'Þ', r'\x0000df' : 'ß', r'\x0000e0' : 'à', r'\x0000e1' : 'á', r'\x0000e2' : 'â', r'\x0000e3' : 'ã', r'\x0000e4' : 'ä', r'\x0000e5' : 'å', r'\x0000e6' : 'æ', r'\x0000e7' : 'ç', r'\x0000e8' : 'è', r'\x0000e9' : 'é', r'\x0000ea' : 'ê', r'\x0000eb' : 'ë', r'\x0000ec' : 'ì', r'\x0000ed' : 'í', r'\x0000ee' : 'î', r'\x0000ef' : 'ï', r'\x0000f0' : 'ð', r'\x0000f1' : 'ñ', r'\x0000f2' : 'ò', r'\x0000f3' : 'ó', r'\x0000f4' : 'ô', r'\x0000f5' : 'õ', r'\x0000f6' : 'ö', r'\x0000f7' : '÷', r'\x0000f8' : 'ø', r'\x0000f9' : 'ù', r'\x0000fa' : 'ú', r'\x0000fb' : 'û', r'\x0000fc' : 'ü', r'\x0000fd' : 'ý', r'\x0000fe' : 'þ', r'\x0000ff' : 'ÿ' }

    def decoded(self):
        answer = self.mystring
        for i in self.mystring:
            for i, j in self.hex_ei4.iteritems():
                answer = answer.replace(i, j)
        return answer

    def encoded(self):
        answer = ''
        for i in self.mystring:
            for k in self.hex_ei4:
                if i in self.hex_ei4[k]:
                    answer += k
                    break
            else:
                answer += i
        return answer
