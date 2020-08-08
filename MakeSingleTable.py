
# to make a single table for inserting into a database merge the previous dicts into
# one single dictionary while keeping only the entries that don't have 
# joins from multiple entries. Empty areas are indicated as 'None'

# below use the previous functions to get the information from your own data
yourgene=GetGeneInfo('yourgenebank.gz')
yourprot=GetProtInfo('yourgenebank.gz')
yourloc=GetLocation('yourgenebank.gz')
yourname=GetGeneName('yourgenebank.gz')

for key in yourgene.keys():
    if key in yourprot.keys():
        yourgene[key].append(str(yourprot[key][0]))
        yourgene[key].append(str(yourprot[key][1]))
    else:
        yourgene[key].append('None')
        yourgene[key].append('None')

for k in yourgene.keys():
    if k in yourloc.keys():
        yourgene[k].append(str(yourloc[k]))
    else:
        yourgene[k].append('None')

for k in yourgene.keys():
    if k in yourname.keys():
        yourgene[k].append(str(yourname[k]))
    else:
        yourgene[k].append('None')


