from datetime import date
import ezsheets
import pandas as pd


def is_float(x):
    try:
        float(x)
    except ValueError:
        return False
    return True


def read_guava_qc_data(file):
    try:
        xlsx = pd.ExcelFile(file)
        try:
            df_temp = pd.read_excel(xlsx, sheet_name="Summary - QC record", header=None)
            operator = df_temp[df_temp[1] == "QC Operator"].iloc[0, 4]
            date = df_temp[df_temp[1] == "QC date"].iloc[0, 4]
            wo = df_temp[df_temp[1] == "Work Order #"].iloc[0, 4]
            pn = df_temp[df_temp[1] == "10X Part Number"].iloc[0, 4]
            lot = df_temp[df_temp[1] == "Lot Number"].iloc[0, 4]
            desc = df_temp[df_temp[1] == "Product QC'ed"].iloc[0, 4]
        except:
            print(f"{file} could not be processed")
        try:
            df_temp1 = pd.read_excel(
                xlsx, sheet_name="Analysis (Single Cell)", header=None
            )
            data_s = df_temp1.index[
                df_temp1[1] == "Final Dispensed Strip Samples"
            ].tolist()
            data1 = df_temp1[data_s[0] + 2 :]
            data1 = data1[[1, 2, 4, 5, 6]]
            data1 = data1.rename(
                columns={
                    1: "plate",
                    2: "strip",
                    4: "pbeads",
                    5: "gb_conc",
                    6: "avg_conc_per_well",
                }
            )
            data1["strip"] = data1["strip"].fillna(method="pad", limit=2)
            data1["plate"] = data1["plate"].fillna(method="pad", limit=2)
            data1 = data1[data1.pbeads.apply(lambda x: is_float(x))]
            data1 = data1.dropna(subset=["pbeads"])
        except:
            data1 = pd.DataFrame()
        try:
            df_temp2 = pd.read_excel(
                xlsx, sheet_name="Analysis (Single Cell) (2)", header=None
            )
            data_s = df_temp2.index[
                df_temp2[1] == "Final Dispensed Strip Samples"
            ].tolist()
            data2 = df_temp2[data_s[0] + 2 :]
            data2 = data2[[1, 2, 4, 5, 6]]
            data2 = data2.rename(
                columns={
                    1: "plate",
                    2: "strip",
                    4: "pbeads",
                    5: "gb_conc",
                    6: "avg_conc_per_well",
                }
            )
            data2["strip"] = data2["strip"].fillna(method="pad", limit=2)
            data2["plate"] = data2["plate"].fillna(method="pad", limit=2)
            data2 = data2[data2.pbeads.apply(lambda x: is_float(x))]
            data2 = data2.dropna(subset=["pbeads"])
        except:
            data2 = pd.DataFrame()
        try:
            df_temp3 = pd.read_excel(
                xlsx, sheet_name="Analysis (Single Cell) (3)", header=None
            )
            data_s = df_temp3.index[
                df_temp3[1] == "Final Dispensed Strip Samples"
            ].tolist()
            data3 = df_temp3[data_s[0] + 2 :]
            data3 = data3[[1, 2, 4, 5, 6]]
            data3 = data3.rename(
                columns={
                    1: "plate",
                    2: "strip",
                    4: "pbeads",
                    5: "gb_conc",
                    6: "avg_conc_per_well",
                }
            )
            data3["strip"] = data3["strip"].fillna(method="pad", limit=2)
            data3["plate"] = data3["plate"].fillna(method="pad", limit=2)
            data3 = data3[data3.pbeads.apply(lambda x: is_float(x))]
            data3 = data3.dropna(subset=["pbeads"])
        except:
            data3 = pd.DataFrame()

        data = data1.append(data2).append(data3)
        data = data.assign(
            pn=pn, pn_desc=desc, lot=lot, wo=wo, operator=operator, date=date
        )
    except:
        print(f"{file} could not be processed")
        data = pd.DataFrame()

    return data


