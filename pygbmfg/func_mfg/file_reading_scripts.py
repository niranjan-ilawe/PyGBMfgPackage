import pandas as pd

### Maverick ------------
def read_maverick_br(file):
    try:
        xlsx = pd.ExcelFile(file, engine="openpyxl")
        # Extracting WO's
        df_temp = pd.read_excel(xlsx, sheet_name="Labels", header=None)
        unfunc_wo = df_temp[df_temp[1] == "Unfunctionalized GB Work Order #"].iloc[0, 2]
        oh1_wo = df_temp[df_temp[1] == " Overhang 1 Work Order #"].iloc[0, 2]
        oh2_wo = df_temp[df_temp[1] == " Overhang 2 Work Order #"].iloc[0, 2]
        oh3_wo = df_temp[df_temp[1] == " Overhang 3 Work Order #"].iloc[0, 2]
        oh4_wo = df_temp[df_temp[1] == " Overhang 4 Work Order #"].iloc[0, 2]

        # Overhang 1 & 2
        df_temp = pd.read_excel(xlsx, sheet_name="Overhangs 1+2", header=None)
        unfunc_gb_vol_1 = df_temp[df_temp[1] == "Total"].iloc[0, 3]
        alpha_lig1_vol = df_temp[df_temp[0] == "Ligation 1, Overhang 1, Bottle 1"].iloc[
            0, 4
        ]
        beta_lig1_vol = df_temp[df_temp[0] == "Ligation 1, Overhang 2, Bottle 1"].iloc[
            0, 4
        ]
        alpha_lig2_vol = df_temp[df_temp[0] == "Ligation 2, Overhang 1, Bottle 1"].iloc[
            0, 4
        ]
        beta_lig2_vol = df_temp[df_temp[0] == "Ligation 2, Overhang 2, Bottle 1"].iloc[
            0, 4
        ]

        # Overhang 3 & 4
        df_temp = pd.read_excel(xlsx, sheet_name="Overhangs 3+4", header=None)
        unfunc_gb_vol_2 = df_temp[df_temp[1].str.contains("Total", na=False)].iloc[0, 3]
        gamma_lig1_vol = df_temp[df_temp[0] == "Ligation 1, Overhang 3, Bottle 1"].iloc[
            0, 4
        ]
        delta_lig1_vol = df_temp[df_temp[0] == "Ligation 1, Overhang 4, Bottle 1"].iloc[
            0, 4
        ]
        gamma_lig2_vol = df_temp[df_temp[0] == "Ligation 2, Overhang 3, Bottle 1"].iloc[
            0, 4
        ]
        delta_lig2_vol = df_temp[df_temp[0] == "Ligation 2, Overhang 4, Bottle 1"].iloc[
            0, 4
        ]

        # Extracting final volumes
        df_temp = pd.read_excel(xlsx, sheet_name="Yield", header=None)
        oh1_vol = df_temp[
            df_temp[0] == "Single Cell 3' v3 Functionalized Gel Beads, Overhang 1"
        ].iloc[0, 9]
        oh2_vol = df_temp[
            df_temp[0] == "Single Cell 3' v3 Functionalized Gel Beads, Overhang 2"
        ].iloc[0, 9]
        oh3_vol = df_temp[
            df_temp[0] == "Single Cell 3' v3 Functionalized Gel Beads, Overhang 3"
        ].iloc[0, 9]
        oh4_vol = df_temp[
            df_temp[0] == "Single Cell 3' v3 Functionalized Gel Beads, Overhang 4"
        ].iloc[0, 9]

        # Extracting Lot Info
        df_temp = pd.read_excel(xlsx, sheet_name="Summary", header=None)
        lot_no = df_temp[df_temp[1] == "Lot Number"].iloc[0, 4]
        mfg_date = df_temp[df_temp[1] == "Manufacturing Date"].iloc[0, 4]
        exp_date = df_temp[df_temp[1] == "Expiration Date"].iloc[0, 4]
        mfg_by = df_temp[df_temp[1] == "Manufactured by"].iloc[0, 4]
        planned_vol = df_temp[df_temp[1] == "Planned batch size (UOM)"].iloc[0, 4]
        pn = "2000058"
        pn_desc = "Chromium Single Cell 3' v3 Functionalized GBs"

        oh1_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh1_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                "unfunc_wo": unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol_1,
                "unfunc_gb_vol_2": unfunc_gb_vol_2,
                "lig1_vol": alpha_lig1_vol,
                "lig2_vol": alpha_lig2_vol,
                "final_vol": oh1_vol,
            },
            index=[0],
        )

        oh2_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh2_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                "unfunc_wo": unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol_1,
                "unfunc_gb_vol_2": unfunc_gb_vol_2,
                "lig1_vol": beta_lig1_vol,
                "lig2_vol": beta_lig2_vol,
                "final_vol": oh2_vol,
            },
            index=[0],
        )

        oh3_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh3_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                "unfunc_wo": unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol_1,
                "unfunc_gb_vol_2": unfunc_gb_vol_2,
                "lig1_vol": gamma_lig1_vol,
                "lig2_vol": gamma_lig2_vol,
                "final_vol": oh3_vol,
            },
            index=[0],
        )

        oh4_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh4_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                "unfunc_wo": unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol_1,
                "unfunc_gb_vol_2": unfunc_gb_vol_2,
                "lig1_vol": delta_lig1_vol,
                "lig2_vol": delta_lig2_vol,
                "final_vol": oh4_vol,
            },
            index=[0],
        )

        tmp = oh1_df.append(oh2_df.append(oh3_df.append(oh4_df)))

    except:
        print(f"### --- {file} skipped --- ###")
        tmp = pd.DataFrame()

    return tmp


