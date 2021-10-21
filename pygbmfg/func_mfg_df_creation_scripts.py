from pybox import get_box_client, box_ls, box_parse_excel
from func_mfg_file_reading_scripts import read_maverick_func_br, read_vdj_func_br
import pandas as pd


def get_maverick_data(last_modified_date, mav_folder_id="110045466676"):

    client = get_box_client()

    files = box_ls(
        client=client,
        folder_id=mav_folder_id,
        file_extension="xlsx",
        pattern="SC3",
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
                    parsing_func=read_maverick_func_br,
                )
            )

        dfs1 = dfs1.dropna(subset=["wo", "ln"])
        dfs1 = dfs1.drop_duplicates(subset=["wo"])
        dfs1["unfunc_wo"] = pd.to_numeric(
            dfs1["unfunc_wo"], errors="coerce", downcast="integer"
        )
        dfs1 = dfs1.fillna(0)
        dfs1 = dfs1.assign(
            mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Functionalization"
        )

    return dfs1


def get_vdj_data(last_modified_date, mav_folder_id="110046232258"):

    client = get_box_client()

    files = box_ls(
        client=client,
        folder_id=mav_folder_id,
        file_extension="xlsx",
        pattern="VDJ",
        last_modified=last_modified_date,
    )

    total_no_files = len(files)
    print(f"New files to read .. {total_no_files}")

    dfs2 = pd.DataFrame()
    if total_no_files > 0:
        ## READ NEW FILES ----------------------------------
        for file_id in files.keys():
            print(f"Parsing file: {files[file_id]}")
            dfs2 = dfs2.append(
                box_parse_excel(
                    client=client, file_id=file_id, parsing_func=read_vdj_func_br
                )
            )
        dfs2 = dfs2.dropna(subset=["wo", "ln"])
        dfs2 = dfs2.drop_duplicates(subset=["wo"])
        dfs2 = dfs2.assign(
            mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Functionalization"
        )

    return dfs2
