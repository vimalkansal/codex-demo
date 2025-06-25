import sys

def test_python_version_is_gt_3_10():
    major, minor = sys.version_info[:2]
    assert (major, minor) > (3, 10), f"Python version {major}.{minor} must be > 3.10"
