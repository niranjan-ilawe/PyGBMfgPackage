from datetime import date, timedelta
from pybox import box_create_df_from_files, get_box_client

import pandas as pd

from pygbmfg.func_qc.file_reading_scripts import (
    read_flowcam_file,
    read_flowcam_standards_file,
    read_agora_divvar_file_revB,
    read_mav_divvar_file,
    read_vdj_divvar_file_revL,
    read_orion_divvar_file_revB,
    read_vdj_divvar_file_revJ,
)


def get_flowcam_data(days=3):

    last_modified_date = str(date.today() - timedelta(days=days))
    print(f"Looking for new data since {last_modified_date} ....")

    client = get_box_client()

    ## Get Maverick Flowcam Data
    mav = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="112743475504",
        file_extension="xlsx",
        file_pattern="FlowCam",
        file_parsing_functions=read_flowcam_file,
    )

    if mav.shape[0] > 0:
        mav.date = mav.date.astype(str)
        mav = mav.assign(site="CA")

    ## Get SG Maverick Flowcam Data
    mav_sg = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="137080509572",
        file_extension="xlsx",
        file_pattern="FlowCam",
        file_parsing_functions=read_flowcam_file,
    )

    if mav_sg.shape[0] > 0:
        mav_sg.date = mav_sg.date.astype(str)
        mav_sg = mav_sg.assign(site="SG")

    ## Get VDJ Flowcam Data
    vdj = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="112736689427",
        file_extension="xlsx",
        file_pattern="FlowCam",
        file_parsing_functions=read_flowcam_file,
    )

    if vdj.shape[0] > 0:
        vdj.date = vdj.date.astype(str)
        vdj = vdj.assign(site="CA")

    ## Get SG VDJ Flowcam Data
    vdj_sg = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="146648435004",
        file_extension="xlsx",
        file_pattern="FlowCam",
        file_parsing_functions=read_flowcam_file,
    )

    if vdj_sg.shape[0] > 0:
        vdj_sg.date = vdj_sg.date.astype(str)
        vdj_sg = vdj_sg.assign(site="SG")

    ## Get Orion Flowcam Data
    orion = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="112528373429",
        file_extension="xlsx",
        file_pattern="FlowCam",
        file_parsing_functions=read_flowcam_file,
    )

    if orion.shape[0] > 0:
        orion.date = orion.date.astype(str)
        orion = orion.assign(site="CA")

    ## Get Agora Flowcam Data
    agora = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="121309822366",
        file_extension="xlsx",
        file_pattern="FlowCam",
        file_parsing_functions=read_flowcam_file,
    )

    if agora.shape[0] > 0:
        agora.date = agora.date.astype(str)
        agora = agora.assign(site="CA")

    ## Get VDJ Goose Flowcam Data
    vdj_goose = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="141540150435",
        file_extension="xlsx",
        file_pattern="FlowCam",
        file_parsing_functions=read_flowcam_file,
    )

    if vdj_goose.shape[0] > 0:
        vdj_goose.date = vdj_goose.date.astype(str)
        vdj_goose = vdj_goose.assign(site="CA")

    ## Get Mav Goose Flowcam Data
    mav_goose = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="142980374443",
        file_extension="xlsx",
        file_pattern="FlowCam",
        file_parsing_functions=read_flowcam_file,
    )

    if mav_goose.shape[0] > 0:
        mav_goose.date = mav_goose.date.astype(str)
        mav_goose = mav_goose.assign(site="CA")

    dfs1 = mav.append(
        vdj.append(
            orion.append(
                agora.append(vdj_goose.append(mav_goose.append(mav_sg.append(vdj_sg))))
            )
        )
    )
    if dfs1.shape[0] > 0:
        dfs1.date = dfs1.date.astype(str)

    return dfs1


