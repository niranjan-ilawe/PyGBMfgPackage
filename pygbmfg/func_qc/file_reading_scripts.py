import pandas as pd
import re


def read_mav_divvar_file(file):
    try:
        xlsx = pd.ExcelFile(file)
        df_temp = pd.read_excel(xlsx, sheet_name="Summary-QC records")
        try:
            overhang = df_temp[
                df_temp[
                    "Quality Control Method: SC5' Gel Bead Diversity, Variance, and Whitelist Contamination"
                ]
                == "Overhang Part Number"
            ].iloc[0][3]
            if type(overhang) == int:
                overhang = str(overhang)
            overhang = re.findall(r"\d$", overhang)[0]
            pn = df_temp[
                df_temp[
                    "Quality Control Method: SC5' Gel Bead Diversity, Variance, and Whitelist Contamination"
                ]
                == "Part Number(s)"
            ].iloc[0][3]
            wo = df_temp[
                df_temp[
                    "Quality Control Method: SC5' Gel Bead Diversity, Variance, and Whitelist Contamination"
                ]
                == "Work Order #(s)"
            ].iloc[0][3]
            if type(wo) == int:
                wo = str(wo)
            wo = re.findall(r"\d+", wo)[0]
            ln = df_temp[
                df_temp[
                    "Quality Control Method: SC5' Gel Bead Diversity, Variance, and Whitelist Contamination"
                ]
                == "Lot Number(s)"
            ].iloc[0][3]
            date = df_temp[
                df_temp[
                    "Quality Control Method: SC5' Gel Bead Diversity, Variance, and Whitelist Contamination"
                ]
                == "QC date"
            ].iloc[0][3]
            metrics_start = df_temp.index[
                df_temp["Unnamed: 0"] == "SC3'v3 Metrics1"
            ].tolist()
            metrics_end = df_temp.index[df_temp["Unnamed: 0"] == "LT Metrics1"].tolist()
            qc_metrics = df_temp.iloc[int(metrics_start[0]) : int(metrics_end[0])]

            poly_dt_s = qc_metrics.index[
                qc_metrics[
                    "Quality Control Method: SC5' Gel Bead Diversity, Variance, and Whitelist Contamination"
                ]
                == "Poly (dT)"
            ].tolist()
            poly_dt_e = qc_metrics.index[
                qc_metrics[
                    "Quality Control Method: SC5' Gel Bead Diversity, Variance, and Whitelist Contamination"
                ]
                == "x22_v2_6"
            ].tolist()
            poly_dt_metrics = df_temp.iloc[int(poly_dt_s[0]) + 1 : int(poly_dt_e[0])]
            poly_dt_metrics = poly_dt_metrics.assign(family="Poly (dT)")

            x22_s = qc_metrics.index[
                qc_metrics[
                    "Quality Control Method: SC5' Gel Bead Diversity, Variance, and Whitelist Contamination"
                ]
                == "x22_v2_6"
            ].tolist()
            x22_e = qc_metrics.index[
                qc_metrics[
                    "Quality Control Method: SC5' Gel Bead Diversity, Variance, and Whitelist Contamination"
                ]
                == "v22_v2_8"
            ].tolist()
            x22_metrics = df_temp.iloc[int(x22_s[0]) + 1 : int(x22_e[0])]
            x22_metrics = x22_metrics.assign(family="x22_v2_6")

            v22_s = qc_metrics.index[
                qc_metrics[
                    "Quality Control Method: SC5' Gel Bead Diversity, Variance, and Whitelist Contamination"
                ]
                == "v22_v2_8"
            ].tolist()
            v22_metrics = df_temp.iloc[int(v22_s[0]) + 1 : qc_metrics.index[-1]]
            v22_metrics = v22_metrics.assign(family="v22_v2_8")

            qc_metrics = poly_dt_metrics.append(x22_metrics).append(v22_metrics)
            qc_metrics = qc_metrics[
                [
                    "Quality Control Method: SC5' Gel Bead Diversity, Variance, and Whitelist Contamination",
                    "Unnamed: 3",
                    "family",
                    "QC000083",
                ]
            ].dropna()
            qc_metrics = qc_metrics.rename(
                columns={
                    "Quality Control Method: SC5' Gel Bead Diversity, Variance, and Whitelist Contamination": "data_name",
                    "Unnamed: 3": "data_value",
                    "QC000083": "disposition",
                }
            )
            qc_metrics = qc_metrics.assign(
                pn=pn, ln=ln, wo=wo, date=date, overhang=overhang
            )
        except:
            print(f"{file} does not have overhang specific data")
            qc_metrics = pd.DataFrame()
    except:
        print(f"{file} could not be processed")
        qc_metrics = pd.DataFrame()

    return qc_metrics


