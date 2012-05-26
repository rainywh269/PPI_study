#coding=utf-8

from __future__ import division
from Bio.Blast import NCBIStandalone
import os,json

PDB_DIR = 'F:\\wgw\\pdb abstract\\'
BLAST_DIR = 'F:\\wgw\\blast_cmpd\\'
index = 0
for p,d,f in os.walk(PDB_DIR):
    for files in f:
        if files.endswith('.zz'):
            index += 1
            print index,files[:4]
            pair = open(os.path.join(p,files))
            pair_list = []
            for line in pair:
                pair_list.append(line.rstrip())    
            pair.close()
            
            blast = open(os.path.join(BLAST_DIR,files[:4]))
            blast_parser = NCBIStandalone.BlastParser()
            blast_iterator = NCBIStandalone.Iterator(blast, blast_parser)
            align_summary = {}
            for blast_record in blast_iterator:
                chain = blast_record.query.split('|')[0].split(':')[1] 
                align_summary[chain] = {}
                for alignment in blast_record.alignments:
                    align_summary[chain][alignment.title] = {}
                    for hsp in alignment.hsps:
                        sim = hsp.identities[0] / hsp.identities[1]
                        if sim >= 0.3:
                            ss = hsp.query_start
                            loc = {}
                            for i in range(len(hsp.query)):
                                if hsp.query[i] == hsp.match[i]:
                                    clean = hsp.query[:i + 1].replace('-','')
                                    loc[len(clean) + ss - 1] = hsp.match[i]
                            align_summary[chain][alignment.title] = loc
            blast.close()
            '''
            with open('align.json','w+') as js:
                json.dump(align_summary,js,indent = 2)
            '''
            out = open(os.path.join(p,files) + '.ww','w+')
            for item in pair_list:
                out.write(item + '\n')
                ch_1 = item.split(',')[0].split('\t')[0]
                ind_1 = item.split(',')[0].split('\t')[1]
                ch_2 = item.split(',')[1].split('\t')[0]
                ind_2 = item.split(',')[1].split('\t')[1]
                result = {}
                if (align_summary.has_key(ch_1))&(align_summary.has_key(ch_2)):
                    result[ch_1] = []
                    result[ch_2] = []
                    for k in align_summary[ch_1].keys():
                        for kk in align_summary[ch_1][k].keys():
                            if ind_1 == str(kk):
                                result[ch_1].append(k)
                    for k in align_summary[ch_2].keys():
                        for kk in align_summary[ch_2][k].keys():
                            if ind_2 == str(kk):
                                result[ch_2].append(k)
                    if (len(result[ch_1]) > 0)&(len(result[ch_2]) > 0):
                        out.write(ch_1 + ':\n')
                        for m in result[ch_1]:
                            out.write('\t' + m + '\n')
                        out.write(ch_2 + ':\n')
                        for n in result[ch_2]:
                            out.write('\t' + n + '\n')
                    else:
                        out.write('No Alignment Found !\n')
            out.close()


            

