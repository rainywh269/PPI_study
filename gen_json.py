#coding=utf-8

import json

aa_lkp = {}
aa_lkp['ALA'] = 'A'
aa_lkp['ARG'] = 'R'
aa_lkp['ASN'] = 'N'
aa_lkp['ASP'] = 'D'
aa_lkp['CYS'] = 'C'
aa_lkp['GLN'] = 'Q'
aa_lkp['GLU'] = 'E'
aa_lkp['GLY'] = 'G'
aa_lkp['HIS'] = 'H'
aa_lkp['ILE'] = 'I'
aa_lkp['LEU'] = 'L'
aa_lkp['LYS'] = 'K'
aa_lkp['MET'] = 'M'
aa_lkp['PHE'] = 'F'
aa_lkp['PRO'] = 'P'
aa_lkp['SER'] = 'S'
aa_lkp['THR'] = 'T'
aa_lkp['TRP'] = 'W'
aa_lkp['TYR'] = 'Y'
aa_lkp['VAL'] = 'V'

with open('aa_lkp.json','w+') as js:
    json.dump(aa_lkp,js,indent = 2)
