#coding=utf-8

import os

PDB_DIR = 'F:\\wgw\\pdb abstract\\'
for p,d,f in os.walk(PDB_DIR):
    for files in f:
        if files.endswith('.ss'):
            infile = open(os.path.join(p,files))
            for line in infile:
                if len(line.split(',')[0].split('\t')[2]) > 3:
                    print os.path.join(p,files)
                    print line
                    break
                

