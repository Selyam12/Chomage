"""Transcription locale horodatee de l'entretien France Travail du 23/09/2026."""

from pathlib import Path
import json

from faster_whisper import WhisperModel


source = Path(r"C:\Users\Marc\Videos\2026-09-23 10-36-43.mp4")
output = Path("suivi") / "2026-09-23_france-travail_transcription_raw.json"
output.parent.mkdir(exist_ok=True)

model = WhisperModel("base", device="cuda", compute_type="float16")
segments, info = model.transcribe(
    str(source),
    language="fr",
    beam_size=5,
    vad_filter=True,
    vad_parameters={"min_silence_duration_ms": 500},
    word_timestamps=True,
    condition_on_previous_text=True,
)

result = {
    "source": str(source),
    "language": info.language,
    "language_probability": info.language_probability,
    "segments": [
        {
            "start": round(segment.start, 3),
            "end": round(segment.end, 3),
            "text": segment.text.strip(),
            "words": [
                {
                    "start": round(word.start, 3),
                    "end": round(word.end, 3),
                    "word": word.word,
                }
                for word in (segment.words or [])
            ],
        }
        for segment in segments
    ],
}
output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {output}")
