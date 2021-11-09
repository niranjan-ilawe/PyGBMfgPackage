import pandas as pd


def read_vdj_ligation_plate_br(file):
    try:
        xlsx = pd.ExcelFile(file, engine="openpyxl")
        # Extracting WO's
        df_temp = pd.read_excel(xlsx, sheet_name="Lot Numbers", header=None)
        df1 = df_temp.iloc[2:7, 0:2].rename(columns={0: "plate", 1: "lot"})
        df2 = df_temp.iloc[2:7, 3:5].rename(columns={3: "plate", 4: "lot"})
        df3 = df_temp.iloc[2:7, 6:8].rename(columns={6: "plate", 7: "lot"})
        df4 = df_temp.iloc[2:7, 9:11].rename(columns={9: "plate", 10: "lot"})
        df = df1.append(df2.append(df3.append(df4)))

        df_temp = pd.read_excel(xlsx, sheet_name="Weight Checks", header=None)
        mfg_date = df_temp[
            df_temp[0].str.contains("Date of dispensing", na=False)
        ].iloc[0, 1]

        df_temp = pd.read_excel(xlsx, sheet_name="Procedure", header=None)
        pn = df_temp[df_temp[9].str.contains("PN", na=False)].iloc[0, 10]
        wo = df_temp[df_temp[9].str.contains("WO", na=False)].iloc[0, 10]

        tmp = df.assign(pn=pn, wo=wo, mfg_date=mfg_date)
    except:
        print(f"### --- {file} skipped --- ###")
        tmp = pd.DataFrame()

    return tmp


def read_mav_ligation_plate_br(file):
    try:
        xlsx = pd.ExcelFile(file, engine="openpyxl")
        # Extracting WO's
        df_temp = pd.read_excel(xlsx, sheet_name="Lot Numbers", header=None)
        df1 = df_temp.iloc[2:12, 0:2].rename(columns={0: "plate", 1: "lot"})
        df2 = df_temp.iloc[2:12, 3:5].rename(columns={3: "plate", 4: "lot"})
        df3 = df_temp.iloc[2:12, 6:8].rename(columns={6: "plate", 7: "lot"})
        df4 = df_temp.iloc[2:12, 9:11].rename(columns={9: "plate", 10: "lot"})
        df = df1.append(df2.append(df3.append(df4)))

        df_temp = pd.read_excel(xlsx, sheet_name="Weight Checks", header=None)
        wo = df_temp[df_temp[0].str.contains("Work Order", na=False)].iloc[0, 1]
        mfg_date = df_temp[
            df_temp[0].str.contains("Date of Dispensing", na=False)
        ].iloc[0, 1]

        df_temp = pd.read_excel(xlsx, sheet_name="Procedure", header=None)
        pn = df_temp[df_temp[9].str.contains("PN", na=False)].iloc[0, 10]

        tmp = df.assign(pn=pn, wo=wo, mfg_date=mfg_date)
    except:
        print(f"### --- {file} skipped --- ###")
        tmp = pd.DataFrame()

    return tmp
