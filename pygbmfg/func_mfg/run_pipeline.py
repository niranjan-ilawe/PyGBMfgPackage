from datetime import date, timedelta
from pygbmfg import func_mfg


def run_pipeline(days=3):

    last_modified_date = str(date.today() - timedelta(days=days))

    # get new data from maverick
    df1 = func_mfg.df_creation_scripts.get_maverick_data(
        last_modified_date=last_modified_date
    )

    try:
        print("Trying to upload Maverick data")
        func_mfg.db_upload_scripts.upload_data(dfs=df1)
        print("--Maverick upload done")
    except:
        print("Maverick data upload failed")

    # get new data for vdj
    df2 = func_mfg.df_creation_scripts.get_vdj_data(
        last_modified_date=last_modified_date
    )

    try:
        print("Trying to upload VDJ data")
        func_mfg.db_upload_scripts.upload_data(dfs=df2)
        print("--VDJ upload done")
    except:
        print("VDJ data upload failed")

    # get new data for vdj-vh
    df3 = func_mfg.df_creation_scripts.get_5hv_data(
        last_modified_date=last_modified_date
    )

    try:
        print("Trying to upload VDJ-VH data")
        func_mfg.db_upload_scripts.upload_data(dfs=df3)
        print("--VDJ-VH upload done")
    except:
        print("VDJ-VH data upload failed")

    # get new data for mav-vh
    df4 = func_mfg.df_creation_scripts.get_3hv_data(
        last_modified_date=last_modified_date,
    )

    try:
        print("Trying to upload Maverick-VH data")
        func_mfg.db_upload_scripts.upload_data(dfs=df4)
        print("--Maverick-VH upload done")
    except:
        print("Maverick-VH data upload failed")

    # get new data for orion
    df5 = func_mfg.df_creation_scripts.get_orion_data(
        last_modified_date=last_modified_date,
    )

    try:
        print("Trying to upload Orion data")
        func_mfg.db_upload_scripts.upload_data(dfs=df5)
        print("--Orion upload done")
    except:
        print("Orion data upload failed")

    # get new data for agora
    df6 = func_mfg.df_creation_scripts.get_agora_data(
        last_modified_date=last_modified_date,
    )

    try:
        print("Trying to upload Agora data")
        func_mfg.db_upload_scripts.upload_data(dfs=df6)
        print("--Agora upload done")
    except:
        print("Agora data upload failed")

    return 0
