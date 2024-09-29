# Neural Network Perceptron

Currently, the focus of this project is on developing the graphical user interface (UI) to visualize and interact with a perceptron-based neural network. The UI is designed using Qt Creator, and the project is primarily implemented in Python using PyQt6.

## Features
- **Graphical User Interface**: The UI provides an easy and interactive way to work with perceptrons and neural networks.
- **Custom Paint Widget**: The project includes a custom `PaintWidget` that allows drawing figures using the mouse. This helps with visualizing perceptron training and testing.

## Getting Started

### Scripts

- **install-requirements.sh**: This script is used to install the required dependencies listed in requirements.txt automatically. It runs the command:
```sh
pip install -r requirements.txt
```

- **install-pyqt-mac.sh**: A helper script specifically for macOS users. It installs PyQt using Homebrew to ensure compatibility:
```sh
brew install pyqt
```

- **mainwindow.sh**: This script is used to generate the Python code for the UI from the .ui file
```sh
pyuic6 -x mainwindow.ui -o mainwindow.py
```
This helps automate the process of converting the UI file created in Qt Designer (mainwindow.ui) into a Python file (mainwindow.py), which can then be used in the application.