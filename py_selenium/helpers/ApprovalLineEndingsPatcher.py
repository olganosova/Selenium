# patch the approval tests library so that it ignore line endings (windows/unix)
from os import path

from approvaltests import FileApprover

from py_selenium.helpers.file_helpers import compare_files


def are_files_the_same(approved_file, received_file):
    if not path.isfile(approved_file) or not path.isfile(received_file):
        return False

    return compare_files(approved_file, received_file)


def patch_approval_library_to_ignore_line_endings():
    """
    The approval tests library compares files including line endings.
    In order to be able to run this on Linux without worrying about line ending differences
    patch the approval tests library with own comparison.
    """
    setattr(FileApprover, 'are_files_the_same', staticmethod(are_files_the_same))
