# from pydb import get_postgres_connection, batch_upload_df


# def upload_data(dfs, username="cpdda", db_name="cpdda"):

#     conn = get_postgres_connection(
#         service_name="cpdda-postgres", username=username, db_name=db_name
#     )

#     cur = conn.cursor()
#     new_wo = tuple(dfs.wo.unique().astype(str))

#     if len(new_wo) <= 1:
#         cur.execute(f"DELETE FROM gbmfg.disp_mfgdata WHERE wo = '{new_wo[0]}';")
#         conn.commit()
#     else:
#         cur.execute(f"DELETE FROM gbmfg.disp_mfgdata WHERE wo IN {new_wo};")
#         conn.commit()

#     res = batch_upload_df(conn=conn, df=dfs, tablename="gbmfg.disp_mfgdata")
#     conn.commit()
