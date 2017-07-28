#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: fullwidth4.py
Purpose: Class Encode/Decode with Unicode Fullwidth.
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

class CodingFW4:
    def __init__(self, mystring):
        self.mystring = mystring
	# Encode Unicode FullWidth4
        self.fw4 = { '&#xff00;' : '', '&#xff01;' : '!', '&#xff02;' : '"', '&#xff03;' : '#', '&#xff04;' : '$', '&#xff05;' : '%', '&#xff06;' : '&', '&#xff07;' : "'", '&#xff08;' : '(', '&#xff09;' : ')', '&#xff0a;' : '*', '&#xff0b;' : '+', '&#xff0c;' : ',', '&#xff0d;' : '-', '&#xff0e;' : '.', '&#xff0f;' : '/', '&#xff10;' : '0', '&#xff11;' : '1', '&#xff12;' : '2', '&#xff13;' : '3', '&#xff14;' : '4', '&#xff15;' : '5', '&#xff16;' : '6', '&#xff17;' : '7', '&#xff18;' : '8', '&#xff19;' : '9', '&#xff1a;' : ':', '&#xff1b;' : ';', '&#xff1c;' : '<', '&#xff1d;' : '=', '&#xff1e;' : '>', '&#xff1f;' : '?', '&#xff20;' : '@', '&#xff21;' : 'A', '&#xff22;' : 'B', '&#xff23;' : 'C', '&#xff24;' : 'D', '&#xff25;' : 'E', '&#xff26;' : 'F', '&#xff27;' : 'G', '&#xff28;' : 'H', '&#xff29;' : 'I', '&#xff2a;' : 'J', '&#xff2b;' : 'K', '&#xff2c;' : 'L', '&#xff2d;' : 'M', '&#xff2e;' : 'N', '&#xff2f;' : 'O', '&#xff30;' : 'P', '&#xff31;' : 'Q', '&#xff32;' : 'R', '&#xff33;' : 'S', '&#xff34;' : 'T', '&#xff35;' : 'U', '&#xff36;' : 'V', '&#xff37;' : 'W', '&#xff38;' : 'X', '&#xff39;' : 'Y', '&#xff3a;' : 'Z', '&#xff3b;' : '[', '&#xff3c;' : '\\', '&#xff3d;' : '[', '&#xff3e;' : '^', '&#xff3f;' : '_', '&#xff40;' : '`', '&#xff41;' : 'a', '&#xff42;' : 'b', '&#xff43;' : 'c', '&#xff44;' : 'd', '&#xff45;' : 'e', '&#xff46;' : 'f', '&#xff47;' : 'g', '&#xff48;' : 'h', '&#xff49;' : 'i', '&#xff4a;' : 'j', '&#xff4b;' : 'k', '&#xff4c;' : 'l', '&#xff4d;' : 'm', '&#xff4e;' : 'n', '&#xff4f;' : 'o', '&#xff50;' : 'p', '&#xff51;' : 'q', '&#xff52;' : 'r', '&#xff53;' : 's', '&#xff54;' : 't', '&#xff55;' : 'u', '&#xff56;' : 'v', '&#xff57;' : 'w', '&#xff58;' : 'x', '&#xff59;' : 'y', '&#xff5a;' : 'z', '&#xff5b;' : '{', '&#xff5c;' : '|', '&#xff5d;' : '}', '&#xff5e;' : '~', '&#xa0; ' : ' ', '&#xff81;' : '¡', '&#xff82;' : '¢', '&#xff83;' : '£', '&#xff84;' : '¤', '&#xff85;' : '¥', '&#xff86;' : '¦', '&#xff87;' : '§', '&#xff88;' : '¨', '&#xff89;' : '©', '&#xff8a;' : 'ª', '&#xff8b;' : '«', '&#xff8c;' : '¬', '&#xff8d;' : '­', '&#xff8e;' : '®', '&#xff8f;' : '¯', '&#xff90;' : '°', '&#xff91;' : '±', '&#xff92;' : '²', '&#xff93;' : '³', '&#xff94;' : '´', '&#xff95;' : 'µ', '&#xff96;' : '¶', '&#xff97;' : '·', '&#xff98;' : '¸', '&#xff99;' : '¹', '&#xff9a;' : 'º', '&#xff9b;' : '»', '&#xff9c;' : '¼', '&#xff9d;' : '½', '&#xff9e;' : '¾', '&#xff9f;' : '¿', '&#xffa0;' : 'À', '&#xffa1;' : 'Á', '&#xffa2;' : 'Â', '&#xffa3;' : 'Ã', '&#xffa4;' : 'Ä', '&#xffa5;' : 'Å', '&#xffa6;' : 'Æ', '&#xffa7;' : 'Ç', '&#xffa8;' : 'È', '&#xffa9;' : 'É', '&#xffaa;' : 'Ê', '&#xffab;' : 'Ë', '&#xffac;' : 'Ì', '&#xffad;' : 'Í', '&#xffae;' : 'Î', '&#xffaf;' : 'Ï', '&#xffb0;' : 'Ð', '&#xffb1;' : 'Ñ', '&#xffb2;' : 'Ò', '&#xffb3;' : 'Ó', '&#xffb4;' : 'Ô', '&#xffb5;' : 'Õ', '&#xffb6;' : 'Ö', '&#xffb7;' : '×', '&#xffb8;' : 'Ø', '&#xffb9;' : 'Ù', '&#xffba;' : 'Ú', '&#xffbb;' : 'Û', '&#xffbc;' : 'Ü', '&#xffbd;' : 'Ý', '&#xffbe;' : 'Þ', '&#xffbf;' : 'ß', '&#xffc0;' : 'à', '&#xffc1;' : 'á', '&#xffc2;' : 'â', '&#xffc3;' : 'ã', '&#xffc4;' : 'ä', '&#xffc5;' : 'å', '&#xffc6;' : 'æ', '&#xffc7;' : 'ç', '&#xffc8;' : 'è', '&#xffc9;' : 'é', '&#xffca;' : 'ê', '&#xffcb;' : 'ë', '&#xffcc;' : 'ì', '&#xffcd;' : 'í', '&#xffce;' : 'î', '&#xffcf;' : 'ï', '&#xffd0;' : 'ð', '&#xffd1;' : 'ñ', '&#xffd2;' : 'ò', '&#xffd3;' : 'ó', '&#xffd4;' : 'ô', '&#xffd5;' : 'õ', '&#xffd6;' : 'ö', '&#xffd7;' : '÷', '&#xffd8;' : 'ø', '&#xffd9;' : 'ù', '&#xffda;' : 'ú', '&#xffdb;' : 'û', '&#xffdc;' : 'ü', '&#xffdd;' : 'ý', '&#xffde;' : 'þ', '&#xffdf;' : 'ÿ', '&#xfeff;' : '' }

    def decoded(self):
        answer = self.mystring
        for i in self.mystring:
            for i, j in self.fw4.iteritems():
                answer = answer.replace(i, j)
        return answer

    def encoded(self):
        answer = '&#xfeff;'
        for i in self.mystring:
            for k in self.fw4:
                if i in self.fw4[k]:
                    answer += k
                    break
            else:
                answer += i
        return answer