### VDJ ------------
def read_vdj_br(file):
    try:
        xlsx = pd.ExcelFile(file, engine="openpyxl")
        # Extracting WO's
        # df_temp   = pd.read_excel(xlsx, sheet_name="Labels", header=None)
        # unfunc_wo = df_temp[df_temp[1] == "Unfunctionalized GB Work Order #"].iloc[0,2]

        # Extracting Lig volumes
        df_temp = pd.read_excel(xlsx, sheet_name="Process Record", header=None)
        unfunc_gb_vol = df_temp[df_temp[1] == "Total"].iloc[0, 3]
        alpha_lig1_vol = df_temp[
            df_temp[0] == "Ligation 1, Overhang 1 (Alpha), Bottle 1"
        ].iloc[0, 4]
        beta_lig1_vol = df_temp[
            df_temp[0] == "Ligation 1, Overhang 2 (Beta), Bottle 1"
        ].iloc[0, 4]
        gamma_lig1_vol = df_temp[
            df_temp[0] == "Ligation 1, Overhang 3 (Gamma), Bottle 1"
        ].iloc[0, 4]
        delta_lig1_vol = df_temp[
            df_temp[0] == "Ligation 1, Overhang 4 (Delta), Bottle 1"
        ].iloc[0, 4]
        total_lig1_vol = df_temp.iloc[74, 3]

        alpha_lig2_vol = df_temp[
            df_temp[0] == "Ligation 2, Overhang 1 (Alpha), Bottle 1"
        ].iloc[0, 4]
        beta_lig2_vol = df_temp[
            df_temp[0] == "Ligation 2, Overhang 2 (Beta), Bottle 1"
        ].iloc[0, 4]
        gamma_lig2_vol = df_temp[
            df_temp[0] == "Ligation 2, Overhang 3 (Gamma), Bottle 1"
        ].iloc[0, 4]
        delta_lig2_vol = df_temp[
            df_temp[0] == "Ligation 2, Overhang 4 (Delta), Bottle 1"
        ].iloc[0, 4]
        total_lig2_vol = df_temp.iloc[112, 4]

        # Extracting final volumes
        df_temp = pd.read_excel(xlsx, sheet_name="Yield", header=None)
        oh1_vol = df_temp[
            df_temp[0] == "SC5' VDJ Functionalized Gel Beads, Overhang 1"
        ].iloc[0, 9]
        oh2_vol = df_temp[
            df_temp[0] == "SC5' VDJ Functionalized Gel Beads, Overhang 2"
        ].iloc[0, 9]
        oh3_vol = df_temp[
            df_temp[0] == "SC5' VDJ Functionalized Gel Beads, Overhang 3"
        ].iloc[0, 9]
        oh4_vol = df_temp[
            df_temp[0] == "SC5' VDJ Functionalized Gel Beads, Overhang 4"
        ].iloc[0, 9]

        # Extracting Lot Info
        df_temp = pd.read_excel(xlsx, sheet_name="Summary", header=None)
        lot_no = df_temp[df_temp[1] == "Lot Number"].iloc[0, 4]
        all_wo = df_temp[df_temp[1] == "Work Order #"].iloc[0, 4]
        all_wo = all_wo.split(",")
        oh1_wo = all_wo[0].strip()
        oh2_wo = all_wo[1].strip()
        oh3_wo = all_wo[2].strip()
        oh4_wo = all_wo[3].strip()

        mfg_date = df_temp[df_temp[1] == "Manufacturing Date"].iloc[0, 4]
        exp_date = df_temp[df_temp[1] == "Expiration Date"].iloc[0, 4]
        mfg_by = df_temp[df_temp[1] == "Manufactured by"].iloc[0, 4]
        planned_vol = df_temp[df_temp[1] == "Planned batch size (UOM)"].iloc[0, 4]
        pn = "210170"
        pn_desc = "Chromium VDJ 5' 737K Functionalized Gel Beads"

        oh1_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh1_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                #'unfunc_wo' : unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol,
                "lig1_vol": alpha_lig1_vol,
                "lig2_vol": alpha_lig2_vol,
                "total_lig1_vol": total_lig1_vol,
                "total_lig2_vol": total_lig2_vol,
                "final_vol": oh1_vol,
            },
            index=[0],
        )

        oh2_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh2_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                #'unfunc_wo' : unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol,
                "lig1_vol": beta_lig1_vol,
                "lig2_vol": beta_lig2_vol,
                "total_lig1_vol": total_lig1_vol,
                "total_lig2_vol": total_lig2_vol,
                "final_vol": oh2_vol,
            },
            index=[0],
        )

        oh3_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh3_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                #'unfunc_wo' : unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol,
                "lig1_vol": gamma_lig1_vol,
                "lig2_vol": gamma_lig2_vol,
                "total_lig1_vol": total_lig1_vol,
                "total_lig2_vol": total_lig2_vol,
                "final_vol": oh3_vol,
            },
            index=[0],
        )

        oh4_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh4_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                #'unfunc_wo' : unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol,
                "lig1_vol": delta_lig1_vol,
                "lig2_vol": delta_lig2_vol,
                "total_lig1_vol": total_lig1_vol,
                "total_lig2_vol": total_lig2_vol,
                "final_vol": oh4_vol,
            },
            index=[0],
        )

        tmp = oh1_df.append(oh2_df.append(oh3_df.append(oh4_df)))

    except:
        print(f"### --- {file} skipped --- ###")
        tmp = pd.DataFrame()

    return tmp


