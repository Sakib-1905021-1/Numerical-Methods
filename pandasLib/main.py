import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

population = pd.read_csv("population_2020.csv")
print(population)
print("Initial max_rows value : " + str(pd.options.display.max_rows))
print("Initial max_columns value : " + str(pd.options.display.max_columns))
pd.set_option("display.max_columns", 80)
print("After changes max_columns value : " + str(pd.options.display.max_columns))
pd.set_option("display.max_rows", 50)
print("After changes max_rows value : " + str(pd.options.display.max_rows))
if pd.options.display.max_rows > 50:
    pd.set_option("display.max_rows", 50)
if pd.options.display.max_columns > 50:
    pd.set_option("display.max_columns", 50)
print(population.head())
print(population.tail())
print(population["Population (2020)"])
print(population["Yearly Change"])
print(population["Net Change"])
print(population["Net Change"].value_counts())


