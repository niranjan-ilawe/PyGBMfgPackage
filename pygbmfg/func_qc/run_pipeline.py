# from datetime import date, timedelta

# from pygbmfg.func_qc import df_creation_scripts, db_upload_scripts


# def run_pipeline(days=3):

#     last_modified_date = str(date.today() - timedelta(days=days))

#     # get maverick divvar data
#     try:
#         print("Trying to upload Maverick DivVar data")
#         db_upload_scripts.upload_divvar_data(
#             dfs=df_creation_scripts.get_mav_divvar_data(
#                 last_modified_date=last_modified_date
#             )
#         )
#         print("--Maverick DivVar upload done")
#     except:
#         print("Maverick DivVar data upload failed")

#     # get SG maverick divvar data
#     try:
#         print("Trying to upload SG Maverick DivVar data")
#         db_upload_scripts.upload_divvar_data(
#             dfs=df_creation_scripts.get_sg_mav_divvar_data(
#                 last_modified_date=last_modified_date
#             )
#         )
#         print("--SG Maverick DivVar upload done")
#     except:
#         print("SG Maverick DivVar data upload failed")

#     # get vdj divvar data
#     try:
#         print("Trying to upload VDJ DivVar data")
#         db_upload_scripts.upload_divvar_data(
#             dfs=df_creation_scripts.get_vdj_divvar_data(
#                 last_modified_date=last_modified_date
#             )
#         )
#         print("--VDJ DivVar upload done")
#     except:
#         print("VDJ DivVar data upload failed")

#     # get SG vdj divvar data
#     try:
#         print("Trying to upload SG VDJ DivVar data")
#         db_upload_scripts.upload_divvar_data(
#             dfs=df_creation_scripts.get_sg_vdj_divvar_data(
#                 last_modified_date=last_modified_date
#             )
#         )
#         print("--SG VDJ DivVar upload done")
#     except:
#         print("SG VDJ DivVar data upload failed")

#     # get orion divvar data
#     try:
#         print("Trying to upload Orion DivVar data")
#         db_upload_scripts.upload_divvar_data(
#             dfs=df_creation_scripts.get_orion_divvar_data(
#                 last_modified_date=last_modified_date
#             )
#         )
#         print("--Orion DivVar upload done")
#     except:
#         print("Orion DivVar data upload failed")

#     # get agora divvar data
#     try:
#         print("Trying to upload Agora DivVar data")
#         db_upload_scripts.upload_divvar_data(
#             dfs=df_creation_scripts.get_agora_divvar_data(
#                 last_modified_date=last_modified_date
#             )
#         )
#         print("--Agora DivVar upload done")
#     except:
#         print("Agora DivVar data upload failed")

#     # get maverick flowcam data
#     try:
#         print("Trying to upload Maverick Flowcam data")
#         db_upload_scripts.upload_divvar_data(
#             dfs=df_creation_scripts.get_flowcam_data(
#                 last_modified_date=last_modified_date, folder_id="112743475504"
#             )
#         )
#         print("--Maverick Flowcam upload done")
#     except:
#         print("Maverick Flowcam data upload failed")

#     # get VDJ flowcam data
#     try:
#         print("Trying to upload VDJ Flowcam data")
#         db_upload_scripts.upload_divvar_data(
#             dfs=df_creation_scripts.get_flowcam_data(
#                 last_modified_date=last_modified_date, folder_id="112736689427"
#             )
#         )
#         print("--VDJ Flowcam upload done")
#     except:
#         print("VDJ Flowcam data upload failed")

#     # get orion flowcam data
#     try:
#         print("Trying to upload Orion Flowcam data")
#         db_upload_scripts.upload_divvar_data(
#             dfs=df_creation_scripts.get_flowcam_data(
#                 last_modified_date=last_modified_date, folder_id="112528373429"
#             )
#         )
#         print("--Orion Flowcam upload done")
#     except:
#         print("Orion Flowcam data upload failed")

#     # get agora flowcam data
#     try:
#         print("Trying to upload Agora Flowcam data")
#         db_upload_scripts.upload_divvar_data(
#             dfs=df_creation_scripts.get_flowcam_data(
#                 last_modified_date=last_modified_date, folder_id="121309822366"
#             )
#         )
#         print("--Agora Flowcam upload done")
#     except:
#         print("Agora Flowcam data upload failed")

#     # get vdj goose flowcam data
#     try:
#         print("Trying to upload VDJ Goose Flowcam data")
#         db_upload_scripts.upload_divvar_data(
#             dfs=df_creation_scripts.get_flowcam_data(
#                 last_modified_date=last_modified_date, folder_id="141540150435"
#             )
#         )
#         print("--VDJ Goose Flowcam upload done")
#     except:
#         print("VDJ Goose Flowcam data upload failed")

#     # get mav goose flowcam data
#     try:
#         print("Trying to upload Mav Goose Flowcam data")
#         db_upload_scripts.upload_divvar_data(
#             dfs=df_creation_scripts.get_flowcam_data(
#                 last_modified_date=last_modified_date, folder_id="142980374443"
#             )
#         )
#         print("--Mav Goose Flowcam upload done")
#     except:
#         print("Mav Goose Flowcam data upload failed")

#     return 0