### 5HV ------------
def read_5hv_br(file):
    try:
        xlsx = pd.ExcelFile(file, engine="openpyxl")
        # Extracting WO's
        # df_temp   = pd.read_excel(xlsx, sheet_name="Labels", header=None)
        # unfunc_wo = df_temp[df_temp[1] == "Unfunctionalized GB Work Order #"].iloc[0,2]

        # Extracting Lig volumes
        df_temp = pd.read_excel(xlsx, sheet_name="Mass Data Records", header=None)
        unfunc_gb_vol = df_temp[df_temp[2].str.contains("Total", na=False)].iloc[0, 3]
        alpha_lig1_vol = df_temp[
            df_temp[0].str.contains("Ligation 1, Overhang 1, Bottle 1", na=False)
        ].iloc[0, 4]
        beta_lig1_vol = df_temp[
            df_temp[0].str.contains("Ligation 1, Overhang 2, Bottle 1", na=False)
        ].iloc[0, 4]
        gamma_lig1_vol = df_temp[
            df_temp[0].str.contains("Ligation 1, Overhang 3, Bottle 1", na=False)
        ].iloc[0, 4]
        delta_lig1_vol = df_temp[
            df_temp[0].str.contains("Ligation 1, Overhang 4, Bottle 1", na=False)
        ].iloc[0, 4]
        total_lig1_vol = (
            alpha_lig1_vol + beta_lig1_vol + gamma_lig1_vol + delta_lig1_vol
        )

        alpha_lig2_vol = (
            df_temp[
                df_temp[0].str.contains("Ligation 2, Overhang 1, Bottle 1", na=False)
            ].iloc[0, 3]
            + df_temp[
                df_temp[0].str.contains("Ligation 2, Overhang 1, Bottle 2", na=False)
            ].iloc[0, 3]
        )
        beta_lig2_vol = (
            df_temp[
                df_temp[0].str.contains("Ligation 2, Overhang 2, Bottle 1", na=False)
            ].iloc[0, 3]
            + df_temp[
                df_temp[0].str.contains("Ligation 2, Overhang 2, Bottle 2", na=False)
            ].iloc[0, 3]
        )
        gamma_lig2_vol = (
            df_temp[
                df_temp[0].str.contains("Ligation 2, Overhang 3, Bottle 1", na=False)
            ].iloc[0, 3]
            + df_temp[
                df_temp[0].str.contains("Ligation 2, Overhang 3, Bottle 2", na=False)
            ].iloc[0, 3]
        )
        delta_lig2_vol = (
            df_temp[
                df_temp[0].str.contains("Ligation 2, Overhang 4, Bottle 1", na=False)
            ].iloc[0, 3]
            + df_temp[
                df_temp[0].str.contains("Ligation 2, Overhang 4, Bottle 2", na=False)
            ].iloc[0, 3]
        )
        total_lig2_vol = (
            alpha_lig2_vol + beta_lig2_vol + gamma_lig2_vol + delta_lig2_vol
        )

        # Extracting final volumes
        df_temp = pd.read_excel(xlsx, sheet_name="Yield", header=None)
        oh1_vol = df_temp[
            df_temp[0].str.contains(
                "SC5' v1, Functionalized Gel Beads, Overhang 1", na=False
            )
        ].iloc[0, 10]
        oh2_vol = df_temp[
            df_temp[0].str.contains(
                "SC5' v1, Functionalized Gel Beads, Overhang 2", na=False
            )
        ].iloc[0, 10]
        oh3_vol = df_temp[
            df_temp[0].str.contains(
                "SC5' v1, Functionalized Gel Beads, Overhang 3", na=False
            )
        ].iloc[0, 10]
        oh4_vol = df_temp[
            df_temp[0].str.contains(
                "SC5' v1, Functionalized Gel Beads, Overhang 4", na=False
            )
        ].iloc[0, 10]

        # Extracting Lot Info
        df_temp = pd.read_excel(xlsx, sheet_name="Summary", header=None)
        lot_no = df_temp[df_temp[1].str.contains("Lot Number", na=False)].iloc[0, 4]
        all_wo = df_temp[df_temp[1].str.contains("Work Order", na=False)].iloc[0, 4]
        all_wo = all_wo.split(",")
        oh1_wo = all_wo[0].strip()
        oh2_wo = all_wo[1].strip()
        oh3_wo = all_wo[2].strip()
        oh4_wo = all_wo[3].strip()

        mfg_date = df_temp[
            df_temp[1].str.contains("Manufacturing Date", na=False)
        ].iloc[0, 4]
        exp_date = df_temp[df_temp[1].str.contains("Expiration Date", na=False)].iloc[
            0, 4
        ]
        mfg_by = df_temp[df_temp[1].str.contains("Manufactured by", na=False)].iloc[
            0, 4
        ]
        planned_vol = df_temp[
            df_temp[1].str.contains("Planned Batch Size", na=False)
        ].iloc[0, 4]
        pn = "2000461"
        pn_desc = "Bulk, Chromium SC5' v1 Functionalized GBs"

        oh1_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh1_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                #'unfunc_wo' : unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol,
                "lig1_vol": alpha_lig1_vol,
                "lig2_vol": alpha_lig2_vol,
                "total_lig1_vol": total_lig1_vol,
                "total_lig2_vol": total_lig2_vol,
                "final_vol": oh1_vol,
            },
            index=[0],
        )

        oh2_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh2_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                #'unfunc_wo' : unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol,
                "lig1_vol": beta_lig1_vol,
                "lig2_vol": beta_lig2_vol,
                "total_lig1_vol": total_lig1_vol,
                "total_lig2_vol": total_lig2_vol,
                "final_vol": oh2_vol,
            },
            index=[0],
        )

        oh3_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh3_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                #'unfunc_wo' : unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol,
                "lig1_vol": gamma_lig1_vol,
                "lig2_vol": gamma_lig2_vol,
                "total_lig1_vol": total_lig1_vol,
                "total_lig2_vol": total_lig2_vol,
                "final_vol": oh3_vol,
            },
            index=[0],
        )

        oh4_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh4_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                #'unfunc_wo' : unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol,
                "lig1_vol": delta_lig1_vol,
                "lig2_vol": delta_lig2_vol,
                "total_lig1_vol": total_lig1_vol,
                "total_lig2_vol": total_lig2_vol,
                "final_vol": oh4_vol,
            },
            index=[0],
        )

        tmp = oh1_df.append(oh2_df.append(oh3_df.append(oh4_df)))

    except:
        print(f"### --- {file} skipped --- ###")
        tmp = pd.DataFrame()

    return tmp


