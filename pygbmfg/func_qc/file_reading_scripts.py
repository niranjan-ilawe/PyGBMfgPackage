from datetime import datetime
import pandas as pd
import re
import numpy as np


def read_probehyb_file(file):
    try:
        xlsx = pd.ExcelFile(file)
        data = pd.read_excel(xlsx, sheet_name="Summary - QC records", header=None)

        # extract lot metadata
        pn = data[data[1].str.contains("10X Part", na=False)].iloc[0, 2]
        overhang_pn = data[data[1].str.contains("Overhang Part", na=False)].iloc[0, 2]
        lot = data[data[1].str.contains("Lot Number", na=False)].iloc[0, 2]
        wo = data[data[1].str.contains("Work Order", na=False)].iloc[0, 2]
        qc_by = data[data[1].str.contains("QC'ed by", na=False)].iloc[0, 2]
        # convert python datetime object to formatted date string
        qc_date = (
            data[data[1].str.contains("QC date", na=False)]
            .iloc[0, 2]
            .strftime("%m-%d-%Y")
        )

        # QC metrics
        # first get start and end indices to metrics box
        met_start = data.index[data[1].str.contains("Percent in box", na=False)][0]
        met_end = data.index[data[1].str.contains("Disposition", na=False)][0]

        # extract rows in that box
        met = data.iloc[met_start:met_end]

        # select relevant cols and rename them
        met = met[[1, 2]]
        met = met.rename(columns={1: "data_name", 2: "data_value"})

        # filter rows with empty values
        met = met.dropna(subset=["data_value"])

        # assign lot meta data
        met = met.assign(
            pn=pn, overhang_pn=overhang_pn, lot=lot, wo=wo, qc_by=qc_by, qc_date=qc_date
        )

    except ValueError as err:
        if "Worksheet" in err.args[0]:
            print(f"Error: 'Summary - QC records sheet' not found in '{file}'")
        met = pd.DataFrame()

    return met


def read_flowcam_file(file):
    try:
        xlsx = pd.ExcelFile(file)
        summary = pd.read_excel(xlsx, sheet_name="Summary - QC record")
        try:
            overhang = summary[
                summary["Quality Control Method"] == "Overhang Part Number "
            ].iloc[0][3]
            if type(overhang) == int:
                overhang = str(overhang)
            overhang = re.findall(r"\d$", overhang)[0]
        except:
            overhang = "NA"
        summary = summary[["Quality Control Method", "Unnamed: 2"]]
        pn = summary[summary["Quality Control Method"] == "10X Part Number:"].iloc[0][1]
        wo = summary[summary["Quality Control Method"] == "Work Order #:"].iloc[0][1]
        ln = summary[summary["Quality Control Method"] == "Lot Number:"].iloc[0][1]
        date = summary[summary["Quality Control Method"] == "QC date:"].iloc[0][1]
        qc_metrics_start = summary.index[
            summary["Quality Control Method"] == "QC Results"
        ].tolist()
        qc_metrics_end = summary.index[
            summary["Quality Control Method"] == "Disposition"
        ].tolist()
        qc_metrics = summary.iloc[
            int(qc_metrics_start[0]) + 2 : int(qc_metrics_end[0]) - 1
        ]
        qc_metrics = qc_metrics[["Quality Control Method", "Unnamed: 2"]].dropna()
        qc_metrics = qc_metrics.rename(
            columns={"Quality Control Method": "data_name", "Unnamed: 2": "data_value"}
        )
        qc_metrics = qc_metrics.assign(
            pn=pn, ln=ln, date=date, wo=wo, overhang=overhang
        )
    except:
        print(f"{file} could not be processed")
        qc_metrics = pd.DataFrame()

    return qc_metrics


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


