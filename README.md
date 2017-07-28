# how2convert #

Estes scripts foram criados inspirados na palestra do Felipe Balestra, em sua palestra no ROADSEC com o título: "Dos ataques avançados ditos pela mídia à realidade dos PenTests" e da ferramenta OWASP Project - CAL9000 de Chris Loomis.

Eles têm a finalidade de Encode/Decode de strings para ofuscar suas entradas em um processo de auditoria de teste de intrusão. Ou descobrir qual o encode utilizado em uma aplicação.

Aproveito para pedir desculpas pela deselegância do código, já que estou me aventurando nesta linguagem que estou apaixonado, porém ainda na fase do namoro.

Espero que gostem.

# Uso #

    ./how2encode.py -h
        usage: how2encode.py [-t type_encode] [--str="data"]

    optional arguments:
     -h, --help            show this help message and exit
     -t {hex,uni,dec,fwd,html,js,b64,b32,b16,full}, --type {hex,uni,dec,fwd,html,js,b64,b32,b16,full}
                            Type of Encode strings. Select [hex => Hexadecimal] or
                            [uni => Unicode] or [dec => Decimal] or [fwd =>
                            Fullwidth]or [html => escape javascript] or [b64 =>
                           base64] or [full => envery encode]
      --str TXT             The String Encode/Decode
      --version             show program's version number and exit

    ./how2encode.py -t full --str "<Well/>"

    [+] HEXA Standard: 0x3c0x570x650x6c0x6c0x2f0x3e
    [+] HEXA Straigth: 0x3c57656c6c2f3e
    [+] HEXA EI0: \x3c\x57\x65\x6c\x6c\x2f\x3e
    [+] HEXA EI1: \x03c\x057\x065\x06c\x06c\x02f\x03e
    [+] HEXA EI2: \x003c\x0057\x0065\x006c\x006c\x002f\x003e
    [+] HEXA EI3: \x0003c\x00057\x00065\x0006c\x0006c\x0002f\x0003e
    [+] HEXA EI4: \x00003c\x000057\x000065\x00006c\x00006c\x00002f\x00003e
    [+] HEXA EI5: \x000003c\x0000057\x0000065\x000006c\x000006c\x000002f\x000003e
    [+] HEXA Entity: &#x3c;&#x57;&#x65;&#x6c;&#x6c;&#x2f;&#x3e;
    [+] HEXA4 Entity: &#x003c;&#x0057;&#x0065;&#x006c;&#x006c;&#x002f;&#x003e;
    [+] HEXA URL: %3c%57%65%6c%6c%2f%3e
    [+] DEC Straigth: 60.87.101.108.108.47.62.
    [+] DEC Long: &#60&#87&#101&#108&#108&#47&#62
    [+] DEC EId: \60\87\101\108\108\47\62
    [+] Unicode Standard: u003cu0057u0065u006cu006cu002fu003e
    [+] Unicode Straigth: 003c00570065006c006c002f003e
    [+] Unicode EIu: \u003c\u0057\u0065\u006c\u006c\u002f\u003e
    [+] Unicode URL: %u003c%u0057%u0065%u006c%u006c%u002f%u003e
    [+] Fullwidth 1: efbc9cefbcb7efbd85efbd8cefbd8cefbc8fefbc9e
    [+] Fullwidth 2: u+ff1cu+ff37u+ff45u+ff4cu+ff4cu+ff0fu+ff1e
    [+] Fullwidth 3: %ef%bc%9c%ef%bc%b7%ef%bd%85%ef%bd%8c%ef%bd%8c%ef%bc%8f%ef%bc%9e
    [+] Fullwidth 4: &#xfeff;&#xff1c;&#xff37;&#xff45;&#xff4c;&#xff4c;&#xff0f;&#xff1e;
    [+] JavaScript Escape: %3cWell%2f%3e
    [+] HTML Escape: &lt;Well&sol;&gt;
    [+] Base16: 3C57656C6C2F3E
    [+] Base32: HRLWK3DMF47A====
    [+] Base64: PFdlbGwvPg==

# Licença #

Author: Wellington Silva a.k.a. Well

Date: July 2017

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

More details: <http://www.how2security.com.br>
