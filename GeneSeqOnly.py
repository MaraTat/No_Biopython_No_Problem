### *************** NO NEED FOR REGEX FOR GENE CODE SUPER FAST ********* ########
### The code below is much faster than the RegEx one but it only returns the gene sequence from a genbank file with multiple entries ###

### The idea for the multisplit function was from stackoverflow here: 
### https://stackoverflow.com/questions/1059559/split-strings-into-words-with-multiple-word-boundary-delimiters ###

def multisplit(s, sep):
    mylist = [s]    # to convert a string into a list
    for char in sep:
        slices = []
        for item in mylist:
            slices.extend(item.split(char))
        mylist = slices
    return mylist

with open ('yourgenebankfile.csv', 'r') as file:
    genbank = file.read()#.split('//\n')

genbank2=multisplit(genbank, ('LOCUS', 'ORIGIN'))
del genbank2[0] # to remove the first empty string

genbank3=genbank2[::-2] # to get only the gene sequence, it reverses the order
genbank4=genbank3[::-1] # to get the genes in the right order
genbank4 = [x.replace('\n', '').replace(' ', '').replace('//', '') for x in genbank4]

# yes I know I could have kept one file and used a lambda or something similar here instead of genbank 2-3-4 but this helped me keep track of mistakes
# this code was a quick'n'dirty one that never made it all the way to the final coursework though ;-) 

final_geneseq=[re.sub(r'\d+', '', entry) for entry in genbank4]




