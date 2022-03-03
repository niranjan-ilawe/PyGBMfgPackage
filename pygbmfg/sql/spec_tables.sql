create table gbmfg.specs (
    process varchar(50) NULL,
    pn varchar(20) NULL,
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

INSERT INTO gbmfg.specs (process, pn, data_name, usl, lsl) VALUES
('Kit','1000123','reads_mapped_confidently_to_intronic_regions', 0.421, NULL),
('Kit','1000123','sscrofa111_umi_counts_per_cell_cv', 1.495, NULL),
('Kit','1000123','reads_mapped_confidently_to_intergenic_regions', 0.077, NULL),
('Kit','1000123','multiplet_rate_per_1000_cells', 0.124, NULL),
('Kit','1000123','fraction_reads_in_cells', NULL, 0.922),
('Kit','1000123','relative_difference_of_detected_cells_from_expected_cells', 0.4, -0.4 ),
('Kit','1000123','fraction_umi_counts_for_genes_greaterthan1500nt', NULL, 0.505),
('Kit','1000123','sscrofa111_fraction_reads_in_cells', NULL, 0.895),
('Kit','1000123','grch38_median_genes_per_cell_50k_raw_reads_per_cell', NULL, 1537.6),
('Kit','1000123','sscrofa111_fraction_ribosomal_protein_umi_counts', 0.188, NULL),
('Kit','1000123','valid_barcodes', NULL, 0.977),
('Kit','1000123','grch38_fraction_reads_in_cells', NULL, 0.907),
('Kit','1000123','sscrofa111_fraction_mitochondrial_umi_counts', 0.097, NULL),
('Kit','1000123','sscrofa111_median_umi_counts_per_cell_50k_raw_reads_per_cell', NULL, 3122.1),
('Kit','1000123','grch38_median_umi_counts_per_cell_50k_raw_reads_per_cell', NULL, 5605.7),
('Kit','1000123','sscrofa111_median_genes_per_cell_50k_raw_reads_per_cell', NULL, 1087.3),
('Kit','1000123','fraction_umi_counts_for_genes_500_1000nt', 0.263, NULL),
('Kit','1000123','grch38_fraction_mitochondrial_umi_counts', 0.065, NULL),
('Kit','1000123','fraction_umi_counts_for_genes_lessthan500nt', 0.035, NULL),
('Kit','1000123','fraction_reads_with_primer_or_homopolymer_sequence', 0.119, NULL),
('Kit','1000123','reads_mapped_confidently_to_transcriptome', NULL, 0392),
('Kit','1000123','reads_mapped_confidently_to_exonic_regions', NULL, 0.425),
('Kit','1000123','mean_umi_count_purity_50k_raw_reads_per_cell', NULL, 0.98),
('Kit','1000123','grch38_fraction_ribosomal_protein_umi_counts', 0.371, NULL),
('Kit','1000123','grch38_umi_counts_per_cell_cv', 0.651, NULL),
('Kit','1000123','fraction_reads_usable', NULL, 0.363),
('Kit','1000123','cdna_pcr_duplication_50k_raw_reads_per_cell', 0.72, NULL),
('Kit','1000123','valid_umis', NULL, 0.998),
('Kit','1000123','fraction_umi_counts_for_genes_1000_1500nt', 0.203, NULL);