from pybox import get_box_client, box_ls, box_parse_excel

import pandas as pd

from pygbmfg.func_lin import file_reading_scripts


def get_agora_func_lineage_data(last_modified_date, folder_id="110057752779"):
    client = get_box_client()

    files = box_ls(
        client=client,
        folder_id=folder_id,
        file_extension="xlsx",
        pattern="",
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
                    parsing_func=file_reading_scripts.read_agora_lineage_br,
                )
            )

    dfs1 = dfs1.dropna()
    return dfs1


def get_orion_func_lineage_data(last_modified_date, folder_id="110057176461"):
    client = get_box_client()

    files = box_ls(
        client=client,
        folder_id=folder_id,
        file_extension="xlsx",
        pattern="",
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
                    parsing_func=file_reading_scripts.read_orion_lineage_br,
                )
            )

    dfs1 = dfs1.dropna()
    return dfs1


def get_mav_func_lineage_data(last_modified_date, folder_id="110045466676"):
    client = get_box_client()

    files = box_ls(
        client=client,
        folder_id=folder_id,
        file_extension="xlsx",
        pattern="",
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
                    parsing_func=file_reading_scripts.read_mav_lineage_br,
                )
            )

    dfs1 = dfs1.dropna()
    return dfs1


def get_vdj_func_lineage_data(last_modified_date, folder_id="110046232258"):
    client = get_box_client()

    files = box_ls(
        client=client,
        folder_id=folder_id,
        file_extension="xlsx",
        pattern="",
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
                    parsing_func=file_reading_scripts.read_vdj_lineage_br,
                )
            )

    dfs1 = dfs1.dropna()
    return dfs1


def get_mav_ligation_lineage_data(last_modified_date, folder_id="110050633740"):
    client = get_box_client()

    files = box_ls(
        client=client,
        folder_id=folder_id,
        file_extension="xlsx",
        pattern="",
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
                    parsing_func=file_reading_scripts.read_mav_ligation_plate_br,
                )
            )

    dfs1 = dfs1.dropna()
    return dfs1


def get_vdj_ligation_lineage_data(last_modified_date, folder_id="110045955262"):
    client = get_box_client()

    files = box_ls(
        client=client,
        folder_id=folder_id,
        file_extension="xlsx",
        pattern="",
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
                    parsing_func=file_reading_scripts.read_vdj_ligation_plate_br,
                )
            )

    dfs1 = dfs1.dropna()

    return dfs1
