from datetime import date, timedelta
from func_mfg_df_creation_scripts import get_maverick_data, get_vdj_data
from func_mfg_db_upload_scripts import upload_func_data


def run_gb_func_pipeline(days=3):

    last_modified_date = str(date.today() - timedelta(days=days))

    # get new data from maverick
    df1 = get_maverick_data(last_modified_date=last_modified_date)
    # get new data for vdj
    df2 = get_vdj_data(last_modified_date=last_modified_date)

    df = df1.append(df2)

    # upload all data
    upload_func_data(dfs=df)