def get_divvar_data(days=3):

    last_modified_date = str(date.today() - timedelta(days=days))
    print(f"Looking for new data since {last_modified_date} ....")

    client = get_box_client()

    ## Get Maverick Divvar Data
    mav = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="112743475504",
        file_extension="xlsx",
        file_pattern="DivVar",
        file_parsing_functions=read_mav_divvar_file,
    )

    if mav.shape[0] > 0:
        mav.date = mav.date.astype(str)
        mav = mav.assign(site="CA")

    ## Get SG Maverick Divvar Data
    mav_sg = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="137080509572",
        file_extension="xlsx",
        file_pattern="DivVar",
        file_parsing_functions=read_mav_divvar_file,
    )

    if mav_sg.shape[0] > 0:
        mav_sg.date = mav_sg.date.astype(str)
        mav_sg = mav_sg.assign(site="SG")

    ## Get VDJ Divvar Data
    vdj_1 = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="112736689427",
        file_extension="xlsx",
        file_pattern="DivVar",
        file_parsing_functions=read_vdj_divvar_file_revJ,
    )

    vdj_2 = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="112736689427",
        file_extension="xlsx",
        file_pattern="DivVar",
        file_parsing_functions=read_vdj_divvar_file_revL,
    )

    vdj = vdj_1.append(vdj_2)

    if vdj.shape[0] > 0:
        vdj.date = vdj.date.astype(str)
        vdj = vdj.assign(site="CA")

    ## Get SG VDJ Divvar Data
    vdj_sg_1 = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="146648435004",
        file_extension="xlsx",
        file_pattern="DivVar",
        file_parsing_functions=read_vdj_divvar_file_revJ,
    )

    vdj_sg_2 = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="146648435004",
        file_extension="xlsx",
        file_pattern="DivVar",
        file_parsing_functions=read_vdj_divvar_file_revL,
    )

    vdj_sg = vdj_sg_1.append(vdj_sg_2)

    if vdj_sg.shape[0] > 0:
        vdj_sg.date = vdj_sg.date.astype(str)
        vdj_sg = vdj_sg.assign(site="SG")

    ## Get Orion Divvar Data
    orion = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="112528373429",
        file_extension="xlsx",
        file_pattern="DivVar",
        file_parsing_functions=read_orion_divvar_file_revB,
    )

    if orion.shape[0] > 0:
        orion.date = orion.date.astype(str)
        orion = orion.assign(site="CA")

    ## Get Agora Divvar Data
    agora = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="121309822366",
        file_extension="xlsx",
        file_pattern="DivVar",
        file_parsing_functions=read_agora_divvar_file_revB,
    )

    if agora.shape[0] > 0:
        agora.date = agora.date.astype(str)
        agora = agora.assign(site="CA")

    df = mav.append(mav_sg.append(vdj.append(vdj_sg.append(orion.append(agora)))))

    return df


def get_flowcam_std_data(days=3):

    last_modified_date = str(date.today() - timedelta(days=days))
    print(f"Looking for new data since {last_modified_date} ....")

    client = get_box_client()

    ## Get Maverick Flowcam Data
    mav = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="112743475504",
        file_extension="xlsx",
        file_pattern="FlowCam",
        file_parsing_functions=read_flowcam_standards_file,
    )

    if mav.shape[0] > 0:
        mav.date = mav.date.astype(str)
        mav = mav.assign(site="CA")

    ## Get SG Maverick Flowcam Data
    mav_sg = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="137080509572",
        file_extension="xlsx",
        file_pattern="FlowCam",
        file_parsing_functions=read_flowcam_standards_file,
    )

    if mav_sg.shape[0] > 0:
        mav_sg.date = mav_sg.date.astype(str)
        mav_sg = mav_sg.assign(site="SG")

        ## Get VDJ Flowcam Data
    vdj = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="112736689427",
        file_extension="xlsx",
        file_pattern="FlowCam",
        file_parsing_functions=read_flowcam_standards_file,
    )

    if vdj.shape[0] > 0:
        vdj.date = vdj.date.astype(str)
        vdj = vdj.assign(site="CA")

    ## Get SG VDJ Flowcam Data
    vdj_sg = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="146648435004",
        file_extension="xlsx",
        file_pattern="FlowCam",
        file_parsing_functions=read_flowcam_standards_file,
    )

    if vdj_sg.shape[0] > 0:
        vdj_sg.date = vdj_sg.date.astype(str)
        vdj_sg = vdj_sg.assign(site="SG")

    ## Get Orion Flowcam Data
    orion = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="112528373429",
        file_extension="xlsx",
        file_pattern="FlowCam",
        file_parsing_functions=read_flowcam_standards_file,
    )

    if orion.shape[0] > 0:
        orion.date = orion.date.astype(str)
        orion = orion.assign(site="CA")

    ## Get Agora Flowcam Data
    agora = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="121309822366",
        file_extension="xlsx",
        file_pattern="FlowCam",
        file_parsing_functions=read_flowcam_standards_file,
    )

    if agora.shape[0] > 0:
        agora.date = agora.date.astype(str)
        agora = agora.assign(site="CA")

    ## Get VDJ Goose Flowcam Data
    vdj_goose = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="141540150435",
        file_extension="xlsx",
        file_pattern="FlowCam",
        file_parsing_functions=read_flowcam_standards_file,
    )

    if vdj_goose.shape[0] > 0:
        vdj_goose.date = vdj_goose.date.astype(str)
        vdj_goose = vdj_goose.assign(site="CA")

    ## Get Mav Goose Flowcam Data
    mav_goose = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="142980374443",
        file_extension="xlsx",
        file_pattern="FlowCam",
        file_parsing_functions=read_flowcam_standards_file,
    )

    if mav_goose.shape[0] > 0:
        mav_goose.date = mav_goose.date.astype(str)
        mav_goose = mav_goose.assign(site="CA")

    dfs1 = mav.append(
        vdj.append(
            orion.append(
                agora.append(vdj_goose.append(mav_goose.append(mav_sg.append(vdj_sg))))
            )
        )
    )
    if dfs1.shape[0] > 0:
        dfs1.date = dfs1.date.astype(str)

    dfs1 = dfs1[pd.to_numeric(dfs1['dia1'], errors='coerce').notnull()]
    dfs1 = dfs1[pd.to_numeric(dfs1['dia2'], errors='coerce').notnull()]
    dfs1 = dfs1[pd.to_numeric(dfs1['dia3'], errors='coerce').notnull()]

    return dfs1


