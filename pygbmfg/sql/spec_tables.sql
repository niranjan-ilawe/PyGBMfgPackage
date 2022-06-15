drop table gbmfg.specs;
create table gbmfg.specs (
    process varchar(50) NULL,
    pn varchar(20) NULL,
    data_name varchar(100) NULL,
    data_name varchar(100) NULL,
    usl numeric NULL,
    lsl numeric NULL
);


INSERT INTO gbmfg.specs (process, pn, data_name, usl, lsl) VALUES
('Func', '210170', 'Avg. % of GB''s > 61.4 µm  ', 3.5, NULL),
('Func', '210170', 'Avg. % of GB''s > Q3 + (1.5 x IQR)', 7.5, NULL),
('Func', '210170', 'Avg. Standard Deviation (µm)', 2.0, NULL),
('Func', '210170', 'Avg. Mean Diameter (µm)', 56.85, 54.25),
('Func', '210170', '% of GB''s 70.0-80.0 µm', 0.01, NULL),
('Func', '210170', 'Avg. N (number of GB''s)', NULL, 2000),
('Func', '210170', 'Max. Largest GB  (µm)', 80.0, NULL);

INSERT INTO gbmfg.specs (process, pn, data_name, usl, lsl) VALUES
('Func', '2000461', 'Avg. % of GB''s > 61.4 µm  ', 3.5, NULL),
('Func', '2000461', 'Avg. % of GB''s > Q3 + (1.5 x IQR)', 7.5, NULL),
('Func', '2000461', 'Avg. Standard Deviation (µm)', 2.0, NULL),
('Func', '2000461', 'Avg. Mean Diameter (µm)', 56.85, 54.25),
('Func', '2000461', '% of GB''s 70.0-80.0 µm', 0.01, NULL),
('Func', '2000461', 'Avg. N (number of GB''s)', NULL, 2000),
('Func', '2000461', 'Max. Largest GB  (µm)', 80.0, NULL);

INSERT INTO gbmfg.specs (process, pn, data_name, usl, lsl) VALUES
('Func', '2000058', 'Avg. % of GB''s > 60.0 µm  ', 3.5, NULL),
('Func', '2000058', 'Avg. % of GB''s > Q3 + (1.5 x IQR)', 7.5, NULL),
('Func', '2000058', 'Avg. Standard Deviation (µm)', 2.0, NULL),
('Func', '2000058', 'Avg. Mean Diameter (µm)', 56.25, 54.25),
('Func', '2000058', '% of GB''s 70.0-80.0 µm', 0.01, NULL),
('Func', '2000058', 'Avg. N (number of GB''s)', NULL, 2000),
('Func', '2000058', 'Max. Largest GB  (µm)', 80.0, NULL);

INSERT INTO gbmfg.specs (process, pn, data_name, usl, lsl) VALUES
('Func', '2000211', 'Avg. % of GB''s > 60.0 µm  ', 3.5, NULL),
('Func', '2000211', 'Avg. % of GB''s > Q3 + (1.5 x IQR)', 7.5, NULL),
('Func', '2000211', 'Avg. Standard Deviation (µm)', 2.0, NULL),
('Func', '2000211', 'Avg. Mean Diameter (µm)', 56.25, 54.25),
('Func', '2000211', '% of GB''s 70.0-80.0 µm', 0.01, NULL),
('Func', '2000211', 'Avg. N (number of GB''s)', NULL, 2000),
('Func', '2000211', 'Max. Largest GB  (µm)', 80.0, NULL);

INSERT INTO gbmfg.specs (process, pn, data_name, usl, lsl) VALUES
('Func', '2000114', 'Avg. % of GB''s > 60.0 µm  ', 3.5, NULL),
('Func', '2000114', 'Avg. % of GB''s > Q3 + (1.5 x IQR)', 7.5, NULL),
('Func', '2000114', 'Avg. Standard Deviation (µm)', 2.0, NULL),
('Func', '2000114', 'Avg. Mean Diameter (µm)', 56.25, 54.25),
('Func', '2000114', '% of GB''s 70.0-80.0 µm', 0.01, NULL),
('Func', '2000114', 'Avg. N (number of GB''s)', NULL, 2000),
('Func', '2000114', 'Max. Largest GB  (µm)', 80.0, NULL);

INSERT INTO gbmfg.specs (process, pn, data_name, usl, lsl) VALUES
('Func', '2000260', 'Avg. % of GB''s > 60.0 µm  ', 3.5, NULL),
('Func', '2000260', 'Avg. % of GB''s > Q3 + (1.5 x IQR)', 7.5, NULL),
('Func', '2000260', 'Avg. Standard Deviation (µm)', 2.0, NULL),
('Func', '2000260', 'Avg. Mean Diameter (µm)', 56.25, 54.25),
('Func', '2000260', '% of GB''s 70.0-80.0 µm', 0.01, NULL),
('Func', '2000260', 'Avg. N (number of GB''s)', NULL, 2000),
('Func', '2000260', 'Max. Largest GB  (µm)', 80.0, NULL);

