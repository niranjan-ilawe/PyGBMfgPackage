from datetime import date, timedelta
from pybox import box_create_df_from_files, get_box_client

import pandas as pd

from pygbmfg.disp_mfg.file_reading_scripts import (
    read_agora_br_revB,
    read_agora_br_revD,
    read_mav_br_revD,
    read_mav_br_revE,
    read_mav_br_revF,
    read_orion_br_revC,
    read_orion_br_revD,
    read_vdj_br_revD,
    read_vdj_br_revE,
)


def get_disp_mfg_data(days=3):

    last_modified_date = str(date.today() - timedelta(days=days))
    print(f"Looking for new data since {last_modified_date} ....")

    client = get_box_client()

    ## Get GB Dispensing MFG Data
    mav = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="110045548381",
        file_extension="xlsx",
        file_pattern="Next GEM",
        file_parsing_functions=read_mav_br_revD,
    )

    mav = mav.append(
        box_create_df_from_files(
            box_client=client,
            last_modified_date=last_modified_date,
            box_folder_id="110045548381",
            file_extension="xlsx",
            file_pattern="Next GEM",
            file_parsing_functions=read_mav_br_revE,
        )
    )

    mav = mav.append(
        box_create_df_from_files(
            box_client=client,
            last_modified_date=last_modified_date,
            box_folder_id="110045548381",
            file_extension="xlsx",
            file_pattern="Next GEM",
            file_parsing_functions=read_mav_br_revF,
        )
    )

    if mav.shape[0] > 0:
        mav = mav.dropna(subset=["wo", "ln"])
        mav = mav.drop_duplicates(subset=["wo"])
        mav["wo"] = pd.to_numeric(mav["wo"], errors="coerce", downcast="integer")
        mav = mav.assign(mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Dispensing")
        mav.mfg_date = mav.mfg_date.astype(str)

    mav_sg = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="141795338496",
        file_extension="xlsx",
        file_pattern="Next GEM",
        file_parsing_functions=read_mav_br_revF,
    )

    if mav_sg.shape[0] > 0:
        mav_sg = mav_sg.dropna(subset=["wo", "ln"])
        mav_sg = mav_sg.drop_duplicates(subset=["wo"])
        mav_sg["wo"] = pd.to_numeric(mav_sg["wo"], errors="coerce", downcast="integer")
        mav_sg = mav_sg.assign(
            mfg_site="SG", mfg_area="GB MFG", mfg_process="GB Dispensing"
        )
        mav_sg.mfg_date = mav_sg.mfg_date.astype(str)

    vdj = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="110047069633",
        file_extension="xlsx",
        file_pattern="Strip",
        file_parsing_functions=read_vdj_br_revD,
    )

    vdj = vdj.append(
        box_create_df_from_files(
            box_client=client,
            last_modified_date=last_modified_date,
            box_folder_id="110047069633",
            file_extension="xlsx",
            file_pattern="Strip",
            file_parsing_functions=read_vdj_br_revE,
        )
    )

    if vdj.shape[0] > 0:
        vdj = vdj.dropna(subset=["wo", "ln"])
        vdj = vdj.drop_duplicates(subset=["wo"])
        vdj["wo"] = pd.to_numeric(vdj["wo"], errors="coerce", downcast="integer")
        vdj = vdj.assign(mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Dispensing")
        vdj.mfg_date = vdj.mfg_date.astype(str)

    vdj_sg = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="148976871240",
        file_extension="xlsx",
        file_pattern="Strip",
        file_parsing_functions=read_vdj_br_revD,
    )

    if vdj_sg.shape[0] > 0:
        vdj_sg = vdj_sg.dropna(subset=["wo", "ln"])
        vdj_sg = vdj_sg.drop_duplicates(subset=["wo"])
        vdj_sg["wo"] = pd.to_numeric(vdj_sg["wo"], errors="coerce", downcast="integer")
        vdj_sg = vdj_sg.assign(
            mfg_site="SG", mfg_area="GB MFG", mfg_process="GB Dispensing"
        )
        vdj_sg.mfg_date = vdj_sg.mfg_date.astype(str)

    orion = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="110058190356",
        file_extension="xlsx",
        file_pattern="Strip",
        file_parsing_functions=read_orion_br_revC,
    )

    orion = orion.append(
        box_create_df_from_files(
            box_client=client,
            last_modified_date=last_modified_date,
            box_folder_id="110058190356",
            file_extension="xlsx",
            file_pattern="Strip",
            file_parsing_functions=read_orion_br_revD,
        )
    )

    if orion.shape[0] > 0:
        orion = orion.dropna(subset=["wo", "ln"])
        orion = orion.drop_duplicates(subset=["wo"])
        orion["wo"] = pd.to_numeric(orion["wo"], errors="coerce", downcast="integer")
        orion = orion.assign(
            mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Dispensing"
        )
        orion.mfg_date = orion.mfg_date.astype(str)

    agora = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="120705401637",
        file_extension="xlsx",
        file_pattern="Strip",
        file_parsing_functions=read_agora_br_revB,
    )

    agora = agora.append(
        box_create_df_from_files(
            box_client=client,
            last_modified_date=last_modified_date,
            box_folder_id="120705401637",
            file_extension="xlsx",
            file_pattern="Strip",
            file_parsing_functions=read_agora_br_revD,
        )
    )

    if agora.shape[0] > 0:
        agora = agora.dropna(subset=["wo", "ln"])
        agora = agora.drop_duplicates(subset=["wo"])
        agora["wo"] = pd.to_numeric(agora["wo"], errors="coerce", downcast="integer")
        agora = agora.assign(
            mfg_site="CA", mfg_area="GB MFG", mfg_process="GB Dispensing"
        )
        agora.mfg_date = agora.mfg_date.astype(str)

    dfs = mav.append(mav_sg.append(vdj.append(vdj_sg.append(orion.append(agora)))))

    return dfs
