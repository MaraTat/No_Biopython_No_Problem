# Importing necessary libraries

import gzip
import re

#==============================================================================

# Function to extract entry location below. In case of a file where very few entries have location information 
# consider to put this in a separate table to avoid too many 'None' entries but for ease of use in this case 
# it was eventually merged with all other data in the end

def GetLocation(arg):
    """ This is a function that extracts the entry location where available from 
        all entries in a GenBank record file. It accepts as a single argument 
        a zipped GenBank file containing one or multiple entires 
        e.g. an entire chromosome. Entries without location are excluded.
        This function calls on another function: ChromUnzip().
                        
        Input = zipped GenBank record file (one or multiple gene entries)
        Return = a dictionary with the accession number as key and the location
                as value only from entries that have location information.
    """

    genbank = ChromUnzip(arg)
    
    p1=re.compile(r'(?:ACCESSION\s+)(\w+\d+)')
    p9=re.compile(r'(?:/map=")(.+?)(?:"\s+)')   

    loc_dict={}
  
    for entry in genbank:   
        loc_list=[]
        loc_it_9=p9.finditer(entry)
        gene_it_1=p1.finditer(entry)
        for hit in loc_it_9:
            loc_list.append(hit.group(1))
            for item in gene_it_1:
                loc_dict[item.group(1)]=loc_list[0]
    
    return loc_dict
    
    
    
