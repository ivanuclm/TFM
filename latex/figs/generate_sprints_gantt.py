from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.dates as mdates
import matplotlib.pyplot as plt


@dataclass(frozen=True)
class Sprint:
    code: str
    label: str
    start: date
    end: date
    color: str


SPRINTS = [
    Sprint("Sprint 1", "OSRM remoto", date(2025, 12, 2), date(2025, 12, 5), "#3b82f6"),
    Sprint("Sprint 2", "OSRM local", date(2025, 12, 6), date(2025, 12, 11), "#2563eb"),
    Sprint("Sprint 3", "GTFS Toledo", date(2025, 12, 12), date(2025, 12, 18), "#0ea5e9"),
    Sprint("Sprint 4", "OTP multimodal", date(2025, 12, 19), date(2026, 2, 12), "#06b6d4"),
    Sprint("Sprint 5", "Diseño web", date(2025, 12, 20), date(2026, 2, 20), "#14b8a6"),
    Sprint("Sprint 6", "LPMC y datos", date(2025, 12, 21), date(2026, 1, 17), "#22c55e"),
    Sprint("Sprint 7", "Modelos y validación", date(2026, 1, 18), date(2026, 2, 21), "#84cc16"),
    Sprint("Sprint 8", "Memoria", date(2026, 1, 27), date(2026, 3, 24), "#f59e0b"),
    Sprint("Sprint 9", "Integración inferencia", date(2026, 2, 22), date(2026, 3, 8), "#f97316"),
]

OUTPUT = Path(__file__).with_name("sprints_timeline.png")


def build_chart() -> None:
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(16, 8.2), dpi=220)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("#f8fafc")

    ordered = list(reversed(SPRINTS))
    for row, sprint in enumerate(ordered):
        left = mdates.date2num(datetime.combine(sprint.start, datetime.min.time()))
        right = mdates.date2num(datetime.combine(sprint.end, datetime.min.time()))
        width = max(1.0, right - left)

        ax.barh(
            row,
            width,
            left=left,
            height=0.64,
            color=sprint.color,
            edgecolor="#0f172a",
            linewidth=0.8,
        )
        ax.text(
            left + 1.5,
            row,
            f"{sprint.code}  {sprint.label}",
            va="center",
            ha="left",
            fontsize=12.6,
            color="#0f172a",
            fontweight="bold",
        )

    min_start = min(s.start for s in SPRINTS)
    max_end = max(s.end for s in SPRINTS)

    ax.set_yticks([])
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    ax.xaxis.set_minor_locator(mdates.WeekdayLocator(interval=2))
    ax.tick_params(axis="x", labelsize=12)
    ax.grid(axis="x", which="major", linestyle="--", linewidth=0.8, color="#94a3b8", alpha=0.6)
    ax.grid(axis="x", which="minor", linestyle=":", linewidth=0.4, color="#cbd5e1", alpha=0.6)
    ax.set_xlim(
        mdates.date2num(datetime(min_start.year, min_start.month, 1)),
        mdates.date2num(datetime(max_end.year, max_end.month, max_end.day + 4)),
    )

    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color("#94a3b8")

    plt.tight_layout()
    plt.savefig(OUTPUT, bbox_inches="tight", pad_inches=0.08)


if __name__ == "__main__":
    build_chart()
