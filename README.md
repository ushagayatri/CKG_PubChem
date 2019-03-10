# CKG_PubChem
CKG representation of PubChem Neighbor
Processed 3 files of different sizes and observed that data size is reduced to 80% based ct or st values >=90.
See that there are 3505 files in https://ftp.ncbi.nlm.nih.gov/pubchem/Compound_3D/similar_conformers/10/ 
We can start generating the CKG data files for the output files generated.
We are proposing the new CKG format, which is described in the picture.
The CKG format is extended on the top of the RDF Turtle format https://www.w3.org/TR/turtle/
in the way that each subject/predicate/object can include the list of key-value pairs appended 
prefix:entity?key1=value1&key2=value2 
