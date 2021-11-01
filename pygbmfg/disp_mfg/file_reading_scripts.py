import pandas as pd


def read_mav_br_revD(file):
    try:
        xlsx = pd.ExcelFile(file, engine="openpyxl")
        df_temp = pd.read_excel(xlsx, sheet_name="summary", header=None)
        try:
            pn = df_temp[df_temp[1] == "10X Part Number"].iloc[0][4]
            wo = df_temp[df_temp[1] == "Work Order #"].iloc[0][4]
            ln = df_temp[df_temp[1] == "Lot Number"].iloc[0][4]
            mfg_date = df_temp[df_temp[1] == "Manufacturing Date"].iloc[0][4]
            planned_qty = df_temp[df_temp[1] == "Planned batch size (UOM)"].iloc[0][4]
            qty_to_inventory = df_temp[df_temp[1] == "Qty to inventory (UOM)"].iloc[0][
                4
            ]

            df_temp = pd.read_excel(
                xlsx, sheet_name="weight check records ", header=None
            )
            gb_vol_for_dispense = df_temp[
                df_temp[1] == "Bulk, Single Cell 3' v3 Functionalized Gel Beads"
            ].iloc[0, 3]
            gb_vol_for_packaging = df_temp[
                df_temp[3] == "Total volume of GB for packaging (mL):"
            ].iloc[0, 4]
            pn_desc = "Strip, Next GEM Single Cell 3' v3.1 Gel Beads"

            tmp = pd.DataFrame(
                {
                    "pn": pn,
                    "pn_desc": pn_desc,
                    "ln": ln,
                    "wo": wo,
                    "mfg_date": mfg_date,
                    "planned_qty": planned_qty,
                    "qty_to_inventory": qty_to_inventory,
                    "gb_vol_for_dispense": gb_vol_for_dispense,
                    "gb_vol_for_packaging": gb_vol_for_packaging,
                },
                index=[0],
            )
        except:
            print(f"### --- {file} skipped --- ###")
            tmp = pd.DataFrame()

    except:
        print(f"### --- {file} skipped --- ###")
        tmp = pd.DataFrame()

    # tmp = tmp.dropna(subset=["qty_to_inventory"])
    # tmp = tmp[tmp["ln"] != "Enter Here"]

    return tmp


def read_mav_br_revE(file):
    try:
        xlsx = pd.ExcelFile(file, engine="openpyxl")
        df_temp = pd.read_excel(xlsx, sheet_name="Summary", header=None)
        pn = df_temp[df_temp[1] == "10X Part Number"].iloc[0][4]
        wo = df_temp[df_temp[1] == "Work Order #"].iloc[0][4]
        ln = df_temp[df_temp[1] == "Lot Number"].iloc[0][4]
        mfg_date = df_temp[df_temp[1] == "Manufacturing Date"].iloc[0][4]
        planned_qty = df_temp[df_temp[1] == "Planned batch size (UOM)"].iloc[0][4]
        qty_to_inventory = df_temp[df_temp[1] == "Qty to inventory (UOM)"].iloc[0][4]

        df_temp = pd.read_excel(xlsx, sheet_name="Gel Bead Formulation", header=None)
        mfg_qty = df_temp[df_temp[1] == "Actual # of Packaged Gel Bead strips:"].iloc[
            0, 2
        ]
        scrap_qty = df_temp[df_temp[1] == "# of Gel Bead Strips for Scrap:"].iloc[0, 2]
        prod_retain_qty = df_temp[
            df_temp[1] == "# of Gel Bead Strips for Production Retain:"
        ].iloc[0, 2]
        qc_retain_qty = df_temp[
            df_temp[1] == "# of Gel Bead Strips for QC (retain and submission):"
        ].iloc[0, 2]
        addn_testing_qty = df_temp[df_temp[1] == "Additional Strips for Testing:"].iloc[
            0, 2
        ]
        gb_vol_for_dispense = df_temp[
            df_temp[1] == "Bulk, Single Cell 3' v3 Functionalized Gel Beads"
        ].iloc[0, 3]
        gb_vol_for_packaging = df_temp[
            df_temp[3] == "Total volume of GB for packaging (mL):"
        ].iloc[0, 4]
        pn_desc = "Strip, Next GEM Single Cell 3' v3.1 Gel Beads"

        tmp = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": ln,
                "wo": wo,
                "mfg_date": mfg_date,
                "planned_qty": planned_qty,
                "qty_to_inventory": qty_to_inventory,
                "mfg_qty": mfg_qty,
                "scrap_qty": scrap_qty,
                "prod_retain_qty": prod_retain_qty,
                "qc_retain_qty": qc_retain_qty,
                "addn_testing_qty": addn_testing_qty,
                "gb_vol_for_dispense": gb_vol_for_dispense,
                "gb_vol_for_packaging": gb_vol_for_packaging,
            },
            index=[0],
        )
    except:
        print(f"### --- {file} skipped --- ###")
        tmp = pd.DataFrame()

    # tmp = tmp.dropna(subset=["qty_to_inventory"])
    # tmp = tmp[tmp["ln"] != "Enter Here"]

    return tmp


