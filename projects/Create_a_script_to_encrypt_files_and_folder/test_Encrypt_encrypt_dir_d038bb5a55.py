import os
import pytest
from unittest.mock import patch
import encrypt

def test_traverse_all_files(mocker):
    with patch('os.walk') as mock_walk:
        mock_walk.return_value = [
            ('root', ['dir1'], ['file1', 'file2']),
            ('root/dir1', [], ['file3'])
        ]
        with patch('encrypt.encrypt_file') as mock_encrypt_file:
            encrypt.encrypt_dir('root')
            calls = [mocker.call('root/file1'), mocker.call('root/file2'), mocker.call('root/dir1/file3')]
            mock_encrypt_file.assert_has_calls(calls)

def test_empty_directory(mocker):
    with patch('os.walk') as mock_walk:
        mock_walk.return_value = []
        with patch('encrypt.encrypt_file') as mock_encrypt_file:
            encrypt.encrypt_dir('empty_dir')
            mock_encrypt_file.assert_not_called()

def test_directory_no_files(mocker):
    with patch('os.walk') as mock_walk:
        mock_walk.return_value = [('root', ['dir1'], [])]
        with patch('encrypt.encrypt_file') as mock_encrypt_file:
            encrypt.encrypt_dir('root')
            mock_encrypt_file.assert_not_called()

def test_directory_hidden_files(mocker):
    with patch('os.walk') as mock_walk:
        mock_walk.return_value = [('root', [], ['.hidden_file'])]
        with patch('encrypt.encrypt_file') as mock_encrypt_file:
            encrypt.encrypt_dir('root')
            mock_encrypt_file.assert_called_once_with('root/.hidden_file')

def test_directory_no_permission_files(mocker):
    with patch('os.walk') as mock_walk:
        mock_walk.return_value = [('root', [], ['no_permission_file'])]
        with patch('encrypt.encrypt_file') as mock_encrypt_file:
            mock_encrypt_file.side_effect = PermissionError
            with pytest.raises(PermissionError):
                encrypt.encrypt_dir('root')
