#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: fullwidth3.py
Purpose: Class Encode/Decode with Unicode Fullwidth.
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

class CodingFW3:
    def __init__(self, mystring):
        self.mystring = mystring
	# Encode Unicode Fullwidth3
        self.fw3 = { r'%ef%bc%80' : ' ', r'%ef%bc%81' : '!', r'%ef%bc%82' : '"', r'%ef%bc%83' : '#', r'%ef%bc%84' : '$', r'%ef%bc%85' : r'%', r'%ef%bc%86' : '&', r'%ef%bc%87' : "'", r'%ef%bc%88' : '(', r'%ef%bc%89' : ')', r'%ef%bc%8a' : '*', r'%ef%bc%8b' : '+', r'%ef%bc%8c' : ',', r'%ef%bc%8d' : '-', r'%ef%bc%8e' : '.', r'%ef%bc%8f' : '/', r'%ef%bc%90' : '0', r'%ef%bc%91' : '1', r'%ef%bc%92' : '2', r'%ef%bc%93' : '3', r'%ef%bc%94' : '4', r'%ef%bc%95' : '5', r'%ef%bc%96' : '6', r'%ef%bc%97' : '7', r'%ef%bc%98' : '8', r'%ef%bc%99' : '9', r'%ef%bc%9a' : ':', r'%ef%bc%9b' : ';', r'%ef%bc%9c' : '<', r'%ef%bc%9d' : '=', r'%ef%bc%9e' : '>', r'%ef%bc%9f' : '?', r'%ef%bc%a0' : '@', r'%ef%bc%a1' : 'A', r'%ef%bc%a2' : 'B', r'%ef%bc%a3' : 'C', r'%ef%bc%a4' : 'D', r'%ef%bc%a5' : 'E', r'%ef%bc%a6' : 'F', r'%ef%bc%a7' : 'G', r'%ef%bc%a8' : 'H', r'%ef%bc%a9' : 'I', r'%ef%bc%aa' : 'J', r'%ef%bc%ab' : 'K', r'%ef%bc%ac' : 'L', r'%ef%bc%ad' : 'M', r'%ef%bc%ae' : 'N', r'%ef%bc%af' : 'O', r'%ef%bc%b0' : 'P', r'%ef%bc%b1' : 'Q', r'%ef%bc%b2' : 'R', r'%ef%bc%b3' : 'S', r'%ef%bc%b4' : 'T', r'%ef%bc%b5' : 'U', r'%ef%bc%b6' : 'V', r'%ef%bc%b7' : 'W', r'%ef%bc%b8' : 'X', r'%ef%bc%b9' : 'Y', r'%ef%bc%ba' : 'Z', r'%ef%bc%bb' : '[', r'%ef%bc%bc' : '\\', r'%ef%bc%bd' : '[', r'%ef%bc%be' : '^', r'%ef%bc%bf' : '_', r'%ef%bd%80' : '`', r'%ef%bd%81' : 'a', r'%ef%bd%82' : 'b', r'%ef%bd%83' : 'c', r'%ef%bd%84' : 'd', r'%ef%bd%85' : 'e', r'%ef%bd%86' : 'f', r'%ef%bd%87' : 'g', r'%ef%bd%88' : 'h', r'%ef%bd%89' : 'i', r'%ef%bd%8a' : 'j', r'%ef%bd%8b' : 'k', r'%ef%bd%8c' : 'l', r'%ef%bd%8d' : 'm', r'%ef%bd%8e' : 'n', r'%ef%bd%8f' : 'o', r'%ef%bd%90' : 'p', r'%ef%bd%91' : 'q', r'%ef%bd%92' : 'r', r'%ef%bd%93' : 's', r'%ef%bd%94' : 't', r'%ef%bd%95' : 'u', r'%ef%bd%96' : 'v', r'%ef%bd%97' : 'w', r'%ef%bd%98' : 'x', r'%ef%bd%99' : 'y', r'%ef%bd%9a' : 'z', r'%ef%bd%9b' : '{', r'%ef%bd%9c' : '|', r'%ef%bd%9d' : '}', r'%ef%bd%9e' : '~', r'%ef%be%80' : ' ', r'%ef%be%81' : '¡', r'%ef%be%82' : '¢', r'%ef%be%83' : '£', r'%ef%be%84' : '¤', r'%ef%be%85' : '¥', r'%ef%be%86' : '¦', r'%ef%be%87' : '§', r'%ef%be%88' : '¨', r'%ef%be%89' : '©', r'%ef%be%8a' : 'ª', r'%ef%be%8b' : '«', r'%ef%be%8c' : '¬', r'%ef%be%8d' : '­', r'%ef%be%8e' : '®', r'%ef%be%8f' : '¯', r'%ef%be%90' : '°', r'%ef%be%91' : '±', r'%ef%be%92' : '²', r'%ef%be%93' : '³', r'%ef%be%94' : '´', r'%ef%be%95' : 'µ', r'%ef%be%96' : '¶', r'%ef%be%97' : '·', r'%ef%be%98' : '¸', r'%ef%be%99' : '¹', r'%ef%be%9a' : 'º', r'%ef%be%9b' : '»', r'%ef%be%9c' : '¼', r'%ef%be%9d' : '½', r'%ef%be%9e' : '¾', r'%ef%be%9f' : '¿', r'%ef%be%a0' : 'À', r'%ef%be%a1' : 'Á', r'%ef%be%a2' : 'Â', r'%ef%be%a3' : 'Ã', r'%ef%be%a4' : 'Ä', r'%ef%be%a5' : 'Å', r'%ef%be%a6' : 'Æ', r'%ef%be%a7' : 'Ç', r'%ef%be%a8' : 'È', r'%ef%be%a9' : 'É', r'%ef%be%aa' : 'Ê', r'%ef%be%ab' : 'Ë', r'%ef%be%ac' : 'Ì', r'%ef%be%ad' : 'Í', r'%ef%be%ae' : 'Î', r'%ef%be%af' : 'Ï', r'%ef%be%b0' : 'Ð', r'%ef%be%b1' : 'Ñ', r'%ef%be%b2' : 'Ò', r'%ef%be%b3' : 'Ó', r'%ef%be%b4' : 'Ô', r'%ef%be%b5' : 'Õ', r'%ef%be%b6' : 'Ö', r'%ef%be%b7' : '×', r'%ef%be%b8' : 'Ø', r'%ef%be%b9' : 'Ù', r'%ef%be%ba' : 'Ú', r'%ef%be%bb' : 'Û', r'%ef%be%bc' : 'Ü', r'%ef%be%bd' : 'Ý', r'%ef%be%be' : 'Þ', r'%ef%be%bf' : 'ß', r'%ef%bf%80' : 'à', r'%ef%bf%81' : 'á', r'%ef%bf%82' : 'â', r'%ef%bf%83' : 'ã', r'%ef%bf%84' : 'ä', r'%ef%bf%85' : 'å', r'%ef%bf%86' : 'æ', r'%ef%bf%87' : 'ç', r'%ef%bf%88' : 'è', r'%ef%bf%89' : 'é', r'%ef%bf%8a' : 'ê', r'%ef%bf%8b' : 'ë', r'%ef%bf%8c' : 'ì', r'%ef%bf%8d' : 'í', r'%ef%bf%8e' : 'î', r'%ef%bf%8f' : 'ï', r'%ef%bf%90' : 'ð', r'%ef%bf%91' : 'ñ', r'%ef%bf%92' : 'ò', r'%ef%bf%93' : 'ó', r'%ef%bf%94' : 'ô', r'%ef%bf%95' : 'õ', r'%ef%bf%96' : 'ö', r'%ef%bf%97' : '÷', r'%ef%bf%98' : 'ø', r'%ef%bf%99' : 'ù', r'%ef%bf%9a' : 'ú', r'%ef%bf%9b' : 'û', r'%ef%bf%9c' : 'ü', r'%ef%bf%9d' : 'ý', r'%ef%bf%9e' : 'þ', r'%ef%bf%9f' : 'ÿ' }

    def decoded(self):
        answer = self.mystring
        for i in self.mystring:
            for i, j in self.fw3.iteritems():
                answer = answer.replace(i, j)
        return answer

    def encoded(self):
        answer = ''
        for i in self.mystring:
            for k in self.fw3:
                if i in self.fw3[k]:
                    answer += k
                    break
            else:
                answer += i
        return answer
