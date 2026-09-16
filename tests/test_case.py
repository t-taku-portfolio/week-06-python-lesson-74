import pytest

from lesson74.system_health_dashboard import create_report_json


def test_failure_case():
    # pass wrong path
    with pytest.raises(FileNotFoundError):
        create_report_json('this_is_wrong_path')