# Function to convert the dictionaries into lists that can be inserted in the database

def Dict2List(d):    
    """ This is a function that converts a dictionary to a list by joining the
        keys to the values and generates a list which can be loaded into databases.
        
        Input = a dictionary
        Return = a list with merged keys and values
    """

    listkeys=[]
    listvalues=[]

    try:
        for k,v in d.items():
            listkeys.append(k)
            listvalues.append(v)
               
        joinedlist= [[listkeys[i]] + listvalues[i] for i in range(0, len(listkeys))]
        joinedlist = [tuple(l) for l in joinedlist]               
        return joinedlist
        
    except:
        print('Please enter a dictionary')
        
        
