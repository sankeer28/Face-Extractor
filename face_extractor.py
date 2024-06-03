import cv2
import os
import argparse
import numpy as np
from mtcnn import MTCNN

def extract_faces(input_folder, output_folder, padding=0.2, confidence_threshold=0.8, annotate=False):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    detector = MTCNN()
    detector.min_face_size = 7
    detector.thresholds = [confidence_threshold, confidence_threshold, confidence_threshold]
    extensions = ['.jpg', '.jpeg', '.png']
    for filename in os.listdir(input_folder):
        if any(filename.lower().endswith(ext) for ext in extensions):
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path)
            if img is None:
                print(f"Warning: Couldn't read image {img_path}")
                continue
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            faces = detector.detect_faces(rgb_img)
            if annotate:
                for i, face in enumerate(faces):
                    (x, y, w, h) = face['box']
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(img, f"Face {i+1}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                annotated_img_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_annotated.jpg")
                cv2.imwrite(annotated_img_path, img)
                print(f"Saved annotated image: {annotated_img_path}")
            else:
                for i, face in enumerate(faces):
                    (x, y, w, h) = face['box']
                    padding_x = int(padding * w)
                    padding_y = int(padding * h)
                    x1 = max(x - padding_x, 0)
                    y1 = max(y - padding_y, 0)
                    x2 = min(x + w + padding_x, img.shape[1])
                    y2 = min(y + h + padding_y, img.shape[0])

                    cropped_face = img[y1:y2, x1:x2]
                    face_filename = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_face_{i}.jpg")
                    cv2.imwrite(face_filename, cropped_face)
                    print(f"Saved {face_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract faces from images.")
    parser.add_argument("--input", required=True, help="Path to the input folder.")
    parser.add_argument("--output", required=True, help="Path to the output folder.")
    parser.add_argument("--padding", type=float, default=0.2, help="Padding ratio around the face (default: 0.2)")
    parser.add_argument("--confidence_threshold", type=float, default=0.8, help="Confidence threshold for face detection (default: 0.8)")
    parser.add_argument("--annotate", action="store_true", help="Add numbers to detected faces on the output images.")
    
    args = parser.parse_args()

    extract_faces(args.input, args.output, padding=args.padding, confidence_threshold=args.confidence_threshold, annotate=args.annotate)
