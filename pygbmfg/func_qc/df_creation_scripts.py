from pybox import get_box_client, box_ls, box_parse_excel

import pandas as pd

from pygbmfg.func_qc import file_reading_scripts


def get_flowcam_data(last_modified_date, folder_id):
    client = get_box_client()
    files = box_ls(
        client=client,
        folder_id=folder_id,
        file_extension="xlsx",
        pattern="FlowCam",
        last_modified=last_modified_date,
    )

    total_no_files = len(files)
    print(f"New files to read .. {total_no_files}")

    dfs1 = pd.DataFrame()
    if total_no_files > 0:
        ## READ NEW FILES ----------------------------------
        for file_id in files.keys():
            print(f"Parsing file: {files[file_id]}")
            dfs1 = dfs1.append(
                box_parse_excel(
                    client=client,
                    file_id=file_id,
                    parsing_func=file_reading_scripts.read_flowcam_file,
                )
            )

    if dfs1.shape[0] > 0:
        dfs1.date = dfs1.date.astype(str)

    return dfs1


def get_mav_divvar_data(last_modified_date, folder_id="112743475504"):
    client = get_box_client()
    files = box_ls(
        client=client,
        folder_id=folder_id,
        file_extension="xlsx",
        pattern="DivVar",
        last_modified=last_modified_date,
    )

    total_no_files = len(files)
    print(f"New files to read .. {total_no_files}")

    dfs1 = pd.DataFrame()
    if total_no_files > 0:
        ## READ NEW FILES ----------------------------------
        for file_id in files.keys():
            print(f"Parsing file: {files[file_id]}")
            dfs1 = dfs1.append(
                box_parse_excel(
                    client=client,
                    file_id=file_id,
                    parsing_func=file_reading_scripts.read_mav_divvar_file,
                )
            )

    if dfs1.shape[0] > 0:
        dfs1.date = dfs1.date.astype(str)

    return dfs1


def get_vdj_divvar_data(last_modified_date, folder_id="112736689427"):
    client = get_box_client()
    files = box_ls(
        client=client,
        folder_id=folder_id,
        file_extension="xlsx",
        pattern="DivVar",
        last_modified=last_modified_date,
    )

    total_no_files = len(files)
    print(f"New files to read .. {total_no_files}")

    dfs1 = pd.DataFrame()
    if total_no_files > 0:
        ## READ NEW FILES ----------------------------------
        for file_id in files.keys():
            print(f"Parsing file: {files[file_id]}")
            dfs1 = dfs1.append(
                box_parse_excel(
                    client=client,
                    file_id=file_id,
                    parsing_func=file_reading_scripts.read_vdj_divvar_file_revJ,
                )
            )

    dfs2 = pd.DataFrame()
    if total_no_files > 0:
        ## READ NEW FILES ----------------------------------
        for file_id in files.keys():
            print(f"Parsing file: {files[file_id]}")
            dfs2 = dfs2.append(
                box_parse_excel(
                    client=client,
                    file_id=file_id,
                    parsing_func=file_reading_scripts.read_vdj_divvar_file_revL,
                )
            )

    dfs = dfs1.append(dfs2)

    if dfs.shape[0] > 0:
        dfs.date = dfs.date.astype(str)

    return dfs


def get_orion_divvar_data(last_modified_date, folder_id="112528373429"):
    client = get_box_client()
    files = box_ls(
        client=client,
        folder_id=folder_id,
        file_extension="xlsx",
        pattern="DivVar",
        last_modified=last_modified_date,
    )

    total_no_files = len(files)
    print(f"New files to read .. {total_no_files}")

    dfs1 = pd.DataFrame()
    if total_no_files > 0:
        ## READ NEW FILES ----------------------------------
        for file_id in files.keys():
            print(f"Parsing file: {files[file_id]}")
            dfs1 = dfs1.append(
                box_parse_excel(
                    client=client,
                    file_id=file_id,
                    parsing_func=file_reading_scripts.read_orion_divvar_file_revB,
                )
            )

    if dfs1.shape[0] > 0:
        dfs1.date = dfs1.date.astype(str)

    return dfs1


def get_agora_divvar_data(last_modified_date, folder_id="121309822366"):
    client = get_box_client()
    files = box_ls(
        client=client,
        folder_id=folder_id,
        file_extension="xlsx",
        pattern="DivVar",
        last_modified=last_modified_date,
    )

    total_no_files = len(files)
    print(f"New files to read .. {total_no_files}")

    dfs1 = pd.DataFrame()
    if total_no_files > 0:
        ## READ NEW FILES ----------------------------------
        for file_id in files.keys():
            print(f"Parsing file: {files[file_id]}")
            dfs1 = dfs1.append(
                box_parse_excel(
                    client=client,
                    file_id=file_id,
                    parsing_func=file_reading_scripts.read_agora_divvar_file_revB,
                )
            )

    if dfs1.shape[0] > 0:
        dfs1.date = dfs1.date.astype(str)

    return dfs1
