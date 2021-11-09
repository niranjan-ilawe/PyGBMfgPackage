from pybox import get_box_client, box_ls, box_parse_excel

import pandas as pd

from pygbmfg.gen_lin import file_reading_scripts


def get_mav_lineage_data(last_modified_date, folder_id="124985822291"):
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
                    parsing_func=file_reading_scripts.read_gb_lineage,
                )
            )

    return dfs1


def get_vdj_lineage_data(last_modified_date, folder_id="124985456555"):
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
                    parsing_func=file_reading_scripts.read_gb_lineage,
                )
            )

    return dfs1


def get_orion_lineage_data(last_modified_date, folder_id="125795845514"):
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
                    parsing_func=file_reading_scripts.read_gb_lineage,
                )
            )

    return dfs1


def get_agora_lineage_data(last_modified_date, folder_id="125796208104"):
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
                    parsing_func=file_reading_scripts.read_gb_lineage,
                )
            )

    return dfs1
