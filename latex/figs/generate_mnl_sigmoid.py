"""
Genera la figura mnl_sigmoid.png para la memoria del TFM.
Ilustra la forma sigmoidal de la probabilidad de elección en el modelo MNL
(caso binario con la alternativa de referencia normalizada a V_jn = 0).

Ejecutar desde este directorio:
    python generate_mnl_sigmoid.py
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 6, 400)
P = 1 / (1 + np.exp(-x))

fig, ax = plt.subplots(figsize=(7, 4.5))

ax.plot(x, P, color='#2563eb', linewidth=3.5)

ax.axhline(0.5, color='#9ca3af', linewidth=1.5, linestyle='--')
ax.axvline(0, color='#9ca3af', linewidth=1.5, linestyle='--')

ax.set_xlabel(r'Utilidad sistemática $V_{in}$', fontsize=15)
ax.set_ylabel(r'$P_{in}$ (probabilidad de elección)', fontsize=15)
ax.tick_params(labelsize=13)

ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
ax.set_yticklabels(['0', '0.25', '0.5', '0.75', '1'], fontsize=13)
ax.set_ylim(-0.04, 1.04)
ax.set_xlim(-6, 6)

ax.annotate('Zona de mayor\nsensibilidad', xy=(0, 0.5), xytext=(1.5, 0.3),
            fontsize=12, color='#374151',
            arrowprops=dict(arrowstyle='->', color='#6b7280', lw=1.5))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)

plt.tight_layout()
plt.savefig('mnl_sigmoid.png', dpi=220, bbox_inches='tight', facecolor='white')
print('Guardado: mnl_sigmoid.png')
