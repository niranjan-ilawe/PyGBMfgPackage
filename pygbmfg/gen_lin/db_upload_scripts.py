from pydb import get_postgres_connection, batch_upload_df


def upload_lineage_data(dfs, username="cpdda", db_name="cpdda"):

    conn = get_postgres_connection(
        service_name="cpdda-postgres", username=username, db_name=db_name
    )

    cur = conn.cursor()
    new_wo = tuple(dfs.wo.unique().astype(str))
    cur.execute(f"DELETE FROM gbmfg.gen_lineagedata WHERE wo IN {new_wo};")
    conn.commit()

    res = batch_upload_df(conn=conn, df=dfs, tablename="gbmfg.gen_lineagedata")
    conn.commit()
