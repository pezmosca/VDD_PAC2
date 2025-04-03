import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import ptitprince as pt


agenda_df = pd.read_csv("agenda.csv", low_memory=False)
agenda_df["Data"] = pd.to_datetime(agenda_df["Data"], errors="coerce", dayfirst=True)


agenda_2024 = agenda_df[
    (agenda_df["Data"].dt.year == 2024) &
    (agenda_df["Càrrec"].str.contains("President de la Generalitat", na=False))
].copy()


agenda_2024["month_num"] = agenda_2024["Data"].dt.month
agenda_2024 = agenda_2024.dropna(subset=["Activitat", "month_num"])

CATEGORIES = ["Reunió", "Acte"]
COLORS = ["#1f77b4", "#ff7f0e"]


fig, ax = plt.subplots(figsize=(8, 6))


pt.half_violinplot(
    x="Activitat", y="month_num", scale="area",
    palette=COLORS, inner=None, data=agenda_2024,
    width=0.8, ax=ax, order=CATEGORIES
)


RAIN_SHIFT = 0.15
for i, category in enumerate(CATEGORIES):
    data = agenda_2024[agenda_2024["Activitat"] == category]
    x = np.random.normal(loc=i + RAIN_SHIFT, scale=0.05, size=len(data))
    y = data["month_num"]
    ax.scatter(x, y, color=COLORS[i], alpha=0.6)


medianprops = {"linewidth": 1.5, "color": "black"}
boxprops = {"linewidth": 1.5, "color": "black"}

boxplot_data = [agenda_2024[agenda_2024["Activitat"] == cat]["month_num"] for cat in CATEGORIES]
box_positions = [i + RAIN_SHIFT / 2 for i in range(len(CATEGORIES))]

ax.boxplot(
    boxplot_data,
    positions=box_positions,
    widths=0.1,
    vert=True,
    patch_artist=False,
    medianprops=medianprops,
    whiskerprops=boxprops,
    boxprops=boxprops,
    showcaps=False,
    showfliers=False
)


month_names = ['Gen', 'Feb', 'Mar', 'Abr', 'Mai', 'Jun',
               'Jul', 'Ag', 'Sep', 'Oct', 'Nov', 'Dec']
ax.set_yticks(range(1, 13))
ax.set_yticklabels(month_names)

# Labels and title
ax.set_ylabel("Mes", fontsize=13)
ax.set_xticks([0, 1])
ax.set_xticklabels(CATEGORIES)
ax.set_xlabel("Tipus d'activitat", fontsize=13)
ax.set_title("Events del President de la Generalitat durant l'any 2024", fontsize=15)
ax.tick_params(labelsize=11)

plt.tight_layout()
plt.show()