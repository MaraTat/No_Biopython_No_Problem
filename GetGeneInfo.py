# Importing necessary libraries

import gzip
import re

#==============================================================================

def GetGeneInfo(arg):
    """ This is a function that extracts the gene size, the CDS joins, 
        the CDS information e.g. complement or not and the DNA sequencce from 
        all entries in a GenBank record file. It accepts as a single argument 
        a zipped GenBank file containing one or multiple entires 
        e.g. an entire chromosome.
        CDS joins that include multiple different accessions are excuded
        This function calls on another function: ChromUnzip().
                        
        Input = zipped GenBank record file (one or multiple gene entries)
        Return = a dictionary with accession number as key and a list with 
                the gene size, CDS joins, CDS info and gene sequence as value
                from single accession entries only.
    """

    genbank = ChromUnzip(arg)
        
    p1=re.compile(r'(?:ACCESSION\s+)(\w+\d+)')      # ACCESSION regex
    p3 = re.compile(r'(?:ORIGIN\s+)(((\d+\s+)((\w+\s+){1,}){1,})(\w+))')      # gene seq regex
    p5=re.compile(r'(CDS\s+)((\w+)?(\(\w+)?(\(?\<?))((\d*?,?)(\d+\..\>?\d+,?\s*?)(\s*?\d+\..\d+,?\s*?){0,})(\)?)')     # CDS joins regex, excludes mutiple entries joins
    p5_2=re.compile(r'(CDS\s+)(complement)?(\w+)?')    # CDS info regex
    p7=re.compile(r'(?:source \s+)(\d+..\d+)(?:\s+)')     # gene size regex

    full_dict={} 

    for entry in genbank:    
        CDS_info=[]
        CDS_info_2=[]
        gene_size_list=[]
        final_geneseq=[]
        CDS_it_1 = p1.finditer(entry)   
        CDS_it_5_2 = p5_2.finditer(entry)
        gene_it_7 = p7.finditer(entry)
        gene_it_3 = p3.finditer(entry)
        for hit in CDS_it_5_2:
            CDS_info.append(str(hit.group(2)))
            CDS_info_2.append(CDS_info[0])
        for hit in gene_it_7:
            gene_size_list.append(hit.group(1))
            gene_size_list_2=[x.replace('1..', '') for x in gene_size_list]
        for match in gene_it_3:
            final_geneseq.append(match.group(1))        
            for i in final_geneseq:
                final_geneseq=[re.sub(r'\d+', '', i) for i in final_geneseq]                    
                final_geneseq=[i.replace(' ', '') for i in final_geneseq]
        for item in CDS_it_1:
            full_dict[item.group(1)]=[gene_size_list_2[0], str(CDS_info_2[0]), final_geneseq[0]]

    CDS_joins_dict={}

    for entry in genbank:
        CDS_list=[]    
        CDS_it_5=p5.finditer(entry)    
        CDS_it_1=p1.finditer(entry)
        for hit in CDS_it_5:
            CDS_list.append(hit.group(6))
            CDS_list= [x.replace('>', '') for x in CDS_list] # to remove symbols and keep only the numbers
            CDS_list= [y.replace(' ', '') for y in CDS_list] # to remove the space from multiple lines
            for item in CDS_it_1:            
                CDS_joins_dict[item.group(1)]=[CDS_list[0]]

    for key in full_dict.keys():
        if key in CDS_joins_dict.keys():
            CDS_joins_dict[key] = CDS_joins_dict[key] + full_dict[key]
    
    return CDS_joins_dict
# the returned dictionary is very important as there CDS_joins regex excludes
# multiple entries joins and we only want to keep those
