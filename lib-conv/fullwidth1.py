#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: fullwidth1.py
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

class CodingFW1:
    def __init__(self, mystring):
        self.mystring = mystring
	# Encode Unicode FullWidth1
        self.fw1 = { 'efbc80' : '', 'efbc81' : '!', 'efbc82' : '"', 'efbc83' : '#', 'efbc84' : '$', 'efbc85' : '%', 'efbc86' : '&', 'efbc87' : "'", 'efbc88' : '(', 'efbc89' : ')', 'efbc8a' : '*', 'efbc8b' : '+', 'efbc8c' : ',', 'efbc8d' : '-', 'efbc8e' : '.', 'efbc8f' : '/', 'efbc90' : '0', 'efbc91' : '1', 'efbc92' : '2', 'efbc93' : '3', 'efbc94' : '4', 'efbc95' : '5', 'efbc96' : '6', 'efbc97' : '7', 'efbc98' : '8', 'efbc99' : '9', 'efbc9a' : ':', 'efbc9b' : ';', 'efbc9c' : '<', 'efbc9d' : '=', 'efbc9e' : '>', 'efbc9f' : '?', 'efbca0' : '@', 'efbca1' : 'A', 'efbca2' : 'B', 'efbca3' : 'C', 'efbca4' : 'D', 'efbca5' : 'E', 'efbca6' : 'F', 'efbca7' : 'G', 'efbca8' : 'H', 'efbca9' : 'I', 'efbcaa' : 'J', 'efbcab' : 'K', 'efbcac' : 'L', 'efbcad' : 'M', 'efbcae' : 'N', 'efbcaf' : 'O', 'efbcb0' : 'P', 'efbcb1' : 'Q', 'efbcb2' : 'R', 'efbcb3' : 'S', 'efbcb4' : 'T', 'efbcb5' : 'U', 'efbcb6' : 'V', 'efbcb7' : 'W', 'efbcb8' : 'X', 'efbcb9' : 'Y', 'efbcba' : 'Z', 'efbcbb' : '[', 'efbcbd' : '[', 'efbcbc' : '\\', 'efbcbe' : '^', 'efbcbf' : '_', 'efbd80' : '`', 'efbd81' : 'a', 'efbd82' : 'b', 'efbd83' : 'c', 'efbd84' : 'd', 'efbd85' : 'e', 'efbd86' : 'f', 'efbd87' : 'g', 'efbd88' : 'h', 'efbd89' : 'i', 'efbd8a' : 'j', 'efbd8b' : 'k', 'efbd8c' : 'l', 'efbd8d' : 'm', 'efbd8e' : 'n', 'efbd8f' : 'o', 'efbd90' : 'p', 'efbd91' : 'q', 'efbd92' : 'r', 'efbd93' : 's', 'efbd94' : 't', 'efbd95' : 'u', 'efbd96' : 'v', 'efbd97' : 'w', 'efbd98' : 'x', 'efbd99' : 'y', 'efbd9a' : 'z', 'efbd9b' : '{', 'efbd9c' : '|', 'efbd9d' : '}', 'efbd9e' : '~', 'efbe80' : ' ', 'efbe81' : '¡', 'efbe82' : '¢', 'efbe83' : '£', 'efbe84' : '¤', 'efbe85' : '¥', 'efbe86' : '¦', 'efbe87' : '§', 'efbe88' : '¨', 'efbe89' : '©', 'efbe8a' : 'ª', 'efbe8b' : '«', 'efbe8c' : '¬', 'efbe8d' : '­', 'efbe8e' : '®', 'efbe8f' : '¯', 'efbe90' : '°', 'efbe91' : '±', 'efbe92' : '²', 'efbe93' : '³', 'efbe94' : '´', 'efbe95' : 'µ', 'efbe96' : '¶', 'efbe97' : '·', 'efbe98' : '¸', 'efbe99' : '¹', 'efbe9a' : 'º', 'efbe9b' : '»', 'efbe9c' : '¼', 'efbe9d' : '½', 'efbe9e' : '¾', 'efbe9f' : '¿', 'efbea0' : 'À', 'efbea1' : 'Á', 'efbea2' : 'Â', 'efbea3' : 'Ã', 'efbea4' : 'Ä', 'efbea5' : 'Å', 'efbea6' : 'Æ', 'efbea7' : 'Ç', 'efbea8' : 'È', 'efbea9' : 'É', 'efbeaa' : 'Ê', 'efbeab' : 'Ë', 'efbeac' : 'Ì', 'efbead' : 'Í', 'efbeae' : 'Î', 'efbeaf' : 'Ï', 'efbeb0' : 'Ð', 'efbeb1' : 'Ñ', 'efbeb2' : 'Ò', 'efbeb3' : 'Ó', 'efbeb4' : 'Ô', 'efbeb5' : 'Õ', 'efbeb6' : 'Ö', 'efbeb7' : '×', 'efbeb8' : 'Ø', 'efbeb9' : 'Ù', 'efbeba' : 'Ú', 'efbebb' : 'Û', 'efbebc' : 'Ü', 'efbebd' : 'Ý', 'efbebe' : 'Þ', 'efbebf' : 'ß', 'efbf80' : 'à', 'efbf81' : 'á', 'efbf82' : 'â', 'efbf83' : 'ã', 'efbf84' : 'ä', 'efbf85' : 'å', 'efbf86' : 'æ', 'efbf87' : 'ç', 'efbf88' : 'è', 'efbf89' : 'é', 'efbf8a' : 'ê', 'efbf8b' : 'ë', 'efbf8c' : 'ì', 'efbf8d' : 'í', 'efbf8e' : 'î', 'efbf8f' : 'ï', 'efbf90' : 'ð', 'efbf91' : 'ñ', 'efbf92' : 'ò', 'efbf93' : 'ó', 'efbf94' : 'ô', 'efbf95' : 'õ', 'efbf96' : 'ö', 'efbf97' : '÷', 'efbf98' : 'ø', 'efbf99' : 'ù', 'efbf9a' : 'ú', 'efbf9b' : 'û', 'efbf9c' : 'ü', 'efbf9d' : 'ý', 'efbf9e' : 'þ', 'efbf9f' : 'ÿ' }

    def decoded(self):
        answer = self.mystring
        for i in self.mystring:
            for i, j in self.fw1.iteritems():
                answer = answer.replace(i, j)
        return answer

    def encoded(self):
        answer = ''
        for i in self.mystring:
            for k in self.fw1:
                if i in self.fw1[k]:
                    answer += k
                    break
            else:
                answer += i
        return answer
