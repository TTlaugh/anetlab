import os
import sys

PARENT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

def vendor_loader() -> None:
    vendor_dir = os.path.join(PARENT_DIR, 'vendor')
    sys.path.append(vendor_dir)