def read_mav_br_revF(file):
    try:
        xlsx = pd.ExcelFile(file, engine="openpyxl")
        df_temp = pd.read_excel(xlsx, sheet_name="Summary", header=None)
        pn = df_temp[df_temp[1] == "10X Part Number"].iloc[0][4]
        wo = df_temp[df_temp[1] == "Work Order #"].iloc[0][4]
        ln = df_temp[df_temp[1] == "Lot Number"].iloc[0][4]
        mfg_date = df_temp[df_temp[1] == "Manufacturing Date"].iloc[0][4]
        planned_qty = df_temp[df_temp[1] == "Planned batch size (UOM)"].iloc[0][4]
        qty_to_inventory = df_temp[df_temp[1] == "Qty to inventory (UOM)"].iloc[0][4]

        df_temp = pd.read_excel(xlsx, sheet_name="GB Formulation", header=None)
        mfg_qty = df_temp[df_temp[1] == "Actual # of Packaged Gel Bead strips:"].iloc[
            0, 2
        ]
        scrap_qty = df_temp[df_temp[1] == "# of Gel Bead Strips for Scrap:"].iloc[0, 2]
        prod_retain_qty = df_temp[
            df_temp[1] == "# of Gel Bead Strips for Production Retain:"
        ].iloc[0, 2]
        qc_retain_qty = df_temp[
            df_temp[1] == "# of Gel Bead Strips for QC (retain and submission):"
        ].iloc[0, 2]
        addn_testing_qty = df_temp[df_temp[1] == "Additional Strips for Testing:"].iloc[
            0, 2
        ]
        gb_vol_for_dispense = df_temp[df_temp[0] == "2000058 - 1,2,3,4"].iloc[0, 3]
        gb_vol_for_packaging = df_temp[
            df_temp[3] == "Total volume of GB for packaging (mL):"
        ].iloc[0, 4]
        pn_desc = "Strip, Next GEM Single Cell 3' v3.1 Gel Beads"

        tmp = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": ln,
                "wo": wo,
                "mfg_date": mfg_date,
                "planned_qty": planned_qty,
                "qty_to_inventory": qty_to_inventory,
                "mfg_qty": mfg_qty,
                "scrap_qty": scrap_qty,
                "prod_retain_qty": prod_retain_qty,
                "qc_retain_qty": qc_retain_qty,
                "addn_testing_qty": addn_testing_qty,
                "gb_vol_for_dispense": gb_vol_for_dispense,
                "gb_vol_for_packaging": gb_vol_for_packaging,
            },
            index=[0],
        )
    except:
        print(f"### --- {file} skipped --- ###")
        tmp = pd.DataFrame()
    # tmp = tmp.dropna(subset=["qty_to_inventory"])
    # tmp = tmp[tmp["ln"] != "Enter Here"]

    return tmp


