-- Bulk Div table
drop table if exists gbmfg.bulkdiv;
create table gbmfg.bulkdiv (
	pn varchar(50) null,
	wo varchar(50) null,
	lot varchar(50) null,
	"date" varchar(50) null,
	sheet varchar(100) null,
    "type" varchar(20) null,
    plate varchar(20) null,
    well varchar(10) null,
    counts numeric null,
    median numeric null,
    disposition varchar(10) null
);