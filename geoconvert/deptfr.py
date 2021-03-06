# -*- coding: utf8 -*-
import re

tab = dict()
tab['01'] = 'ain'
tab['02'] = 'aisne'
tab['03'] = 'allier'
tab['04'] = 'alpes-de-hautes-provence'
tab['05'] = 'hautes-alpes'
tab['06'] = 'alpes-maritimes'
tab['07'] = 'ardeche'
tab['08'] = 'ardennes'
tab['09'] = 'ariege'
tab['10'] = 'aube'
tab['11'] = 'aude'
tab['12'] = 'aveyron'
tab['13'] = 'bouches-du-rhone'
tab['14'] = 'calvados'
tab['15'] = 'cantal'
tab['16'] = 'charente'
tab['17'] = 'charente-maritime'
tab['18'] = 'cher'
tab['19'] = 'correze'
tab['2A'] = 'corse-du-sud'
tab['2B'] = 'haute-corse'  
tab['21'] = 'cote-d\'or'  
tab['22'] = 'cotes-d\'armor'
tab['23'] = 'creuse'
tab['24'] = 'dordogne'
tab['25'] = 'doubs'
tab['26'] = 'drome'
tab['27'] = 'eure'
tab['28'] = 'eure-et-loir'
tab['29'] = 'finistere'
tab['30'] = 'gard'
tab['31'] = 'haute-garonne'
tab['32'] = 'gers'
tab['33'] = 'gironde'
tab['34'] = 'herault'
tab['35'] = 'ille-et-vilaine'
tab['36'] = 'indre'
tab['37'] = 'indre-et-loire'
tab['38'] = 'isere'
tab['39'] = 'jura'
tab['40'] = 'landes'
tab['41'] = 'loir-et-cher'
tab['42'] = 'loire'
tab['43'] = 'haute-loire'
tab['44'] = 'loire-atlantique'
tab['45'] = 'loiret'
tab['46'] = 'lot'
tab['47'] = 'lot-et-garonne'
tab['48'] = 'lozere'
tab['49'] = 'maine-et-loire'
tab['50'] = 'manche'
tab['51'] = 'marne'
tab['52'] = 'haute-marne'
tab['53'] = 'mayenne'
tab['54'] = 'meurthe-et-moselle'
tab['55'] = 'meuse'
tab['56'] = 'morbihan'
tab['57'] = 'moselle'
tab['58'] = 'nievre'
tab['59'] = 'nord'
tab['60'] = 'oise'
tab['61'] = 'orne'
tab['62'] = 'pas-de-calais'
tab['63'] = 'puy-de-dome'
tab['64'] = 'pyrenees-atlantique'
tab['65'] = 'hautes-pyrenees'
tab['66'] = 'pyrenees-orientales'
tab['67'] = 'bas-rhin'
tab['68'] = 'haut-rhin'
tab['69'] = 'rhone'
tab['70'] = 'haute-saone'
tab['71'] = 'saone-et-loire'
tab['72'] = 'sarthe'
tab['73'] = 'savoie'
tab['74'] = 'haute-savoie'
tab['75'] = 'paris'
tab['76'] = 'seine-maritime'
tab['77'] = 'seine-et-marne'
tab['78'] = 'yvelines'
tab['79'] = 'deux-sevres'
tab['80'] = 'somme'
tab['81'] = 'tarn'
tab['82'] = 'tarn-et-garonne'
tab['83'] = 'var'
tab['84'] = 'vaucluse'
tab['85'] = 'vendee'
tab['86'] = 'vienne'
tab['87'] = 'haute-vienne'
tab['88'] = 'vosges'
tab['94'] = 'yonne'
tab['90'] = 'territoire-de-belfort'
tab['91'] = 'essonne'
tab['92'] = 'hauts-de-seine'
tab['93'] = 'seine-saint-denis'
tab['94'] = 'val-de-marne'
tab['95'] = 'val-d\'oise'
tab['971'] = 'guadeloupe'
tab['972'] = 'martinique'
tab['973'] = 'guyane'
tab['974'] = 'la-reunion'
tab['976'] = 'mayotte'

def cp2dept(cp):
    """
    Return the departement name from a CP or the departement number
    
    >>> cp2dept('121')

    >>> cp2dept('44000')
    'loire-atlantique'

    >>> cp2dept('2A')
    'corse-du-sud'

    """


    if (len(cp) == 5 and cp[:2] in tab.keys()):
        return tab[cp[:2]]
    elif (len(cp) == 5 and cp[:3] in tab.keys()):
        return tab[cp[:3]]
    elif cp in tab.keys():
        return tab[cp]
    else:
        return None


def adr2cp(chaine):
    """
    Return the departement number from any text which contains any zip code

    >>> adr2cp(u"Chemin du Solarium\\n Le Haut Vigneau\\n 33175 GRADIGNAN CEDEX")
    '33'

    >>> adr2cp("Chemin du Solarium 061256784589 Le Haut Vigneau 33175 GRADIGNAN CEDEX ")
    '33'

    >>> adr2cp("Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX 061256784589")
    '33'

    >>> adr2cp("Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX")
    '33'

    >>> adr2cp('7 cours Grandval\\nBP 414 - 20183 AJACCIO - CEDEX')
    '2A'

    >>> adr2cp('20212   Erbajolo')
    '2B'

    >>> adr2cp('20223   Solenzara Air')
    '2A'

    >>> adr2cp('BP 55342 20223   Solenzara Air')
    '2A'
    """

    #Test de la chaine de caracteres passée en parametre
    for line in chaine.splitlines():
        word = re.search(r"(?:\s+|^)(\d{5})\s+[a-zA-Z]+", line)
        if word:
            word = word.group(1)
            if word[:2] != '20':
                try:
                    if int(word) and len(word) == 5:
                        for key in tab.keys():
                            if word[:2] == key or word[:3] == key:
                                return key 
                except ValueError:
                    pass
            else:
                if int(word) < 20200 or int(word) in [20223, 20900]:
                    return '2A'
                else:
                    return '2B'
    return None

def dept2cp(chaine):
    """
    Return the departement number from the departement name

    >>> dept2cp('Martinique')
    '972'

    >>> dept2cp("cotes d'armr")

    >>> dept2cp("cotes d'armor")
    '22'

    >>> dept2cp(u'Hauts-de-Seine ')
    '92'

    >>> dept2cp(u'H\xe9rault')
    '34'

    >>> dept2cp(u'Seine-Saint-Denis ')
    '93'

    >>> dept2cp(u'Loire')
    '42'

    >>> dept2cp(u'')

    """
    if chaine:
        try:
            nom_dep = chaine.strip(' ').replace(" ","-").lower().encode('ASCII', 'replace').replace('?', '.')
        except:
            nom_dep = chaine.replace(" ","-").lower()
        for key,value in tab.items():
            if nom_dep == value:
                return key
        for key,value in tab.items():
            if re.search(nom_dep, value):
                return key
    return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()