def read_orion_divvar_file_revB(file):
    try:
        xlsx = pd.ExcelFile(file)
        df_temp = pd.read_excel(xlsx, sheet_name="Summary-QC records", header=None)
        try:
            # overhang = df_temp[
            #    df_temp[2].str.contains("Overhang Part Number", na=False)
            # ].iloc[0][4]
            # if type(overhang) == int:
            #    overhang = str(overhang)
            # overhang = re.findall(r"\d$", overhang)[0]
            pn = df_temp[df_temp[1].str.contains("Part Number\(s\)", na=False)].iloc[0][
                3
            ]
            wo = df_temp[df_temp[1].str.contains("Work Order #\(s\)", na=False)].iloc[
                0
            ][3]
            if type(wo) == int:
                wo = str(wo)
            wo = re.findall(r"\d+", wo)
            ln = df_temp[df_temp[1].str.contains("Lot Number\(s\)", na=False)].iloc[0][
                3
            ]
            date = df_temp[df_temp[1].str.contains("QC date", na=False)].iloc[0][3]
            metrics_start = df_temp.index[
                df_temp[0].str.contains("Multiome A Metrics OH1", na=False)
            ].tolist()
            metrics_end = df_temp.index[
                df_temp[0].str.contains("Multiome A Metrics OH2", na=False)
            ].tolist()
            qc_metrics = df_temp.iloc[int(metrics_start[0]) + 1 : int(metrics_end[0])]
            qc_metrics = qc_metrics.assign(
                family="Multiome A Metrics", overhang="1", wo=wo[0]
            )
            qc_metrics = qc_metrics[[1, 3, 6, "family", "overhang", "wo"]].dropna()
            qc_metrics = qc_metrics.rename(
                columns={
                    1: "data_name",
                    3: "data_value",
                    6: "disposition",
                }
            )
            tmp = qc_metrics
            metrics_start = df_temp.index[
                df_temp[0].str.contains("Multiome A Metrics OH2", na=False)
            ].tolist()
            metrics_end = df_temp.index[
                df_temp[0].str.contains("Multiome A Metrics OH3", na=False)
            ].tolist()
            qc_metrics = df_temp.iloc[int(metrics_start[0]) + 1 : int(metrics_end[0])]
            qc_metrics = qc_metrics.assign(
                family="Multiome A Metrics", overhang="2", wo=wo[1]
            )
            qc_metrics = qc_metrics[[1, 3, 6, "family", "overhang", "wo"]].dropna()
            qc_metrics = qc_metrics.rename(
                columns={
                    1: "data_name",
                    3: "data_value",
                    6: "disposition",
                }
            )
            tmp = tmp.append(qc_metrics)
            metrics_start = df_temp.index[
                df_temp[0].str.contains("Multiome A Metrics OH3", na=False)
            ].tolist()
            metrics_end = df_temp.index[
                df_temp[0].str.contains("Multiome A Metrics OH4", na=False)
            ].tolist()
            qc_metrics = df_temp.iloc[int(metrics_start[0]) + 1 : int(metrics_end[0])]
            qc_metrics = qc_metrics.assign(
                family="Multiome A Metrics", overhang="3", wo=wo[2]
            )
            qc_metrics = qc_metrics[[1, 3, 6, "family", "overhang", "wo"]].dropna()
            qc_metrics = qc_metrics.rename(
                columns={
                    1: "data_name",
                    3: "data_value",
                    6: "disposition",
                }
            )
            tmp = tmp.append(qc_metrics)
            metrics_start = df_temp.index[
                df_temp[0].str.contains("Multiome A Metrics OH4", na=False)
            ].tolist()
            metrics_end = df_temp.index[
                df_temp[0].str.contains("Released by", na=False)
            ].tolist()
            qc_metrics = df_temp.iloc[int(metrics_start[0]) + 1 : int(metrics_end[0])]
            qc_metrics = qc_metrics.assign(
                family="Multiome A Metrics", overhang="4", wo=wo[3]
            )
            qc_metrics = qc_metrics[[1, 3, 6, "family", "overhang", "wo"]].dropna()
            qc_metrics = qc_metrics.rename(
                columns={
                    1: "data_name",
                    3: "data_value",
                    6: "disposition",
                }
            )
            tmp = tmp.append(qc_metrics)

            qc_metrics = tmp
            qc_metrics = qc_metrics.assign(pn=pn, ln=ln, date=date)
            qc_metrics = qc_metrics.drop_duplicates()
        except:
            print(f"{file} does not have overhang specific data")
            qc_metrics = pd.DataFrame()
    except:
        print(f"{file} not a valid DivVar QC file")
        qc_metrics = pd.DataFrame()

    return qc_metrics


