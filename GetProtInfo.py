# Importing necessary libraries

import gzip
import re

#==============================================================================

# Function to extract information for the protein, includes protein sequence and protein name. 
# Important Note: not all entries have a sequence e.g. pseudogenes, these are not considered

def GetProtInfo(arg):
    """ This is a function that extracts the protein sequence and the protein 
        name from all entries in a GenBank record file. 
        It accepts as a single argument a zipped GenBank file containing one 
        or multiple entires e.g. an entire chromosome. Entries without a protein
        sequence are excluded even if they have a name
        This function calls on another function: ChromUnzip().
                        
        Input = zipped GenBank record file (one or multiple gene entries)
        Return = a dictionary with accession number as the key and a list with
                the protein sequence and the protein name as value only from 
                entries that have a protein sequence available.
    """

    genbank = ChromUnzip(arg)
        
    p1=re.compile(r'(?:ACCESSION\s+)(\w+\d+)') # accession regex
    p4=re.compile(r'(?:translation=")((\w*\s*?)((\s*?\w+\s*?){1,}))(?:\")') # prot seq regex
    p8=re.compile(r'(?:/product=")(.+?)(?:"\s+)') # prot name regex

    prot_seq_dict={}   

    for entry in genbank:
        prot_list=[]    
        prot_it_4=p4.finditer(entry)
        prot_it_1=p1.finditer(entry)
        for match in prot_it_4:
            prot_list.append(match.group(1))
            prot_list=[re.sub(r'\s+', '', prot) for prot in prot_list] # to remove the space from multiple lines
            for item in prot_it_1:
                prot_seq_dict[item.group(1)]=[prot_list[0]]

    prot_name_dict={}
  
    for entry in genbank:    
        name_list=[]
        prot_it_8=p8.finditer(entry)
        gene_it_1=p1.finditer(entry)    
        for hit in prot_it_8:
            name_list.append(hit.group(1))
            for item in gene_it_1:
                prot_name_dict[item.group(1)]=[str(name_list[0])]

    for key in prot_seq_dict.keys():
        if key in prot_name_dict.keys():
            prot_seq_dict[key] = prot_name_dict[key] + prot_seq_dict[key]
        else:
            prot_seq_dict[key] = ['None'] + prot_seq_dict[key]
           
    return prot_seq_dict
    
    
    
