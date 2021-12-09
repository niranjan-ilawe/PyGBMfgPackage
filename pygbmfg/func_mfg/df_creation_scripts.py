from datetime import date, timedelta
from pybox import box_create_df_from_files, get_box_client

import pandas as pd

from pygbmfg.func_mfg.file_reading_scripts import (
    read_maverick_br,
    read_3hv_br,
    read_5hv_br,
    read_agora_br,
    read_orion_br,
    read_vdj_br,
)


def get_func_mfg_data(days=3):

    last_modified_date = str(date.today() - timedelta(days=days))
    print(f"Looking for new data since {last_modified_date} ....")

    client = get_box_client()

    ## Get Mav Func Data
    mav = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="110045466676",
        file_extension="xlsx",
        file_pattern="SC3",
        file_parsing_functions=read_maverick_br,
    )

    if mav.shape[0] > 0:
        mav = mav.dropna(subset=["wo", "ln"])
        mav = mav.drop_duplicates(subset=["wo"])
        mav["unfunc_wo"] = pd.to_numeric(
            mav["unfunc_wo"], errors="coerce", downcast="integer"
        )
        mav = mav.fillna(0)
        mav = mav.assign(
            mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Functionalization"
        )

    ## Get Mav SG Func Data
    mav_sg = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="140066820062",
        file_extension="xlsx",
        file_pattern="SC3",
        file_parsing_functions=read_maverick_br,
    )

    if mav_sg.shape[0] > 0:
        mav_sg = mav_sg.dropna(subset=["wo", "ln"])
        mav_sg = mav_sg.drop_duplicates(subset=["wo"])
        mav_sg["unfunc_wo"] = pd.to_numeric(
            mav_sg["unfunc_wo"], errors="coerce", downcast="integer"
        )
        mav_sg = mav_sg.fillna(0)
        mav_sg = mav_sg.assign(
            mfg_site="SG", mfg_area="GB MFG", mfg_process="GB Functionalization"
        )

    ## Get VDJ Func Data
    vdj = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="110046232258",
        file_extension="xlsx",
        file_pattern="VDJ",
        file_parsing_functions=read_vdj_br,
    )

    if vdj.shape[0] > 0:
        vdj = vdj.dropna(subset=["wo", "ln"])
        vdj = vdj.drop_duplicates(subset=["wo"])
        vdj = vdj.fillna(0)
        vdj = vdj.assign(
            mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Functionalization"
        )

    ## Get VDJ SG Func Data
    vdj_sg = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="145954162301",
        file_extension="xlsx",
        file_pattern="VDJ",
        file_parsing_functions=read_maverick_br,
    )

    if vdj_sg.shape[0] > 0:
        vdj_sg = vdj_sg.dropna(subset=["wo", "ln"])
        vdj_sg = vdj_sg.drop_duplicates(subset=["wo"])
        vdj_sg = vdj_sg.fillna(0)
        vdj_sg = vdj_sg.assign(
            mfg_site="SG", mfg_area="GB MFG", mfg_process="GB Functionalization"
        )

    ## Get 5HV Func Data
    hv5 = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="110046232258",
        file_extension="xlsx",
        file_pattern="HV",
        file_parsing_functions=read_5hv_br,
    )

    if hv5.shape[0] > 0:
        hv5 = hv5.dropna(subset=["wo", "ln"])
        hv5 = hv5.drop_duplicates(subset=["wo"])
        hv5 = hv5.fillna(0)
        hv5 = hv5.assign(
            mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Functionalization"
        )

    ## Get 3HV Func Data
    hv3 = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="110045466676",
        file_extension="xlsx",
        file_pattern="HV",
        file_parsing_functions=read_3hv_br,
    )

    if hv3.shape[0] > 0:
        hv3 = hv3.dropna(subset=["wo", "ln"])
        hv3 = hv3.drop_duplicates(subset=["wo"])
        hv3 = hv3.fillna(0)
        hv3 = hv3.assign(
            mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Functionalization"
        )

    ## Get Orion Func Data
    orion = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="110057176461",
        file_extension="xlsx",
        file_pattern="Orion",
        file_parsing_functions=read_orion_br,
    )

    if orion.shape[0] > 0:
        orion = orion.dropna(subset=["wo", "ln"])
        orion = orion.drop_duplicates(subset=["wo"])
        orion = orion.fillna(0)
        orion = orion.assign(
            mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Functionalization"
        )

    ## Get Agora Func Data
    agora = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="110057752779",
        file_extension="xlsx",
        file_pattern="ATAC",
        file_parsing_functions=read_agora_br,
    )

    if agora.shape[0] > 0:
        agora = agora.dropna(subset=["wo", "ln"])
        agora = agora.drop_duplicates(subset=["wo"])
        agora = agora.fillna(0)
        agora = agora.assign(
            mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Functionalization"
        )

    df = mav.append(
        mav_sg.append(
            vdj.append(vdj_sg.append(hv5.append(hv3.append(orion.append(agora)))))
        )
    )

    return df

    # def get_maverick_data(last_modified_date, mav_folder_id="110045466676"):

    #     client = get_box_client()

    #     files = box_ls(
    #         client=client,
    #         folder_id=mav_folder_id,
    #         file_extension="xlsx",
    #         pattern="SC3",
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
    #                     parsing_func=file_reading_scripts.read_maverick_br,
    #                 )
    #             )

    #         dfs1 = dfs1.dropna(subset=["wo", "ln"])
    #         dfs1 = dfs1.drop_duplicates(subset=["wo"])
    #         dfs1["unfunc_wo"] = pd.to_numeric(
    #             dfs1["unfunc_wo"], errors="coerce", downcast="integer"
    #         )
    #         dfs1 = dfs1.fillna(0)
    #         dfs1 = dfs1.assign(
    #             mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Functionalization"
    #         )

    #     return dfs1

    # def get_sg_maverick_data(last_modified_date, mav_folder_id="140066820062"):

    #     client = get_box_client()

    #     files = box_ls(
    #         client=client,
    #         folder_id=mav_folder_id,
    #         file_extension="xlsx",
    #         pattern="SC3",
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
    #                     parsing_func=file_reading_scripts.read_maverick_br,
    #                 )
    #             )

    #         dfs1 = dfs1.dropna(subset=["wo", "ln"])
    #         dfs1 = dfs1.drop_duplicates(subset=["wo"])
    #         dfs1["unfunc_wo"] = pd.to_numeric(
    #             dfs1["unfunc_wo"], errors="coerce", downcast="integer"
    #         )
    #         dfs1 = dfs1.fillna(0)
    #         dfs1 = dfs1.assign(
    #             mfg_site="SG", mfg_area="GB MFG", mfg_process="GB Functionalization"
    #         )

    #     return dfs1

    # def get_vdj_data(last_modified_date, mav_folder_id="110046232258"):

    #     client = get_box_client()

    #     files = box_ls(
    #         client=client,
    #         folder_id=mav_folder_id,
    #         file_extension="xlsx",
    #         pattern="VDJ",
    #         last_modified=last_modified_date,
    #     )

    #     total_no_files = len(files)
    #     print(f"New files to read .. {total_no_files}")

    #     dfs2 = pd.DataFrame()
    #     if total_no_files > 0:
    #         ## READ NEW FILES ----------------------------------
    #         for file_id in files.keys():
    #             print(f"Parsing file: {files[file_id]}")
    #             dfs2 = dfs2.append(
    #                 box_read_excel_file(
    #                     client=client,
    #                     file_id=file_id,
    #                     parsing_func=file_reading_scripts.read_vdj_br,
    #                 )
    #             )
    #         dfs2 = dfs2.dropna(subset=["wo", "ln"])
    #         dfs2 = dfs2.drop_duplicates(subset=["wo"])
    #         dfs2 = dfs2.assign(
    #             mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Functionalization"
    #         )

    #     return dfs2

    # def get_sg_vdj_data(last_modified_date, mav_folder_id="145954162301"):

    #     client = get_box_client()

    #     files = box_ls(
    #         client=client,
    #         folder_id=mav_folder_id,
    #         file_extension="xlsx",
    #         pattern="VDJ",
    #         last_modified=last_modified_date,
    #     )

    #     total_no_files = len(files)
    #     print(f"New files to read .. {total_no_files}")

    #     dfs2 = pd.DataFrame()
    #     if total_no_files > 0:
    #         ## READ NEW FILES ----------------------------------
    #         for file_id in files.keys():
    #             print(f"Parsing file: {files[file_id]}")
    #             dfs2 = dfs2.append(
    #                 box_read_excel_file(
    #                     client=client,
    #                     file_id=file_id,
    #                     parsing_func=file_reading_scripts.read_vdj_br,
    #                 )
    #             )
    #         dfs2 = dfs2.dropna(subset=["wo", "ln"])
    #         dfs2 = dfs2.drop_duplicates(subset=["wo"])
    #         dfs2 = dfs2.assign(
    #             mfg_site="SG", mfg_area="GB MFG", mfg_process="GB Functionalization"
    #         )

    #     return dfs2

    # def get_5hv_data(last_modified_date, mav_folder_id="110046232258"):

    #     client = get_box_client()

    #     files = box_ls(
    #         client=client,
    #         folder_id=mav_folder_id,
    #         file_extension="xlsx",
    #         pattern="HV",
    #         last_modified=last_modified_date,
    #     )

    #     total_no_files = len(files)
    #     print(f"New files to read .. {total_no_files}")

    #     dfs2 = pd.DataFrame()
    #     if total_no_files > 0:
    #         ## READ NEW FILES ----------------------------------
    #         for file_id in files.keys():
    #             print(f"Parsing file: {files[file_id]}")
    #             dfs2 = dfs2.append(
    #                 box_read_excel_file(
    #                     client=client,
    #                     file_id=file_id,
    #                     parsing_func=file_reading_scripts.read_5hv_br,
    #                 )
    #             )
    #         dfs2 = dfs2.dropna(subset=["wo", "ln"])
    #         dfs2 = dfs2.drop_duplicates(subset=["wo"])
    #         dfs2 = dfs2.assign(
    #             mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Functionalization"
    #         )

    #     return dfs2

    # def get_3hv_data(last_modified_date, mav_folder_id="110045466676"):

    #     client = get_box_client()

    #     files = box_ls(
    #         client=client,
    #         folder_id=mav_folder_id,
    #         file_extension="xlsx",
    #         pattern="HV",
    #         last_modified=last_modified_date,
    #     )

    #     total_no_files = len(files)
    #     print(f"New files to read .. {total_no_files}")

    #     dfs2 = pd.DataFrame()
    #     if total_no_files > 0:
    #         ## READ NEW FILES ----------------------------------
    #         for file_id in files.keys():
    #             print(f"Parsing file: {files[file_id]}")
    #             dfs2 = dfs2.append(
    #                 box_read_excel_file(
    #                     client=client,
    #                     file_id=file_id,
    #                     parsing_func=file_reading_scripts.read_3hv_br,
    #                 )
    #             )
    #         dfs2 = dfs2.dropna(subset=["wo", "ln"])
    #         dfs2 = dfs2.drop_duplicates(subset=["wo"])
    #         dfs2 = dfs2.assign(
    #             mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Functionalization"
    #         )

    #     return dfs2

    # def get_orion_data(last_modified_date, mav_folder_id="110057176461"):

    #     client = get_box_client()

    #     files = box_ls(
    #         client=client,
    #         folder_id=mav_folder_id,
    #         file_extension="xlsx",
    #         pattern="Orion",
    #         last_modified=last_modified_date,
    #     )

    #     total_no_files = len(files)
    #     print(f"New files to read .. {total_no_files}")

    #     dfs2 = pd.DataFrame()
    #     if total_no_files > 0:
    #         ## READ NEW FILES ----------------------------------
    #         for file_id in files.keys():
    #             print(f"Parsing file: {files[file_id]}")
    #             dfs2 = dfs2.append(
    #                 box_read_excel_file(
    #                     client=client,
    #                     file_id=file_id,
    #                     parsing_func=file_reading_scripts.read_orion_br,
    #                 )
    #             )
    #         dfs2 = dfs2.dropna(subset=["wo", "ln"])
    #         dfs2 = dfs2.drop_duplicates(subset=["wo"])
    #         dfs2 = dfs2.assign(
    #             mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Functionalization"
    #         )

    #     return dfs2

    # def get_agora_data(last_modified_date, mav_folder_id="110057752779"):

    client = get_box_client()

    files = box_ls(
        client=client,
        folder_id=mav_folder_id,
        file_extension="xlsx",
        pattern="ATAC",
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
                box_read_excel_file(
                    client=client,
                    file_id=file_id,
                    parsing_func=file_reading_scripts.read_agora_br,
                )
            )
        dfs2 = dfs2.dropna(subset=["wo", "ln"])
        dfs2 = dfs2.drop_duplicates(subset=["wo"])
        dfs2 = dfs2.assign(
            mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Functionalization"
        )

    return dfs2
