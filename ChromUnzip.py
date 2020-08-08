# Importing necessary libraries

import gzip
import re

#==============================================================================

# Primary function to open the zipped chromosome file and extract the data 
# returned as a list split per entry. 

def ChromUnzip(arg):
    """ This function accepts a single argument which is a zipped GenBank 
        file stored on a local drive
                
        Input = zipped input file
        Return = list of unzipped GenBank file to be used in downstream functions
    """
    try:
        with gzip.open (arg, 'rt') as file:
            genbank = file.read().split('//\n')
            genbank = [x.replace('\n', '') for x in genbank]
            genbank = genbank[:(len(genbank)-1):] # necessary because the end of the file contains an empty line
            return genbank
    except:
        return print('Please enter a file in the form of filename.gz')
