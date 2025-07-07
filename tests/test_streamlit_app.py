import runpy
from pathlib import Path


def test_import_streamlit_app():
    """Ensure streamlit_app runs without raising exceptions when executed."""
    path = Path(__file__).resolve().parents[1] / "streamlit_app.py"
    runpy.run_path(str(path))