# def get_flowcam_data(last_modified_date, folder_id):
#     client = get_box_client()
#     files = box_ls(
#         client=client,
#         folder_id=folder_id,
#         file_extension="xlsx",
#         pattern="FlowCam",
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
#                     parsing_func=file_reading_scripts.read_flowcam_file,
#                 )
#             )

#     if dfs1.shape[0] > 0:
#         dfs1.date = dfs1.date.astype(str)

#     return dfs1


# def get_mav_divvar_data(last_modified_date, folder_id="112743475504"):
#     client = get_box_client()
#     files = box_ls(
#         client=client,
#         folder_id=folder_id,
#         file_extension="xlsx",
#         pattern="DivVar",
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
#                     parsing_func=file_reading_scripts.read_mav_divvar_file,
#                 )
#             )

#     if dfs1.shape[0] > 0:
#         dfs1.date = dfs1.date.astype(str)
#         dfs1 = dfs1.assign(site="CA")

#     return dfs1


# def get_sg_mav_divvar_data(last_modified_date, folder_id="137080509572"):
#     client = get_box_client()
#     files = box_ls(
#         client=client,
#         folder_id=folder_id,
#         file_extension="xlsx",
#         pattern="DivVar",
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
#                     parsing_func=file_reading_scripts.read_mav_divvar_file,
#                 )
#             )

#     if dfs1.shape[0] > 0:
#         dfs1.date = dfs1.date.astype(str)
#         dfs1 = dfs1.assign(site="SG")

#     return dfs1


# def get_vdj_divvar_data(last_modified_date, folder_id="112736689427"):
#     client = get_box_client()
#     files = box_ls(
#         client=client,
#         folder_id=folder_id,
#         file_extension="xlsx",
#         pattern="DivVar",
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
#                     parsing_func=file_reading_scripts.read_vdj_divvar_file_revJ,
#                 )
#             )

#     dfs2 = pd.DataFrame()
#     if total_no_files > 0:
#         ## READ NEW FILES ----------------------------------
#         for file_id in files.keys():
#             print(f"Parsing file: {files[file_id]}")
#             dfs2 = dfs2.append(
#                 box_read_excel_file(
#                     client=client,
#                     file_id=file_id,
#                     parsing_func=file_reading_scripts.read_vdj_divvar_file_revL,
#                 )
#             )

#     dfs = dfs1.append(dfs2)

#     if dfs.shape[0] > 0:
#         dfs.date = dfs.date.astype(str)
#         dfs = dfs.assign(site="CA")

#     return dfs


# def get_sg_vdj_divvar_data(last_modified_date, folder_id="146648435004"):
#     client = get_box_client()
#     files = box_ls(
#         client=client,
#         folder_id=folder_id,
#         file_extension="xlsx",
#         pattern="DivVar",
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
#                     parsing_func=file_reading_scripts.read_vdj_divvar_file_revJ,
#                 )
#             )

#     dfs2 = pd.DataFrame()
#     if total_no_files > 0:
#         ## READ NEW FILES ----------------------------------
#         for file_id in files.keys():
#             print(f"Parsing file: {files[file_id]}")
#             dfs2 = dfs2.append(
#                 box_read_excel_file(
#                     client=client,
#                     file_id=file_id,
#                     parsing_func=file_reading_scripts.read_vdj_divvar_file_revL,
#                 )
#             )

#     dfs = dfs1.append(dfs2)

#     if dfs.shape[0] > 0:
#         dfs.date = dfs.date.astype(str)
#         dfs = dfs.assign(site="SG")

#     return dfs


# def get_orion_divvar_data(last_modified_date, folder_id="112528373429"):
#     client = get_box_client()
#     files = box_ls(
#         client=client,
#         folder_id=folder_id,
#         file_extension="xlsx",
#         pattern="DivVar",
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
#                     parsing_func=file_reading_scripts.read_orion_divvar_file_revB,
#                 )
#             )

#     if dfs1.shape[0] > 0:
#         dfs1.date = dfs1.date.astype(str)

#     return dfs1


# def get_agora_divvar_data(last_modified_date, folder_id="121309822366"):
#     client = get_box_client()
#     files = box_ls(
#         client=client,
#         folder_id=folder_id,
#         file_extension="xlsx",
#         pattern="DivVar",
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
#                     parsing_func=file_reading_scripts.read_agora_divvar_file_revB,
#                 )
#             )

#     if dfs1.shape[0] > 0:
#         dfs1.date = dfs1.date.astype(str)

#     return dfs1
