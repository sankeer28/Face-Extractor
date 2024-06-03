# Face Extractor

The Face Extractor is a Python script that automates the process of detecting and extracting faces from images. It utilizes the MTCNN (Multi-task Cascaded Convolutional Networks) algorithm for robust face detection and cropping.

## Features

- Automatic face detection and cropping from images
- Adjustable padding ratio around detected faces
- Customizable confidence threshold for controlling face detection sensitivity
- Supports various image formats including JPG, JPEG, and PNG
- Output folder organization: Each extracted face is saved with a unique identifier and placed in the output folder

## Installation

1. Clone the repository:

```
https://github.com/sankeer28/Face-Extractor.git
```

2. Install the required Python packages:

```
pip install -r requirements.txt
```

## Usage

```
python face_extractor.py --input <input_folder> --output <output_folder> [--padding <padding_ratio>] [--confidence_threshold <confidence_threshold>]
```

- `--input`: Path to the input folder containing images.
- `--output`: Path to the output folder where extracted faces will be saved.
- `--padding`: Padding ratio around the detected faces (default: 0.2).
- `--confidence_threshold`: Confidence threshold for face detection (default: 0.8).

## Examples

Extract faces from images in the `input` folder and save them to the `output` folder with default settings:

```
python face_extractor.py --input input --output output
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Uses
- [MTCNN](https://github.com/ipazc/mtcnn): Multi-task Cascaded Convolutional Networks for face detection.
- [OpenCV](https://opencv.org/): Open Source Computer Vision Library.
- [NumPy](https://numpy.org/): Fundamental package for scientific computing with Python.
- [Tensorflow](https://www.tensorflow.org/) : Free and open-source software library for machine learning and artificial intelligence.
