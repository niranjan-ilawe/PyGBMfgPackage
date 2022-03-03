import pandas as pd


def read_funcseq_qc_data(file):
    try:
        xlsx = pd.ExcelFile(file)
        try:
            df_temp = pd.read_excel(xlsx, sheet_name="Summary-QC records", header=None)
            pn = df_temp[df_temp[1].str.contains("10X Part Number", na=False)].iloc[
                0, 2
            ]
            lot = df_temp[df_temp[1].str.contains("Lot Number", na=False)].iloc[0, 2]
            wo = df_temp[df_temp[1].str.contains("Work Order", na=False)].iloc[0, 2]
            date = df_temp[df_temp[1].str.contains("QC date", na=False)].iloc[0, 2]
        except:
            print(f"Error in Summary section of {file}")
        try:
            df_temp1 = pd.read_excel(xlsx, sheet_name="Disposition", header=None)
            data_s = df_temp1.index[
                df_temp1[0].str.contains("Enter Row # for Each TEST Sample", na=False)
            ].tolist()
            data_e = df_temp1.index[
                df_temp1[0].str.contains("Control Results", na=False)
            ].tolist()

            data1 = df_temp1[data_s[0] : data_s[1]]
            data1 = data1[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
            data1.columns = data1.iloc[0]
            data1 = data1.iloc[1:, :]
            data1.reset_index(drop=True, inplace=True)
            data1 = data1.dropna(subset=["Sequencer"])

            data2 = df_temp1[data_s[1] : data_s[2]]
            data2 = data2[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
            data2.columns = data2.iloc[0]
            data2 = data2.iloc[1:, :]
            data2.reset_index(drop=True, inplace=True)
            data2 = data2.dropna(subset=["Sequencer"])

            data3 = df_temp1[data_s[2] : data_e[0]]
            data3 = data3[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
            data3.columns = data3.iloc[0]
            data3 = data3.iloc[1:, :]
            data3.reset_index(drop=True, inplace=True)
            data3 = data3.dropna(subset=["Sequencer"])

            result = pd.concat([data1, data2, data3], axis=1, join="inner")
            result = result.loc[:, ~result.columns.duplicated()]
        except:
            print(f"Error in Disposition section of {file}")

        data = result.assign(pn=pn, lot=lot, wo=wo, date=date)

        data.columns = (
            data.columns.str.strip()
            .str.lower()
            .str.replace(" ", "_")
            .str.replace("-", "_")
            .str.replace("(", "")
            .str.replace(")", "")
            .str.replace(".", "")
            .str.replace("<", "lessthan")
            .str.replace(">", "greaterthan")
        )

        data = data.melt(
            id_vars=["pn", "wo", "lot", "date", "description", "sequencer"],
            var_name="data_name",
            value_name="data_value",
        )

    except:
        print(f"{file} could not be processed")
        data = pd.DataFrame()

    return data
