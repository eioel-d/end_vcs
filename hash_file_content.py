from pathlib import Path
from hashlib import md5
from zlib import compress
import sys
from return_file_content import return_file_content


def hash_file_content(file_name):
    if not Path(file_name).exists() and Path(file_name).is_file():
        print(f"{file_name} not found")
        return
    file = Path(file_name).read_bytes()
    header = f"blob {len(file)}\0".encode("utf-8")
    data = header + file
    file = compress(data)
    hashed_content = md5(file).hexdigest()
    folder_name = hashed_content[:2]
    blob_name = hashed_content[2:]
    Path(folder_name).mkdir(exist_ok=True)
    blob_path = f"{folder_name}/{blob_name}"
    with open(blob_path, "wb") as f:
        f.write(file)
    print(f"File was created in {blob_path}")
    uncompressed = return_file_content(blob_path)

    current_dir = Path(__file__).resolve().parent
    write_path = f"{current_dir}/new.py"
    with open(write_path, "wb") as f:
        f.write(uncompressed)
    print(current_dir)


hash_file_content(sys.argv[1])
