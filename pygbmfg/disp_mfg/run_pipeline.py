from datetime import date, timedelta

from pygbmfg.disp_mfg import db_upload_scripts, df_creation_scripts


def run_pipeline(days=3):

    last_modified_date = str(date.today() - timedelta(days=days))

    # get new data from maverick
    df1 = df_creation_scripts.get_maverick_data(last_modified_date=last_modified_date)

    try:
        print("Trying to upload Maverick data")
        db_upload_scripts.upload_data(dfs=df1)
        print("--Maverick upload done")
    except:
        print("Maverick data upload failed")

    # get new data for vdj
    df2 = df_creation_scripts.get_vdj_data(last_modified_date=last_modified_date)

    try:
        print("Trying to upload VDJ data")
        db_upload_scripts.upload_data(dfs=df2)
        print("--VDJ upload done")
    except:
        print("VDJ data upload failed")

    # get new data for orion
    df3 = df_creation_scripts.get_orion_data(last_modified_date=last_modified_date)

    try:
        print("Trying to upload Orion data")
        db_upload_scripts.upload_data(dfs=df3)
        print("--Orion upload done")
    except:
        print("Orion data upload failed")

    # get new data for orion
    df4 = df_creation_scripts.get_agora_data(last_modified_date=last_modified_date)

    try:
        print("Trying to upload Agora data")
        db_upload_scripts.upload_data(dfs=df4)
        print("--Agora upload done")
    except:
        print("Agora data upload failed")

    return 0
