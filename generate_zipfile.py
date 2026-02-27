import zipfile
from pathlib import Path


def create_zip(output_name: str = "miraita-resources.zip") -> Path:
    root = Path(__file__).resolve().parent
    output_path = root / output_name
    
    excluded_dirs = {".github", ".git"}
    excluded_files = {Path(__file__).name}

    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in root.rglob("*"):
            if path == output_path:
                continue
            if any(part in excluded_dirs for part in path.parts):
                continue
            if path.name in excluded_files:
                continue
            if path.is_dir():
                continue

            zf.write(path, path.relative_to(root))

    return output_path


if __name__ == "__main__":
    zip_path = create_zip()
    print(f"Created: {zip_path}")
