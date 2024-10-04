import os
import sys

parent_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
vendor_dir = os.path.join(parent_dir, 'vendor')

def vendor_loader() -> None:
    sys.path.append(vendor_dir)
