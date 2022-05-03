from termcolor import colored

from pydb import get_postgres_connection, batch_upload_df

from pygbmfg.disp_mfg.df_creation_scripts import get_disp_mfg_data
from pygbmfg.disp_qc.df_creation_scripts import get_disp_guava_data, get_disp_hsv_data
from pygbmfg.func_lin.df_creation_scripts import (
    get_func_ligation_lineage_data,
    get_func_lineage_data,
)
from pygbmfg.func_mfg.df_creation_scripts import get_func_mfg_data
from pygbmfg.func_qc.df_creation_scripts import (
    get_divvar_data,
    get_flowcam_data,
    get_flowcam_std_data,
    get_probehyb_data,
)
from pygbmfg.gen_lin.df_creation_scripts import get_gen_lineage_data
from pygbmfg.gen_mfg.file_reading_scripts import (
    read_channel_yield_sheet,
    read_sg_channel_yield_sheet,
)
from pygbmfg.kit_qc.df_creation_scripts import get_funcseq_data


def run_gb_pipeline(days=3):

    print(colored("****** Pipeline Starting ******", "green"))

    conn = get_postgres_connection(
        service_name="cpdda-postgres", username="cpdda", db_name="cpdda"
    )

    print("---- Getting Kitting QC Data ----")
    try:
        df = get_funcseq_data(days)
        print(colored("---- Uploading Kitting QC Data ----", "green"))
        batch_upload_df(
            conn=conn,
            df=df,
            tablename="gbmfg.kit_funcseq_data",
            insert_type="update",
            key_cols="wo",
        )
    except:
        print(colored("---- Skipping Kitting QC Data ----", "yellow"))

    print("---- Getting Dispensing Mfg Data ----")
    try:
        df = get_disp_mfg_data(days)
        print(colored("---- Uploading Dispensing Mfg Data ----", "green"))
        batch_upload_df(
            conn=conn,
            df=df,
            tablename="gbmfg.disp_mfgdata",
            insert_type="update",
            key_cols="wo",
        )
    except:
        print(colored("---- Skipping Dispensing Mfg Data ----", "yellow"))

    print("---- Getting Dispensing QC Data ----")
    try:
        df1 = get_disp_guava_data(days)
        print(colored("---- Uploading Dispensing QC Data ----", "green"))
        batch_upload_df(
            conn=conn,
            df=df1,
            tablename="gbmfg.disp_guava_data",
            insert_type="update",
            key_cols="wo",
        )
    except:
        print(colored("---- Skipping Guava Data", "yellow"))

    print("---- Getting Dispensing HSV Data ----")
    try:
        df2 = get_disp_hsv_data()
        print(colored("---- Uploading Dispensing HSV Data ----", "green"))
        batch_upload_df(
            conn=conn, df=df2, tablename="gbmfg.disp_hsv_data", insert_type="refresh"
        )
    except:
        print(colored("---- Skipping HSV Data ----", "yellow"))

    print("---- Getting Functionalization Lineage Data ----")
    try:
        df1 = get_func_lineage_data(days)
        print(colored("---- Uploading Functionalization Lineage Data ----", "green"))
        batch_upload_df(
            conn=conn,
            df=df1,
            tablename="gbmfg.func_lineagedata",
            insert_type="update",
            key_cols="wo",
        )
    except:
        print(colored("---- Skipping Functionalization Lineage Data -----", "yellow"))

    print("---- Getting Functionalization Ligation Lineage Data ----")
    try:
        df2 = get_func_ligation_lineage_data(days)
        print(
            colored(
                "---- Uploading Functionalization Ligation Lineage Data ----", "green"
            )
        )
        batch_upload_df(
            conn=conn,
            df=df2,
            tablename="gbmfg.func_lig_lineagedata",
            insert_type="update",
            key_cols="wo",
        )
    except:
        print(
            colored(
                "---- Skipping Functionalization Ligation Lineage Data -----", "yellow"
            )
        )

    print("---- Getting Functionalization Mfg Data ----")
    try:
        df = get_func_mfg_data(days)
        print(colored("---- Uploading Functionalization Mfg Data ----", "green"))
        batch_upload_df(
            conn=conn,
            df=df,
            tablename="gbmfg.func_mfgdata",
            insert_type="update",
            key_cols="wo",
        )
    except:
        print(colored("---- Skipping Functionalization Mfg Data ----", "yellow"))

    print("---- Getting Functionalization Flowcam QC Data ----")
    try:
        df1 = get_flowcam_data(days)
        print(colored("---- Uploading Functionalization Flowcam QC Data ----", "green"))
        batch_upload_df(
            conn=conn,
            df=df1,
            tablename="gbmfg.func_flowcam_data",
            insert_type="update",
            key_cols="wo",
        )
    except:
        print(
            colored("---- Skipping Functionalization Flowcam QC Data -----", "yellow")
        )

    print("---- Getting Functionalization Flowcam Standards Data ----")
    try:
        df1 = get_flowcam_std_data(days)
        # df1 = df1[~df1["dia1"].str.contains("Diameter", na=False)]
        # df1 = df1[~df1["dia1"].str.contains("Sample", na=False)]
        # df1 = df1[~df1["dia2"].str.contains("Sample", na=False)]
        # df1 = df1[~df1["dia3"].str.contains("Sample", na=False)]
        print(
            colored(
                "---- Uploading Functionalization Flowcam Standards Data ----", "green"
            )
        )
        batch_upload_df(
            conn=conn,
            df=df1,
            tablename="gbmfg.func_flowcam_std_data",
            insert_type="update",
            key_cols="wo",
        )
    except:
        print(
            colored(
                "---- Skipping Functionalization Flowcam Standards Data -----", "yellow"
            )
        )

    print("---- Getting Functionalization DivVar QC Data ----")
    try:
        df2 = get_divvar_data(days)
        print(colored("---- Uploading Functionalization DivVar QC Data ----", "green"))
        batch_upload_df(
            conn=conn,
            df=df2,
            tablename="gbmfg.func_divvar_data",
            insert_type="update",
            key_cols="wo",
        )
    except:
        print(colored("---- Skipping Functionalization DivVar Data -----", "yellow"))

    print("---- Getting Functionalization ProbeHyb QC Data ----")
    try:
        df2 = get_probehyb_data(days)
        print(
            colored("---- Uploading Functionalization ProbeHyb QC Data ----", "green")
        )
        batch_upload_df(
            conn=conn,
            df=df2,
            tablename="gbmfg.func_probehyb_data",
            insert_type="update",
            key_cols="wo",
        )
    except:
        print(colored("---- Skipping Functionalization ProbeHyb Data -----", "yellow"))

    print("---- Getting Generation Lineage Data ----")
    try:
        df = get_gen_lineage_data(days)
        print(colored("---- Uploading Generation Lineage Data ----", "green"))
        batch_upload_df(
            conn=conn,
            df=df,
            tablename="gbmfg.gen_lineagedata",
            insert_type="update",
            key_cols="wo",
        )
    except:
        print(colored("---- Skipping Generation Lineage Data ----", "yellow"))

    print("---- Getting PLSTN Generation Yield Data ----")
    try:
        df = read_channel_yield_sheet()
        print(colored("---- Uploading PLSTN Generation Yield Data ----", "green"))
        batch_upload_df(
            conn=conn, df=df, tablename="yield.gb_gen", insert_type="refresh"
        )
    except:
        print(colored("---- Skipping PLSTN Generation Yield Data ----", "yellow"))

    print("---- Getting SG Generation Yield Data ----")
    try:
        df = read_sg_channel_yield_sheet()
        print(colored("---- Uploading SG Generation Yield Data ----", "green"))
        batch_upload_df(
            conn=conn, df=df, tablename="yield.gb_sg_gen", insert_type="refresh"
        )
    except:
        print(colored("---- Skipping SG Generation Yield Data ----", "yellow"))

    print(colored("****** Pipeline Completed ******", "green"))
