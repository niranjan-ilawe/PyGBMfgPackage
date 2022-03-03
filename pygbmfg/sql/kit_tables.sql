drop table if exists gbmfg.kit_funcseq_data;
create table gbmfg.kit_funcseq_data (
    pn varchar(60) null,
    lot varchar(30) null,
    wo varchar(40) null,
    date varchar(50) null,
    site varchar(10) null,
    description varchar(100) null,
    sequencer varchar(100) null,
    data_name varchar(100) null,
    data_value numeric null
);