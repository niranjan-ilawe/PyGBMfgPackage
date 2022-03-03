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
    df1 = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="112745334633",
        file_extension="xlsx",
        file_pattern="Guava",
        file_parsing_functions=read_guava_qc_data,
    )
    if df1.shape[0] > 0:
        df1 = df1.assign(site="CA")

    df2 = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="112745326233",
        file_extension="xlsx",
        file_pattern="Guava",
        file_parsing_functions=read_guava_qc_data,
    )
    if df2.shape[0] > 0:
        df2 = df2.assign(site="CA")

    df3 = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="115715039784",
        file_extension="xlsx",
        file_pattern="Guava",
        file_parsing_functions=read_guava_qc_data,
    )
    if df3.shape[0] > 0:
        df3 = df3.assign(site="CA")

    df4 = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="122324562169",
        file_extension="xlsx",
        file_pattern="Guava",
        file_parsing_functions=read_guava_qc_data,
    )
    if df4.shape[0] > 0:
        df4 = df4.assign(site="CA")

    df5 = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="136030428178",
        file_extension="xlsx",
        file_pattern="Guava",
        file_parsing_functions=read_guava_qc_data,
    )
    if df5.shape[0] > 0:
        df5 = df5.assign(site="CA")

    df6 = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="135944908979",
        file_extension="xlsx",
        file_pattern="Guava",
        file_parsing_functions=read_guava_qc_data,
    )
    if df6.shape[0] > 0:
        df6 = df6.assign(site="CA")

    df7 = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="148802605060",
        file_extension="xlsx",
        file_pattern="Guava",
        file_parsing_functions=read_guava_qc_data,
    )
    if df7.shape[0] > 0:
        df7 = df7.assign(site="SG")

    df8 = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="139290694966",
        file_extension="xlsx",
        file_pattern="Guava",
        file_parsing_functions=read_guava_qc_data,
    )
    if df8.shape[0] > 0:
        df8 = df8.assign(site="SG")

    guava = df1.append(
        df2.append(df3.append(df4.append(df5.append(df6.append(df7.append(df8))))))
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
