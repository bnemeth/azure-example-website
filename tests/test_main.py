from unittest.mock import patch

from azure_example_website.__main__ import main
from azure_example_website.app import app


def test_main_default_port():
    with patch("azure_example_website.__main__.uvicorn.run") as mock_run, \
         patch("sys.argv", ["prog"]):
        main()
        mock_run.assert_called_once_with(app, host="0.0.0.0", port=8000)


def test_main_custom_port():
    with patch("azure_example_website.__main__.uvicorn.run") as mock_run, \
         patch("sys.argv", ["prog", "--port", "9000"]):
        main()
        mock_run.assert_called_once_with(app, host="0.0.0.0", port=9000)
