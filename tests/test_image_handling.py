import pytest
import os
import io
from fastapi import UploadFile
from app.utils.image_handling import ImageHandler

@pytest.mark.asyncio
def test_image_upload():
    assert ImageHandler.upload_file("tests/testing_files/BlankAvatar.png", "test_image.png")

@pytest.mark.asyncio
def test_tmp_image_delete():
    with open(f"tmp/test.png", "wb") as f:
        f.write(b"test")
        f.close;
    assert ImageHandler.delete_temp_file("test.png")
    
