from datetime import date, timedelta
from pygbmfg import disp_mfg


def run_pipeline(days=3):

    last_modified_date = str(date.today() - timedelta(days=days))

    # get new data from maverick
    df1 = disp_mfg.df_creation_scripts.get_maverick_data(
        last_modified_date=last_modified_date
    )

    try:
        print("Trying to upload Maverick data")
        disp_mfg.db_upload_scripts.upload_data(dfs=df1)
        print("--Maverick upload done")
    except:
        print("Maverick data upload failed")

    # get new data for vdj
    df2 = disp_mfg.df_creation_scripts.get_vdj_data(
        last_modified_date=last_modified_date
    )

    try:
        print("Trying to upload VDJ data")
        disp_mfg.db_upload_scripts.upload_data(dfs=df2)
        print("--VDJ upload done")
    except:
        print("VDJ data upload failed")

    # get new data for orion
    df3 = disp_mfg.df_creation_scripts.get_orion_data(
        last_modified_date=last_modified_date
    )

    try:
        print("Trying to upload Orion data")
        disp_mfg.db_upload_scripts.upload_data(dfs=df3)
        print("--Orion upload done")
    except:
        print("Orion data upload failed")

    # get new data for orion
    df4 = disp_mfg.df_creation_scripts.get_agora_data(
        last_modified_date=last_modified_date
    )

    try:
        print("Trying to upload Agora data")
        disp_mfg.db_upload_scripts.upload_data(dfs=df4)
        print("--Agora upload done")
    except:
        print("Agora data upload failed")

    return 0