def read_vdj_br_revE(file):
    try:
        xlsx = pd.ExcelFile(file, engine="openpyxl")
        df_temp = pd.read_excel(xlsx, sheet_name="Summary", header=None)
        pn = df_temp[df_temp[1] == "10X Part Number"].iloc[0][4]
        wo = df_temp[df_temp[1] == "Work Order #"].iloc[0][4]
        ln = df_temp[df_temp[1] == "Lot Number"].iloc[0][4]
        mfg_date = df_temp[df_temp[1] == "Manufacturing Date"].iloc[0][4]
        planned_qty = df_temp[df_temp[1] == "Planned batch size (UOM)"].iloc[0][4]
        qty_to_inventory = df_temp[df_temp[1] == "Qty to inventory (UOM)"].iloc[0][4]

        df_temp = pd.read_excel(xlsx, sheet_name="GB Formulation", header=None)
        mfg_qty = df_temp[df_temp[1] == "Actual # of Packaged Gel Bead strips:"].iloc[
            0, 2
        ]
        scrap_qty = df_temp[df_temp[1] == "# of Gel Bead Strips for Scrap:"].iloc[0, 2]
        prod_retain_qty = df_temp[
            df_temp[1] == "# of Gel Bead Strips for Production Retain:"
        ].iloc[0, 2]
        qc_retain_qty = df_temp[
            df_temp[1] == "# of Gel Bead Strips for QC (retain and submission):"
        ].iloc[0, 2]
        addn_testing_qty = df_temp[df_temp[1] == "Additional Strips for Testing:"].iloc[
            0, 2
        ]
        gb_vol_for_dispense = df_temp[
            df_temp[0].str.contains("210170 - 1,2,3,4", na=False)
        ].iloc[0, 3]
        gb_vol_for_packaging = df_temp[
            df_temp[3] == "Total volume of GB for packaging (mL):"
        ].iloc[0, 4]
        pn_desc = "Strip, Single Cell VDJ 5' v1.1 Gel Beads"

        tmp = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": ln,
                "wo": wo,
                "mfg_date": mfg_date,
                "planned_qty": planned_qty,
                "qty_to_inventory": qty_to_inventory,
                "mfg_qty": mfg_qty,
                "scrap_qty": scrap_qty,
                "prod_retain_qty": prod_retain_qty,
                "qc_retain_qty": qc_retain_qty,
                "addn_testing_qty": addn_testing_qty,
                "gb_vol_for_dispense": gb_vol_for_dispense,
                "gb_vol_for_packaging": gb_vol_for_packaging,
            },
            index=[0],
        )
    except:
        print(f"### --- {file} skipped --- ###")
        tmp = pd.DataFrame()
    # tmp = tmp.dropna(subset=["qty_to_inventory"])
    # tmp = tmp[tmp["ln"] != "Enter Here"]

    return tmp


def read_vdj_br_revD(file):
    try:
        xlsx = pd.ExcelFile(file, engine="openpyxl")
        df_temp = pd.read_excel(xlsx, sheet_name="summary", header=None)
        try:
            pn = df_temp[df_temp[1] == "10X Part Number"].iloc[0][4]
            wo = df_temp[df_temp[1] == "Work Order #"].iloc[0][4]
            ln = df_temp[df_temp[1] == "Lot Number"].iloc[0][4]
            mfg_date = df_temp[df_temp[1] == "Manufacturing Date"].iloc[0][4]
            planned_qty = df_temp[df_temp[1] == "Planned batch size (UOM)"].iloc[0][4]
            qty_to_inventory = df_temp[df_temp[1] == "Qty to inventory (UOM)"].iloc[0][
                4
            ]

            df_temp = pd.read_excel(
                xlsx, sheet_name="weight check records ", header=None
            )
            gb_vol_for_dispense = df_temp[
                df_temp[1].str.contains(
                    "Bulk, Single Cell 5' VDJ 737K Functionalized Gel Beads", na=False
                )
            ].iloc[0, 3]
            gb_vol_for_packaging = df_temp[
                df_temp[3] == "Total volume of GB for packaging (mL):"
            ].iloc[0, 4]
            pn_desc = "Strip, Single Cell VDJ 5' V1.1 Gel Beads"

            tmp = pd.DataFrame(
                {
                    "pn": pn,
                    "pn_desc": pn_desc,
                    "ln": ln,
                    "wo": wo,
                    "mfg_date": mfg_date,
                    "planned_qty": planned_qty,
                    "qty_to_inventory": qty_to_inventory,
                    "gb_vol_for_dispense": gb_vol_for_dispense,
                    "gb_vol_for_packaging": gb_vol_for_packaging,
                },
                index=[0],
            )
        except:
            print(f"### --- {file} skipped --- ###")
            tmp = pd.DataFrame()

    except:
        print(f"### --- {file} skipped --- ###")
        tmp = pd.DataFrame()

    # tmp = tmp.dropna(subset=["qty_to_inventory"])
    # tmp = tmp[tmp["ln"] != "Enter Here"]

    return tmp


