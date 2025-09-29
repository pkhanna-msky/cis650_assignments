import os

def list_files(folder: str) -> list[str]:
    """Return a list of regular files (not folders) in `folder`."""
    try:
        entries = []
        for name in os.listdir(folder):
            path = os.path.join(folder, name)
            if os.path.isfile(path):
                entries.append(name)
        return sorted(entries)
    except PermissionError:
        print("Error: Permission denied when listing that folder.")
        return []
    except FileNotFoundError:
        print("Error: Folder not found (it may have been moved or deleted).")
        return []
    except OSError as e:
        print(f"Error reading folder: {e}")
        return []

def pick_file(files: list[str]) -> str | None:
    """Let the user pick by number or exact filename (case-insensitive match allowed)."""
    if not files:
        return None

    print("\nFiles:")
    for i, name in enumerate(files, 1):
        print(f"  {i}. {name}")

    choice = input("\nEnter the number OR exact file name to rename (or just Enter to cancel): ").strip()
    if not choice:
        print("Canceled.")
        return None

    if choice.isdigit():
        idx = int(choice)
        if 1 <= idx <= len(files):
            return files[idx - 1]
        print("Invalid number.")
        return None

    lower_map = {f.lower(): f for f in files}
    return lower_map.get(choice.lower())

def main() -> None:
    folder = input("Enter folder path: ").strip()
    if not folder:
        print("No folder provided.")
        return

    folder = os.path.abspath(os.path.expanduser(folder))

    if not os.path.isdir(folder):
        print("That path is not a folder or does not exist.")
        return

    files = list_files(folder)
    if not files:
        print("No regular files found in this folder.")
        return

    old_name = pick_file(files)
    if not old_name:
        return

    new_name = input("Enter new file name (with extension): ").strip()
    if not new_name:
        print("New name cannot be empty.")
        return

    old_path = os.path.join(folder, old_name)
    new_path = os.path.join(folder, new_name)

    if os.path.abspath(old_path) == os.path.abspath(new_path):
        print("Old and new names are the same. Nothing to do.")
        return

    if os.path.exists(new_path):
        print("A file with that new name already exists. Choose a different name.")
        return

    try:
        os.rename(old_path, new_path)
        print(f"Renamed '{old_name}' → '{new_name}' successfully.")
    except FileNotFoundError:
        print("The selected file no longer exists.")
    except PermissionError:
        print("Permission denied while renaming (file may be in use).")
    except OSError as e:
        print(f"OS error while renaming: {e}")

if __name__ == "__main__":
    main() 