# from datetime import date, timedelta

# from pygbmfg.disp_qc import db_upload_scripts, file_reading_scripts, df_creation_scripts


# def run_pipeline(days=3):

#     last_modified_date = str(date.today() - timedelta(days=days))

#     # get new data from maverick
#     df1 = file_reading_scripts.get_hsv_gsheet_data()

#     try:
#         print("Trying to upload HSV data")
#         db_upload_scripts.upload_hsv_data(dfs=df1)
#         print("--HSV upload done")
#     except:
#         print("HSV data upload failed")

#     # get VDJ Guava data
#     try:
#         print("Getting VDJ Guava data")
#         db_upload_scripts.upload_guava_data(
#             df_creation_scripts.get_guava_data(
#                 last_modified_date, mav_folder_id="112745334633"
#             )
#         )
#         print("VDJ Guava data done")
#     except:
#         print("VDJ Guava data upload failed")

#     # get Maverick Guava data
#     try:
#         print("Getting Mav Guava data")
#         db_upload_scripts.upload_guava_data(
#             df_creation_scripts.get_guava_data(
#                 last_modified_date, mav_folder_id="112745326233"
#             )
#         )
#         print("Mav Guava data done")
#     except:
#         print("Mav Guava data upload failed")

#     # get Orion Guava Data
#     try:
#         print("Getting Orion Guava data")
#         db_upload_scripts.upload_guava_data(
#             df_creation_scripts.get_guava_data(
#                 last_modified_date, mav_folder_id="115715039784"
#             )
#         )
#         print("Orion Guava data done")
#     except:
#         print("Orion Guava data upload failed")

#     # get Agora Guava Data
#     try:
#         print("Getting Agora Guava data")
#         db_upload_scripts.upload_guava_data(
#             df_creation_scripts.get_guava_data(
#                 last_modified_date, mav_folder_id="122324562169"
#             )
#         )
#         print("Agora Guava data done")
#     except:
#         print("Agora Guava data upload failed")

#     # get MavHV Guava Data
#     try:
#         print("Getting MavHV Guava data")
#         db_upload_scripts.upload_guava_data(
#             df_creation_scripts.get_guava_data(
#                 last_modified_date, mav_folder_id="136030428178"
#             )
#         )
#         print("MavHV Guava data done")
#     except:
#         print("MavHV Guava data upload failed")

#     # get VDJHV Guava Data
#     try:
#         print("Getting VDJHV Guava data")
#         db_upload_scripts.upload_guava_data(
#             df_creation_scripts.get_guava_data(
#                 last_modified_date, mav_folder_id="135944908979"
#             )
#         )
#         print("VDJHV Guava data done")
#     except:
#         print("VDJHV Guava data upload failed")

#     return 0