### 3HV ------------
def read_3hv_br(file):
    try:
        xlsx = pd.ExcelFile(file, engine="openpyxl")
        # Extracting WO's
        # df_temp   = pd.read_excel(xlsx, sheet_name="Labels", header=None)
        # unfunc_wo = df_temp[df_temp[1] == "Unfunctionalized GB Work Order #"].iloc[0,2]

        # Extracting Lig volumes
        df_temp = pd.read_excel(xlsx, sheet_name="Mass Data Records", header=None)
        unfunc_gb_vol = df_temp[df_temp[2].str.contains("Total", na=False)].iloc[0, 3]
        alpha_lig1_vol = df_temp[
            df_temp[0].str.contains("Ligation 1, Overhang 1, Bottle 1", na=False)
        ].iloc[0, 4]
        beta_lig1_vol = df_temp[
            df_temp[0].str.contains("Ligation 1, Overhang 2, Bottle 1", na=False)
        ].iloc[0, 4]
        gamma_lig1_vol = df_temp[
            df_temp[0].str.contains("Ligation 1, Overhang 3, Bottle 1", na=False)
        ].iloc[0, 4]
        delta_lig1_vol = df_temp[
            df_temp[0].str.contains("Ligation 1, Overhang 4, Bottle 1", na=False)
        ].iloc[0, 4]
        total_lig1_vol = (
            alpha_lig1_vol + beta_lig1_vol + gamma_lig1_vol + delta_lig1_vol
        )

        alpha_lig2_vol = (
            df_temp[
                df_temp[0].str.contains("Ligation 2, Overhang 1, Bottle 1", na=False)
            ].iloc[0, 3]
            + df_temp[
                df_temp[0].str.contains("Ligation 2, Overhang 1, Bottle 2", na=False)
            ].iloc[0, 3]
        )
        beta_lig2_vol = (
            df_temp[
                df_temp[0].str.contains("Ligation 2, Overhang 2, Bottle 1", na=False)
            ].iloc[0, 3]
            + df_temp[
                df_temp[0].str.contains("Ligation 2, Overhang 2, Bottle 2", na=False)
            ].iloc[0, 3]
        )
        gamma_lig2_vol = (
            df_temp[
                df_temp[0].str.contains("Ligation 2, Overhang 3, Bottle 1", na=False)
            ].iloc[0, 3]
            + df_temp[
                df_temp[0].str.contains("Ligation 2, Overhang 3, Bottle 2", na=False)
            ].iloc[0, 3]
        )
        delta_lig2_vol = (
            df_temp[
                df_temp[0].str.contains("Ligation 2, Overhang 4, Bottle 1", na=False)
            ].iloc[0, 3]
            + df_temp[
                df_temp[0].str.contains("Ligation 2, Overhang 4, Bottle 2", na=False)
            ].iloc[0, 3]
        )
        total_lig2_vol = (
            alpha_lig2_vol + beta_lig2_vol + gamma_lig2_vol + delta_lig2_vol
        )

        # Extracting final volumes
        df_temp = pd.read_excel(xlsx, sheet_name="Yield", header=None)
        oh1_vol = df_temp[
            df_temp[0].str.contains(
                "SC3' v3, Functoinalized Gel Beads, Overhang 1", na=False
            )
        ].iloc[0, 10]
        oh2_vol = df_temp[
            df_temp[0].str.contains(
                "SC3' v3, Functoinalized Gel Beads, Overhang 2", na=False
            )
        ].iloc[0, 10]
        oh3_vol = df_temp[
            df_temp[0].str.contains(
                "SC3' v3, Functoinalized Gel Beads, Overhang 3", na=False
            )
        ].iloc[0, 10]
        oh4_vol = df_temp[
            df_temp[0].str.contains(
                "SC3' v3, Functoinalized Gel Beads, Overhang 4", na=False
            )
        ].iloc[0, 10]

        # Extracting Lot Info
        df_temp = pd.read_excel(xlsx, sheet_name="Summary", header=None)
        lot_no = df_temp[df_temp[1].str.contains("Lot Number", na=False)].iloc[0, 4]
        all_wo = df_temp[df_temp[1].str.contains("Work Order", na=False)].iloc[0, 4]
        all_wo = all_wo.split(",")
        oh1_wo = all_wo[0].strip()
        oh2_wo = all_wo[1].strip()
        oh3_wo = all_wo[2].strip()
        oh4_wo = all_wo[3].strip()

        mfg_date = df_temp[
            df_temp[1].str.contains("Manufacturing Date", na=False)
        ].iloc[0, 4]
        exp_date = df_temp[df_temp[1].str.contains("Expiration Date", na=False)].iloc[
            0, 4
        ]
        mfg_by = df_temp[df_temp[1].str.contains("Manufactured by", na=False)].iloc[
            0, 4
        ]
        planned_vol = df_temp[
            df_temp[1].str.contains("Planned Batch Size", na=False)
        ].iloc[0, 4]
        pn = "2000211"
        pn_desc = "Bulk, Chromium SC3' v3 Functionalized GBs"

        oh1_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh1_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                #'unfunc_wo' : unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol,
                "lig1_vol": alpha_lig1_vol,
                "lig2_vol": alpha_lig2_vol,
                "total_lig1_vol": total_lig1_vol,
                "total_lig2_vol": total_lig2_vol,
                "final_vol": oh1_vol,
            },
            index=[0],
        )

        oh2_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh2_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                #'unfunc_wo' : unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol,
                "lig1_vol": beta_lig1_vol,
                "lig2_vol": beta_lig2_vol,
                "total_lig1_vol": total_lig1_vol,
                "total_lig2_vol": total_lig2_vol,
                "final_vol": oh2_vol,
            },
            index=[0],
        )

        oh3_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh3_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                #'unfunc_wo' : unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol,
                "lig1_vol": gamma_lig1_vol,
                "lig2_vol": gamma_lig2_vol,
                "total_lig1_vol": total_lig1_vol,
                "total_lig2_vol": total_lig2_vol,
                "final_vol": oh3_vol,
            },
            index=[0],
        )

        oh4_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh4_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                #'unfunc_wo' : unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol,
                "lig1_vol": delta_lig1_vol,
                "lig2_vol": delta_lig2_vol,
                "total_lig1_vol": total_lig1_vol,
                "total_lig2_vol": total_lig2_vol,
                "final_vol": oh4_vol,
            },
            index=[0],
        )

        tmp = oh1_df.append(oh2_df.append(oh3_df.append(oh4_df)))

    except:
        print(f"### --- {file} skipped --- ###")
        tmp = pd.DataFrame()

    return tmp


