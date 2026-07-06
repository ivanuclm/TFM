# -*- coding: utf-8 -*-
"""
Gantt de sprints del TFM -- 15 filas (Fase inicial + S1-S14), nov 2025 -- jul 2026.
Nombres de sprint en el eje Y (no dentro de las barras) para maximizar legibilidad
cuando la figura se escala a textwidth en el PDF final.
Exporta sprints_timeline.pdf (vectorial) y sprints_timeline.png (220 dpi).
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")

import matplotlib.dates as mdates
import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.ticker
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path


# -- Fuente ------------------------------------------------------------------
def _setup_font() -> None:
    available = {f.name for f in fm.fontManager.ttflist}
    for name in ("Calibri", "Arial", "Helvetica Neue", "DejaVu Sans"):
        if name in available:
            matplotlib.rcParams.update({
                "font.family": "sans-serif",
                "font.sans-serif": [name],
            })
            return


# -- Paleta ------------------------------------------------------------------
COLORS = {
    "planificacion": "#9AA0A6",   # gris
    "infra":         "#1A73E8",   # azul
    "ml":            "#188038",   # verde
    "memoria":       "#E37400",   # naranja
    "consolidacion": "#00897B",   # teal
}

LEGEND_LABELS = {
    "planificacion": "Fase inicial de planificación",
    "infra":         "Infraestructura y servicios",
    "ml":            "Machine Learning e IA",
    "memoria":       "Memoria (transversal)",
    "consolidacion": "Consolidación y entrega",
}

ES_MES = {
    1: "Ene", 2: "Feb", 3: "Mar", 4: "Abr",
    5: "May", 6: "Jun", 7: "Jul", 8: "Ago",
    9: "Sep", 10: "Oct", 11: "Nov", 12: "Dic",
}


# -- Datos -------------------------------------------------------------------
@dataclass(frozen=True)
class Sprint:
    num: int
    label: str      # texto abreviado para el eje Y
    start: date
    end: date
    group: str


SPRINTS: list[Sprint] = [
    Sprint( 0, "Fase inicial",       date(2025, 11,  6), date(2025, 12,  3), "planificacion"),
    Sprint( 1, "OSRM remoto",        date(2025, 12,  4), date(2025, 12,  9), "infra"),
    Sprint( 2, "OSRM local",         date(2025, 12,  4), date(2025, 12, 10), "infra"),
    Sprint( 3, "GTFS Toledo",        date(2025, 12, 11), date(2025, 12, 14), "infra"),
    Sprint( 4, "OTP multimodal",     date(2025, 12, 11), date(2026,  2, 12), "infra"),
    Sprint( 5, "Diseño web",       date(2025, 12, 11), date(2026,  2, 20), "infra"),
    Sprint( 6, "LPMC y datos",         date(2025, 12, 21), date(2026,  1, 17), "ml"),
    Sprint( 7, "Entrenamiento ML",     date(2026,  1, 18), date(2026,  2, 21), "ml"),
    Sprint( 8, "Memoria",              date(2026,  1, 27), date(2026,  6, 23), "memoria"),
    Sprint( 9, "Integración ML",  date(2026,  2, 21), date(2026,  3,  8), "ml"),
    Sprint(10, "Arquitectura",         date(2026,  3, 17), date(2026,  4, 15), "consolidacion"),
    Sprint(11, "RF + DNN",             date(2026,  4, 28), date(2026,  5,  6), "ml"),
    Sprint(12, "Cap. 5 + UI",          date(2026,  5, 19), date(2026,  6, 10), "consolidacion"),
    Sprint(13, "Consolidación",   date(2026,  6, 11), date(2026,  6, 25), "consolidacion"),
    Sprint(14, "Pulido final",       date(2026,  6, 28), date(2026,  7,  6), "consolidacion"),
]

HERE    = Path(__file__).parent
OUT_PDF = HERE / "sprints_timeline.pdf"
OUT_PNG = HERE / "sprints_timeline.png"

DATE_START = date(2025, 11, 1)
DATE_END   = date(2026, 7, 14)


def _num(d: date) -> float:
    return mdates.date2num(datetime(d.year, d.month, d.day))


def _ytick(sp: Sprint) -> str:
    """Etiqueta del eje Y: 'S1  OSRM remoto' o 'Fase inicial' para S0."""
    if sp.num == 0:
        return "Fase inicial"
    return f"S{sp.num:<2}  {sp.label}"


# -- Construccion del grafico ------------------------------------------------
def build() -> None:
    _setup_font()

    n = len(SPRINTS)   # 15
    ROW_H  = 0.62
    FIG_W  = 10        # ancho reducido: escalado en LaTeX ~0.61 → fuentes 16pt → ~10pt final
    FIG_H  = 12

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    # Amplio margen izquierdo para las etiquetas del eje Y (nombres de sprint)
    plt.subplots_adjust(left=0.30, right=0.99, top=0.97, bottom=0.07)

    # -- Franjas zebra de fondo
    x0 = _num(DATE_START)
    x1 = _num(DATE_END)
    for i in range(n):
        if i % 2 == 0:
            ax.fill_betweenx(
                [i - 0.5, i + 0.5], x0, x1,
                color="#F8F9FA", zorder=0,
            )

    # -- Barras (sin texto dentro; los nombres van en el eje Y)
    for idx, sp in enumerate(SPRINTS):
        row   = n - 1 - idx        # S0 arriba (fila 14), S14 abajo (fila 0)
        left  = _num(sp.start)
        right = _num(sp.end)
        width = max(10.0, right - left)   # minimo 10 dias para visibilidad
        color = COLORS[sp.group]

        ax.barh(
            row, width, left=left,
            height=ROW_H,
            color=color,
            edgecolor="white",
            linewidth=0.8,
            zorder=2,
        )

    # -- Eje Y: sprint ID + nombre
    ytick_labels = [_ytick(SPRINTS[n - 1 - i]) for i in range(n)]
    ax.set_yticks(range(n))
    ax.set_yticklabels(
        ytick_labels,
        fontsize=16, fontweight="bold", color="#202124",
    )
    ax.tick_params(axis="y", left=False, pad=5)

    # -- Eje X: gridlines mensuales, labels cada 2 meses
    ax.set_xlim(_num(DATE_START), _num(DATE_END))
    ax.set_ylim(-0.6, n - 0.4)

    ax.xaxis.set_major_locator(mdates.MonthLocator())

    def _fmt_mes(x, _pos=None) -> str:
        dt = mdates.num2date(x)
        m, y = dt.month, dt.year
        if m not in (11, 1, 3, 5, 7):
            return ""
        name = ES_MES[m]
        if y == 2025 or (y == 2026 and m == 1) or (y == 2026 and m == 7):
            return f"{name}\n{y}"
        return name

    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(_fmt_mes))
    ax.tick_params(axis="x", labelsize=14, colors="#5F6368", pad=4)

    ax.grid(
        axis="x", which="major",
        linestyle="--", linewidth=0.65,
        color="#DADCE0", alpha=0.9, zorder=1,
    )

    # -- Bordes
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color("#DADCE0")
    ax.spines["bottom"].set_linewidth(0.8)

    # -- Leyenda
    patches = [
        mpatches.Patch(color=COLORS[g], label=LEGEND_LABELS[g])
        for g in ("planificacion", "infra", "ml", "memoria", "consolidacion")
    ]
    ax.legend(
        handles=patches,
        loc="upper right",
        ncol=1,
        fontsize=12,
        frameon=True,
        framealpha=0.97,
        edgecolor="#DADCE0",
        handlelength=1.4,
        handleheight=1.0,
    )

    fig.savefig(OUT_PDF, bbox_inches="tight", pad_inches=0.06)
    fig.savefig(OUT_PNG, dpi=220, bbox_inches="tight", pad_inches=0.06)
    print("OK: " + str(OUT_PDF))
    print("OK: " + str(OUT_PNG))


if __name__ == "__main__":
    build()
