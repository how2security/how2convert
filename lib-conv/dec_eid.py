#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: dec_eid.py
Purpose: Class Encode/Decode with Decimal EId.
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

class CodingDecEId:
    def __init__(self, mystring):
        self.mystring = mystring
	# Encode ASCII Decimal EId
        self.dec_eid = { r'\00' : '', r'\32' : ' ', r'\33' : '!', r'\34' : '"', r'\35' : '#', r'\36' : '$', r'\37' : '%', r'\38' : '&', r'\39' : "'", r'\40' : '(', r'\41' : ')', r'\42' : '*', r'\43' : '+', r'\44' : ',', r'\45' : '-', r'\46' : '.', r'\47' : '/', r'\48' : '0', r'\49' : '1', r'\50' : '2', r'\51' : '3', r'\52' : '4', r'\53' : '5', r'\54' : '6', r'\55' : '7', r'\56' : '8', r'\57' : '9', r'\58' : ':', r'\59' : ';', r'\60' : '<', r'\61' : '=', r'\62' : '>', r'\63' : '?', r'\64' : '@', r'\65' : 'A', r'\66' : 'B', r'\67' : 'C', r'\68' : 'D', r'\69' : 'E', r'\70' : 'F', r'\71' : 'G', r'\72' : 'H', r'\73' : 'I', r'\74' : 'J', r'\75' : 'K', r'\76' : 'L', r'\77' : 'M', r'\78' : 'N', r'\79' : 'O', r'\80' : 'P', r'\81' : 'Q', r'\82' : 'R', r'\83' : 'S', r'\84' : 'T', r'\85' : 'U', r'\86' : 'V', r'\87' : 'W', r'\88' : 'X', r'\89' : 'Y', r'\90' : 'Z', r'\91' : '[', r'\92' : '\\', r'\93' : '[', r'\94' : '^', r'\95' : '_', r'\96' : '`', r'\97' : 'a', r'\98' : 'b', r'\99' : 'c', r'\100' : 'd', r'\101' : 'e', r'\102' : 'f', r'\103' : 'g', r'\104' : 'h', r'\105' : 'i', r'\106' : 'j', r'\107' : 'k', r'\108' : 'l', r'\109' : 'm', r'\110' : 'n', r'\111' : 'o', r'\112' : 'p', r'\113' : 'q', r'\114' : 'r', r'\115' : 's', r'\116' : 't', r'\117' : 'u', r'\118' : 'v', r'\119' : 'w', r'\120' : 'x', r'\121' : 'y', r'\122' : 'z', r'\123' : '{', r'\124' : '|', r'\125' : '}', r'\126' : '~', r'\160' : ' ', r'\161' : '¡', r'\162' : '¢', r'\163' : '£', r'\164' : '¤', r'\165' : '¥', r'\166' : '¦', r'\167' : '§', r'\168' : '¨', r'\169' : '©', r'\170' : 'ª', r'\171' : '«', r'\172' : '¬', r'\173' : '­', r'\174' : '®', r'\175' : '¯', r'\176' : '°', r'\177' : '±', r'\178' : '²', r'\179' : '³', r'\180' : '´', r'\181' : 'µ', r'\182' : '¶', r'\183' : '·', r'\184' : '¸', r'\185' : '¹', r'\186' : 'º', r'\187' : '»', r'\188' : '¼', r'\189' : '½', r'\190' : '¾', r'\191' : '¿', r'\192' : 'À', r'\193' : 'Á', r'\194' : 'Â', r'\195' : 'Ã', r'\196' : 'Ä', r'\197' : 'Å', r'\198' : 'Æ', r'\199' : 'Ç', r'\200' : 'È', r'\201' : 'É', r'\202' : 'Ê', r'\203' : 'Ë', r'\204' : 'Ì', r'\205' : 'Í', r'\206' : 'Î', r'\207' : 'Ï', r'\208' : 'Ð', r'\209' : 'Ñ', r'\210' : 'Ò', r'\211' : 'Ó', r'\212' : 'Ô', r'\213' : 'Õ', r'\214' : 'Ö', r'\215' : '×', r'\216' : 'Ø', r'\217' : 'Ù', r'\218' : 'Ú', r'\219' : 'Û', r'\220' : 'Ü', r'\221' : 'Ý', r'\222' : 'Þ', r'\223' : 'ß', r'\224' : 'à', r'\225' : 'á', r'\226' : 'â', r'\227' : 'ã', r'\228' : 'ä', r'\229' : 'å', r'\230' : 'æ', r'\231' : 'ç', r'\232' : 'è', r'\233' : 'é', r'\234' : 'ê', r'\235' : 'ë', r'\236' : 'ì', r'\237' : 'í', r'\238' : 'î', r'\239' : 'ï', r'\240' : 'ð', r'\241' : 'ñ', r'\242' : 'ò', r'\243' : 'ó', r'\244' : 'ô', r'\245' : 'õ', r'\246' : 'ö', r'\247' : '÷', r'\248' : 'ø', r'\249' : 'ù', r'\250' : 'ú', r'\251' : 'û', r'\252' : 'ü', r'\253' : 'ý', r'\254' : 'þ', r'\255' : 'ÿ' }

    def decoded(self):
        answer = self.mystring
        for i in self.mystring:
            for i, j in self.dec_eid.iteritems():
                answer = answer.replace(i, j)
        return answer

    def encoded(self):
        answer = ''
        for i in self.mystring:
            for k in self.dec_eid:
                if i in self.dec_eid[k]:
                    answer += k
                    break
            else:
                answer += i
        return answer
