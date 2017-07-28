#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: fullwidth2.py
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

class CodingFW2:
    def __init__(self, mystring):
        self.mystring = mystring
	# Encode Unicode FullWidth2
        self.fw2 = { 'u+ff00' : '', 'u+ff01' : '!', 'u+ff02' : '"', 'u+ff03' : '#', 'u+ff04' : '$', 'u+ff05' : '%', 'u+ff06' : '&', 'u+ff07' : "'", 'u+ff08' : '(', 'u+ff09' : ')', 'u+ff0a' : '*', 'u+ff0b' : '+', 'u+ff0c' : ',', 'u+ff0d' : '-', 'u+ff0e' : '.', 'u+ff0f' : r'/', 'u+ff10' : '0', 'u+ff11' : '1', 'u+ff12' : '2', 'u+ff13' : '3', 'u+ff14' : '4', 'u+ff15' : '5', 'u+ff16' : '6', 'u+ff17' : '7', 'u+ff18' : '8', 'u+ff19' : '9', 'u+ff1a' : ':', 'u+ff1b' : ';', 'u+ff1c' : '<', 'u+ff1d' : '=', 'u+ff1e' : '>', 'u+ff1f' : '?', 'u+ff20' : '@', 'u+ff21' : 'A', 'u+ff22' : 'B', 'u+ff23' : 'C', 'u+ff24' : 'D', 'u+ff25' : 'E', 'u+ff26' : 'F', 'u+ff27' : 'G', 'u+ff28' : 'H', 'u+ff29' : 'I', 'u+ff2a' : 'J', 'u+ff2b' : 'K', 'u+ff2c' : 'L', 'u+ff2d' : 'M', 'u+ff2e' : 'N', 'u+ff2f' : 'O', 'u+ff30' : 'P', 'u+ff31' : 'Q', 'u+ff32' : 'R', 'u+ff33' : 'S', 'u+ff34' : 'T', 'u+ff35' : 'U', 'u+ff36' : 'V', 'u+ff37' : 'W', 'u+ff38' : 'X', 'u+ff39' : 'Y', 'u+ff3a' : 'Z', 'u+ff3b' : '[', 'u+ff3c' : '\\', 'u+ff3d' : '[', 'u+ff3e' : '^', 'u+ff3f' : '_', 'u+ff40' : '`', 'u+ff41' : 'a', 'u+ff42' : 'b', 'u+ff43' : 'c', 'u+ff44' : 'd', 'u+ff45' : 'e', 'u+ff46' : 'f', 'u+ff47' : 'g', 'u+ff48' : 'h', 'u+ff49' : 'i', 'u+ff4a' : 'j', 'u+ff4b' : 'k', 'u+ff4c' : 'l', 'u+ff4d' : 'm', 'u+ff4e' : 'n', 'u+ff4f' : 'o', 'u+ff50' : 'p', 'u+ff51' : 'q', 'u+ff52' : 'r', 'u+ff53' : 's', 'u+ff54' : 't', 'u+ff55' : 'u', 'u+ff56' : 'v', 'u+ff57' : 'w', 'u+ff58' : 'x', 'u+ff59' : 'y', 'u+ff5a' : 'z', 'u+ff5b' : '{', 'u+ff5c' : '|', 'u+ff5d' : '}', 'u+ff5e' : '~', 'efbe80' : ' ', 'u+ff81' : '¡', 'u+ff82' : '¢', 'u+ff83' : '£', 'u+ff84' : '¤', 'u+ff85' : '¥', 'u+ff86' : '¦', 'u+ff87' : '§', 'u+ff88' : '¨', 'u+ff89' : '©', 'u+ff8a' : 'ª', 'u+ff8b' : '«', 'u+ff8c' : '¬', 'u+ff8d' : '­', 'u+ff8e' : '®', 'u+ff8f' : '¯', 'u+ff90' : '°', 'u+ff91' : '±', 'u+ff92' : '²', 'u+ff93' : '³', 'u+ff94' : '´', 'u+ff95' : 'µ', 'u+ff96' : '¶', 'u+ff97' : '·', 'u+ff98' : '¸', 'u+ff99' : '¹', 'u+ff9a' : 'º', 'u+ff9b' : '»', 'u+ff9c' : '¼', 'u+ff9d' : '½', 'u+ff9e' : '¾', 'u+ff9f' : '¿', 'u+ffa0' : 'À', 'u+ffa1' : 'Á', 'u+ffa2' : 'Â', 'u+ffa3' : 'Ã', 'u+ffa4' : 'Ä', 'u+ffa5' : 'Å', 'u+ffa6' : 'Æ', 'u+ffa7' : 'Ç', 'u+ffa8' : 'È', 'u+ffa9' : 'É', 'u+ffaa' : 'Ê', 'u+ffab' : 'Ë', 'u+ffac' : 'Ì', 'u+ffad' : 'Í', 'u+ffae' : 'Î', 'u+ffaf' : 'Ï', 'u+ffb0' : 'Ð', 'u+ffb1' : 'Ñ', 'u+ffb2' : 'Ò', 'u+ffb3' : 'Ó', 'u+ffb4' : 'Ô', 'u+ffb5' : 'Õ', 'u+ffb6' : 'Ö', 'u+ffb7' : '×', 'u+ffb8' : 'Ø', 'u+ffb9' : 'Ù', 'u+ffba' : 'Ú', 'u+ffbb' : 'Û', 'u+ffbc' : 'Ü', 'u+ffbd' : 'Ý', 'u+ffbe' : 'Þ', 'u+ffbf' : 'ß', 'u+ffc0' : 'à', 'u+ffc1' : 'á', 'u+ffc2' : 'â', 'u+ffc3' : 'ã', 'u+ffc4' : 'ä', 'u+ffc5' : 'å', 'u+ffc6' : 'æ', 'u+ffc7' : 'ç', 'u+ffc8' : 'è', 'u+ffc9' : 'é', 'u+ffca' : 'ê', 'u+ffcb' : 'ë', 'u+ffcc' : 'ì', 'u+ffcd' : 'í', 'u+ffce' : 'î', 'u+ffcf' : 'ï', 'u+ffd0' : 'ð', 'u+ffd1' : 'ñ', 'u+ffd2' : 'ò', 'u+ffd3' : 'ó', 'u+ffd4' : 'ô', 'u+ffd5' : 'õ', 'u+ffd6' : 'ö', 'u+ffd7' : '÷', 'u+ffd8' : 'ø', 'u+ffd9' : 'ù', 'u+ffda' : 'ú', 'u+ffdb' : 'û', 'u+ffdc' : 'ü', 'u+ffdd' : 'ý', 'u+ffde' : 'þ', 'u+ffdf' : 'ÿ' }

    def decoded(self):
        answer = self.mystring
        for i in self.mystring:
            for i, j in self.fw2.iteritems():
                answer = answer.replace(i, j)
        return answer

    def encoded(self):
        answer = ''
        for i in self.mystring:
            for k in self.fw2:
                if i in self.fw2[k]:
                    answer += k
                    break
            else:
                answer += i
        return answer
