from datetime import date, timedelta
from pybox import box_create_df_from_files, get_box_client

import pandas as pd

from pygbmfg.func_lin.file_reading_scripts import (
    read_agora_lineage_br,
    read_mav_ligation_plate_br,
    read_mav_lineage_br,
    read_orion_lineage_br,
    read_vdj_ligation_plate_br,
    read_vdj_lineage_br,
)


def get_func_lineage_data(days=3):
    last_modified_date = str(date.today() - timedelta(days=days))
    print(f"Looking for new data since {last_modified_date} ....")

    client = get_box_client()

    ## Get Agora Lineage ---------
    agora = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="110057752779",
        file_extension="xlsx",
        file_pattern="",
        file_parsing_functions=read_agora_lineage_br,
    )

    agora = agora.dropna()

    ## Get Orion Lineage ---------
    orion = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="110057176461",
        file_extension="xlsx",
        file_pattern="",
        file_parsing_functions=read_orion_lineage_br,
    )

    orion = orion.dropna()

    ## Get Maverick CA Lineage ---------
    mav_ca = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="110045466676",
        file_extension="xlsx",
        file_pattern="",
        file_parsing_functions=read_mav_lineage_br,
    )

    mav_ca = mav_ca.dropna()

    ## Get Maverick SG Lineage ---------
    mav_sg = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="140066820062",
        file_extension="xlsx",
        file_pattern="",
        file_parsing_functions=read_mav_lineage_br,
    )

    mav_sg = mav_sg.dropna()

    ## Get VDJ CA Lineage ---------
    vdj_ca = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="110046232258",
        file_extension="xlsx",
        file_pattern="",
        file_parsing_functions=read_vdj_lineage_br,
    )

    vdj_ca = vdj_ca.dropna()

    ## Get VDJ SG Lineage ---------
    vdj_sg = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="145954162301",
        file_extension="xlsx",
        file_pattern="",
        file_parsing_functions=read_vdj_lineage_br,
    )

    vdj_sg = vdj_sg.dropna()

    ## Get Mav Ligation Lineage ---------
    vdj_sg = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="145954162301",
        file_extension="xlsx",
        file_pattern="",
        file_parsing_functions=read_vdj_lineage_br,
    )

    vdj_sg = vdj_sg.dropna()

    df = agora.append(orion.append(mav_ca.append(mav_sg.append(vdj_ca.append(vdj_sg)))))

    return df


def get_func_ligation_lineage_data(days=3):
    last_modified_date = str(date.today() - timedelta(days=days))
    print(f"Looking for new data since {last_modified_date} ....")

    client = get_box_client()

    ## Get Maverick Ligation Lineage ---------
    mav_lig = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="110050633740",
        file_extension="xlsx",
        file_pattern="",
        file_parsing_functions=read_mav_ligation_plate_br,
    )

    mav_lig = mav_lig.dropna()

    ## Get VDJ Ligation Lineage ---------
    vdj_lig = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="110045955262",
        file_extension="xlsx",
        file_pattern="",
        file_parsing_functions=read_vdj_ligation_plate_br,
    )

    vdj_lig = vdj_lig.dropna()

    df = mav_lig.append(vdj_lig)

    return df


# def get_agora_func_lineage_data(last_modified_date, folder_id="110057752779"):
#     client = get_box_client()

#     files = box_ls(
#         client=client,
#         folder_id=folder_id,
#         file_extension="xlsx",
#         pattern="",
#         last_modified=last_modified_date,
#     )

#     total_no_files = len(files)
#     print(f"New files to read .. {total_no_files}")

#     dfs1 = pd.DataFrame()
#     if total_no_files > 0:
#         ## READ NEW FILES ----------------------------------
#         for file_id in files.keys():
#             print(f"Parsing file: {files[file_id]}")
#             dfs1 = dfs1.append(
#                 box_read_excel_file(
#                     client=client,
#                     file_id=file_id,
#                     parsing_func=file_reading_scripts.read_agora_lineage_br,
#                 )
#             )

#     dfs1 = dfs1.dropna()
#     return dfs1


# def get_orion_func_lineage_data(last_modified_date, folder_id="110057176461"):
#     client = get_box_client()

#     files = box_ls(
#         client=client,
#         folder_id=folder_id,
#         file_extension="xlsx",
#         pattern="",
#         last_modified=last_modified_date,
#     )

#     total_no_files = len(files)
#     print(f"New files to read .. {total_no_files}")

#     dfs1 = pd.DataFrame()
#     if total_no_files > 0:
#         ## READ NEW FILES ----------------------------------
#         for file_id in files.keys():
#             print(f"Parsing file: {files[file_id]}")
#             dfs1 = dfs1.append(
#                 box_read_excel_file(
#                     client=client,
#                     file_id=file_id,
#                     parsing_func=file_reading_scripts.read_orion_lineage_br,
#                 )
#             )

#     dfs1 = dfs1.dropna()
#     return dfs1


# def get_mav_func_lineage_data(last_modified_date, folder_id="110045466676"):
#     client = get_box_client()

