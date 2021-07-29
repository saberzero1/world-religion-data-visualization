import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import ipywidgets as widgets
from IPython.display import display

country_codes  = pd.read_csv("datasets/cow-country-codes.csv")
global_stats   = pd.read_csv("datasets/WRP-global-data.csv")
national_stats = pd.read_csv("datasets/WRP-national-data.csv")
regional_stats = pd.read_csv("datasets/WRP-regional-data.csv")

print("Finished loading datasets.")

def cc(country):
    return country_codes.query('StateNme == @country')["StateAbb"].iloc[0]

print(f"Get country code by country name. Example: cc('United States of America').")
cc('United States of America')

global_all_combine = pd.DataFrame(global_stats,columns=["year","chrstprot","chrstcat","chrstorth","chrstang","chrstothr","chrstgen","judorth","jdcons","judref","judothr","judgen","islmsun","islmshi","islmibd","islmnat","islmalw","islmahm","islmothr","islmgen","budmah","budthr","budothr","budgen","zorogen","hindgen","sikhgen","shntgen","bahgen","taogen","jaingen","confgen","syncgen","anmgen","nonrelig","othrgen","worldpop"])
def find_row_by_year(year):
    return global_stats.loc[global_stats["year"]==year].iloc[0]

print(f"Get row by year. Example: find_row_by_year(1945).")
find_row_by_year(1945)

global_all_judaism = pd.Series(global_stats.iloc[13],index=["judorth","jdcons","judref","judothr"],name="Distribution of Judaism in 2010")
global_all_islam = pd.Series(global_stats.iloc[13],index=["islmsun","islmshi","islmibd","islmnat","islmalw","islmahm","islmothr"],name="Distribution of Islam in 2010")
global_all_buddhism = pd.Series(global_stats.iloc[13],index=["budmah","budthr","budothr"],name="Distribution of Buddhism in 2010")
cols_to_sum = pd.Series(global_stats.iloc[13],index=["zorogen","sikhgen","shntgen","bahgen","taogen","jaingen","confgen","syncgen","anmgen"]).sum()
global_all_general = pd.Series(global_stats.iloc[13],index=["judgen","chrstgen","islmgen","budgen","hindgen","nonrelig","misc","othrgen"],name="Distribution of Major religions in 2010").replace(to_replace=np.nan, value=cols_to_sum)
global_all_misc = pd.Series(global_stats.iloc[13],index=["zorogen","sikhgen","shntgen","syncgen","anmgen","bahgen","taogen","jaingen","confgen"],name="Distribution of Miscellaneous in 2010")
print("Finished generating distribution charts.")