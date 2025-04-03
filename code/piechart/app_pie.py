import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    personal_path = "personal.csv"
    return pd.read_csv(personal_path)

personal_df = load_data()


gender_counts = personal_df.groupby("Sexe")["Nombre de personal"].sum()

fig1, ax1 = plt.subplots(figsize=(6, 6))
ax1.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
ax1.set_title("Distribució de personal per sexe")
ax1.axis('equal')


plt.show()