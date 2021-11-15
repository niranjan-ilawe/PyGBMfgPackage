create schema gbmfg;

-- MFG DATA TABLE
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

-- DIVVAR DATA TABLE

drop table if exists gbmfg.func_divvar_data;

CREATE TABLE gbmfg.func_divvar_data (
	pn varchar(20) NOT NULL,
	"ln" varchar(50) NOT NULL,
	wo varchar(50) NOT NULL,
	"date" varchar(20) NOT NULL,
	overhang varchar(10) NULL,
	"family" varchar(30) NULL,
	data_name varchar(100) NOT NULL,
	data_value float4 NULL,
	disposition varchar(30) NULL
);

-- FLOWCAM DATA TABLE

drop table if exists gbmfg.func_flowcam_data;

CREATE TABLE gbmfg.func_flowcam_data (
	pn varchar(20) NOT NULL,
	"ln" varchar(50) NOT NULL,
	wo varchar(50) NOT NULL,
	"date" varchar(20) NOT NULL,
	overhang varchar(10) NULL,
	"family" varchar(30) NULL,
	data_name varchar(100) NOT NULL,
	data_value float4 NULL
);

-- LIGATION LINEAGE DATA TABLE
drop table if exists gbmfg.func_lig_lineagedata;
create table gbmfg.func_lig_lineagedata (
	pn varchar(30) null,
	wo varchar(30) null,
	mfg_date varchar(30) null,
	lot varchar(30) null,
    plate varchar(100) null
);

-- FUNC LINEAGE DATA TABLE
drop table if exists gbmfg.func_lineagedata;
create table gbmfg.func_lineagedata (
	pn varchar(30) null,
	wo varchar(100) null,
	ln varchar(30) null,
	mfg_date varchar(30) null,
	lig1 varchar(30) null,
    lig2 varchar(30) null
);