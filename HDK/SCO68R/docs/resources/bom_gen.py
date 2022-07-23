#!/usr/bin/python3
import csv
import pandas as pd


def csv2table(fp: str):
    df = pd.read_csv(fp)
    with open( fp.replace(".csv",".md"), 'w') as md:
        df.to_markdown(buf=md, tablefmt="grid")

if __name__=="__main__":        
    csv_file_path = "HDK/FAB/SCO68-4R-REV1-0/SCO68R_BOM.csv"
    #takes input of the type of delimiter in CSV file

    csv2table("HDK/FAB/SCO68-4R-REV1-0/SCO68R_BOM.csv")
