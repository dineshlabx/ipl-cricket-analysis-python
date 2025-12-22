import pandas as pd
import matplotlib.pyplot as plt

#step1  read csv file

#step2 show data
df = pd.read_csv("ipl_matches.csv")

#step3 to remove whitespace in file
df.columns=df.columns.str.strip()

#step4 average runs per team
avg_runs = df.groupby("team") ["runs"].mean()

print("\nAverage runs per team:", avg_runs)


#step5 plot the chart

avg_runs.plot(kind='bar')
plt.title("Average runs by IPL team")
plt.xlabel("team")
plt.ylabel("Average runs per team")
plt.show()