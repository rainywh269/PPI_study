#coding=utf-8
import os

def findAnswer(content,block_begin,block_end):
    answer_index = []
    start = []
    end = []
    indicator = []
    for t in range(block_begin,block_end):
        if content[t].startswith('Query: '):
            answer_index.append(t + 1)
            start.append(int(content[t].split()[1]))
            end.append(int(content[t].split()[3]))
            indicator.append(content[t].find(content[t].split()[2]))
    if len(answer_index) > 1:
        hit_start = min(start)
        hit_end = max(end)
        answer = ''
        for tt in range(len(indicator)):
            answer += content[answer_index[tt]][indicator[tt]:-1]   
    else:
        hit_start = start[0]
        hit_end = end[0]
        answer = content[answer_index[0]][indicator[0]:-1]
    return answer,hit_start,hit_end


BASE_DIR = 'F:\\wgw\\blast_cmpd_2\\'
OUT_DIR = 'F:\\wgw\\blast_ex_2\\'
for files in os.listdir(BASE_DIR):
    print files
    infile = open(os.path.join(BASE_DIR,files))
    out = open(os.path.join(OUT_DIR,files) + '.txt','w+')
    index = 0
    content = {}
    chain = []
    sbjct = []
    for line in infile:
        index += 1
        content[index] = line
        if line.startswith('Query='):
            chain.append(index)
        if line.startswith('>'):
            sbjct.append(index)
    infile.close()

    for i in range(0,len(chain) - 1):
        out.write('CHAIN: ' + content[chain[i]][12] + '\n')
        sub_sbjct = []
        for s in sbjct:
            if (s > chain[i])&( s < chain[i + 1]):
                sub_sbjct.append(s)
        if len(sub_sbjct) > 0:
            for j in range(0,len(sub_sbjct) - 1):
                sbjct_name = content[sub_sbjct[j]]
                sbjct_answer,s,e = findAnswer(content,sub_sbjct[j],sub_sbjct[j + 1])
                out.write(sbjct_name)
                out.write(str(s) + '\t' + str(e) + '\n')
                out.write(sbjct_answer + '\n')
            #processinging the last sbjct   
            last_sbj_name = content[sub_sbjct[-1]]
            last_sbj_answer,ss,ee = findAnswer(content,sub_sbjct[-1],chain[i + 1])
            out.write(last_sbj_name)
            out.write(str(ss) + '\t' + str(ee) + '\n')
            out.write(last_sbj_answer + '\n')
        else:
            out.write('No hits found\n')


    #processing the last chain
    out.write('CHAIN: ' + content[chain[-1]][12] + '\n')
    sub_sbjct = []
    for s in sbjct:
        if s > chain[-1]:
            sub_sbjct.append(s)
    if len(sub_sbjct) > 0:
        for j in range(0,len(sub_sbjct) - 1):
            sbjct_name = content[sub_sbjct[j]]
            sbjct_answer,s,e = findAnswer(content,sub_sbjct[j],sub_sbjct[j+1])
            out.write(sbjct_name)
            out.write(str(s) + '\t' + str(e) + '\n')
            out.write(sbjct_answer + '\n')
        last_sbj_name = content[sub_sbjct[-1]]
        last_sbj_answer,ss,ee = findAnswer(content,sub_sbjct[-1],max(content.keys()))
        out.write(last_sbj_name)
        out.write(str(ss) + '\t' + str(ee) + '\n')
        out.write(last_sbj_answer + '\n')
        out.close()
    else:
        out.write('No hits found\n')


    
            
            
            
                    

            
                
                    
            
        
