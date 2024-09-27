import pytest
from unittest.mock import patch
import os
import encrypt

DIR_PATH = "path/to/directory"
EMPTY_DIR_PATH = "path/to/empty/directory"
NON_EXISTENT_DIR_PATH = "path/to/non/existent/directory"
FILE_PATH = "path/to/file"
LARGE_DIR_PATH = "path/to/large/directory"
DIFF_PERMISSIONS_DIR_PATH = "path/to/diff/permissions/directory"
SPECIAL_CHAR_DIR_PATH = "path/to/special/char/directory"

def test_encrypt_dir_correct_traversal():
    with patch('encrypt.encrypt_file') as mock_encrypt_file:
        encrypt.encrypt_dir(DIR_PATH)
        assert mock_encrypt_file.call_count == len([name for name in os.listdir(DIR_PATH) if os.path.isfile(os.path.join(DIR_PATH, name))])

def test_encrypt_dir_encrypts_all_files():
    with patch('encrypt.encrypt_file') as mock_encrypt_file:
        encrypt.encrypt_dir(DIR_PATH)
        assert mock_encrypt_file.call_count == len([name for name in os.listdir(DIR_PATH) if os.path.isfile(os.path.join(DIR_PATH, name))])

def test_encrypt_dir_encrypts_all_files_in_subdirectories():
    with patch('encrypt.encrypt_file') as mock_encrypt_file:
        encrypt.encrypt_dir(DIR_PATH)
        assert mock_encrypt_file.call_count == sum([len(files) for r, d, files in os.walk(DIR_PATH)])

def test_encrypt_dir_handles_empty_directory():
    with patch('encrypt.encrypt_file') as mock_encrypt_file:
        encrypt.encrypt_dir(EMPTY_DIR_PATH)
        assert mock_encrypt_file.call_count == 0

def test_encrypt_dir_handles_non_existent_directory():
    with pytest.raises(FileNotFoundError):
        encrypt.encrypt_dir(NON_EXISTENT_DIR_PATH)

def test_encrypt_dir_handles_large_directories():
    with patch('encrypt.encrypt_file') as mock_encrypt_file:
        encrypt.encrypt_dir(LARGE_DIR_PATH)
        assert mock_encrypt_file.call_count == sum([len(files) for r, d, files in os.walk(LARGE_DIR_PATH)])

def test_encrypt_dir_handles_files_with_diff_permissions():
    with patch('encrypt.encrypt_file') as mock_encrypt_file:
        encrypt.encrypt_dir(DIFF_PERMISSIONS_DIR_PATH)
        assert mock_encrypt_file.call_count == sum([len(files) for r, d, files in os.walk(DIFF_PERMISSIONS_DIR_PATH)])

def test_encrypt_dir_handles_files_with_special_chars():
    with patch('encrypt.encrypt_file') as mock_encrypt_file:
        encrypt.encrypt_dir(SPECIAL_CHAR_DIR_PATH)
        assert mock_encrypt_file.call_count == len([name for name in os.listdir(SPECIAL_CHAR_DIR_PATH) if os.path.isfile(os.path.join(SPECIAL_CHAR_DIR_PATH, name))])

def test_encrypt_dir_handles_file_path_instead_of_directory():
    with pytest.raises(NotADirectoryError):
        encrypt.encrypt_dir(FILE_PATH)
