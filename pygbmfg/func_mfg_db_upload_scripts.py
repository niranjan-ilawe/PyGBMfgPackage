from pydb import get_postgres_connection, batch_upload_df


def upload_func_data(dfs, username="cpdda", db_name="cpdda"):

    dfs = dfs[
        [
            "pn",
            "pn_desc",
            "ln",
            "wo",
            "mfg_date",
            "exp_date",
            "mfg_by",
            "planned_vol",
            "unfunc_gb_vol_1",
            "lig1_vol",
            "lig2_vol",
            "total_lig1_vol",
            "total_lig2_vol",
            "final_vol",
            "mfg_site",
            "mfg_area",
            "mfg_process",
        ]
    ]

    conn = get_postgres_connection(
        service_name="cpdda-postgres", username=username, db_name=db_name
    )

    cur = conn.cursor()
    new_wo = tuple(dfs.wo.unique().astype(str))
    cur.execute(f"DELETE FROM gbmfg.func_mfgdata WHERE wo IN {new_wo};")
    conn.commit()

    res = batch_upload_df(conn=conn, df=dfs, tablename="gbmfg.func_mfgdata")
    conn.commit()
