from pathlib import Path
import shutil

#Defining the default directory and subfolders

DIRECTORY = Path.home() / "Downloads"

SUBFOLDERS = {
    "Photos": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".tiff", ".tif", ".bmp", ".heic", ".raw"],
    "Videos": [".mp4", ".mov", ".mkv", ".avi", ".webm", ".flv", ".wmv", ".3gp", ".m4v"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf", ".html", ".htm", ".md", ".csv", ".json", ".xml", ".yaml", ".psd", ".ai", ".indd"],
    "Audio": [".mp3", ".wav", ".aac", ".m4a", ".ogg", ".flac", ".alac", ".aiff"]
}

#Defining the <organize()> funciton

def organize():

    #First we check wich folder the user wants to use the script on
    print("""The default directory is set to Downloads. If you want to change it it please provide the full directory, or press "Enter" to use the Downloads folder""")
    NEW_DIRECTORY = Path(input(""))
    if NEW_DIRECTORY:
        DIRECTORY = NEW_DIRECTORY


    #Now we make sure the directory exists so we can work with it and it doesnt raise an error in the Path Library and then we loop.
    if DIRECTORY.exists() and DIRECTORY.is_dir():
        for item in DIRECTORY.iterdir():
            if item.is_file():
                for folder, extensions in SUBFOLDERS.items():
                    if item.suffix.lower() in extensions:
                        destination = DIRECTORY / folder
                        destination.mkdir(exist_ok=True)
                        shutil.move(str(item), str(destination / item.name))
                        
                    else:
                        other = DIRECTORY / "Other"
                        other.mkdir(exist_ok=True)
                        shutil.move(str(item), str(other / item.name))
                    print(f"{item.name} has been moved to {folder}")
                    break
    else:
        print("Directory does not exist or is not a directory")




    

if __name__ == "__main__":
    organize()