def read_vdj_divvar_file_revL(file):
    try:
        xlsx = pd.ExcelFile(file)
        df_temp = pd.read_excel(xlsx, sheet_name="Summary-QC records", header=None)
        try:
            overhang = df_temp[
                df_temp[2].str.contains("Overhang Part Number", na=False)
            ].iloc[0][4]
            if type(overhang) == int:
                overhang = str(overhang)
            overhang = re.findall(r"\d$", overhang)[0]
            pn = df_temp[df_temp[2].str.contains("Part Number\(s\)", na=False)].iloc[0][
                4
            ]
            wo = df_temp[df_temp[2].str.contains("Work Order #\(s\)", na=False)].iloc[
                0
            ][4]
            if type(wo) == int:
                wo = str(wo)
            wo = re.findall(r"\d+", wo)[0]
            ln = df_temp[df_temp[2].str.contains("Lot Number\(s\)", na=False)].iloc[0][
                4
            ]
            date = df_temp[df_temp[2].str.contains("QC date", na=False)].iloc[0][4]
            metrics_start = df_temp.index[
                df_temp[1].str.contains("SC5' Overhang 1 Metrics", na=False)
            ].tolist()
            metrics_end = df_temp.index[
                df_temp[1].str.contains("SC5' Overhang 2 Metrics", na=False)
            ].tolist()
            qc_metrics = df_temp.iloc[int(metrics_start[0]) + 1 : int(metrics_end[0])]
            qc_metrics = qc_metrics.assign(family="SC 5' Metric(s)", overhang="1")
            qc_metrics = qc_metrics[[2, 4, 7, "family", "overhang"]].dropna()
            qc_metrics = qc_metrics.rename(
                columns={
                    2: "data_name",
                    4: "data_value",
                    7: "disposition",
                }
            )
            tmp = qc_metrics
            metrics_start = df_temp.index[
                df_temp[1].str.contains("SC5' Overhang 2 Metrics", na=False)
            ].tolist()
            metrics_end = df_temp.index[
                df_temp[1].str.contains("SC5' Overhang 3 Metrics", na=False)
            ].tolist()
            qc_metrics = df_temp.iloc[int(metrics_start[0]) + 1 : int(metrics_end[0])]
            qc_metrics = qc_metrics.assign(family="SC 5' Metric(s)", overhang="2")
            qc_metrics = qc_metrics[[2, 4, 7, "family", "overhang"]].dropna()
            qc_metrics = qc_metrics.rename(
                columns={
                    2: "data_name",
                    4: "data_value",
                    7: "disposition",
                }
            )
            tmp = tmp.append(qc_metrics)
            metrics_start = df_temp.index[
                df_temp[1].str.contains("SC5' Overhang 3 Metrics", na=False)
            ].tolist()
            metrics_end = df_temp.index[
                df_temp[1].str.contains("SC5' Overhang 4 Metrics", na=False)
            ].tolist()
            qc_metrics = df_temp.iloc[int(metrics_start[0]) + 1 : int(metrics_end[0])]
            qc_metrics = qc_metrics.assign(family="SC 5' Metric(s)", overhang="3")
            qc_metrics = qc_metrics[[2, 4, 7, "family", "overhang"]].dropna()
            qc_metrics = qc_metrics.rename(
                columns={
                    2: "data_name",
                    4: "data_value",
                    7: "disposition",
                }
            )
            tmp = tmp.append(qc_metrics)
            metrics_start = df_temp.index[
                df_temp[1].str.contains("SC5' Overhang 4 Metrics", na=False)
            ].tolist()
            metrics_end = df_temp.index[
                df_temp[1].str.contains("Released by:", na=False)
            ].tolist()
            qc_metrics = df_temp.iloc[int(metrics_start[0]) + 1 : int(metrics_end[0])]
            qc_metrics = qc_metrics.assign(family="SC 5' Metric(s)", overhang="4")
            qc_metrics = qc_metrics[[2, 4, 7, "family", "overhang"]].dropna()
            qc_metrics = qc_metrics.rename(
                columns={
                    2: "data_name",
                    4: "data_value",
                    7: "disposition",
                }
            )
            tmp = tmp.append(qc_metrics)

            qc_metrics = tmp
            qc_metrics = qc_metrics.assign(pn=pn, ln=ln, wo=wo, date=date)
            qc_metrics = qc_metrics.drop_duplicates()
        except:
            print(f"{file} does not have overhang specific data")
            qc_metrics = pd.DataFrame()
    except:
        print(f"{file} not a valid DivVar QC file")
        qc_metrics = pd.DataFrame()

    return qc_metrics