### Orion ------------
def read_orion_br(file):
    try:
        xlsx = pd.ExcelFile(file, engine="openpyxl")
        # Extracting WO's
        # df_temp   = pd.read_excel(xlsx, sheet_name="Labels", header=None)
        # unfunc_wo = df_temp[df_temp[1] == "Unfunctionalized GB Work Order #"].iloc[0,2]

        # Extracting Lig volumes
        df_temp = pd.read_excel(xlsx, sheet_name="Process Record", header=None)
        unfunc_gb_vol = df_temp[df_temp[1] == "Total"].iloc[0, 3]
        alpha_lig1_vol = df_temp[
            df_temp[0].str.contains("Ligation 1, Overhang 1, Bottle 1", na=False)
        ].iloc[0, 4]
        beta_lig1_vol = df_temp[
            df_temp[0].str.contains("Ligation 1, Overhang 2, Bottle 1", na=False)
        ].iloc[0, 4]
        gamma_lig1_vol = df_temp[
            df_temp[0].str.contains("Ligation 1, Overhang 3, Bottle 1", na=False)
        ].iloc[0, 4]
        delta_lig1_vol = df_temp[
            df_temp[0].str.contains("Ligation 1, Overhang 4, Bottle 1", na=False)
        ].iloc[0, 4]
        total_lig1_vol = (
            alpha_lig1_vol + beta_lig1_vol + gamma_lig1_vol + delta_lig1_vol
        )

        alpha_lig2_vol = df_temp[
            df_temp[0].str.contains("Ligation 2, Overhang 1, Bottle 1", na=False)
        ].iloc[0, 4]
        beta_lig2_vol = df_temp[
            df_temp[0].str.contains("Ligation 2, Overhang 2, Bottle 1", na=False)
        ].iloc[0, 4]
        gamma_lig2_vol = df_temp[
            df_temp[0].str.contains("Ligation 2, Overhang 3, Bottle 1", na=False)
        ].iloc[0, 4]
        delta_lig2_vol = df_temp[
            df_temp[0].str.contains("Ligation 2, Overhang 4, Bottle 1", na=False)
        ].iloc[0, 4]
        total_lig2_vol = (
            alpha_lig2_vol + beta_lig2_vol + gamma_lig2_vol + delta_lig2_vol
        )

        # Extracting final volumes
        df_temp = pd.read_excel(xlsx, sheet_name="Yield", header=None)
        oh1_vol = df_temp[
            df_temp[0].str.contains(
                "Orion Functionalized Gel Beads, Overhang 1", na=False
            )
        ].iloc[0, 9]
        oh2_vol = df_temp[
            df_temp[0].str.contains(
                "Orion Functionalized Gel Beads, Overhang 2", na=False
            )
        ].iloc[0, 9]
        oh3_vol = df_temp[
            df_temp[0].str.contains(
                "Orion Functionalized Gel Beads, Overhang 3", na=False
            )
        ].iloc[0, 9]
        oh4_vol = df_temp[
            df_temp[0].str.contains(
                "Orion Functionalized Gel Beads, Overhang 4", na=False
            )
        ].iloc[0, 9]

        # Extracting Lot Info
        df_temp = pd.read_excel(xlsx, sheet_name="Summary", header=None)
        lot_no = df_temp[df_temp[1] == "Lot Number"].iloc[0, 4]
        all_wo = df_temp[df_temp[1] == "Work Order #"].iloc[0, 4]
        all_wo = all_wo.split(",")
        oh1_wo = all_wo[0].strip()
        oh2_wo = all_wo[1].strip()
        oh3_wo = all_wo[2].strip()
        oh4_wo = all_wo[3].strip()

        mfg_date = df_temp[df_temp[1] == "Manufacturing Date"].iloc[0, 4]
        exp_date = df_temp[df_temp[1] == "Expiration Date"].iloc[0, 4]
        mfg_by = df_temp[df_temp[1] == "Manufactured by"].iloc[0, 4]
        planned_vol = df_temp[df_temp[1] == "Planned batch size (UOM)"].iloc[0, 4]
        pn = "2000260"
        pn_desc = "Orion Functionalized Gel Beads"

        oh1_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh1_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                #'unfunc_wo' : unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol,
                "lig1_vol": alpha_lig1_vol,
                "lig2_vol": alpha_lig2_vol,
                "total_lig1_vol": total_lig1_vol,
                "total_lig2_vol": total_lig2_vol,
                "final_vol": oh1_vol,
            },
            index=[0],
        )

        oh2_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh2_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                #'unfunc_wo' : unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol,
                "lig1_vol": beta_lig1_vol,
                "lig2_vol": beta_lig2_vol,
                "total_lig1_vol": total_lig1_vol,
                "total_lig2_vol": total_lig2_vol,
                "final_vol": oh2_vol,
            },
            index=[0],
        )

        oh3_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh3_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                #'unfunc_wo' : unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol,
                "lig1_vol": gamma_lig1_vol,
                "lig2_vol": gamma_lig2_vol,
                "total_lig1_vol": total_lig1_vol,
                "total_lig2_vol": total_lig2_vol,
                "final_vol": oh3_vol,
            },
            index=[0],
        )

        oh4_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh4_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                #'unfunc_wo' : unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol,
                "lig1_vol": delta_lig1_vol,
                "lig2_vol": delta_lig2_vol,
                "total_lig1_vol": total_lig1_vol,
                "total_lig2_vol": total_lig2_vol,
                "final_vol": oh4_vol,
            },
            index=[0],
        )

        tmp = oh1_df.append(oh2_df.append(oh3_df.append(oh4_df)))

    except:
        print(f"### --- {file} skipped --- ###")
        tmp = pd.DataFrame()

    return tmp


