from datetime import date, timedelta
from pybox import box_create_df_from_files, get_box_client

from pygbmfg.kit_qc.file_reading_scripts import read_funcseq_qc_data


def get_funcseq_data(days=3):

    last_modified_date = str(date.today() - timedelta(days=days))
    print(f"Looking for new data since {last_modified_date} ....")

    client = get_box_client()

    ## Get CA SC3' kit data
    ca_sc3 = box_create_df_from_files(
        box_client=client,
        last_modified_date=last_modified_date,
        box_folder_id="112734413150",
        file_extension="xlsx",
        file_pattern="Sequencing",
        file_parsing_functions=read_funcseq_qc_data,
    )

    if ca_sc3.shape[0] > 0:
        ca_sc3 = ca_sc3.assign(site="CA")

    return ca_sc3