def read_agora_divvar_file_revB(file):
    try:
        xlsx = pd.ExcelFile(file)
        df_temp = pd.read_excel(xlsx, sheet_name="Summary-QC records", header=None)
        try:
            # overhang = df_temp[
            #    df_temp[2].str.contains("Overhang Part Number", na=False)
            # ].iloc[0][4]
            # if type(overhang) == int:
            #    overhang = str(overhang)
            # overhang = re.findall(r"\d$", overhang)[0]
            pn = df_temp[df_temp[1].str.contains("Part Number", na=False)].iloc[0][3]
            wo = df_temp[df_temp[1].str.contains("Work Order #", na=False)].iloc[0][3]
            if type(wo) == int:
                wo = str(wo)
            wo = re.findall(r"\d+", wo)
            ln = df_temp[df_temp[1].str.contains("Lot Number", na=False)].iloc[0][3]
            date = df_temp[df_temp[1].str.contains("QC date", na=False)].iloc[0][3]
            metrics_start = df_temp.index[
                df_temp[1].str.contains("ATAC' Metric\(s\) Overhang 1", na=False)
            ].tolist()
            metrics_end = df_temp.index[
                df_temp[1].str.contains("ATAC' Metric\(s\)  Overhang 2", na=False)
            ].tolist()
            qc_metrics = df_temp.iloc[int(metrics_start[0]) + 1 : int(metrics_end[0])]
            qc_metrics = qc_metrics.assign(
                family="ATAC Metrics", overhang="1", wo=wo[0]
            )
            qc_metrics = qc_metrics[[1, 3, 6, "family", "overhang", "wo"]].dropna()
            qc_metrics = qc_metrics.rename(
                columns={
                    1: "data_name",
                    3: "data_value",
                    6: "disposition",
                }
            )
            tmp = qc_metrics
            metrics_start = df_temp.index[
                df_temp[1].str.contains("ATAC' Metric\(s\)  Overhang 2", na=False)
            ].tolist()
            metrics_end = df_temp.index[
                df_temp[1].str.contains("ATAC' Metric\(s\) Overhang 3", na=False)
            ].tolist()
            qc_metrics = df_temp.iloc[int(metrics_start[0]) + 1 : int(metrics_end[0])]
            qc_metrics = qc_metrics.assign(
                family="ATAC Metrics", overhang="2", wo=wo[1]
            )
            qc_metrics = qc_metrics[[1, 3, 6, "family", "overhang", "wo"]].dropna()
            qc_metrics = qc_metrics.rename(
                columns={
                    1: "data_name",
                    3: "data_value",
                    6: "disposition",
                }
            )
            tmp = tmp.append(qc_metrics)
            metrics_start = df_temp.index[
                df_temp[1].str.contains("ATAC' Metric\(s\) Overhang 3", na=False)
            ].tolist()
            metrics_end = df_temp.index[
                df_temp[1].str.contains("ATAC' Metric\(s\) Overhang 4", na=False)
            ].tolist()
            qc_metrics = df_temp.iloc[int(metrics_start[0]) + 1 : int(metrics_end[0])]
            qc_metrics = qc_metrics.assign(
                family="ATAC Metrics", overhang="3", wo=wo[2]
            )
            qc_metrics = qc_metrics[[1, 3, 6, "family", "overhang", "wo"]].dropna()
            qc_metrics = qc_metrics.rename(
                columns={
                    1: "data_name",
                    3: "data_value",
                    6: "disposition",
                }
            )
            tmp = tmp.append(qc_metrics)
            metrics_start = df_temp.index[
                df_temp[1].str.contains("ATAC' Metric\(s\) Overhang 4", na=False)
            ].tolist()
            metrics_end = df_temp.index[
                df_temp[1].str.contains("Disposition", na=False)
            ].tolist()
            qc_metrics = df_temp.iloc[int(metrics_start[0]) + 1 : int(metrics_end[0])]
            qc_metrics = qc_metrics.assign(
                family="ATAC Metrics", overhang="4", wo=wo[3]
            )
            qc_metrics = qc_metrics[[1, 3, 6, "family", "overhang", "wo"]].dropna()
            qc_metrics = qc_metrics.rename(
                columns={
                    1: "data_name",
                    3: "data_value",
                    6: "disposition",
                }
            )
            tmp = tmp.append(qc_metrics)

            qc_metrics = tmp
            qc_metrics = qc_metrics.assign(pn=pn, ln=ln, date=date)
            qc_metrics = qc_metrics.drop_duplicates()
        except:
            print(f"{file} does not have overhang specific data")
            qc_metrics = pd.DataFrame()
    except:
        print(f"{file} not a valid DivVar QC file")
        qc_metrics = pd.DataFrame()

    return qc_metrics