def read_vdj_divvar_file_revJ(file):
    try:
        xlsx = pd.ExcelFile(file)
        df_temp = pd.read_excel(xlsx, sheet_name="Summary-QC records")
        try:
            overhang = df_temp[
                df_temp[
                    "Quality Control Method: SC5' Gel Bead Diversity, Variance, and Whitelist Contamination"
                ]
                == "Overhang Part Number"
            ].iloc[0][3]
            if type(overhang) == int:
                overhang = str(overhang)
            overhang = re.findall(r"\d$", overhang)[0]
            pn = df_temp[
                df_temp[
                    "Quality Control Method: SC5' Gel Bead Diversity, Variance, and Whitelist Contamination"
                ]
                == "Part Number(s)"
            ].iloc[0][3]
            wo = df_temp[
                df_temp[
                    "Quality Control Method: SC5' Gel Bead Diversity, Variance, and Whitelist Contamination"
                ]
                == "Work Order #(s)"
            ].iloc[0][3]
            if type(wo) == int:
                wo = str(wo)
            wo = re.findall(r"\d+", wo)[0]
            ln = df_temp[
                df_temp[
                    "Quality Control Method: SC5' Gel Bead Diversity, Variance, and Whitelist Contamination"
                ]
                == "Lot Number(s)"
            ].iloc[0][3]
            date = df_temp[
                df_temp[
                    "Quality Control Method: SC5' Gel Bead Diversity, Variance, and Whitelist Contamination"
                ]
                == "QC date"
            ].iloc[0][3]
            metrics_start = df_temp.index[
                df_temp[
                    "Quality Control Method: SC5' Gel Bead Diversity, Variance, and Whitelist Contamination"
                ]
                == "SC 5' Metric(s)"
            ].tolist()
            metrics_end = df_temp.index[
                df_temp[
                    "Quality Control Method: SC5' Gel Bead Diversity, Variance, and Whitelist Contamination"
                ]
                == "Poly (dT)"
            ].tolist()
            qc_metrics = df_temp.iloc[int(metrics_start[0]) + 1 : int(metrics_end[0])]
            qc_metrics = qc_metrics.assign(family="SC 5' Metric(s)")
            qc_metrics = qc_metrics[
                [
                    "Quality Control Method: SC5' Gel Bead Diversity, Variance, and Whitelist Contamination",
                    "Unnamed: 3",
                    "family",
                    "QC000083",
                ]
            ].dropna()
            qc_metrics = qc_metrics.rename(
                columns={
                    "Quality Control Method: SC5' Gel Bead Diversity, Variance, and Whitelist Contamination": "data_name",
                    "Unnamed: 3": "data_value",
                    "QC000083": "disposition",
                }
            )
            qc_metrics = qc_metrics.assign(
                pn=pn, ln=ln, wo=wo, date=date, overhang=overhang
            )
        except:
            print(f"{file} does not have overhang specific data")
            qc_metrics = pd.DataFrame()
    except:
        print(f"{file} not a valid DivVar QC file")
        qc_metrics = pd.DataFrame()

    return qc_metrics
