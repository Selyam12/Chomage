"""Formate la transcription brute France Travail en Markdown horodate."""

from pathlib import Path
import json


raw = Path("suivi") / "2026-09-23_france-travail_transcription_raw.json"
out = Path("suivi") / "2026-09-23_appel-france-travail_transcription.md"
data = json.loads(raw.read_text(encoding="utf-8"))


def stamp(seconds: float) -> str:
    seconds = int(seconds)
    return f"{seconds // 3600:02}:{(seconds % 3600) // 60:02}:{seconds % 60:02}"


groups = []
for segment in data["segments"]:
    if (
        not groups
        or segment["start"] - groups[-1]["end"] > 1.5
        or segment["end"] - groups[-1]["start"] > 40
    ):
        groups.append({"start": segment["start"], "end": segment["end"], "text": [segment["text"]]})
    else:
        groups[-1]["end"] = segment["end"]
        groups[-1]["text"].append(segment["text"])

lines = [
    "# Transcription - appel France Travail - 23 septembre 2026",
    "",
    "Source : `C:\\Users\\Marc\\Videos\\2026-09-23 10-36-43.mp4`  ",
    "Durée : 3 min 46 s  ",
    "Langue : français  ",
    "",
    "Transcription automatique locale (Whisper base), sans identification certaine des locuteurs. Les horodatages permettent de vérifier chaque passage dans l'enregistrement ; les noms propres et formulations administratives incertains doivent être contrôlés à l'écoute avant tout usage externe.",
    "",
    "## Transcription",
    "",
]

for group in groups:
    lines.append(f"**[{stamp(group['start'])}-{stamp(group['end'])}]** {' '.join(group['text'])}")
    lines.append("")

out.write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote {out}")
