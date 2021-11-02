from pybox import get_box_client, box_ls, box_parse_excel

import pandas as pd

from pygbmfg.disp_mfg import file_reading_scripts


def get_maverick_data(last_modified_date, mav_folder_id="110045548381"):

    client = get_box_client()

    files = box_ls(
        client=client,
        folder_id=mav_folder_id,
        file_extension="xlsx",
        pattern="Next GEM",
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
                    parsing_func=file_reading_scripts.read_mav_br_revD,
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
                    parsing_func=file_reading_scripts.read_mav_br_revE,
                )
            )

    dfs3 = pd.DataFrame()
    if total_no_files > 0:
        ## READ NEW FILES ----------------------------------
        for file_id in files.keys():
            print(f"Parsing file: {files[file_id]}")
            dfs3 = dfs3.append(
                box_parse_excel(
                    client=client,
                    file_id=file_id,
                    parsing_func=file_reading_scripts.read_mav_br_revF,
                )
            )

    dfs = dfs1.append(dfs2.append(dfs3))

    if dfs.shape[0] > 0:
        dfs = dfs.dropna(subset=["wo", "ln"])
        dfs = dfs.drop_duplicates(subset=["wo"])
        dfs["wo"] = pd.to_numeric(dfs["wo"], errors="coerce", downcast="integer")
        dfs = dfs.assign(mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Dispensing")
        dfs.mfg_date = dfs.mfg_date.astype(str)

    return dfs


def get_vdj_data(last_modified_date, mav_folder_id="110047069633"):

    client = get_box_client()

    files = box_ls(
        client=client,
        folder_id=mav_folder_id,
        file_extension="xlsx",
        pattern="Strip",
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
                    parsing_func=file_reading_scripts.read_vdj_br_revD,
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
                    parsing_func=file_reading_scripts.read_vdj_br_revE,
                )
            )

    dfs = dfs1.append(dfs2)

    if dfs.shape[0] > 0:
        dfs = dfs.dropna(subset=["wo", "ln"])
        dfs = dfs.drop_duplicates(subset=["wo"])
        dfs["wo"] = pd.to_numeric(dfs["wo"], errors="coerce", downcast="integer")
        dfs = dfs.assign(mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Dispensing")
        dfs.mfg_date = dfs.mfg_date.astype(str)

    return dfs


def get_orion_data(last_modified_date, mav_folder_id="110058190356"):

    client = get_box_client()

    files = box_ls(
        client=client,
        folder_id=mav_folder_id,
        file_extension="xlsx",
        pattern="Strip",
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
                    parsing_func=file_reading_scripts.read_orion_br_revD,
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
                    parsing_func=file_reading_scripts.read_orion_br_revC,
                )
            )

    dfs = dfs1.append(dfs2)

    if dfs.shape[0] > 0:
        dfs = dfs.dropna(subset=["wo", "ln"])
        dfs = dfs.drop_duplicates(subset=["wo"])
        dfs["wo"] = pd.to_numeric(dfs["wo"], errors="coerce", downcast="integer")
        dfs = dfs.assign(mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Dispensing")
        dfs.mfg_date = dfs.mfg_date.astype(str)

    return dfs


def get_agora_data(last_modified_date, mav_folder_id="120705401637"):

    client = get_box_client()

    files = box_ls(
        client=client,
        folder_id=mav_folder_id,
        file_extension="xlsx",
        pattern="Strip",
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
                    parsing_func=file_reading_scripts.read_agora_br_revD,
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
                    parsing_func=file_reading_scripts.read_agora_br_revB,
                )
            )

    dfs = dfs1.append(dfs2)

    if dfs.shape[0] > 0:
        dfs = dfs.dropna(subset=["wo", "ln"])
        dfs = dfs.drop_duplicates(subset=["wo"])
        dfs["wo"] = pd.to_numeric(dfs["wo"], errors="coerce", downcast="integer")
        dfs = dfs.assign(mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Dispensing")
        dfs.mfg_date = dfs.mfg_date.astype(str)

    return dfs
