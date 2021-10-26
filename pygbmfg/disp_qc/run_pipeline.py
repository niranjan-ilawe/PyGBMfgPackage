from datetime import date, timedelta
from pygbmfg import disp_qc


def run_pipeline(days=3):

    last_modified_date = str(date.today() - timedelta(days=days))

    # get new data from maverick
    df1 = disp_qc.file_reading_scripts.get_hsv_gsheet_data()

    try:
        print("Trying to upload HSV data")
        disp_qc.db_upload_scripts.upload_hsv_data(dfs=df1)
        print("--HSV upload done")
    except:
        print("HSV data upload failed")

    return 0
