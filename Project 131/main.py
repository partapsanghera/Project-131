import csv
import pandas as pd

df = pd.read_csv("main.csv")

print(df.columns)
print(df.dtypes)

del df['Unnamed: 0']

print(df.columns)

print(df.head())

radius = df['Radius'].to_list()
mass = df['Mass'].to_list()
gravity =[]

def convert_to_si(radius,mass):
    for i in range(0,len(radius)-1):
        radius[i] = radius[i]*6.957e+8
        mass[i] = mass[i]*1.989e+30
        
convert_to_si(radius,mass)
def gravity_calculation(radius,mass):
    G = 6.674e-11
    for index in range(0,len(mass)):
        g= (mass[index]*G)/((radius[index])**2)
        gravity.append(g)
        
gravity_calculation(radius,mass)

df["Gravity"] = gravity
df

df.to_csv("final.csv")