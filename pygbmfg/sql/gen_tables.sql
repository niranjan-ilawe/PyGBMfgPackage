-- LINEAGE DATA TABLE
drop table if exists gbmfg.gen_lineagedata;
create table gbmfg.gen_lineagedata (
	pn varchar(30) null,
	wo varchar(30) null,
	ln varchar(30) null,
	mfg_date varchar(30) null,
	from_pn varchar(30) null,
    from_desc varchar(100) null,
    from_wo varchar(100) null
);