### Agora ------------
def read_agora_br(file):
    try:
        xlsx = pd.ExcelFile(file, engine="openpyxl")
        # Extracting WO's
        # df_temp   = pd.read_excel(xlsx, sheet_name="Labels", header=None)
        # unfunc_wo = df_temp[df_temp[1] == "Unfunctionalized GB Work Order #"].iloc[0,2]

        # Extracting Lig volumes
        df_temp = pd.read_excel(xlsx, sheet_name="Process Record", header=None)
        unfunc_gb_vol = df_temp[df_temp[1] == "Total"].iloc[0, 3]
        alpha_lig1_vol = df_temp[
            df_temp[0] == "Ligation 1, Overhang 1 (Alpha), Bottle 1"
        ].iloc[0, 4]
        beta_lig1_vol = df_temp[
            df_temp[0] == "Ligation 1, Overhang 2 (Beta), Bottle 1"
        ].iloc[0, 4]
        gamma_lig1_vol = df_temp[
            df_temp[0] == "Ligation 1, Overhang 3 (Gamma), Bottle 1"
        ].iloc[0, 4]
        delta_lig1_vol = df_temp[
            df_temp[0] == "Ligation 1, Overhang 4 (Delta), Bottle 1"
        ].iloc[0, 4]
        total_lig1_vol = (
            alpha_lig1_vol + beta_lig1_vol + gamma_lig1_vol + delta_lig1_vol
        )

        alpha_lig2_vol = df_temp[
            df_temp[0] == "Ligation 2, Overhang 1 (Alpha), Bottle 1"
        ].iloc[0, 4]
        beta_lig2_vol = df_temp[
            df_temp[0] == "Ligation 2, Overhang 2 (Beta), Bottle 1"
        ].iloc[0, 4]
        gamma_lig2_vol = df_temp[
            df_temp[0] == "Ligation 2, Overhang 3 (Gamma), Bottle 1"
        ].iloc[0, 4]
        delta_lig2_vol = df_temp[
            df_temp[0] == "Ligation 2, Overhang 4 (Delta), Bottle 1"
        ].iloc[0, 4]
        total_lig2_vol = (
            alpha_lig2_vol + beta_lig2_vol + gamma_lig2_vol + delta_lig2_vol
        )

        # Extracting final volumes
        df_temp = pd.read_excel(xlsx, sheet_name="Yield", header=None)
        oh1_vol = df_temp[
            df_temp[0] == "SC-ATAC Functionalized Gel Beads, Overhang 1"
        ].iloc[0, 9]
        oh2_vol = df_temp[
            df_temp[0] == "SC-ATAC Functionalized Gel Beads, Overhang 2"
        ].iloc[0, 9]
        oh3_vol = df_temp[
            df_temp[0] == "SC-ATAC Functionalized Gel Beads, Overhang 3"
        ].iloc[0, 9]
        oh4_vol = df_temp[
            df_temp[0] == "SC-ATAC Functionalized Gel Beads, Overhang 4"
        ].iloc[0, 9]

        # Extracting Lot Info
        df_temp = pd.read_excel(xlsx, sheet_name="Summary", header=None)
        lot_no = df_temp[df_temp[1] == "Lot Number"].iloc[0, 4]
        all_wo = df_temp[df_temp[1] == "Work Order #"].iloc[0, 4]
        all_wo = all_wo.split(",")
        oh1_wo = all_wo[0].strip()
        oh2_wo = all_wo[1].strip()
        oh3_wo = all_wo[2].strip()
        oh4_wo = all_wo[3].strip()

        mfg_date = df_temp[df_temp[1] == "Manufacturing Date"].iloc[0, 4]
        exp_date = df_temp[df_temp[1] == "Expiration Date"].iloc[0, 4]
        mfg_by = df_temp[df_temp[1] == "Manufactured by"].iloc[0, 4]
        planned_vol = df_temp[df_temp[1] == "Planned batch size (UOM)"].iloc[0, 4]
        pn = "2000114"
        pn_desc = "Chromium Single Cell ATAC Functionalized GBs"

        oh1_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh1_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                #'unfunc_wo' : unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol,
                "lig1_vol": alpha_lig1_vol,
                "lig2_vol": alpha_lig2_vol,
                "total_lig1_vol": total_lig1_vol,
                "total_lig2_vol": total_lig2_vol,
                "final_vol": oh1_vol,
            },
            index=[0],
        )

        oh2_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh2_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                #'unfunc_wo' : unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol,
                "lig1_vol": beta_lig1_vol,
                "lig2_vol": beta_lig2_vol,
                "total_lig1_vol": total_lig1_vol,
                "total_lig2_vol": total_lig2_vol,
                "final_vol": oh2_vol,
            },
            index=[0],
        )

        oh3_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh3_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                #'unfunc_wo' : unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol,
                "lig1_vol": gamma_lig1_vol,
                "lig2_vol": gamma_lig2_vol,
                "total_lig1_vol": total_lig1_vol,
                "total_lig2_vol": total_lig2_vol,
                "final_vol": oh3_vol,
            },
            index=[0],
        )

        oh4_df = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": lot_no,
                "wo": oh4_wo,
                "mfg_date": mfg_date,
                "exp_date": exp_date,
                "mfg_by": mfg_by,
                #'unfunc_wo' : unfunc_wo,
                "planned_vol": planned_vol,
                "unfunc_gb_vol_1": unfunc_gb_vol,
                "lig1_vol": delta_lig1_vol,
                "lig2_vol": delta_lig2_vol,
                "total_lig1_vol": total_lig1_vol,
                "total_lig2_vol": total_lig2_vol,
                "final_vol": oh4_vol,
            },
            index=[0],
        )

        tmp = oh1_df.append(oh2_df.append(oh3_df.append(oh4_df)))

    except:
        print(f"### --- {file} skipped --- ###")
        tmp = pd.DataFrame()

    return tmp
