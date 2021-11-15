-- PN Master
create table gbmfg.pn_master (
	"desc" varchar(100) null,
	unfunc varchar(20) null,
	func varchar(20) null,
	disp varchar(20) null
);

INSERT INTO 
    gbmfg.pn_master ("desc", unfunc, func, disp)
VALUES
    ('Maverick','2000057','2000058','2000164'),
    ('VDJ','2000016','210170','2000209'),
    ('Orion','2000244','2000260','2000261'),
    ('Agora (ATAC)','2000110','2000114','2000210'),
    ('Maverick - HV','2000057','2000211','2000443'),
    ('VDJ - HV','2000057','2000461','2000444'),
    ('Green19','2000358','2000359','2000360'),
    ('Turtle','2000428','2000429','2000430');

--- LINEAGE VIEW
create view gbmfg.v_gb_lineage as
select pn, wo, ln,
max(case when (from_pn = '310220') then from_wo else null end) as acrylamide,
max(case when (from_pn = '310364') then from_wo else null end) as vdj_acrydite,
max(case when (from_pn = '2000158') then from_wo else null end) as gb_oil,
max(case when (from_pn = '3000171') then from_wo else null end) as agora_p5,
max(case when (from_pn = '310368') then from_wo else null end) as acrydite_r1,
max(case when (from_pn = '3000151') then from_wo else null end) as acrydite_nxt_r1
from gbmfg.gen_lineagedata
group by pn, wo, ln
order by wo; 

-- WO LINEAGE
create view gbmfg.v_gb_wo_lineage as
select distinct
	gl."ln",
	gl.pn as unfunc_pn,
	gl.wo as unfunc_wo,
	fm.pn as func_pn,
	fm.wo as func_wo,
	dm.pn as disp_pn,
	dm.wo as disp_wo,
	dm.batch as disp_batch
from
	gbmfg.gen_lineagedata gl 
join gbmfg.pn_master ms
	on gl.pn = ms.unfunc
join gbmfg.func_mfgdata fm 
	on ms.func = fm.pn and gl."ln" = fm."ln" 
join gbmfg.disp_mfgdata dm 
	on ms.disp = dm.pn and gl."ln" = dm."ln" 
;

-- GB Func Yield
create view gbmfg.v_gb_func_yield as
select fm.pn, fm."ln",
	avg(coalesce (fm.unfunc_gb_vol_1 + fm.unfunc_gb_vol_2, fm.unfunc_gb_vol_1)) as unfunc_vol,
	sum(coalesce (fm.total_lig1_vol, fm.lig1_vol)) as total_lig1_volume ,
	sum(coalesce (fm.total_lig2_vol, fm.lig2_vol)) as total_lig2_volume ,
	sum(fm.final_vol) as func_vol 
from gbmfg.func_mfgdata fm 
where fm.pn = '2000058'
group by fm.pn,fm."ln"
union all
select 
	dm.pn, dm."ln" ,
	avg(dm.unfunc_gb_vol_1) as unfunc_vol,
	avg(dm.total_lig1_vol) as total_lig1_volume,
	avg(dm.total_lig2_vol) as total_lig2_volume,
	sum(dm.final_vol) as func_vol 
from gbmfg.func_mfgdata dm 
where dm.pn = '210170'
group by dm.pn,dm."ln"
;

-- GB Yield
create view gbmfg.v_gb_yield as
select 
	t.pn,
	t."ln",
	t.unfunc_vol, 
	t.total_lig1_volume, 
	t.total_lig2_volume,
	t.func_vol,
	dm.planned_qty ,
	dm.gb_vol_for_packaging,
	dm.gb_vol_for_dispense,
	dm.mfg_qty,
	dm.qty_to_inventory 
from gbmfg.v_gb_func_yield t
join gbmfg.pn_master pm 
	on t.pn = pm.func
join gbmfg.disp_mfgdata dm 
	on pm.disp = dm.pn and t."ln" = dm."ln"
;
	


