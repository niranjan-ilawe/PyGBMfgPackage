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