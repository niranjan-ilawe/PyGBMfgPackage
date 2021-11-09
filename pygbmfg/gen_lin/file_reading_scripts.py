import pandas as pd


def read_gb_lineage(file):

    sheet_names = [
        "Formulation",
        "5X Monomer - Formulation Data",
        "Day 1 - Formulation Data",
        "Day 2 - Formulation Data",
        "Day 3 - Formulation Data",
        "Day 4 - Formulation Data",
        "Day 5 - Formulation Data",
    ]

    df = pd.DataFrame()
    for sheet in sheet_names:
        df = df.append(
            read_oil_lineage(file, sheet).append(read_acry_lineage(file, sheet))
        )

    df = df.drop_duplicates()
    return df


def read_oil_lineage(file, sheet):
    try:
        xlsx = pd.ExcelFile(file, engine="openpyxl")
        # Extracting WO's
        df_temp = pd.read_excel(xlsx, sheet_name=sheet, header=None)
        pn = df_temp[df_temp[1].str.contains("Product Part Number", na=False)].iloc[
            0, 2
        ]
        wo = df_temp[df_temp[0].str.contains("Work Order", na=False)].iloc[0, 1]
        ln = df_temp[df_temp[0].str.contains("Lot", na=False)].iloc[0, 1]
        mfg_date = df_temp[
            df_temp[0].str.contains("Manufacturing Date", na=False)
        ].iloc[0, 1]
        tmp = df_temp[df_temp[1].str.contains("GB Oil", na=False)].dropna(subset=[8])
        tmp = tmp[[0, 1, 2]]
        tmp = tmp.rename(columns={0: "from_pn", 1: "from_desc", 2: "from_wo"})
        tmp = tmp.assign(pn=pn, ln=ln, wo=wo, mfg_date=mfg_date)
    except:
        print(f"### --- {file} skipped --- ###")
        tmp = pd.DataFrame()

    return tmp


def read_acry_lineage(file, sheet):
    try:
        xlsx = pd.ExcelFile(file, engine="openpyxl")
        # Extracting WO's
        df_temp = pd.read_excel(xlsx, sheet_name=sheet, header=None)
        pn = df_temp[df_temp[1].str.contains("Product Part Number", na=False)].iloc[
            0, 2
        ]
        wo = df_temp[df_temp[0].str.contains("Work Order", na=False)].iloc[0, 1]
        ln = df_temp[df_temp[0].str.contains("Lot", na=False)].iloc[0, 1]
        mfg_date = df_temp[
            df_temp[0].str.contains("Manufacturing Date", na=False)
        ].iloc[0, 1]
        tmp = df_temp[df_temp[1].str.contains("Acrydite|Acr", na=False)]
        tmp = tmp[[0, 1, 2]]
        tmp = tmp.rename(columns={0: "from_pn", 1: "from_desc", 2: "from_wo"})
        tmp = tmp.assign(pn=pn, ln=ln, wo=wo, mfg_date=mfg_date)
    except:
        print(f"### --- {file} skipped --- ###")
        tmp = pd.DataFrame()

    return tmp
