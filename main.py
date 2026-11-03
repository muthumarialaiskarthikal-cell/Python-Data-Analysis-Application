
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# Sample Dataset
data = {
    "Name": ["Arun", "Priya", "Karthika", "Ravi", "Meena"],
    "Age": [21, 22, 20, 23, 21],
    "Marks": [85, 90, 88, 75, 95]
}

df = pd.DataFrame(data)

# Data Cleaning
df.dropna(inplace=True)

# Data Analysis
print("STUDENT DATA ANALYSIS")
print(df)

print("\nAverage Marks:", np.mean(df["Marks"]))
print("Highest Marks:", np.max(df["Marks"]))
print("Lowest Marks:", np.min(df["Marks"]))

# Data Visualization
plt.bar(df["Name"], df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Analysis")
plt.savefig("student_analysis.png")
plt.show()

# REST API
url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

if response.status_code == 200:
    api_data = response.json()
    print("\nAPI DATA")
    print("Title:", api_data["title"])
else:
    print("API request failed")

# Report Generation
with open("report.txt", "w") as file:
    file.write("PYTHON DATA ANALYSIS REPORT\n")
    file.write(str(df.describe()))

print("\nReport generated successfully!")