#     files = box_ls(
#         client=client,
#         folder_id=folder_id,
#         file_extension="xlsx",
#         pattern="",
#         last_modified=last_modified_date,
#     )

#     total_no_files = len(files)
#     print(f"New files to read .. {total_no_files}")

#     dfs1 = pd.DataFrame()
#     if total_no_files > 0:
#         ## READ NEW FILES ----------------------------------
#         for file_id in files.keys():
#             print(f"Parsing file: {files[file_id]}")
#             dfs1 = dfs1.append(
#                 box_read_excel_file(
#                     client=client,
#                     file_id=file_id,
#                     parsing_func=file_reading_scripts.read_mav_lineage_br,
#                 )
#             )

#     dfs1 = dfs1.dropna()
#     return dfs1


# def get_sg_mav_func_lineage_data(last_modified_date, folder_id="140066820062"):
#     client = get_box_client()

#     files = box_ls(
#         client=client,
#         folder_id=folder_id,
#         file_extension="xlsx",
#         pattern="",
#         last_modified=last_modified_date,
#     )

#     total_no_files = len(files)
#     print(f"New files to read .. {total_no_files}")

#     dfs1 = pd.DataFrame()
#     if total_no_files > 0:
#         ## READ NEW FILES ----------------------------------
#         for file_id in files.keys():
#             print(f"Parsing file: {files[file_id]}")
#             dfs1 = dfs1.append(
#                 box_read_excel_file(
#                     client=client,
#                     file_id=file_id,
#                     parsing_func=file_reading_scripts.read_mav_lineage_br,
#                 )
#             )

#     dfs1 = dfs1.dropna()
#     return dfs1


# def get_vdj_func_lineage_data(last_modified_date, folder_id="110046232258"):
#     client = get_box_client()

#     files = box_ls(
#         client=client,
#         folder_id=folder_id,
#         file_extension="xlsx",
#         pattern="",
#         last_modified=last_modified_date,
#     )

#     total_no_files = len(files)
#     print(f"New files to read .. {total_no_files}")

#     dfs1 = pd.DataFrame()
#     if total_no_files > 0:
#         ## READ NEW FILES ----------------------------------
#         for file_id in files.keys():
#             print(f"Parsing file: {files[file_id]}")
#             dfs1 = dfs1.append(
#                 box_read_excel_file(
#                     client=client,
#                     file_id=file_id,
#                     parsing_func=file_reading_scripts.read_vdj_lineage_br,
#                 )
#             )

#     dfs1 = dfs1.dropna()
#     return dfs1


# def get_sg_vdj_func_lineage_data(last_modified_date, folder_id="145954162301"):
#     client = get_box_client()

#     files = box_ls(
#         client=client,
#         folder_id=folder_id,
#         file_extension="xlsx",
#         pattern="",
#         last_modified=last_modified_date,
#     )

#     total_no_files = len(files)
#     print(f"New files to read .. {total_no_files}")

#     dfs1 = pd.DataFrame()
#     if total_no_files > 0:
#         ## READ NEW FILES ----------------------------------
#         for file_id in files.keys():
#             print(f"Parsing file: {files[file_id]}")
#             dfs1 = dfs1.append(
#                 box_read_excel_file(
#                     client=client,
#                     file_id=file_id,
#                     parsing_func=file_reading_scripts.read_vdj_lineage_br,
#                 )
#             )

#     dfs1 = dfs1.dropna()
#     return dfs1


# def get_mav_ligation_lineage_data(last_modified_date, folder_id="110050633740"):
#     client = get_box_client()

#     files = box_ls(
#         client=client,
#         folder_id=folder_id,
#         file_extension="xlsx",
#         pattern="",
#         last_modified=last_modified_date,
#     )

#     total_no_files = len(files)
#     print(f"New files to read .. {total_no_files}")

#     dfs1 = pd.DataFrame()
#     if total_no_files > 0:
#         ## READ NEW FILES ----------------------------------
#         for file_id in files.keys():
#             print(f"Parsing file: {files[file_id]}")
#             dfs1 = dfs1.append(
#                 box_read_excel_file(
#                     client=client,
#                     file_id=file_id,
#                     parsing_func=file_reading_scripts.read_mav_ligation_plate_br,
#                 )
#             )

#     dfs1 = dfs1.dropna()
#     return dfs1


# def get_vdj_ligation_lineage_data(last_modified_date, folder_id="110045955262"):
#     client = get_box_client()

#     files = box_ls(
#         client=client,
#         folder_id=folder_id,
#         file_extension="xlsx",
#         pattern="",
#         last_modified=last_modified_date,
#     )

#     total_no_files = len(files)
#     print(f"New files to read .. {total_no_files}")

#     dfs1 = pd.DataFrame()
#     if total_no_files > 0:
#         ## READ NEW FILES ----------------------------------
#         for file_id in files.keys():
#             print(f"Parsing file: {files[file_id]}")
#             dfs1 = dfs1.append(
#                 box_read_excel_file(
#                     client=client,
#                     file_id=file_id,
#                     parsing_func=file_reading_scripts.read_vdj_ligation_plate_br,
#                 )
#             )

#     dfs1 = dfs1.dropna()

#     return dfs1
