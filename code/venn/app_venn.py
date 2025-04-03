import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
from matplotlib_venn._venn3 import DefaultLayoutAlgorithm


def load_data():
    flora_path = "normativa.csv"
    return pd.read_csv(flora_path)

flora_df = load_data()


europea = set(flora_df[flora_df["Protecció europea"] != "No inclosa"]["Nom científic"])
estatal = set(flora_df[flora_df["Protecció estatal"] != "No inclosa"]["Nom científic"])
catalana = set(flora_df[flora_df["Protecció catalana"] != "No inclosa"]["Nom científic"])


fig2, ax2 = plt.subplots(figsize=(8, 6))
venn3([europea, estatal, catalana],
      set_labels=('Protecció europea', 'Protecció estatal', 'Protecció catalana'),
      set_colors=('#1f77b4', '#ff7f0e', '#2ca02c'),
      ax=ax2,
      layout_algorithm=DefaultLayoutAlgorithm(fixed_subset_sizes=(1, 1, 1, 1, 1, 1, 1)))
ax2.set_title("Intersecció de les diferents proteccions d'espècies")


plt.show()