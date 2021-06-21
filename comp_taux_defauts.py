import matplotlib.pyplot as plt
import tikzplotlib
import numpy as np
import matplotlib.ticker as mtick

# https://stackoverflow.com/questions/10369681/how-to-plot-bar-graphs-with-same-x-coordinates-side-by-side-dodged

ind = np.arange(2)

width = 0.3


plt.bar(ind,         [0.340, 0.525],  width, label="Pores"               , alpha=0.9)
plt.bar(ind + width, [0.252, 0.041], width, label="Agrégats eutectiques", alpha=0.9)


plt.xticks(ind + width / 2, ["Brut", "Remis en solution"])
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())

plt.xlabel("Étape de traitement thermique de l'échantillon")
plt.ylabel('Proportion surfacique du type de défaut')
# plt.title('Évolution des défauts dans les échantillons\nselon les traitements thermiques appliqués')

plt.tight_layout()
plt.legend()
# plt.show()

tikzplotlib.save("sections/proportions_defauts.tex")
