"""Create a sample zip file in Python at runtime."""

import zipfile


def create_sample_zip_file():
    """
    Create a zip file containing text files at runtime.

    This function creates a zip file named 'texts.zip' and adds two text files
    ('text1.txt' and 'text2.txt') to it using ZIP_DEFLATED compression method.
    """

    with zipfile.ZipFile(
        file="texts.zip", mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as zip_archive:
        zip_archive.write(filename="text1.txt")
        zip_archive.write(filename="text2.txt")

    print("Zip file created successfully.")


if __name__ == "__main__":
    create_sample_zip_file()
