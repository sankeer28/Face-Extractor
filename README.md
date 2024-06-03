# Face Extractor
```
  _____                              _                  _             
 |  ___|_ _  ___ ___        _____  _| |_ _ __ __ _  ___| |_ ___  _ __ 
 | |_ / _` |/ __/ _ \_____ / _ \ \/ / __| '__/ _` |/ __| __/ _ \| '__|
 |  _| (_| | (_|  __/_____|  __/>  <| |_| | | (_| | (__| || (_) | |   
 |_|  \__,_|\___\___|      \___/_/\_\\__|_|  \__,_|\___|\__\___/|_|   
                                                                      
```
The Face Extractor is a Python script that automates the process of detecting and extracting faces from images. It utilizes the MTCNN (Multi-task Cascaded Convolutional Networks) algorithm for robust face detection and cropping.

## Features

- Automatic face detection and cropping from all images in specified folder.
- Adjustable padding ratio around detected faces.
- Customizable confidence threshold for controlling face detection sensitivity.
- Supports various image formats including JPG, JPEG, and PNG.
- Output folder organization: Each extracted face is saved with a unique identifier and placed in the output folder.

## Uses
- [MTCNN](https://github.com/ipazc/mtcnn): Multi-task Cascaded Convolutional Networks for face detection.
- [OpenCV](https://opencv.org/): Open Source Computer Vision Library.
- [NumPy](https://numpy.org/): Fundamental package for scientific computing with Python.
- [Tensorflow](https://www.tensorflow.org/): Free and open-source software library for machine learning and artificial intelligence.
  
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
options:
  -h, --help            show this help message and exit
  --input INPUT         Path to the input folder.
  --output OUTPUT       Path to the output folder.
  --padding PADDING     Padding ratio around the face (default: 0.2)
  --confidence_threshold Confidence threshold for face detection (default: 0.8)
  --annotate            Add numbers to detected faces on the output images.
```

- `--input`: Path to the input folder containing images.
- `--output`: Path to the output folder where extracted faces will be saved.
- `--padding`: Padding ratio around the detected faces (default: 0.2).
- `--confidence_threshold`: Confidence threshold for face detection (default: 0.8).
- `--annotate`: Add numbers to detected faces on the output images.

## Examples

Extract faces from images in the `input` folder and save them to the `output` folder with default settings:

```
python face_extractor.py --input input --output output
```


## Example

#### Input image: 
![gettyimages-200244581-003-612x612](https://github.com/sankeer28/Face-Extractor/assets/112449287/3f00ea72-ea9d-401d-b020-42f886a672e9)

#### Output:
-  after running ` python face_extractor.py --input "C:\Users\san\Downloads\Face-Extractor" --output "C:\Users\san\Downloads\Face-Extractor\out"`

 ![image](https://github.com/sankeer28/Face-Extractor/assets/112449287/6e4a6f8c-0286-4ff8-a47e-fa88792952dd)

 - after running ` python face_extractor.py --input "C:\Users\san\Downloads\Face-Extractor" --output "C:\Users\san\Downloads\Face-Extractor\out" --annotate`
   
![gettyimages-200244581-003-612x612_annotated](https://github.com/sankeer28/Face-Extractor/assets/112449287/a2fbf5b3-f201-4476-8fb1-74e5588b5c3f)

 80 faces were found


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
