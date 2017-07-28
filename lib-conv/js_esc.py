#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: js_esc.py
Purpose: Class Encode/Decode with JavaScript Espace.
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

class CodingJSEsc:
    def __init__(self, mystring):
        self.mystring = mystring
	# Encode JavaScript Escape (Observation => Space can be %20 or '%a0')
        self.js_escape = { '%00' : '', '%07' : '\a', '%08' : '\b', '%09' : '\t', '%0a' : '\n', '%0b' : '\v', '%0c' : '\f', '%0d' : '\r', '%20' : ' ', '%21' : '!', '%22' : '"', '%23' : '#', '%24' : '$', '%25' : '%', '%26' : '&', '%27' : "'", '%28' : '(', '%29' : ')', '%2a' : '*', '%2b' : '+', '%2c' : ',', '%2d' : '-', '%2e' : '.', '%2f' : '/', 	'%3a' : ':', '%3b' : ';', '%3c' : '<', '%3d' : '=', '%3e' : '>', '%3f' : '?', '%40' : '@', '%5b' : '[', '%5c' : '\\', '%5d' : '[', '%5e' : '^', '%5f' : '_', '%60' : '`', '%7b' : '{', '%7c' : '|', '%7d' : '}', '%7e' : '~', '%a1' : '¡', '%a2' : '¢', '%a3' : '£', '%a4' : '¤', '%a5' : '¥', '%a6' : '¦', '%a7' : '§', '%a8' : '¨', '%a9' : '©', '%aa' : 'ª', '%ab' : '«', '%ac' : '¬', '%ad' : '­', '%ae' : '®', '%af' : '¯', '%b0' : '°', '%b1' : '±', '%b2' : '²', '%b3' : '³', '%b4' : '´', '%b5' : 'µ', '%b6' : '¶', '%b7' : '·', '%b8' : '¸', '%b9' : '¹', '%ba' : 'º', '%bb' : '»', '%bc' : '¼', '%bd' : '½', '%be' : '¾', '%bf' : '¿', '%c0' : 'À', '%c1' : 'Á', '%c2' : 'Â', '%c3' : 'Ã', '%c4' : 'Ä', '%c5' : 'Å', '%c6' : 'Æ', '%c7' : 'Ç', '%c8' : 'È', '%c9' : 'É', '%ca' : 'Ê', '%cb' : 'Ë', '%cc' : 'Ì', '%cd' : 'Í', '%ce' : 'Î', '%cf' : 'Ï', '%d0' : 'Ð', '%d1' : 'Ñ', '%d2' : 'Ò', '%d3' : 'Ó', '%d4' : 'Ô', '%d5' : 'Õ', '%d6' : 'Ö', '%d7' : '×', '%d8' : 'Ø', '%d9' : 'Ù', '%da' : 'Ú', '%db' : 'Û', '%dc' : 'Ü', '%dd' : 'Ý', '%de' : 'Þ', '%df' : 'ß', '%e0' : 'à', '%e1' : 'á', '%e2' : 'â', '%e3' : 'ã', '%e4' : 'ä', '%e5' : 'å', '%e6' : 'æ', '%e7' : 'ç', '%e8' : 'è', '%e9' : 'é', '%ea' : 'ê', '%eb' : 'ë', '%ec' : 'ì', '%ed' : 'í', '%ee' : 'î', '%ef' : 'ï', '%f0' : 'ð', '%f1' : 'ñ', '%f2' : 'ò', '%f3' : 'ó', '%f4' : 'ô', '%f5' : 'õ', '%f6' : 'ö', '%f7' : '÷', '%f8' : 'ø', '%f9' : 'ù', '%fa' : 'ú', '%fb' : 'û', '%fc' : 'ü', '%fd' : 'ý', '%fe' : 'þ', '%ff' : 'ÿ' }

    def decoded(self):
        answer = self.mystring
        for i in self.mystring:
            for i, j in self.js_escape.iteritems():
                answer = answer.replace(i, j)
        return answer

    def encoded(self):
        answer = ''
        for i in self.mystring:
            for k in self.js_escape:
                if i in self.js_escape[k]:
                    answer += k
                    break
            else:
                answer += i
        return answer
