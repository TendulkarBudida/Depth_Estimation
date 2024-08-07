# Depth Estimation using Transformers and Tkinter

This project demonstrates how to perform depth estimation on an image using the `transformers` library and a pre-trained model. The application uses `Tkinter` for a graphical user interface to select an image file and `matplotlib` to visualize the depth map.

## Requirements

- Python 3.x
- `transformers` library
- `Pillow` library
- `requests` library
- `tkinter` library (usually included with Python)
- `matplotlib` library

You can install the required libraries using pip:

```sh
pip install transformers Pillow requests matplotlib

python main.py # for running the python file

pyinstaller --onefile depth_estimation_app.py # for exporting into and executable file
