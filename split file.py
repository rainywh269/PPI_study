#coding=utf-8

import os
'''
infile = open('F:\\wgw\\blastnow1.txt')
index = 0
for line in infile:
    if line.startswith('BLASTP 2.2.24'):
        if index != 0:
            out.close()
        index += 1  
        out = open('F:\\wgw\\blast_pre\\' + str(index) + '.txt','w+')
    out.write(line)      
infile.close()
'''

lkp = open('midblastp2.txt')
lkp_list = []
for line in lkp:
    lkp_list.append(line[:4])
lkp_list = list(set(lkp_list))
lkp.close()
print 'done'

BASE = 'F:\\wgw\\blast_pre\\'
cmpd_dict = {}
for files in os.listdir(BASE):
    infile = open(os.path.join(BASE,files))
    cmpd = ''
    for line in infile:
        if line.startswith('Query= '):
            cmpd = line[7:11]
            break
    infile.close()
    if cmpd not in lkp_list:
        continue
    if cmpd_dict.has_key(cmpd):
        cmpd_dict[cmpd].append(files)
    else:
        cmpd_dict[cmpd] = []
        cmpd_dict[cmpd].append(files)
   
print 'ok'

for k in cmpd_dict.keys():
    out = open(os.path.join('F:\\wgw\\blast_cmpd_1\\',k),'w+')
    for f in cmpd_dict[k]:
        infile = open(os.path.join(BASE,f))
        for line in infile:
            out.write(line)
        infile.close()
    out.close()

    
    
    