def get_hsv_gsheet_data_old(
    sheet_id="10bRqRZUBQiQTNIHvMxaCJLk3J3Mjy1zha9kryr1-3L8",
):

    ss = ezsheets.Spreadsheet(sheet_id)
    sheet1 = ss["HSV data"]

    d = {
        "qc_date": sheet1.getColumn(2),
        "pn": sheet1.getColumn(3),
        "wo": sheet1.getColumn(4),
        "qc_operator": sheet1.getColumn(5),
        "run_name": sheet1.getColumn(6),
        "chip_used": sheet1.getColumn(7),
        "layout": sheet1.getColumn(8),
        "chip_lot": sheet1.getColumn(9),
        "oil_lot": sheet1.getColumn(11),
        "bead_lot": sheet1.getColumn(12),
        "hsv": sheet1.getColumn(13),
        "eeprom": sheet1.getColumn(14),
        "is_pinned_gem": sheet1.getColumn(15),
        "is_clog_debris": sheet1.getColumn(16),
        "is_wetting_failure": sheet1.getColumn(17),
        "start_time": sheet1.getColumn(20),
        "end_time": sheet1.getColumn(21),
        "n_equal_0": sheet1.getColumn(22),
        "n_equal_1": sheet1.getColumn(23),
        "n_greater_1": sheet1.getColumn(24),
        "ggf": sheet1.getColumn(25),
        "ggf_cv": sheet1.getColumn(26),
        "bif": sheet1.getColumn(27),
        "bif_cv": sheet1.getColumn(28),
        "cg_rate": sheet1.getColumn(29),
        "tether_rate": sheet1.getColumn(30),
        "drift": sheet1.getColumn(31),
        "big_clump_count": sheet1.getColumn(32),
        "bif_true_cv": sheet1.getColumn(33),
        "small_clump_count": sheet1.getColumn(34),
        "local_noise_cv": sheet1.getColumn(35),
    }

    df = pd.DataFrame(d)
    # drop first row
    df = df.iloc[1:, :]

    # clean empty rows
    nan_value = float("NaN")
    df.replace("", nan_value, inplace=True)
    df = df.dropna(subset=["pn"])
    # df = df.dropna(subset=["qc_date"])
    # df["qc_date"] = pd.to_datetime(df["qc_date"], errors="coerce")

    return df


def get_hsv_gsheet_data_new(
    sheet_id="1pXxjRi0AL5UTdt0lV8VpemN-Aqq7ZetVHtQABfaLVKg",
):

    ss = ezsheets.Spreadsheet(sheet_id)
    sheet1 = ss["Fill Data"]

    d = {
        "chip_used": sheet1.getColumn(1),
        "pn": sheet1.getColumn(9),
        "wo": sheet1.getColumn(10),
        "layout": sheet1.getColumn(2),
        "plateau_ht": sheet1.getColumn(3),
        "qc_date": sheet1.getColumn(4),
        "run_name": sheet1.getColumn(5),
        "chip_lot": sheet1.getColumn(6),
        "novec_lot": sheet1.getColumn(7),
        "bead_lot": sheet1.getColumn(8),
        "oil_lot": sheet1.getColumn(11),
        "eeprom": sheet1.getColumn(12),
        "hsv": sheet1.getColumn(13),
        "start_time": sheet1.getColumn(16),
        "end_time": sheet1.getColumn(17),
        "n_equal_0": sheet1.getColumn(18),
        "n_equal_1": sheet1.getColumn(19),
        "n_greater_1": sheet1.getColumn(20),
        "ggf": sheet1.getColumn(21),
        "ggf_cv": sheet1.getColumn(22),
        "bif": sheet1.getColumn(23),
        "bif_cv": sheet1.getColumn(24),
        "cg_rate": sheet1.getColumn(25),
        "tether_rate": sheet1.getColumn(26),
        "drift": sheet1.getColumn(27),
        "big_clump_count": sheet1.getColumn(28),
        "bif_true_cv": sheet1.getColumn(29),
        "small_clump_count": sheet1.getColumn(30),
        "local_noise_cv": sheet1.getColumn(31),
    }

    df = pd.DataFrame(d)
    # drop first row
    df = df.iloc[1:, :]

    # clean empty rows
    nan_value = float("NaN")
    df.replace("", nan_value, inplace=True)
    df = df.dropna(subset=["chip_used"])
    # df = df.dropna(subset=["qc_date"])
    # df["qc_date"] = pd.to_datetime(df["qc_date"], errors="coerce")

    return df
