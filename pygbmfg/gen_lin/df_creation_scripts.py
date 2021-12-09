from datetime import date, timedelta
from pybox import box_create_df_from_files, get_box_client

import pandas as pd

from pygbmfg.gen_lin.file_reading_scripts import read_gb_lineage


def get_gen_lineage_data(days=3):

    last_modified_date = str(date.today() - timedelta(days=days))
    print(f"Looking for new data since {last_modified_date} ....")

    client = get_box_client()

    ## Get SG Maverick Lineage Data
    mav_sg = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="134887566078",
        file_extension="xlsx",
        file_pattern="",
        file_parsing_functions=read_gb_lineage,
    )

    ## Get Maverick Lineage Data
    mav = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="124985822291",
        file_extension="xlsx",
        file_pattern="",
        file_parsing_functions=read_gb_lineage,
    )

    ## Get VDJ Lineage Data
    vdj = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="124985456555",
        file_extension="xlsx",
        file_pattern="",
        file_parsing_functions=read_gb_lineage,
    )

    ## Get SG VDJ Lineage Data
    vdj_sg = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="145711664796",
        file_extension="xlsx",
        file_pattern="",
        file_parsing_functions=read_gb_lineage,
    )

    ## Get Orion Lineage Data
    orion = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="125795845514",
        file_extension="xlsx",
        file_pattern="",
        file_parsing_functions=read_gb_lineage,
    )

    ## Get Orion Lineage Data
    agora = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="125796208104",
        file_extension="xlsx",
        file_pattern="",
        file_parsing_functions=read_gb_lineage,
    )

    df = mav.append(mav_sg.append(vdj.append(vdj_sg.append(orion.append(agora)))))

    return df


# def get_sg_mav_lineage_data(last_modified_date, folder_id="134887566078"):
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
#                     parsing_func=file_reading_scripts.read_gb_lineage,
#                 )
#             )

#     return dfs1


# def get_mav_lineage_data(last_modified_date, folder_id="124985822291"):
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
#                     parsing_func=file_reading_scripts.read_gb_lineage,
#                 )
#             )

#     return dfs1


# def get_vdj_lineage_data(last_modified_date, folder_id="124985456555"):
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
#                     parsing_func=file_reading_scripts.read_gb_lineage,
#                 )
#             )

#     return dfs1


# def get_sg_vdj_lineage_data(last_modified_date, folder_id="145711664796"):
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
#                     parsing_func=file_reading_scripts.read_gb_lineage,
#                 )
#             )

#     return dfs1


# def get_orion_lineage_data(last_modified_date, folder_id="125795845514"):
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
#                     parsing_func=file_reading_scripts.read_gb_lineage,
#                 )
#             )

#     return dfs1


# def get_agora_lineage_data(last_modified_date, folder_id="125796208104"):
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
#                     parsing_func=file_reading_scripts.read_gb_lineage,
#                 )
#             )

#     return dfs1
