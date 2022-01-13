import ezsheets
import pandas as pd
from pygbmfg.common import _load_credentials, _clear_credentials


def read_channel_yield_sheet(sheet_id="1X5vvqY4pCGoKvCXeUNMvkWfrIheOcd1CmzMYOkBmG4g"):
    _load_credentials()
    ss = ezsheets.Spreadsheet(sheet_id)

    sheet1 = ss["Sheet1"]

    d = {
        "start_date": sheet1.getColumn(3),
        "end_date": sheet1.getColumn(4),
        "build": sheet1.getColumn(6),
        "wo": sheet1.getColumn(7),
        "site": sheet1.getColumn(8),
        "total_channels": sheet1.getColumn(10),
        "passing_channels": sheet1.getColumn(11),
    }

    df = pd.DataFrame(d)
    # drop first row
    df = df.iloc[1:, :]
    # clean empty rows
    nan_value = float("NaN")
    df.replace("", nan_value, inplace=True)
    df = df.dropna(subset=["end_date"])
    _clear_credentials()

    return df


def read_sg_channel_yield_sheet(
    sheet_id="1HiDMxatOyqYc_JMOKcoozEkME2KQ2_MTJHh01358Vns",
):
    _load_credentials()
    ss = ezsheets.Spreadsheet(sheet_id)

    sheet1 = ss["Rig Run Data"]

    d = {
        "start_date": sheet1.getColumn(1),
        "wo": sheet1.getColumn(2),
        "sg_build": sheet1.getColumn(3),
        "rig": sheet1.getColumn(4),
        "channel": sheet1.getColumn(5),
        "status": sheet1.getColumn(6),
        "pass_rate": sheet1.getColumn(7),
        "volume": sheet1.getColumn(8),
        "reason_code": sheet1.getColumn(9),
    }

    df_sg = pd.DataFrame(d)
    # drop first row
    df_sg = df_sg.iloc[1:, :]
    # clean empty rows
    nan_value = float("NaN")
    df_sg.replace("", nan_value, inplace=True)
    df_sg = df_sg.dropna(subset=["start_date"])
    _clear_credentials()

    return df_sg
