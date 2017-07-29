#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: html_esc.py
Purpose: Class Encode/Decode with HTML Escape.
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

class CodingHTMLEsc:
    def __init__(self, mystring):
        self.mystring = mystring
	# Encode HTML Escape
        self.html_escape = { '&sp;' : ' ', '&excl;' : '!', '&quot;' : '"', '&num;' : '#', '&dollar;' : '$', '&percnt;' : '%', '&apos;' : "'", '&lpar;' : '(', '&rpar;' : ')', '&ast;' : '*', '&hyphen;' : '-', '&period;' : '.', '&sol;' : '/', '&colon;' : ':', '&semi;' : ';', '&lt;' : '<', '&equals;' : '=', '&gt;' : '>', '&quest;' : '?', '&commat;' : '@', '&lsqb;' : '[', '&rsqb;' : ']', '&lowbar;' : '_', '&grave;' : '`', '&lcub;' : '{', '&verbar;' : '|', '&rcub;' : '}', '&tilde;' : '~', '&nbsp;' : ' ', '&iexcl;' : '¡', '&cent;' : '¢', '&pound;' : '£', '&curren;' : '¤', '&yen;' : '¥', '&brvbar;' : '¦', '&sect;' : '§', '&uml;' : '¨', '&copy;' : '©', '&ordf;' : 'ª', '&laquo;' : '«', '&not;' : '¬', '&shy;' : '­', '&reg;' : '®', '&macr;' : '¯', '&deg;' : '°', '&plusmn;' : '±', '&sup2;' : '²', '&sup3;' : '³', '&acute;' : '´', '&micro;' : 'µ', '&para;' : '¶', '&middot;' : '·', '&cedil;' : '¸', '&supl;' : '¹', '&ordm;' : 'º', '&raquo;' : '»', '&frac14;' : '¼', '&frac12;' : '½', '&frac34;' : '¾', '&iquest;' : '¿', '&Agrave;' : 'À', '&Aacute;' : 'Á', '&Acir;' : 'Â', '&Atilde;' : 'Ã', '&Auml;' : 'Ä', '&Aring;' : 'Å', '&Aelig;' : 'Æ', '&Ccedil;' : 'Ç', '&Egrave;' : 'È', '&Eacute;' : 'É', '&Ecirc;' : 'Ê', '&Euml;' : 'Ë', '&Igrave;' : 'Ì', '&Iacute;' : 'Í', '&Icirc;' : 'Î', '&Iuml;' : 'Ï', '&ETH;' : 'Ð', '&Ntilde;' : 'Ñ', '&Ograve;' : 'Ò', '&Oacute;' : 'Ó', '&Ocirc;' : 'Ô', '&Otilde;' : 'Õ', '&Ouml;' : 'Ö', '&times;' : '×', '&Oslash;' : 'Ø', '&Ugrave;' : 'Ù', '&Uacute;' : 'Ú', '&Ucirc;' : 'Û', '&Uuml;' : 'Ü', '&Yacute;' : 'Ý', '&THORN;' : 'Þ', '&szlig;' : 'ß', '&agrave;' : 'à', '&aacute;' : 'á', '&acirc;' : 'â', '&atilde;' : 'ã', '&auml;' : 'ä', '&aring;' : 'å', '&aelig;' : 'æ', '&ccedil;' : 'ç', '&egrave;' : 'è', '&eacute;' : 'é', '&ecirc;' : 'ê', '&euml;' : 'ë', '&igrave;' : 'ì', '&iacute;' : 'í', '&icirc;' : 'î', '&iuml;' : 'ï', '&eth;' : 'ð', '&ntilde;' : 'ñ', '&ograve;' : 'ò', '&oacute;' : 'ó', '&ocirc;' : 'ô', '&otilde;' : 'õ', '&ouml;' : 'ö', '&oslash;' : 'ø', '&ugrave;' : 'ù', '&uacute;' : 'ú', '&ucirc;' : 'û', '&uuml;' : 'ü', '&yacute;' : 'ý', '&thorn;' : 'þ', '&yuml;' : 'ÿ', '&OElig;' : 'Œ', '&oelig;' : 'œ', '&Scaron;' : 'Š', '&scaron;' : 'š', '&Yuml;' : 'Ÿ', '&circ;' : 'ˆ', '&ndash;' : '–', '&mdash;' : '—', '&lsquo;' : '‘', '&rsquo;' : '’', '&sbquo;' : '‚', '&ldquo;' : '“', '&rdquo;' : '”', '&bdquo;' : '„', '&dagger;' : '†', '&Dagger;' : '‡', '&hellip;' : '…', '&permil;' : '‰', '&lsaquo;' : '‹', '&rsaquo;' : '›', '&euro;' : '€', '&trade;' : '™', '&plus;' : '+', '&comma;' : ',', '&amp;' : '&' }

    def decoded(self):
        answer = self.mystring
        for i in self.mystring:
            for i, j in self.html_escape.iteritems():
                answer = answer.replace(i, j)
        return answer

    def encoded(self):
        answer = ''
        for i in self.mystring:
            for k in self.html_escape:
                if i in self.html_escape[k]:
                    answer += k
                    break
            else:
                answer += i
        return answer
