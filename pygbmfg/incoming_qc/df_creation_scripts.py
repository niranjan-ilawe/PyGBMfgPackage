from datetime import date, timedelta
from pybox import box_create_df_from_files, get_box_client

from pygbmfg.incoming_qc.file_reading_scripts import read_well_info

def get_bulkdiv_data(days=3):

    last_modified_date = str(date.today() - timedelta(days=days))
    print(f"Looking for new data since {last_modified_date} ....")

    client = get_box_client()

    ## SC5'
    sc5 = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="146474982725",
        file_extension="xlsx",
        file_pattern="Bulk",
        file_parsing_functions=read_well_info,
    )

    ## SC3'
    sc3 = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="152743757566",
        file_extension="xlsx",
        file_pattern="Bulk",
        file_parsing_functions=read_well_info,
    )

    df = sc5.append(sc3)

    return(df)