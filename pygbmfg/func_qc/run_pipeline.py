from datetime import date, timedelta
from pygbmfg import func_qc


def run_pipeline(days=3):

    last_modified_date = str(date.today() - timedelta(days=days))

    # get mav divvar data
    df = func_qc.df_creation_scripts.get_mav_divvar_data(
        last_modified_date=last_modified_date
    )

    try:
        print("Trying to upload Maverick DivVar data")
        func_qc.db_upload_scripts.upload_divvar_data(dfs=df)
        print("--Maverick DivVar upload done")
    except:
        print("Maverick DivVar data upload failed")

    # get vdj divvar data
    df1 = func_qc.df_creation_scripts.get_vdj_divvar_data(
        last_modified_date=last_modified_date
    )

    try:
        print("Trying to upload VDJ DivVar data")
        func_qc.db_upload_scripts.upload_divvar_data(dfs=df1)
        print("--VDJ DivVar upload done")
    except:
        print("VDJ DivVar data upload failed")

    return 0