def read_flowcam_standards_file(file):
    try:
        xlsx = pd.ExcelFile(file)
        summary = pd.read_excel(xlsx, sheet_name="Summary - QC record")
        try:
            overhang = summary[
                summary["Quality Control Method"] == "Overhang Part Number "
            ].iloc[0][3]
            if type(overhang) == int:
                overhang = str(overhang)
            overhang = re.findall(r"\d$", overhang)[0]
        except:
            overhang = "NA"
        summary = summary[["Quality Control Method", "Unnamed: 2"]]
        pn = summary[summary["Quality Control Method"] == "10X Part Number:"].iloc[0][1]
        wo = summary[summary["Quality Control Method"] == "Work Order #:"].iloc[0][1]
        ln = summary[summary["Quality Control Method"] == "Lot Number:"].iloc[0][1]
        date = summary[summary["Quality Control Method"] == "QC date:"].iloc[0][1]

        standards_data = pd.read_excel(xlsx, sheet_name="Raw Data (Standards)")
        standards_data = standards_data[
            ["Diameter (ESD)", "Diameter (ESD).1", "Diameter (ESD).2"]
        ]
        standards_data = standards_data.rename(
            columns={
                "Diameter (ESD)": "dia1",
                "Diameter (ESD).1": "dia2",
                "Diameter (ESD).2": "dia3",
            }
        )
        standards_data = standards_data.dropna(axis=1, how="all")
        standards_data = standards_data.assign(
            pn=pn, ln=ln, date=date, wo=wo, overhang=overhang
        )
    except:
        print(f"{file} could not be processed")
        standards_data = pd.DataFrame()

    return standards_data


