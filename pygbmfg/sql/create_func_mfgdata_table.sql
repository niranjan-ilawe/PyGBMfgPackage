create schema gbmfg;
drop table if exists gbmfg.func_mfgdata;
create table gbmfg.func_mfgdata (
	pn int null,
	pn_desc varchar(50) null,
	wo int null,
	ln varchar(12) null,
	mfg_area varchar(30) null,
	mfg_process varchar(30) null,
	mfg_site varchar(10) null,
	mfg_date varchar(30) null,
	exp_date varchar(30) null,
	mfg_by varchar(30) null,
    planned_vol numeric(12,4) null,
	unfunc_wo numeric(12,4) null,
	unfunc_gb_vol_1 numeric(12,4) null,
	unfunc_gb_vol_2 numeric(12,4) null,
	lig1_vol numeric(12,4) null,
	lig2_vol numeric(12, 4) null,
	total_lig1_vol numeric(12,4) null,
	total_lig2_vol numeric(12,4) null,
	final_vol numeric(12,4) null
);