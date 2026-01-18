import os
import shutil

# --- CONFIGURATION ---
# TARGET_FOLDER: The folder name you want to organize. 
# It must be in the same directory as this script.
TARGET_FOLDER = "example"
# PRO TIP: Uncomment the line below to sort your real Downloads folder!
# TARGET_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")

# Define file types and their extensions
EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".heic"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv", ".md"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".bat", ".sh", ".apk", ".iso"]
}

def create_folders():
    for folder_name in EXTENSIONS.keys():
        folder_path = os.path.join(TARGET_FOLDER, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    others_path = os.path.join(TARGET_FOLDER, "Others")
    if not os.path.exists(others_path):
        os.makedirs(others_path)

def sort_files():
    if not os.path.exists(TARGET_FOLDER):
        print(f"[ERROR] Folder not found: {TARGET_FOLDER}")
        return

    files = os.listdir(TARGET_FOLDER)
    moved_count = 0

    print(f"--- TAYRONUK FILE SORTER STARTED ---")
    print(f"Target: {TARGET_FOLDER}")

    for filename in files:
        file_path = os.path.join(TARGET_FOLDER, filename)

        if os.path.isdir(file_path):
            continue
        
        if filename == "main.py":
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for folder_name, extensions in EXTENSIONS.items():
            if file_ext in extensions:
                destination = os.path.join(TARGET_FOLDER, folder_name, filename)
                shutil.move(file_path, destination)
                print(f"[MOVED] {filename} -> {folder_name}/")
                moved = True
                moved_count += 1
                break
        
        if not moved:
            destination = os.path.join(TARGET_FOLDER, "Others", filename)
            shutil.move(file_path, destination)
            print(f"[OTHER] {filename} -> Others/")
            moved_count += 1

    print(f"--- COMPLETED ---")
    print(f"Total Files Moved: {moved_count}")

if __name__ == "__main__":
    create_folders()
    sort_files()