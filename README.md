# No Biopython - No problem :-)

The code included here is my own work from a coursework during my Bioinformatics studies

With Biopython available to make life easier it seems redundant but this is how you can use RegEx to extract useful information from a Genbank file with multiple Entries including gene sequence, protein sequence, location, name etc

Use it wisely, help yourselves and help others that freaked as I did at first and spread the word/code :-)
Don't be like the duchebag in my group who ripped my code and put his name on it, help whoever needs help :-)

## Conditions to look out for

For the sake of the coursework we had to ignore Gene Entries with multiple sequences (we had to consider only the first) so keep that in mind when using the code and adapt it to suit your needs


## Python functions for:

| Function | Details |
|-------------|-------|
|Entry Accession|Accession number in Genbank file|
|CDS joins|Joins from different Accessions are ignored|
|Gene size|Total size in entry|
|CDS information|Complement strand or not|
|DNA sequence|Total entry sequence from the first entry|
|Protein name|Where provided|
|Protein sequence|Only from the first CDS per entry|
|Entry location|Chromosomal location where provided|
|Gene name|Where provided|

### Additional Python functions for:
| Function | Details |
|-------------|-------|
|Chromosome Unzip|To handle big zipped files and parse the data for extraction|
|Dict2List|To create a table which can be inserted in a mySQL database|


If you have any issues don't hesitate to drop me a line, always happy to help!!
