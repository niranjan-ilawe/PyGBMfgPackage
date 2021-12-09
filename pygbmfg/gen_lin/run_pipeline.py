# from datetime import date, timedelta

# from pygbmfg.gen_lin import df_creation_scripts, db_upload_scripts


# def run_pipeline(days=3):

#     last_modified_date = str(date.today() - timedelta(days=days))

#     # get maverick lineage data
#     try:
#         print("Trying to upload Maverick Lineage data")
#         db_upload_scripts.upload_lineage_data(
#             dfs=df_creation_scripts.get_mav_lineage_data(
#                 last_modified_date=last_modified_date
#             )
#         )
#         print("--Maverick Lineage upload done")
#     except:
#         print("Maverick Lineage data upload failed")

#     # get SG maverick lineage data
#     try:
#         print("Trying to upload SG Maverick Lineage data")
#         db_upload_scripts.upload_lineage_data(
#             dfs=df_creation_scripts.get_sg_mav_lineage_data(
#                 last_modified_date=last_modified_date
#             )
#         )
#         print("--SG Maverick Lineage upload done")
#     except:
#         print("SG Maverick Lineage data upload failed")

#     # get vdj lineage data
#     try:
#         print("Trying to upload VDJ Lineage data")
#         db_upload_scripts.upload_lineage_data(
#             dfs=df_creation_scripts.get_vdj_lineage_data(
#                 last_modified_date=last_modified_date
#             )
#         )
#         print("--VDJ Lineage upload done")
#     except:
#         print("VDJ Lineage data upload failed")

#     # get SG vdj lineage data
#     try:
#         print("Trying to upload SG VDJ Lineage data")
#         db_upload_scripts.upload_lineage_data(
#             dfs=df_creation_scripts.get_sg_vdj_lineage_data(
#                 last_modified_date=last_modified_date
#             )
#         )
#         print("--SG VDJ Lineage upload done")
#     except:
#         print("SG VDJ Lineage data upload failed")

#     # get orion lineage data
#     try:
#         print("Trying to upload Orion Lineage data")
#         db_upload_scripts.upload_lineage_data(
#             dfs=df_creation_scripts.get_orion_lineage_data(
#                 last_modified_date=last_modified_date
#             )
#         )
#         print("--Orion Lineage upload done")
#     except:
#         print("Orion Lineage data upload failed")

#     # get agora lineage data
#     try:
#         print("Trying to upload Agora Lineage data")
#         db_upload_scripts.upload_lineage_data(
#             dfs=df_creation_scripts.get_agora_lineage_data(
#                 last_modified_date=last_modified_date
#             )
#         )
#         print("--Agora Lineage upload done")
#     except:
#         print("Agora Lineage data upload failed")

#     return 0
