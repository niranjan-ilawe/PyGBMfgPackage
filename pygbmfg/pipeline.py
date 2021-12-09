from pydb import get_postgres_connection, batch_upload_df

from pygbmfg.disp_mfg.df_creation_scripts import get_disp_mfg_data
from pygbmfg.disp_qc.df_creation_scripts import get_disp_guava_data, get_disp_hsv_data
from pygbmfg.func_lin.df_creation_scripts import (
    get_func_ligation_lineage_data,
    get_func_lineage_data,
)
from pygbmfg.func_mfg.df_creation_scripts import get_func_mfg_data
from pygbmfg.func_qc.df_creation_scripts import get_divvar_data, get_flowcam_data
from pygbmfg.gen_lin.df_creation_scripts import get_gen_lineage_data


def run_gb_pipeline(days=3):

    print("****** Pipeline Starting ******")

    conn = get_postgres_connection(
        service_name="cpdda-postgres", username="cpdda", db_name="cpdda"
    )

    print("---- Getting Dispensing Mfg Data ----")
    try:
        df = get_disp_mfg_data(days)
        print("---- Uploading Dispensing Mfg Data ----")
        batch_upload_df(
            conn=conn,
            df=df,
            tablename="gbmfg.disp_mfgdata",
            insert_type="update",
            key_cols="wo",
        )
    except:
        print("---- Skipping Dispensing Mfg Data ----")

    print("---- Getting Dispensing QC Data ----")
    try:
        df1 = get_disp_guava_data(days)
        batch_upload_df(
            conn=conn,
            df=df1,
            tablename="gbmfg.disp_guava_data",
            insert_type="update",
            key_cols="wo",
        )
    except:
        print("---- Skipping Guava Data")

    try:
        df2 = get_disp_hsv_data()
        batch_upload_df(
            conn=conn, df=df2, tablename="gbmfg.disp_hsv_data", insert_type="refresh"
        )
    except:
        print("---- Skipping HSV Data ----")

    print("---- Getting Functionalization Lineage Data ----")
    try:
        df1 = get_func_lineage_data(days)
        print("---- Uploading Functionalization Lineage Data ----")
        batch_upload_df(
            conn=conn,
            df=df1,
            tablename="gbmfg.func_lineagedata",
            insert_type="update",
            key_cols="wo",
        )
    except:
        print("---- Skipping Functionalization Lineage Data -----")

    try:
        df2 = get_func_ligation_lineage_data(days)
        print("---- Uploading Functionalization Ligation Lineage Data ----")
        batch_upload_df(
            conn=conn,
            df=df2,
            tablename="gbmfg.func_lig_lineagedata",
            insert_type="update",
            key_cols="wo",
        )
    except:
        print("---- Skipping Functionalization Ligation Lineage Data -----")

    try:
        print("---- Getting Functionalization Mfg Data ----")
        df = get_func_mfg_data(days)
        print("---- Uploading Functionalization Mfg Data ----")
        batch_upload_df(
            conn=conn,
            df=df,
            tablename="gbmfg.func_mfgdata",
            insert_type="update",
            key_cols="wo",
        )
    except:
        print("---- Skipping Functionalization Mfg Data ----")

    try:
        print("---- Getting Functionalization Flowcam QC Data ----")
        df1 = get_flowcam_data(days)
        print("---- Uploading Functionalization Flowcam QC Data ----")
        batch_upload_df(
            conn=conn,
            df=df1,
            tablename="gbmfg.func_flowcam_data",
            insert_type="update",
            key_cols="wo",
        )
    except:
        print("---- Skipping Functionalization Flowcam Data -----")

    try:
        print("---- Getting Functionalization DivVar QC Data ----")
        df2 = get_divvar_data(days)
        print("---- Uploading Functionalization DivVar QC Data ----")
        batch_upload_df(
            conn=conn,
            df=df2,
            tablename="gbmfg.func_divvar_data",
            insert_type="update",
            key_cols="wo",
        )
    except:
        print("---- Skipping Functionalization DivVar Data -----")

    try:
        print("---- Getting Generation Lineage Data ----")
        df = get_gen_lineage_data(days)
        print("---- Uploading Generation Lineage Data ----")
        batch_upload_df(
            conn=conn,
            df=df,
            tablename="gbmfg.gen_lineagedata",
            insert_type="update",
            key_cols="wo",
        )
    except:
        print("---- Skipping Generation Lineage Data ----")

    print("****** Pipeline Completed ******")
