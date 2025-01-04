from project import getting_data, analyzing_data, export_data
import os

def test_getting_data():
    global excluded_paths
    excluded_paths = None
    global test_path
    test_path = "D:\OneDrive\المستندات\My Vault"
    assert getting_data(test_path, excluded_paths) == f"{test_path}\\cleaned_data.txt"


def test_analyzing_data():
    completed, not_completed = analyzing_data(getting_data(test_path, excluded_paths))
    assert isinstance(completed, list)
    assert isinstance(not_completed, list)

def test_export_data():
    test_data = (["- [x] Task 1"], ["- [ ] Task 2"])
    export_data(test_data, test_path)
    assert os.path.exists(f"{test_path}\\analysis.txt")