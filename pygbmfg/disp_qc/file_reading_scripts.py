import ezsheets
import pandas as pd


def get_hsv_gsheet_data(
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

    return df
