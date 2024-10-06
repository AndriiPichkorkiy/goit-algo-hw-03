from pathlib import Path
import shutil


def recursion_copy(src: Path, destination="dict") -> None:
    try:
        # run recursion when the path is directory
        if src.is_dir():
            for child in src.iterdir():
                recursion_copy(child, destination)
            return

        # get extension for create related directory
        extension = src.suffix[1::]
        folder_path = Path(destination, extension)

        try:
            folder_path.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"Error while creating directory {folder_path}: {e}")
            return

        # solve name duplication
        path_to_copy = Path(folder_path, src.name)
        if path_to_copy.exists():
            path_to_copy = Path(folder_path, src.stem + "_copy." + extension)

        try:
            shutil.copy(src, path_to_copy)
        except PermissionError:
            print(f"Permission error {src}. Pass copying.")
        except Exception as e:
            print(f"Error while copying file{src}: {e}")

    except PermissionError:
        print(f"Permission error {src}. Pass copying.")
    except Exception as e:
        print(f"Error while copying file{src}: {e}")


if __name__ == "__main__":
    root = Path("pictures")
    recursion_copy(root, "other folder")