def read_orion_br_revD(file):
    try:
        xlsx = pd.ExcelFile(file, engine="openpyxl")
        df_temp = pd.read_excel(xlsx, sheet_name="Summary", header=None)
        pn = df_temp[df_temp[1] == "10X Part Number"].iloc[0][4]
        wo = df_temp[df_temp[1] == "Work Order #"].iloc[0][4]
        ln = df_temp[df_temp[1] == "Lot Number"].iloc[0][4]
        mfg_date = df_temp[df_temp[1] == "Manufacturing Date"].iloc[0][4]
        planned_qty = df_temp[df_temp[1] == "Planned batch size (UOM)"].iloc[0][4]
        qty_to_inventory = df_temp[df_temp[1] == "Qty to inventory (UOM)"].iloc[0][4]

        df_temp = pd.read_excel(xlsx, sheet_name="GB Formulation", header=None)
        mfg_qty = df_temp[df_temp[1] == "Actual # of Packaged Gel Bead strips:"].iloc[
            0, 2
        ]
        scrap_qty = df_temp[df_temp[1] == "# of Gel Bead Strips for Scrap:"].iloc[0, 2]
        prod_retain_qty = df_temp[
            df_temp[1] == "# of Gel Bead Strips for Production Retain:"
        ].iloc[0, 2]
        qc_retain_qty = df_temp[
            df_temp[1] == "# of Gel Bead Strips for QC (retain and submission):"
        ].iloc[0, 2]
        addn_testing_qty = df_temp[df_temp[1] == "Additional Strips for Testing:"].iloc[
            0, 2
        ]
        gb_vol_for_dispense = df_temp[
            df_temp[0].str.contains("2000260 - 1,2,3,4", na=False)
        ].iloc[0, 3]
        gb_vol_for_packaging = df_temp[
            df_temp[3] == "Total volume of GB for packaging (mL):"
        ].iloc[0, 4]
        pn_desc = "Strip, Next GEM Single Cell Multiome Gel Beads A"

        tmp = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": ln,
                "wo": wo,
                "mfg_date": mfg_date,
                "planned_qty": planned_qty,
                "qty_to_inventory": qty_to_inventory,
                "mfg_qty": mfg_qty,
                "scrap_qty": scrap_qty,
                "prod_retain_qty": prod_retain_qty,
                "qc_retain_qty": qc_retain_qty,
                "addn_testing_qty": addn_testing_qty,
                "gb_vol_for_dispense": gb_vol_for_dispense,
                "gb_vol_for_packaging": gb_vol_for_packaging,
            },
            index=[0],
        )
    except:
        print(f"### --- {file} skipped --- ###")
        tmp = pd.DataFrame()
    # tmp = tmp.dropna(subset=["qty_to_inventory"])
    # tmp = tmp[tmp["ln"] != "Enter Here"]

    return tmp


def read_orion_br_revC(file):
    try:
        xlsx = pd.ExcelFile(file, engine="openpyxl")
        df_temp = pd.read_excel(xlsx, sheet_name="summary", header=None)
        try:
            pn = df_temp[df_temp[1] == "10X Part Number"].iloc[0][4]
            wo = df_temp[df_temp[1] == "Work Order #"].iloc[0][4]
            ln = df_temp[df_temp[1] == "Lot Number"].iloc[0][4]
            mfg_date = df_temp[df_temp[1] == "Manufacturing Date"].iloc[0][4]
            planned_qty = df_temp[df_temp[1] == "Planned batch size (UOM)"].iloc[0][4]
            qty_to_inventory = df_temp[df_temp[1] == "Qty to inventory (UOM)"].iloc[0][
                4
            ]

            df_temp = pd.read_excel(
                xlsx, sheet_name="weight check records ", header=None
            )
            gb_vol_for_dispense = df_temp[
                df_temp[1].str.contains("Bulk,Orion Functionalized Gel Beads", na=False)
            ].iloc[0, 3]
            gb_vol_for_packaging = df_temp[
                df_temp[3] == "Total volume of GB for packaging (mL):"
            ].iloc[0, 4]
            pn_desc = "Strip, Next GEM Single Cell Multiome Gel Beads A"

            tmp = pd.DataFrame(
                {
                    "pn": pn,
                    "pn_desc": pn_desc,
                    "ln": ln,
                    "wo": wo,
                    "mfg_date": mfg_date,
                    "planned_qty": planned_qty,
                    "qty_to_inventory": qty_to_inventory,
                    "gb_vol_for_dispense": gb_vol_for_dispense,
                    "gb_vol_for_packaging": gb_vol_for_packaging,
                },
                index=[0],
            )
        except:
            print(f"### --- {file} skipped --- ###")
            tmp = pd.DataFrame()

    except:
        print(f"### --- {file} skipped --- ###")
        tmp = pd.DataFrame()

    # tmp = tmp.dropna(subset=["qty_to_inventory"])
    # tmp = tmp[tmp["ln"] != "Enter Here"]

    return tmp


