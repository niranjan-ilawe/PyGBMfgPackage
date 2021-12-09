# from pydb import get_postgres_connection, batch_upload_df


# def upload_hsv_data(dfs, username="cpdda", db_name="cpdda"):

#     conn = get_postgres_connection(
#         service_name="cpdda-postgres", username=username, db_name=db_name
#     )

#     cur = conn.cursor()
#     cur.execute(f"DELETE FROM gbmfg.func_hsv_data;")
#     conn.commit()

#     res = batch_upload_df(conn=conn, df=dfs, tablename="gbmfg.func_hsv_data")
#     conn.commit()


# def upload_guava_data(dfs, username="cpdda", db_name="cpdda"):

#     conn = get_postgres_connection(
#         service_name="cpdda-postgres", username=username, db_name=db_name
#     )

#     cur = conn.cursor()
#     new_wo = tuple(dfs.wo.unique().astype(str))
#     cur.execute(f"DELETE FROM gbmfg.disp_guava_data WHERE wo IN {new_wo};")
#     conn.commit()

#     res = batch_upload_df(conn=conn, df=dfs, tablename="gbmfg.disp_guava_data")
#     conn.commit()