INSERT INTO gbmfg.specs (process, pn, data_name, usl, lsl, product) VALUES
('Kit','1000123','Reads Mapped Confidently to Intronic Regions', 0.39, NULL, 'Next GEM SC3''v3.1'),
('Kit','1000123','sscrofa111_umi_counts_per_cell_cv', NULL, NULL, 'Next GEM SC3''v3.1'),
('Kit','1000123','Reads Mapped Confidently to Intergenic Regions', NULL, NULL, 'Next GEM SC3''v3.1'),
('Kit','1000123','multiplet_rate_per_1000_cells', NULL, NULL, 'Next GEM SC3''v3.1'),
('Kit','1000123','Fraction Reads in Cells', NULL, 0.80, 'Next GEM SC3''v3.1'),
('Kit','1000123','Relative difference of detected cells from expected cells', 0.45, -0.45, 'Next GEM SC3''v3.1'),
('Kit','1000123','Fraction UMI counts for genes >1500nt', NULL, 0.41, 'Next GEM SC3''v3.1'),
('Kit','1000123','sscrofa111_fraction_reads_in_cells', NULL, NULL, 'Next GEM SC3''v3.1'),
('Kit','1000123','GRCh38 Median genes per cell (50k raw reads per cell)', NULL, 1397, 'Next GEM SC3''v3.1'),
('Kit','1000123','sscrofa111_fraction_ribosomal_protein_umi_counts', NULL, NULL, 'Next GEM SC3''v3.1'),
('Kit','1000123','Valid Barcodes', NULL, 0.95, 'Next GEM SC3''v3.1'),
('Kit','1000123','grch38_fraction_reads_in_cells', NULL, NULL, 'Next GEM SC3''v3.1'),
('Kit','1000123','sscrofa111_fraction_mitochondrial_umi_counts', NULL, NULL, 'Next GEM SC3''v3.1'),
('Kit','1000123','sscrofa111_median_umi_counts_per_cell_50k_raw_reads_per_cell', NULL, NULL, 'Next GEM SC3''v3.1'),
('Kit','1000123','GRCh38 Median UMI counts per cell (50k raw reads per cell)', NULL, 4378, 'Next GEM SC3''v3.1'),
('Kit','1000123','sscrofa111_median_genes_per_cell_50k_raw_reads_per_cell', NULL, NULL, 'Next GEM SC3''v3.1'),
('Kit','1000123','Fraction UMI counts for genes 500-1000nt', NULL, NULL, 'Next GEM SC3''v3.1'),
('Kit','1000123','GRCh38 Fraction mitochondrial UMI counts', NULL, NULL, 'Next GEM SC3''v3.1'),
('Kit','1000123','Fraction UMI counts for genes <500nt', NULL, NULL, 'Next GEM SC3''v3.1'),
('Kit','1000123','Fraction reads with primer or homopolymer sequence', 0.2, NULL, 'Next GEM SC3''v3.1'),
('Kit','1000123','Reads Mapped Confidently to Transcriptome', NULL, 0.4, 'Next GEM SC3''v3.1'),
('Kit','1000123','Reads Mapped Confidently to Exonic Regions', NULL, NULL, 'Next GEM SC3''v3.1'),
('Kit','1000123','mean_umi_count_purity_50k_raw_reads_per_cell', NULL, NULL, 'Next GEM SC3''v3.1'),
('Kit','1000123','GRCh38 Fraction ribosomal protein UMI counts', NULL, NULL, 'Next GEM SC3''v3.1'),
('Kit','1000123','GRCh38 UMI counts per cell CV', NULL, NULL, 'Next GEM SC3''v3.1'),
('Kit','1000123','Fraction reads usable', NULL, 0.32, 'Next GEM SC3''v3.1'),
('Kit','1000123','cDNA PCR Duplication (50k raw reads per cell)', 0.80, NULL, 'Next GEM SC3''v3.1'),
('Kit','1000123','Valid UMIs', NULL, 0.99, 'Next GEM SC3''v3.1'),
('Kit','1000123','Fraction UMI counts for genes 1000-1500nt', NULL, NULL, 'Next GEM SC3''v3.1');

INSERT INTO gbmfg.specs (process, pn, data_name, usl, lsl, product) VALUES
('Kit','1000123','Relative difference of detected cells from expected cells', 0.5, -0.5, 'Next GEM SC5'' HT v2'),
('Kit','1000123','Valid Barcodes', NULL, 0.80, 'Next GEM SC5'' HT v2'),
('Kit','1000123','Valid UMIs', NULL, 0.91, 'Next GEM SC5'' HT v2'),
('Kit','1000123','Fraction Reads in Cells', NULL, 0.80, 'Next GEM SC5'' HT v2'),
('Kit','1000123','GRCh38 Median genes per cell (50k raw reads per cell)', NULL, 1001, 'Next GEM SC5'' HT v2'),
('Kit','1000123','GRCh38 Median UMI counts per cell (50k raw reads per cell)', NULL, 2143, 'Next GEM SC5'' HT v2'),
('Kit','1000123','Fraction reads usable', NULL, 0.40, 'Next GEM SC5'' HT v2'),
('Kit','1000123','Reads Mapped Confidently to Transcriptome', NULL, 0.40, 'Next GEM SC5'' HT v2'),
('Kit','1000123','Fraction reads with primer or homopolymer sequence', 0.23, NULL, 'Next GEM SC5'' HT v2');