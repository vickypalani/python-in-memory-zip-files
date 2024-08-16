"""Main FastAPI application for exporting user data."""

import zipfile
from io import BytesIO

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


def generate_text_file(filename: str) -> BytesIO:
    """
    Generate a text file with 'Hello World' content.

    Args:
        filename (str): The name of the file to be created.

    Returns:
        BytesIO: An in-memory file object containing the generated text.
    """
    file_content = BytesIO()
    file_content.write(b"Hello World")
    file_content.name = f"{filename}.txt"
    return file_content


@app.get("/{username}")
def export_user_data(username: str):
    """
    Export user data as a zip file.

    Args:
        username (str): The username for which to export data.

    Returns:
        StreamingResponse: A response containing the zip file for download.
    """
    text_files = [generate_text_file(filename=f"{username}_{i}") for i in range(1, 11)]
    zip_buffer = BytesIO()
    with zipfile.ZipFile(
        file=zip_buffer,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as zip_archive:
        for text_file in text_files:
            zip_archive.writestr(zinfo_or_arcname=text_file.name, data=text_file.getvalue())

    zip_buffer.seek(0)

    return StreamingResponse(
        zip_buffer,
        media_type="application/zip",
        headers={"Content-Disposition": f"attachment; filename={username}.zip"},
    )
