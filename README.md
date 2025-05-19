# Optical-Character-Recognition



To develop a reliable and efficient system that converts textual content from images into digital text using Raspberry Pi, Pi Camera, and Optical Character Recognition (OCR) technology, especially focusing on degraded or aged images to improve accessibility and document management.

## Features

- Image Capture via Pi Camera: Uses Raspberry Pi Camera Module to capture high-resolution images of documents or text.
- Text Extraction with OCR: Implements Optical Character Recognition (OCR) to convert image-based text into machine-readable digital text.
- Real-Time Processing: Processes and extracts text in real-time using Raspberry Pi.
- Handles Degraded Images: Capable of recognizing text from blurry, aged, or low-quality images with improved accuracy.

-  Customizable Pipeline: Allows developers to tweak and adapt image preprocessing and OCR steps for specific use cases.
- Cost-Effective Hardware: Leverages low-cost Raspberry Pi setup for an affordable yet powerful solution.
-  Compact and Portable: Easy to deploy in various settings due to the small form factor of Raspberry Pi and accessories.



## Dataset
The project does not use a pre-existing dataset because it works with live image capture using a Raspberry Pi Camera. The text is extracted directly from the images captured in real time, rather than being trained or tested on a dataset.

However, if we want to test or train your OCR model further, you can consider the following popular datasets:

Suggested Datasets (for extension or training):
- IIIT 5K-Word Dataset – for scene text recognition.
- ICDAR (2013/2015/2019) – commonly used for OCR and text detection benchmarking.
- SynthText – a synthetic dataset with millions of annotated images.
- IAM Handwriting Database – for handwritten OCR testing.
- Google’s Open Images Dataset – contains labeled text-in-image examples.7\]]

**Data Flow**
(![Data Flow](https://github.com/user-attachments/assets/3e39a93c-aef6-41fd-a70d-904464383572)


## Installation and Setup

Raspberry Pi Initial Setup:
1. Install Raspberry Pi OS (use Raspberry Pi Imager)
2. Enable Pi Camera:
Open terminal and run:
```bash
sudo raspi-config
```
3. Install Required Software
- Update the System
```bash
sudo apt update && sudo apt upgrade -y
```
- Install OpenCV
```bash
sudo apt install python3-opencv -y
```
- Install Tesseract OCR
```bash
sudo apt install tesseract-ocr -y
```
- Install Python Libraries
```bash
pip3 install pytesseract
```
-  Install PiCamera Library
```bash
sudo apt install python3-picamera -y
```

## Output
- The camera window will open and display real-time video.
- Extracted text from images will be printed in the terminal.


## Code Highlights
1. OCR Text Extraction
```bash
text = pytesseract.image_to_string(image)
```
- This is the core function that extracts text from the captured image using Tesseract OCR.
2. Live Image Capture from Pi Camera- Adjusts randomness in text generation:
```bash
for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
    image = frame.array
```
- Continuously captures live frames from the Pi Camera for real-time processing.


## Results
The project successfully converted captured images into digital text using Raspberry Pi, Pi Camera, and OCR technology. It demonstrated reliable accuracy in recognizing various types of text, proving to be a cost-effective and practical solution. While current results are satisfactory, further improvements can enhance its performance for real-world applications.



