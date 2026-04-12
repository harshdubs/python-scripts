from pathlib import Path
import shutil

# Step 1: Define the mapping of extensions -> folder names
EXTENSION_MAP = {
    # Images
    '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images', '.webp': 'Images',
    # Documents
    '.pdf': 'PDFs',
    '.doc': 'Documents', '.docx': 'Documents', '.txt': 'Documents', '.md': 'Documents',
    # Spreadsheets
    '.xlsx': 'Spreadsheets', '.xls': 'Spreadsheets', '.csv': 'Spreadsheets',
    # Code
    '.py': 'Code', '.js': 'Code', '.html': 'Code', '.css': 'Code', '.json': 'Code',
    # Archives
    '.zip': 'Archives', '.rar': 'Archives', '.7z': 'Archives', '.tar': 'Archives',
    # Videos
    '.mp4': 'Videos', '.mkv': 'Videos', '.mov': 'Videos',
    # Audio
    '.mp3': 'Audio', '.wav': 'Audio',
}

def organize_folder(folder_path):
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Folder not found: {folder}")
        return
    
    moved_count = 0
    
    # Step 2: Loop through every file in the folder
    for item in folder.iterdir():
        # Skip directories, only process files
        if item.is_dir():
            continue
        
        # Step 3: Get the file extension (lowercase for consistency)
        ext = item.suffix.lower()
        
        # Step 4: Look up the target folder, default to 'Other'
        target_folder_name = EXTENSION_MAP.get(ext, 'Other')
        
        # Step 5: Create the target folder if it doesn't exist
        target_folder = folder / target_folder_name
        target_folder.mkdir(exist_ok=True)
        
        # Step 6: Move the file
        destination = target_folder / item.name
        shutil.move(str(item), str(destination))
        print(f"Moved: {item.name} -> {target_folder_name}/")
        moved_count += 1
    
    print(f"\nDone. Organized {moved_count} files.")

if __name__ == "__main__":
    # CHANGE THIS to your actual Downloads path
    organize_folder(r"C:\Users\harsh\Test")