def read_mav_divvar_file_revM(file):
    try:
        xlsx = pd.ExcelFile(file)
        data = pd.read_excel(xlsx, sheet_name="Summary-QC records", header=None)
        # store the 4 overhangs in a list
        overhang = (
            data[data[2].str.contains("Overhang Part", na=False)].iloc[0, 4].split(",")
        )
        lot = data[data[2].str.contains("Lot Number", na=False)].iloc[0, 4]
        # store the 4 WOs in a list
        wo = data[data[2].str.contains("Work Order", na=False)].iloc[0, 4].split(",")
        operator = data[data[2].str.contains("Operator", na=False)].iloc[0, 4]
        qc_date = data[data[2].str.contains("QC date", na=False)].iloc[0, 4]

        # if qc_date is a datetime object change it to str with fixed format
        # so that can be easily uploaded to the DB
        if isinstance(qc_date, datetime):
            qc_date = qc_date.strftime("%m-%d-%y")

        # Extract metrics for each family for each overhang
        poly = data.index[data[2].str.contains("Poly", na=False)].to_list()
        v6 = data.index[data[2].str.contains("x22_v2_6", na=False)].tolist()
        v8 = data.index[data[2].str.contains("v22_v2_8", na=False)].tolist()

        # loop through the 4 overhangs
        df = pd.DataFrame()
        for i in range(0, 4):
            # extract poly relevant rows using above boundaries
            d1 = data[int(poly[i]) : int(v6[i]) - 1]
            d1 = d1[[2, 4, 7]]
            d1 = d1[d1[4] != "Test Value"]
            d1 = d1.rename(columns={2: "data_name", 4: "data_value", 7: "disposition"})
            d1 = d1.assign(
                overhang=re.findall("-(\d)", overhang[i])[0],
                ln=lot,
                wo=wo[i],
                date=qc_date,
                pn=re.findall("(\d+)-", overhang[i])[0],
                family="Poly (dT)",
            )

            # extract x22 relevant rows using above boundaries
            d2 = data[int(v6[i]) : int(v8[i]) - 1]
            d2 = d2[[2, 4, 7]]
            d2 = d2[d2[4] != "Test Value"]
            d2 = d2.rename(columns={2: "data_name", 4: "data_value", 7: "disposition"})
            d2 = d2.assign(
                overhang=re.findall("-(\d)", overhang[i])[0],
                ln=lot,
                wo=wo[i],
                date=qc_date,
                pn=re.findall("(\d+)-", overhang[i])[0],
                family="x22_v2_6",
            )

            # extract v22 relevant rows using above boundaries
            d3 = data[int(v8[i]) : int(v8[i]) + 6]
            d3 = d3[[2, 4, 7]]
            d3 = d3[d3[4] != "Test Value"]
            d3 = d3.rename(columns={2: "data_name", 4: "data_value", 7: "disposition"})
            d3 = d3.assign(
                overhang=re.findall("-(\d)", overhang[i])[0],
                ln=lot,
                wo=wo[i],
                date=qc_date,
                pn=re.findall("(\d+)-", overhang[i])[0],
                family="v22_v2_8",
            )

            df = df.append(d1.append(d2.append(d3)))

    except:
        print(f"Error while reading {file}")
        df = pd.DataFrame()

    return df

    # fill empty rows with above value. in this specific case fill the
    # d1 = d1.fillna(method = "ffill")


def read_vdj_divvar_file_revM(file):
    try:
        xlsx = pd.ExcelFile(file)
        data = pd.read_excel(xlsx, sheet_name="Summary-QC records", header=None)
        # store the 4 overhangs in a list
        overhang = (
            data[data[2].str.contains("Overhang Part", na=False)].iloc[0, 4].split(",")
        )
        lot = data[data[2].str.contains("Lot Number", na=False)].iloc[0, 4]
        # store the 4 WOs in a list
        wo = data[data[2].str.contains("Work Order", na=False)].iloc[0, 4].split(",")
        operator = data[data[2].str.contains("Operator", na=False)].iloc[0, 4]
        qc_date = data[data[2].str.contains("QC date", na=False)].iloc[0, 4]

        # if qc_date is a datetime object change it to str with fixed format
        # so that can be easily uploaded to the DB
        if isinstance(qc_date, datetime):
            qc_date = qc_date.strftime("%m-%d-%y")

        # Extract metrics for each family for each overhang
        mets = data.index[
            data[2].str.contains("Fraction of Barcodes", na=False)
        ].to_list()
        # loop through the 4 overhangs
        df = pd.DataFrame()
        for i in range(0, 4):
            # extract metrics relevant rows using above boundaries
            print(i)
            d1 = data[int(mets[i]) : int(mets[i]) + 5]
            d1 = d1[[2, 4, 7]]
            d1 = d1.rename(columns={2: "data_name", 4: "data_value", 7: "disposition"})
            d1 = d1.assign(
                overhang=re.findall("-(\d)", overhang[i])[0],
                ln=lot,
                wo=wo[i],
                date=qc_date,
                pn=re.findall("(\d+)-", overhang[i])[0],
                family="SC 5' Metric(s)",
            )

            df = df.append(d1)

    except:
        print(f"Error while reading {file}")
        df = pd.DataFrame()

    return df


file = "vdj_sg.xlsx"
read_vdj_divvar_file_revM(file)
