import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Creating data
data = {
    "Student Name": ["Aman", "Riya", "Nikhil", "Priya", "Rahul"],
    "CA1 Marks (25)": [20, 18, 22, 19, 15],
    "CA2 Marks (25)": [21, 20, 23, 18, 14]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Total and Average
df["Total"] = df["CA1 Marks (25)"] + df["CA2 Marks (25)"]
df["Average"] = df["Total"] / 2

print(df)

# NumPy calculations
ca1_mean = np.mean(df["CA1 Marks (25)"])
ca2_mean = np.mean(df["CA2 Marks (25)"])

print("CA1 Average:", ca1_mean)
print("CA2 Average:", ca2_mean)
print("Highest Total:", np.max(df["Total"]))
print("Lowest Total:", np.min(df["Total"]))

# Topper and weak student
topper = df[df["Total"] == df["Total"].max()]
weak = df[df["Total"] == df["Total"].min()]

print("\nTopper:")
print(topper)

print("\nLowest Performer:")
print(weak)

# Bar graph
plt.figure(figsize=(12,6))
plt.bar(df["Student Name"], df["Total"])

plt.xticks(rotation=45)
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.title("Total Marks of Students")

plt.tight_layout()
plt.show()

# Line graph
x = range(len(df))

plt.figure(figsize=(14,6))

plt.plot(x, df["CA1 Marks (25)"], marker="o", label="CA1")
plt.plot(x, df["CA2 Marks (25)"], marker="x", label="CA2")

plt.xticks(x, df["Student Name"], rotation=45)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("CA1 vs CA2 Comparison")

plt.legend()
plt.tight_layout()
plt.show()