# from datetime import date, timedelta
# from pygbmfg.disp_mfg.db_upload_scripts import upload_data

# from pygbmfg.disp_mfg.df_creation_scripts import (
#     get_agora_data,
#     get_maverick_data,
#     get_orion_data,
#     get_sg_maverick_data,
#     get_sg_vdj_data,
#     get_vdj_data,
# )


# def run_pipeline(days=3):

#     last_modified_date = str(date.today() - timedelta(days=days))

#     # get new data from maverick
#     df1 = get_maverick_data(last_modified_date=last_modified_date)

#     try:
#         print("Trying to upload Maverick data")
#         upload_data(dfs=df1)
#         print("--Maverick upload done")
#     except:
#         print("Maverick data upload failed")

#     # get new data from maverick
#     df5 = get_sg_maverick_data(last_modified_date=last_modified_date)

#     try:
#         print("Trying to upload SG Maverick data")
#         upload_data(dfs=df5)
#         print("--SG Maverick upload done")
#     except:
#         print("SG Maverick data upload failed")

#     # get new data for vdj
#     df2 = get_vdj_data(last_modified_date=last_modified_date)

#     try:
#         print("Trying to upload VDJ data")
#         upload_data(dfs=df2)
#         print("--VDJ upload done")
#     except:
#         print("VDJ data upload failed")

#     # get new data for SG vdj
#     df6 = get_sg_vdj_data(last_modified_date=last_modified_date)

#     try:
#         print("Trying to upload SG VDJ data")
#         upload_data(dfs=df6)
#         print("--SG VDJ upload done")
#     except:
#         print("SG VDJ data upload failed")

#     # get new data for orion
#     df3 = get_orion_data(last_modified_date=last_modified_date)

#     try:
#         print("Trying to upload Orion data")
#         upload_data(dfs=df3)
#         print("--Orion upload done")
#     except:
#         print("Orion data upload failed")

#     # get new data for orion
#     df4 = get_agora_data(last_modified_date=last_modified_date)

#     try:
#         print("Trying to upload Agora data")
#         upload_data(dfs=df4)
#         print("--Agora upload done")
#     except:
#         print("Agora data upload failed")

#     return 0
