import pandas as pd

def extract_well_info(file, sheet_names):

    xlsx = pd.ExcelFile(file)
    data = pd.read_excel(xlsx, sheet_name="Summary-QC records", header=None)

    pn = data[data[1].str.contains("Part Number", na=False)].iloc[0,3]
    lot = data[data[1].str.contains("Lot Number", na=False)].iloc[0,3]
    wo = data[data[1].str.contains("Work Order", na=False)].iloc[0,3]
    qc_date = data[data[1].str.contains("QC date", na=False)].iloc[0,3]

    df = pd.DataFrame()

    for sheet in sheet_names:
        tmp = pd.read_excel(xlsx, sheet_name=sheet, header=None)
        tmp = tmp[[0,1,2,4,6,7]]
        tmp = tmp[tmp[0] != "type"]
        tmp = tmp.rename(columns={0: "type", 1: "plate", 2: "well", 4: "counts", 6:"median", 7:"disposition"}).dropna()
        tmp = tmp.assign(pn=pn, lot=lot, wo=wo, date=qc_date, sheet=sheet)
        
        if len(tmp)>0:
            df = df.append(tmp)
        
    return(df)


def read_well_info(file):

    part_a_sheets = ["PartA_Data_Tru","PartA_Data_Nxt_v6","PartA_Data_Nxt_v8"]
    part_b_sheets = ["PartB_Data_Tru","PartB_Data_Nxt_v6","PartB_Data_Nxt_v8"]

    df1 = extract_well_info(file, part_a_sheets)
    df2 = extract_well_info(file, part_b_sheets)

    df = df1.append(df2)

    return(df)