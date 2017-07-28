#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: hex_entity.py
Purpose: Class Encode/Decode with Hexadecimal Entity.
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

class CodingHexEnt:
    def __init__(self, mystring):
        self.mystring = mystring
	# Encode Hexadecimal Entity
        self.hex_ent = { '&#x00;' : '', '&#x20;' : ' ', '&#x21;' : '!', '&#x22;' : '"', '&#x23;' : '#', '&#x24;' : '$', '&#x25;' : '%', '&#x26;' : '&', '&#x27;' : "'", '&#x28;' : '(', '&#x29;' : ')', '&#x2a;' : '*', '&#x2b;' : '+', '&#x2c;' : ',', '&#x2d;' : '-', '&#x2e;' : '.', '&#x2f;' : '/', '&#x30;' : '0', '&#x31;' : '1', '&#x32;' : '2', '&#x33;' : '3', '&#x34;' : '4', '&#x35;' : '5', '&#x36;' : '6', '&#x37;' : '7', '&#x38;' : '8', '&#x39;' : '9', '&#x3a;' : ':', '&#x3b;' : ';', '&#x3c;' : '<', '&#x3d;' : '=', '&#x3e;' : '>', '&#x3f;' : '?', '&#x40;' : '@', '&#x41;' : 'A', '&#x42;' : 'B', '&#x43;' : 'C', '&#x44;' : 'D', '&#x45;' : 'E', '&#x46;' : 'F', '&#x47;' : 'G', '&#x48;' : 'H', '&#x49;' : 'I', '&#x4a;' : 'J', '&#x4b;' : 'K', '&#x4c;' : 'L', '&#x4d;' : 'M', '&#x4e;' : 'N', '&#x4f;' : 'O', '&#x50;' : 'P', '&#x51;' : 'Q', '&#x52;' : 'R', '&#x53;' : 'S', '&#x54;' : 'T', '&#x55;' : 'U', '&#x56;' : 'V', '&#x57;' : 'W', '&#x58;' : 'X', '&#x59;' : 'Y', '&#x5a;' : 'Z', '&#x5b;' : '[', '&#x5c;' : '\\', '&#x5d;' : '[', '&#x5e;' : '^', '&#x5f;' : '_', '&#x60;' : '`', '&#x61;' : 'a', '&#x62;' : 'b', '&#x63;' : 'c', '&#x64;' : 'd', '&#x65;' : 'e', '&#x66;' : 'f', '&#x67;' : 'g', '&#x68;' : 'h', '&#x69;' : 'i', '&#x6a;' : 'j', '&#x6b;' : 'k', '&#x6c;' : 'l', '&#x6d;' : 'm', '&#x6e;' : 'n', '&#x6f;' : 'o', '&#x70;' : 'p', '&#x71;' : 'q', '&#x72;' : 'r', '&#x73;' : 's', '&#x74;' : 't', '&#x75;' : 'u', '&#x76;' : 'v', '&#x77;' : 'w', '&#x78;' : 'x', '&#x79;' : 'y', '&#x7a;' : 'z', '&#x7b;' : '{', '&#x7c;' : '|', '&#x7d;' : '}', '&#x7e;' : '~', '&#xa0;' : ' ', '&#xa1;' : '¡', '&#xa2;' : '¢', '&#xa3;' : '£', '&#xa4;' : '¤', '&#xa5;' : '¥', '&#xa6;' : '¦', '&#xa7;' : '§', '&#xa8;' : '¨', '&#xa9;' : '©', '&#xaa;' : 'ª', '&#xab;' : '«', '&#xac;' : '¬', '&#xad;' : '­', '&#xae;' : '®', '&#xaf;' : '¯', '&#xb0;' : '°', '&#xb1;' : '±', '&#xb2;' : '²', '&#xb3;' : '³', '&#xb4;' : '´', '&#xb5;' : 'µ', '&#xb6;' : '¶', '&#xb7;' : '·', '&#xb8;' : '¸', '&#xb9;' : '¹', '&#xba;' : 'º', '&#xbb;' : '»', '&#xbc;' : '¼', '&#xbd;' : '½', '&#xbe;' : '¾', '&#xbf;' : '¿', '&#xc0;' : 'À', '&#xc1;' : 'Á', '&#xc2;' : 'Â', '&#xc3;' : 'Ã', '&#xc4;' : 'Ä', '&#xc5;' : 'Å', '&#xc6;' : 'Æ', '&#xc7;' : 'Ç', '&#xc8;' : 'È', '&#xc9;' : 'É', '&#xca;' : 'Ê', '&#xcb;' : 'Ë', '&#xcc;' : 'Ì', '&#xcd;' : 'Í', '&#xce;' : 'Î', '&#xcf;' : 'Ï', '&#xd0;' : 'Ð', '&#xd1;' : 'Ñ', '&#xd2;' : 'Ò', '&#xd3;' : 'Ó', '&#xd4;' : 'Ô', '&#xd5;' : 'Õ', '&#xd6;' : 'Ö', '&#xd7;' : '×', '&#xd8;' : 'Ø', '&#xd9;' : 'Ù', '&#xda;' : 'Ú', '&#xdb;' : 'Û', '&#xdc;' : 'Ü', '&#xdd;' : 'Ý', '&#xde;' : 'Þ', '&#xdf;' : 'ß', '&#xe0;' : 'à', '&#xe1;' : 'á', '&#xe2;' : 'â', '&#xe3;' : 'ã', '&#xe4;' : 'ä', '&#xe5;' : 'å', '&#xe6;' : 'æ', '&#xe7;' : 'ç', '&#xe8;' : 'è', '&#xe9;' : 'é', '&#xea;' : 'ê', '&#xeb;' : 'ë', '&#xec;' : 'ì', '&#xed;' : 'í', '&#xee;' : 'î', '&#xef;' : 'ï', '&#xf0;' : 'ð', '&#xf1;' : 'ñ', '&#xf2;' : 'ò', '&#xf3;' : 'ó', '&#xf4;' : 'ô', '&#xf5;' : 'õ', '&#xf6;' : 'ö', '&#xf7;' : '÷', '&#xf8;' : 'ø', '&#xf9;' : 'ù', '&#xfa;' : 'ú', '&#xfb;' : 'û', '&#xfc;' : 'ü', '&#xfd;' : 'ý', '&#xfe;' : 'þ', '&#xff;' : 'ÿ' }

    def decoded(self):
        answer = self.mystring
        for i in self.mystring:
            for i, j in self.hex_ent.iteritems():
                answer = answer.replace(i, j)
        return answer

    def encoded(self):
        answer = ''
        for i in self.mystring:
            for k in self.hex_ent:
                if i in self.hex_ent[k]:
                    answer += k
                    break
            else:
                answer += i
        return answer