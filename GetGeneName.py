# Importing necessary libraries

import gzip
import re

#==============================================================================
# This is a function to extract the gene name. In case where very few entries
# have this information consider to put this in a separate table to avoid too many 'None' 
# but in this case and for ease of use it was eventually merged with all other data in the end

def GetGeneName(arg):
    """ This is a function that extracts the gene name where available from 
        all entries in a GenBank record file. It accepts as a single argument 
        a zipped GenBank file containing one or multiple entires 
        e.g. an entire chromosome. Entries without gene name are excluded.
        This function calls on another function: ChromUnzip().
                        
        Input = zipped GenBank record file (one or multiple gene entries)
        Return = a dictionary with the accession number as key and the gene name
                as value only from entries that have gene name information.
    """

    genbank = ChromUnzip(arg)
       
    p1=re.compile(r'(?:ACCESSION\s+)(\w+\d+)')
    p6=re.compile(r'(?:/gene=")(.+?)(?:"\s+)')

    gene_name_dict={}
  
    for entry in genbank:
        gene_list=[]    
        gene_it_6=p6.finditer(entry)
        gene_it_1=p1.finditer(entry)       
        for hit in gene_it_6:
            gene_list.append(hit.group(1))
            for item in gene_it_1:
                gene_name_dict[item.group(1)]=gene_list[0]
                
    return gene_name_dict
    
    
    
