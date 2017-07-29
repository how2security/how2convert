#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: hex4_entity.py
Purpose: Class Encode/Decode with Hexadecimal Entiry 4.
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

class CodingHex4Ent:
    def __init__(self, mystring):
        self.mystring = mystring
	# Encode Hexadecimal Entity 4
        self.hex4_ent = { '&#x0000;' : '', '&#x0020;' : ' ', '&#x0021;' : '!', '&#x0022;' : '"', '&#x0023;' : '#', '&#x0024;' : '$', '&#x0025;' : '%', '&#x0026;' : '&', '&#x0027;' : "'", '&#x0028;' : '(', '&#x0029;' : ')', '&#x002a;' : '*', '&#x002b;' : '+', '&#x002c;' : ',', '&#x002d;' : '-', '&#x002e;' : '.', '&#x002f;' : '/', '&#x0030;' : '0', '&#x0031;' : '1', '&#x0032;' : '2', '&#x0033;' : '3', '&#x0034;' : '4', '&#x0035;' : '5', '&#x0036;' : '6', '&#x0037;' : '7', '&#x0038;' : '8', '&#x0039;' : '9', '&#x003a;' : ':', '&#x003b;' : ';', '&#x003c;' : '<', '&#x003d;' : '=', '&#x003e;' : '>', '&#x003f;' : '?', '&#x0040;' : '@', '&#x0041;' : 'A', '&#x0042;' : 'B', '&#x0043;' : 'C', '&#x0044;' : 'D', '&#x0045;' : 'E', '&#x0046;' : 'F', '&#x0047;' : 'G', '&#x0048;' : 'H', '&#x0049;' : 'I', '&#x004a;' : 'J', '&#x004b;' : 'K', '&#x004c;' : 'L', '&#x004d;' : 'M', '&#x004e;' : 'N', '&#x004f;' : 'O', '&#x0050;' : 'P', '&#x0051;' : 'Q', '&#x0052;' : 'R', '&#x0053;' : 'S', '&#x0054;' : 'T', '&#x0055;' : 'U', '&#x0056;' : 'V', '&#x0057;' : 'W', '&#x0058;' : 'X', '&#x0059;' : 'Y', '&#x005a;' : 'Z', '&#x005b;' : '[', '&#x005c;' : '\\', '&#x005d;' : '[', '&#x005e;' : '^', '&#x005f;' : '_', '&#x0060;' : '`', '&#x0061;' : 'a', '&#x0062;' : 'b', '&#x0063;' : 'c', '&#x0064;' : 'd', '&#x0065;' : 'e', '&#x0066;' : 'f', '&#x0067;' : 'g', '&#x0068;' : 'h', '&#x0069;' : 'i', '&#x006a;' : 'j', '&#x006b;' : 'k', '&#x006c;' : 'l', '&#x006d;' : 'm', '&#x006e;' : 'n', '&#x006f;' : 'o', '&#x0070;' : 'p', '&#x0071;' : 'q', '&#x0072;' : 'r', '&#x0073;' : 's', '&#x0074;' : 't', '&#x0075;' : 'u', '&#x0076;' : 'v', '&#x0077;' : 'w', '&#x0078;' : 'x', '&#x0079;' : 'y', '&#x007a;' : 'z', '&#x007b;' : '{', '&#x007c;' : '|', '&#x007d;' : '}', '&#x007e;' : '~', '&#x00a0;' : ' ', '&#x00a1;' : '¡', '&#x00a2;' : '¢', '&#x00a3;' : '£', '&#x00a4;' : '¤', '&#x00a5;' : '¥', '&#x00a6;' : '¦', '&#x00a7;' : '§', '&#x00a8;' : '¨', '&#x00a9;' : '©', '&#x00aa;' : 'ª', '&#x00ab;' : '«', '&#x00ac;' : '¬', '&#x00ad;' : '­', '&#x00ae;' : '®', '&#x00af;' : '¯', '&#x00b0;' : '°', '&#x00b1;' : '±', '&#x00b2;' : '²', '&#x00b3;' : '³', '&#x00b4;' : '´', '&#x00b5;' : 'µ', '&#x00b6;' : '¶', '&#x00b7;' : '·', '&#x00b8;' : '¸', '&#x00b9;' : '¹', '&#x00ba;' : 'º', '&#x00bb;' : '»', '&#x00bc;' : '¼', '&#x00bd;' : '½', '&#x00be;' : '¾', '&#x00bf;' : '¿', '&#x00c0;' : 'À', '&#x00c1;' : 'Á', '&#x00c2;' : 'Â', '&#x00c3;' : 'Ã', '&#x00c4;' : 'Ä', '&#x00c5;' : 'Å', '&#x00c6;' : 'Æ', '&#x00c7;' : 'Ç', '&#x00c8;' : 'È', '&#x00c9;' : 'É', '&#x00ca;' : 'Ê', '&#x00cb;' : 'Ë', '&#x00cc;' : 'Ì', '&#x00cd;' : 'Í', '&#x00ce;' : 'Î', '&#x00cf;' : 'Ï', '&#x00d0;' : 'Ð', '&#x00d1;' : 'Ñ', '&#x00d2;' : 'Ò', '&#x00d3;' : 'Ó', '&#x00d4;' : 'Ô', '&#x00d5;' : 'Õ', '&#x00d6;' : 'Ö', '&#x00d7;' : '×', '&#x00d8;' : 'Ø', '&#x00d9;' : 'Ù', '&#x00da;' : 'Ú', '&#x00db;' : 'Û', '&#x00dc;' : 'Ü', '&#x00dd;' : 'Ý', '&#x00de;' : 'Þ', '&#x00df;' : 'ß', '&#x00e0;' : 'à', '&#x00e1;' : 'á', '&#x00e2;' : 'â', '&#x00e3;' : 'ã', '&#x00e4;' : 'ä', '&#x00e5;' : 'å', '&#x00e6;' : 'æ', '&#x00e7;' : 'ç', '&#x00e8;' : 'è', '&#x00e9;' : 'é', '&#x00ea;' : 'ê', '&#x00eb;' : 'ë', '&#x00ec;' : 'ì', '&#x00ed;' : 'í', '&#x00ee;' : 'î', '&#x00ef;' : 'ï', '&#x00f0;' : 'ð', '&#x00f1;' : 'ñ', '&#x00f2;' : 'ò', '&#x00f3;' : 'ó', '&#x00f4;' : 'ô', '&#x00f5;' : 'õ', '&#x00f6;' : 'ö', '&#x00f7;' : '÷', '&#x00f8;' : 'ø', '&#x00f9;' : 'ù', '&#x00fa;' : 'ú', '&#x00fb;' : 'û', '&#x00fc;' : 'ü', '&#x00fd;' : 'ý', '&#x00fe;' : 'þ', '&#x00ff;' : 'ÿ' }

    def decoded(self):
        answer = self.mystring
        for i in self.mystring:
            for i, j in self.hex4_ent.iteritems():
                answer = answer.replace(i, j)
        return answer

    def encoded(self):
        answer = ''
        for i in self.mystring:
            for k in self.hex4_ent:
                if i in self.hex4_ent[k]:
                    answer += k
                    break
            else:
                answer += i
        return answer
