#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: hex_ei1.py
Purpose: Class Encode/Decode with Hexadecimal EI1.
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

class CodingHexEI1:
    def __init__(self, mystring):
        self.mystring = mystring
	# Encode Hexadecimal EI1
        self.hex_ei1 = { r'\x000' : '', r'\x020' : ' ', r'\x021' : '!', r'\x022' : '"', r'\x023' : '#', r'\x024' : '$', r'\x025' : '%', r'\x026' : '&', r'\x027' : "'", r'\x028' : '(', r'\x029' : ')', r'\x02a' : '*', r'\x02b' : '+', r'\x02c' : ',', r'\x02d' : '-', r'\x02e' : '.', r'\x02f' : '/', r'\x030' : '0', r'\x031' : '1', r'\x032' : '2', r'\x033' : '3', r'\x034' : '4', r'\x035' : '5', r'\x036' : '6', r'\x037' : '7', r'\x038' : '8', r'\x039' : '9', r'\x03a' : ':', r'\x03b' : ';', r'\x03c' : '<', r'\x03d' : '=', r'\x03e' : '>', r'\x03f' : '?', r'\x040' : '@', r'\x041' : 'A', r'\x042' : 'B', r'\x043' : 'C', r'\x044' : 'D', r'\x045' : 'E', r'\x046' : 'F', r'\x047' : 'G', r'\x048' : 'H', r'\x049' : 'I', r'\x04a' : 'J', r'\x04b' : 'K', r'\x04c' : 'L', r'\x04d' : 'M', r'\x04e' : 'N', r'\x04f' : 'O', r'\x050' : 'P', r'\x051' : 'Q', r'\x052' : 'R', r'\x053' : 'S', r'\x054' : 'T', r'\x055' : 'U', r'\x056' : 'V', r'\x057' : 'W', r'\x058' : 'X', r'\x059' : 'Y', r'\x05a' : 'Z', r'\x05b' : '[', r'\x05c' : '\\', r'\x05d' : '[', r'\x05e' : '^', r'\x05f' : '_', r'\x060' : '`', r'\x061' : 'a', r'\x062' : 'b', r'\x063' : 'c', r'\x064' : 'd', r'\x065' : 'e', r'\x066' : 'f', r'\x067' : 'g', r'\x068' : 'h', r'\x069' : 'i', r'\x06a' : 'j', r'\x06b' : 'k', r'\x06c' : 'l', r'\x06d' : 'm', r'\x06e' : 'n', r'\x06f' : 'o', r'\x070' : 'p', r'\x071' : 'q', r'\x072' : 'r', r'\x073' : 's', r'\x074' : 't', r'\x075' : 'u', r'\x076' : 'v', r'\x077' : 'w', r'\x078' : 'x', r'\x079' : 'y', r'\x07a' : 'z', r'\x07b' : '{', r'\x07c' : '|', r'\x07d' : '}', r'\x07e' : '~', r'\x0a0' : ' ', r'\x0a1' : '¡', r'\x0a2' : '¢', r'\x0a3' : '£', r'\x0a4' : '¤', r'\x0a5' : '¥', r'\x0a6' : '¦', r'\x0a7' : '§', r'\x0a8' : '¨', r'\x0a9' : '©', r'\x0aa' : 'ª', r'\x0ab' : '«', r'\x0ac' : '¬', r'\x0ad' : '­', r'\x0ae' : '®', r'\x0af' : '¯', r'\x0b0' : '°', r'\x0b1' : '±', r'\x0b2' : '²', r'\x0b3' : '³', r'\x0b4' : '´', r'\x0b5' : 'µ', r'\x0b6' : '¶', r'\x0b7' : '·', r'\x0b8' : '¸', r'\x0b9' : '¹', r'\x0ba' : 'º', r'\x0bb' : '»', r'\x0bc' : '¼', r'\x0bd' : '½', r'\x0be' : '¾', r'\x0bf' : '¿', r'\x0c0' : 'À', r'\x0c1' : 'Á', r'\x0c2' : 'Â', r'\x0c3' : 'Ã', r'\x0c4' : 'Ä', r'\x0c5' : 'Å', r'\x0c6' : 'Æ', r'\x0c7' : 'Ç', r'\x0c8' : 'È', r'\x0c9' : 'É', r'\x0ca' : 'Ê', r'\x0cb' : 'Ë', r'\x0cc' : 'Ì', r'\x0cd' : 'Í', r'\x0ce' : 'Î', r'\x0cf' : 'Ï', r'\x0d0' : 'Ð', r'\x0d1' : 'Ñ', r'\x0d2' : 'Ò', r'\x0d3' : 'Ó', r'\x0d4' : 'Ô', r'\x0d5' : 'Õ', r'\x0d6' : 'Ö', r'\x0d7' : '×', r'\x0d8' : 'Ø', r'\x0d9' : 'Ù', r'\x0da' : 'Ú', r'\x0db' : 'Û', r'\x0dc' : 'Ü', r'\x0dd' : 'Ý', r'\x0de' : 'Þ', r'\x0df' : 'ß', r'\x0e0' : 'à', r'\x0e1' : 'á', r'\x0e2' : 'â', r'\x0e3' : 'ã', r'\x0e4' : 'ä', r'\x0e5' : 'å', r'\x0e6' : 'æ', r'\x0e7' : 'ç', r'\x0e8' : 'è', r'\x0e9' : 'é', r'\x0ea' : 'ê', r'\x0eb' : 'ë', r'\x0ec' : 'ì', r'\x0ed' : 'í', r'\x0ee' : 'î', r'\x0ef' : 'ï', r'\x0f0' : 'ð', r'\x0f1' : 'ñ', r'\x0f2' : 'ò', r'\x0f3' : 'ó', r'\x0f4' : 'ô', r'\x0f5' : 'õ', r'\x0f6' : 'ö', r'\x0f7' : '÷', r'\x0f8' : 'ø', r'\x0f9' : 'ù', r'\x0fa' : 'ú', r'\x0fb' : 'û', r'\x0fc' : 'ü', r'\x0fd' : 'ý', r'\x0fe' : 'þ', r'\x0ff' : 'ÿ' }

    def decoded(self):
        answer = self.mystring
        for i in self.mystring:
            for i, j in self.hex_ei1.iteritems():
                answer = answer.replace(i, j)
        return answer

    def encoded(self):
        answer = ''
        for i in self.mystring:
            for k in self.hex_ei1:
                if i in self.hex_ei1[k]:
                    answer += k
                    break
            else:
                answer += i
        return answer
