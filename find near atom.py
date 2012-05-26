#coding=utf-8

import os,itertools
lkp = open('midblastp2.txt')
lkp_list = []
for line in lkp:
    lkp_list.append(line[:4])
lkp_list = list(set(lkp_list))

ERR_LOG = open('ERR_LOG.txt','w+')
for p,d,f in os.walk('F:\\wgw\\pdb abstract\\'):
    for files in f:
        if (files.endswith('.pdb'))|(files.endswith('.ent')):
            print files
            infile = open(os.path.join(p,files))
            index = 0
            raw = []
            for line in infile:
                if index == 0:
                    cmpd_name = line.split()[-1]
                    index += 1
                    if cmpd_name not in lkp_list:
                        break
                if line.startswith('ATOM '):
                    if line.split()[2] == 'CA':
                        line = line.replace('-',' -')
                        aa = line.split()[3]
                        if len(line.split()[4]) > 1:
                            chain = line.split()[4][0]         
                            num = line.split()[4][1:]
                            cord_x = line.split()[5]
                            cord_y = line.split()[6]
                            cord_z = line.split()[7]
                        else:
                            chain = line.split()[4]          
                            num = line.split()[5]
                            cord_x = line.split()[6]
                            cord_y = line.split()[7]
                            cord_z = line.split()[8]                      
                        raw.append([aa,chain,num,cord_x,cord_y,cord_z])
            infile.close()
            chain_set = []
            for ca in raw:
                chain_set.append(ca[1])
            chain_set = list(set(chain_set))
            data_set = {}
            for c in chain_set:
                data_set[c] = []
            for r in raw:
                info = [r[0],r[2],r[3],r[4],r[5]]
                data_set[r[1]].append(info)
            combin = list(itertools.combinations(data_set.keys(),2))
            if len(combin) == 0:
                continue
            else:
                out = open(os.path.join(p,cmpd_name + '.txt'),'w+')
                for c in combin:
                    chain_1 = data_set[c[0]]
                    chain_2 = data_set[c[1]]
                    for ca1 in chain_1:
                        try:
                            x1 = float(ca1[2])
                            y1 = float(ca1[3])
                            z1 = float(ca1[4])
                        except Exception,data:
                            ERR_LOG.write('SKIP: ' + files + '\n')
                            continue
                        for ca2 in chain_2:
                            try:
                                x2 = float(ca2[2])
                                y2 = float(ca2[3])
                                z2 = float(ca2[4])
                                dist = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
                                if dist <= 64:
                                    out.write(c[0] + '\t' + ca1[1] + '\t' + ca1[0] + ',' + c[1] + '\t' + ca2[1] + '\t' + ca2[0] + '\n')     
                            except Exception,data:
                                ERR_LOG.write('SKIP: ' + files + '\n')
                                continue                               
                out.close()
ERR_LOG.close()
