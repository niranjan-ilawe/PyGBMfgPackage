from datetime import date, timedelta

from pygbmfg.disp_qc import db_upload_scripts, file_reading_scripts


def run_pipeline(days=3):

    last_modified_date = str(date.today() - timedelta(days=days))

    # get new data from maverick
    df1 = file_reading_scripts.get_hsv_gsheet_data()

    try:
        print("Trying to upload HSV data")
        db_upload_scripts.upload_hsv_data(dfs=df1)
        print("--HSV upload done")
    except:
        print("HSV data upload failed")

    return 0
