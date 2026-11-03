from zlib import decompress
from pathlib import Path


def return_file_content(file_path):
    with open(file_path, "rb") as f:
        compressed_data = f.read()

    decompressed_bytes = decompress(compressed_data)

    file = decompressed_bytes.split(b"\0", 1)
    return file[1]
