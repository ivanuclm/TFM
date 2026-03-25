# -*- coding: utf-8 -*-
from __future__ import annotations

from math import cos, pi, sin
from pathlib import Path as FilePath

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch
from matplotlib.path import Path as MplPath


OUTPUT = FilePath(__file__).with_name("scrum_tfm_cycle.png")


BOXES = [
    {
        "label": "Product\nBacklog",
        "angle_deg": 90,
        "facecolor": "#dbe7ff",
        "width": 1.9,
        "height": 0.92,
    },
    {
        "label": "Planificación\ndel sprint",
        "angle_deg": 18,
        "facecolor": "#e6f4dd",
        "width": 2.05,
        "height": 0.92,
    },
    {
        "label": "Desarrollo\ne integración",
        "angle_deg": -54,
        "facecolor": "#fff2bf",
        "width": 2.05,
        "height": 0.92,
    },
    {
        "label": "Revisión\ncon tutor",
        "angle_deg": -126,
        "facecolor": "#f4d7dc",
        "width": 1.95,
        "height": 0.92,
    },
    {
        "label": "Ajuste de backlog\ny prioridades",
        "angle_deg": 162,
        "facecolor": "#eadbfb",
        "width": 2.2,
        "height": 0.92,
    },
]


def polar(radius: float, angle_deg: float) -> tuple[float, float]:
    angle = pi * angle_deg / 180.0
    return radius * cos(angle), radius * sin(angle)


def point_in_box(x: float, y: float, cx: float, cy: float, width: float, height: float, pad: float = 0.08) -> bool:
    return (cx - width / 2 - pad) <= x <= (cx + width / 2 + pad) and (cy - height / 2 - pad) <= y <= (cy + height / 2 + pad)


def box_angle_span(radius: float, center_angle_deg: float, cx: float, cy: float, width: float, height: float) -> tuple[float, float]:
    hits: list[float] = []
    for offset in range(-90, 91):
        angle = center_angle_deg + offset * 0.5
        x, y = polar(radius, angle)
        if point_in_box(x, y, cx, cy, width, height):
            hits.append(angle)
    if not hits:
        return center_angle_deg - 8, center_angle_deg + 8
    return min(hits), max(hits)


def arc_path(radius: float, start_deg: float, end_deg: float, steps: int = 40) -> MplPath:
    while end_deg > start_deg:
        end_deg -= 360
    angles = [start_deg + (end_deg - start_deg) * i / (steps - 1) for i in range(steps)]
    points = []
    codes = []
    for idx, angle_deg in enumerate(angles):
        x, y = polar(radius, angle_deg)
        points.append((x, y))
        codes.append(MplPath.MOVETO if idx == 0 else MplPath.LINETO)
    return MplPath(points, codes)


def draw() -> None:
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(8.4, 8.4), dpi=220)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    cycle_radius = 2.7
    box_radius = 2.7

    ax.add_patch(
        Circle(
            (0, 0),
            cycle_radius,
            facecolor="none",
            edgecolor="#d6dbe7",
            linewidth=1.2,
            linestyle="--",
            alpha=0.9,
        )
    )

    centers: list[tuple[float, float, float, float, float, float, float]] = []
    for spec in BOXES:
        x, y = polar(box_radius, spec["angle_deg"])
        w = spec["width"]
        h = spec["height"]
        span_min, span_max = box_angle_span(cycle_radius, spec["angle_deg"], x, y, w, h)
        centers.append((x, y, w, h, spec["angle_deg"], span_min, span_max))

        rect = FancyBboxPatch(
            (x - w / 2, y - h / 2),
            w,
            h,
            boxstyle="round,pad=0.04,rounding_size=0.08",
            linewidth=1.1,
            edgecolor="#5b6472",
            facecolor=spec["facecolor"],
        )
        ax.add_patch(rect)
        ax.text(x, y, spec["label"], ha="center", va="center", fontsize=10.6, color="#1f2937")

    for idx, (_x1, _y1, _w1, _h1, _a1, span1_min, span1_max) in enumerate(centers):
        _x2, _y2, _w2, _h2, _a2, span2_min, span2_max = centers[(idx + 1) % len(centers)]
        start_deg = span1_min
        end_deg = span2_max
        path = arc_path(cycle_radius, start_deg, end_deg)
        arrow = FancyArrowPatch(
            path=path,
            arrowstyle="-|>",
            mutation_scale=11,
            linewidth=1.5,
            color="#5f6368",
            fill=False,
        )
        ax.add_patch(arrow)

    ax.text(
        0,
        -4.25,
        "SCRUM adaptado a desarrollo unipersonal",
        ha="center",
        va="center",
        fontsize=11.2,
        color="#4b5563",
    )

    ax.set_xlim(-4.25, 4.25)
    ax.set_ylim(-4.45, 4.15)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.tight_layout()
    plt.savefig(OUTPUT, bbox_inches="tight", pad_inches=0.08)


if __name__ == "__main__":
    draw()
