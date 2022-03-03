-- HSV DATA TABLE
drop table if exists gbmfg.disp_hsv_data;
create table gbmfg.disp_hsv_data (
	qc_date varchar(30) null,
	pn varchar(30),
	wo varchar(30),
	qc_operator varchar(30) null,
	run_name varchar(100) null,
	chip_used varchar(50) null,
	layout varchar(20) null,
	chip_lot varchar(20) null,
	oil_lot varchar(20) null,
	bead_lot varchar(20) null,
	hsv varchar(20) null,
	eeprom varchar(20) null,
	is_pinned_gem varchar(20) null,
	is_clog_debris varchar(20) null,
	is_wetting_failure varchar(20) null,
	start_time varchar(30) null,
	end_time varchar(30) null,
	n_equal_0 varchar(20) null,
	n_equal_1 varchar(20) null,
	n_greater_1 varchar(20) null,
	ggf varchar(20) null,
	ggf_cv varchar(20) null,
	bif varchar(20) null,
	bif_cv varchar(20) null,
	cg_rate varchar(20) null,
	tether_rate varchar(20) null,
	drift varchar(20) null,
	big_clump_count varchar(20) null,
	bif_true_cv varchar(20) null,
	small_clump_count varchar(20) null,
	local_noise_cv varchar(20) null,
	plateau_ht varchar(20) null,
	novec_lot varchar(20) null
);

drop table if exists gbmfg.disp_mfgdata;
create table gbmfg.disp_mfgdata (
	pn varchar(20) null,
	pn_desc varchar(50) null,
	wo varchar(20) null,
	ln varchar(12) null,
	mfg_area varchar(30) null,
	mfg_process varchar(30) null,
	mfg_site varchar(10) null,
	mfg_date varchar(30) null,
	planned_qty numeric(12,4) null,
	qty_to_inventory numeric(12,4) null,
	mfg_qty numeric(12,4) null,
	scrap_qty numeric(12,4) null,
	prod_retain_qty numeric(12,4) null,
	qc_retain_qty numeric(12,4) null,
	addn_testing_qty numeric(12,4) null,
	gb_vol_for_dispense numeric(12,4) null,
	gb_vol_for_packaging numeric(12,4) null
);

drop table if exists gbmfg.disp_guava_data;
create table gbmfg.disp_guava_data (
	pn varchar(30) null,
	pn_desc varchar(100) null,
	lot varchar(30) null,
	wo varchar(30) null,
	operator varchar(30) null,
	date varchar(30) null,
	plate varchar(20) null,
	strip varchar(20) null,
	pbeads numeric(12,4) null,
	gb_conc numeric(12,4) null,
	avg_conc_per_well numeric(12,4) null,
	"site" varchar(10) null
);