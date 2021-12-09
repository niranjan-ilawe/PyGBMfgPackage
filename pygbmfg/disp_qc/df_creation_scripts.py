from datetime import date, timedelta
from pybox import box_create_df_from_files, get_box_client

from pygbmfg.disp_qc.file_reading_scripts import (
    read_guava_qc_data,
    get_hsv_gsheet_data_old,
    get_hsv_gsheet_data_new,
)
from pygbmfg.common import _load_credentials, _clear_credentials


def get_disp_guava_data(days=3):

    last_modified_date = str(date.today() - timedelta(days=days))
    print(f"Looking for new data since {last_modified_date} ....")

    client = get_box_client()

    ## Get GB Dispensing MFG Data
    guava = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="112745334633",
        file_extension="xlsx",
        file_pattern="Next GEM",
        file_parsing_functions=read_guava_qc_data,
    )

    guava = guava.append(
        box_create_df_from_files(
            box_client=client,
            last_modified_date=last_modified_date,
            box_folder_id="112745326233",
            file_extension="xlsx",
            file_pattern="Next GEM",
            file_parsing_functions=read_guava_qc_data,
        )
    )

    guava = guava.append(
        box_create_df_from_files(
            box_client=client,
            last_modified_date=last_modified_date,
            box_folder_id="115715039784",
            file_extension="xlsx",
            file_pattern="Next GEM",
            file_parsing_functions=read_guava_qc_data,
        )
    )

    guava = guava.append(
        box_create_df_from_files(
            box_client=client,
            last_modified_date=last_modified_date,
            box_folder_id="122324562169",
            file_extension="xlsx",
            file_pattern="Next GEM",
            file_parsing_functions=read_guava_qc_data,
        )
    )

    guava = guava.append(
        box_create_df_from_files(
            box_client=client,
            last_modified_date=last_modified_date,
            box_folder_id="136030428178",
            file_extension="xlsx",
            file_pattern="Next GEM",
            file_parsing_functions=read_guava_qc_data,
        )
    )

    guava = guava.append(
        box_create_df_from_files(
            box_client=client,
            last_modified_date=last_modified_date,
            box_folder_id="135944908979",
            file_extension="xlsx",
            file_pattern="Next GEM",
            file_parsing_functions=read_guava_qc_data,
        )
    )

    return guava


def get_disp_hsv_data():
    _load_credentials()
    df1 = get_hsv_gsheet_data_old(
        sheet_id="10bRqRZUBQiQTNIHvMxaCJLk3J3Mjy1zha9kryr1-3L8"
    )
    df2 = get_hsv_gsheet_data_new(
        sheet_id="1pXxjRi0AL5UTdt0lV8VpemN-Aqq7ZetVHtQABfaLVKg"
    )
    df = df1.append(df2)
    _clear_credentials()

    return df
