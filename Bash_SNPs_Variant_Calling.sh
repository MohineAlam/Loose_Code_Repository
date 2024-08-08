#====================================#
#Variant Calling steps for SNPs
#====================================#

# align reads to reference: BWA
bwa-mem2 index reference_genome.fa
bwa-mem2 mem -t 8 reference_genome.fa reads.fastq > aligned_reads.sam
# convert, sort, and index: Samtools
bwa-mem2 -@ 8 -bS algined_reads.sam | samtools sort -@ 8 -o aligned_reads.bam
samtools index aligned_reads.bam
# remove duplicates: Picard (optional)
picard MarkDuplicates I=aligned_reads.bam O=dedup_reads.bam M=metrics.txt
samtools index dedup_reads.bam
# call SNP variants: BCFtools
samtools mpileup -uf reference_genome.fa dedup_reads.bam | bcftools call -mv -Ov -o raw_snps.vcf
# filter SNPs: BCF Tools
bcftools filter -i 'QUAL>30 & DP>10' raw_snps.vcf > filtered_snps.vcf
# Annotate SNPs: ANNOVAR/SnpEFF
snpEFF ann reference_genome filtered_snp.vcf > annotated_snps.vcf
