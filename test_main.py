"""Test module for the main application."""

import zipfile
from io import BytesIO

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_zip_file_generation():
    """
    Test the ZIP file generation endpoint.

    This test ensures that:
    1. The endpoint returns a 200 status code.
    2. The response content is a valid ZIP file.
    3. The ZIP file contains the expected number of files with correct names.
    4. The ZIP file is not corrupted.
    """
    base_filename = "dummy"
    expected_filenames = [f"{base_filename}_{i}.txt" for i in range(1, 11)]

    response = client.get("/dummy")
    assert response.status_code == 200

    zip_content = BytesIO(response.content)
    assert zipfile.is_zipfile(zip_content)

    with zipfile.ZipFile(zip_content) as zip_archive:
        assert zip_archive.testzip() is None
        assert sorted(zip_archive.namelist()) == sorted(expected_filenames)
