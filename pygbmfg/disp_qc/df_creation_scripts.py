from pybox import get_box_client, box_ls, box_parse_excel

import pandas as pd

from pygbmfg.disp_qc import file_reading_scripts


def get_guava_data(last_modified_date, mav_folder_id):

    client = get_box_client()

    files = box_ls(
        client=client,
        folder_id=mav_folder_id,
        file_extension="xlsx",
        pattern="Guava",
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
                    parsing_func=file_reading_scripts.read_guava_qc_data,
                )
            )

    return dfs1
