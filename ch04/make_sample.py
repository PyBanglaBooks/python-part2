from pathlib import Path

downloads = Path("downloads")
downloads.mkdir(exist_ok=True)
names = ["result.pdf", "photo1.jpg", "photo2.jpg", "song.mp3",
         "notes.txt", "routine.pdf", "readme"]
for name in names:
    (downloads / name).touch()
print(f"{len(names)} files created in {downloads}")