def read_agora_br_revD(file):
    try:
        xlsx = pd.ExcelFile(file, engine="openpyxl")
        df_temp = pd.read_excel(xlsx, sheet_name="Summary", header=None)
        pn = df_temp[df_temp[1] == "10X Part Number"].iloc[0][4]
        wo = df_temp[df_temp[1] == "Work Order #"].iloc[0][4]
        ln = df_temp[df_temp[1] == "Lot Number"].iloc[0][4]
        mfg_date = df_temp[df_temp[1] == "Manufacturing Date"].iloc[0][4]
        planned_qty = df_temp[df_temp[1] == "Planned batch size (UOM)"].iloc[0][4]
        qty_to_inventory = df_temp[df_temp[1] == "Qty to inventory (UOM)"].iloc[0][4]

        df_temp = pd.read_excel(xlsx, sheet_name="GB Formulation", header=None)
        mfg_qty = df_temp[df_temp[1] == "Actual # of Packaged Gel Bead strips:"].iloc[
            0, 2
        ]
        scrap_qty = df_temp[df_temp[1] == "# of Gel Bead Strips for Scrap:"].iloc[0, 2]
        prod_retain_qty = df_temp[
            df_temp[1] == "# of Gel Bead Strips for Production Retain:"
        ].iloc[0, 2]
        qc_retain_qty = df_temp[
            df_temp[1] == "# of Gel Bead Strips for QC (retain and submission):"
        ].iloc[0, 2]
        addn_testing_qty = df_temp[df_temp[1] == "Additional Strips for Testing:"].iloc[
            0, 2
        ]
        gb_vol_for_dispense = df_temp[
            df_temp[0].str.contains("2000210 - 1,2,3,4", na=False)
        ].iloc[0, 3]
        gb_vol_for_packaging = df_temp[
            df_temp[3] == "Total volume of GB for packaging (mL):"
        ].iloc[0, 4]
        pn_desc = "Strip, Single Cell ATAC Gel Beads v1.1"

        tmp = pd.DataFrame(
            {
                "pn": pn,
                "pn_desc": pn_desc,
                "ln": ln,
                "wo": wo,
                "mfg_date": mfg_date,
                "planned_qty": planned_qty,
                "qty_to_inventory": qty_to_inventory,
                "mfg_qty": mfg_qty,
                "scrap_qty": scrap_qty,
                "prod_retain_qty": prod_retain_qty,
                "qc_retain_qty": qc_retain_qty,
                "addn_testing_qty": addn_testing_qty,
                "gb_vol_for_dispense": gb_vol_for_dispense,
                "gb_vol_for_packaging": gb_vol_for_packaging,
            },
            index=[0],
        )
    except:
        print(f"### --- {file} skipped --- ###")
        tmp = pd.DataFrame()
    # tmp = tmp.dropna(subset=["qty_to_inventory"])
    # tmp = tmp[tmp["ln"] != "Enter Here"]

    return tmp


def read_agora_br_revB(file):
    try:
        xlsx = pd.ExcelFile(file, engine="openpyxl")
        df_temp = pd.read_excel(xlsx, sheet_name="Summary", header=None)
        try:
            pn = df_temp[df_temp[1] == "10X Part Number"].iloc[0][4]
            wo = df_temp[df_temp[1] == "Work Order #"].iloc[0][4]
            ln = df_temp[df_temp[1] == "Lot Number"].iloc[0][4]
            mfg_date = df_temp[df_temp[1] == "Manufacturing Date"].iloc[0][4]
            planned_qty = df_temp[df_temp[1] == "Planned batch size (UOM)"].iloc[0][4]
            qty_to_inventory = df_temp[df_temp[1] == "Qty to inventory (UOM)"].iloc[0][
                4
            ]

            df_temp = pd.read_excel(
                xlsx, sheet_name="Weight Check record ", header=None
            )
            gb_vol_for_dispense = df_temp[
                df_temp[1].str.contains(
                    "Bulk, ATAC 737K Functionalized Gel Beads", na=False
                )
            ].iloc[0, 3]
            gb_vol_for_packaging = df_temp[
                df_temp[3] == "Total volume of GB for packaging (mL):"
            ].iloc[0, 4]
            pn_desc = "Strip, Single Cell ATAC Gel Beads v1.1"

            tmp = pd.DataFrame(
                {
                    "pn": pn,
                    "pn_desc": pn_desc,
                    "ln": ln,
                    "wo": wo,
                    "mfg_date": mfg_date,
                    "planned_qty": planned_qty,
                    "qty_to_inventory": qty_to_inventory,
                    "gb_vol_for_dispense": gb_vol_for_dispense,
                    "gb_vol_for_packaging": gb_vol_for_packaging,
                },
                index=[0],
            )
        except:
            print(f"### --- {file} skipped --- ###")
            tmp = pd.DataFrame()

    except:
        print(f"### --- {file} skipped --- ###")
        tmp = pd.DataFrame()

    # tmp = tmp.dropna(subset=["qty_to_inventory"])
    # tmp = tmp[tmp["ln"] != "Enter Here"]

    return tmp
