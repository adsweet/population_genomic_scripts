## Scripts useful for population genomic analyses

###**random_snps_vcf.py**
This Python script takes SNP calls (rows) from the data lines (no meta and header information) of a VCF file saved in CSV format and randomly selects one SNP per locus/chromosome. The loci/chromosomes need to be ordered (i.e. grouped in consecutive rows). The output file can be transfered to a VCF file with the correct meta and heading information.

Script usage:
```
python3 random_snps_vcf.py [input csv file] [output file]
```
