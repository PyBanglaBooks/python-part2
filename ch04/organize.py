from pathlib import Path

downloads = Path("downloads")
for file in sorted(downloads.iterdir()):
    if not file.is_file():
        continue
    if file.suffix == "":
        folder_name = "others"
    else:
        folder_name = file.suffix[1:]
    folder = downloads / folder_name
    folder.mkdir(exist_ok=True)
    file.rename(folder / file.name)
    print(f"{file.name} -> {folder_name}")
