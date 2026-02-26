from pathlib import Path
import shutil

#Defining the default directory and subfolders

DIRECTORY = Path.home() / "Downloads"

#This is the test directory (only for development stage)
DIRECTORY = Path(r"C:\Users\mayke\OneDrive\Documents\Testing Directory")

SUBFOLDERS = {
    "Photos": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".tiff", ".tif", ".bmp", ".heic", ".raw"],
    "Videos": [".mp4", ".mov", ".mkv", ".avi", ".webm", ".flv", ".wmv", ".3gp", ".m4v"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf", ".html", ".htm", ".md", ".csv", ".json", ".xml", ".yaml", ".psd", ".ai", ".indd"],
    "Audio": [".mp3", ".wav", ".aac", ".m4a", ".ogg", ".flac", ".alac", ".aiff"]
}


#Defining the <pick_directory()> funciton
def pick_directory() -> Path:
    print(
        'Default directory is Downloads.\n'
        'To change it, paste the full path, or press Enter to use Downloads.'
    )
    user_input = input("> ").strip()

    if user_input:
        return Path(user_input)
    global DIRECTORY
    return DIRECTORY


#Defining the <organize()> funciton
def organize() -> None:

    #Picking up the directory to organize
    directory = pick_directory()

    #Now we make sure the directory exists so we can work with it and it doesnt raise an error in the Path Library and then we loop.
    if directory.exists() and directory.is_dir():
        items = directory.iterdir()
        for item in items:
            if item.is_file():
                for folder, extensions in SUBFOLDERS.items():
                    print(f"Current folder is{folder} and current extensions are {extensions}")
                    if item.suffix.lower() in extensions:
                        print(f"Item suffix is{item.suffix.lower()} and is in {extensions}")
                        destination = directory / folder
                        destination.mkdir(exist_ok=True)
                        try:
                            shutil.move(str(item), str(destination / item.name))
                            print(f"{item.name} has been moved to {folder}")
                        except FileNotFoundError:
                            print(f"The file {item.name} was not found in {directory}")


        #Now we iterate to retreive the files that are not included in our dictionary and send them to "Other"
        items = directory.iterdir() #Updating the variable to hold the rest of the files
        for item in items:
            if item.is_file():
                destination = directory / "Other"
                destination.mkdir(exist_ok=True)
                try:
                    shutil.move(str(item), str(destination / item.name))
                    print(f"{item.name} has been moved to Other")
                except FileNotFoundError:
                    print(f"The file {item.name} was not found in {directory}")        

                    
    else:
        print("Directory does not exist or is not a directory")




    

if __name__ == "__main__":
    organize()
