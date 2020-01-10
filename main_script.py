from package1.acquire import *
from package1.wrangle import *
from package1.enrich import *
from package1.reporting import *

if __name__ == "__main__":
    df_master = acquire()
    df_cleaned = wrangling(df_master)
    df_analysis = enrich(df_cleaned)
    reporting(df_analysis)
