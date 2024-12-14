# Fire and Smoke Detection System

This project uses a YOLOv8 model to detect fire and smoke in images and plays an alarm sound when fire or smoke is detected.

## Requirements

- Python 3.12
- ultralytics
- opencv-python
- pygame

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/aayush-ojha/fire-smoke-detection.git
    cd fire-smoke-detection
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Download the YOLOv8 model from Kaggle:
    - Visit [this link](https://www.kaggle.com/models/deepaknr/fire-and-smoke-detection-yolov8)
    - Download the model file `fire_and_smoke_model.pt`
    - Place the model file in the project directory

5. Ensure you have an alarm sound file named `alarm.wav` in the project directory.

## Usage

1. Place the image you want to test in the project directory and name it `test.jpeg`.

2. Run the detection script:
    ```sh
    python3 main.py
    ```

## main.py

The main script performs the following steps:
1. Initializes the pygame mixer.
2. Loads the YOLOv8 model.
3. Performs detection on the image `test.jpeg`.
4. Checks the detection results for fire or smoke.
5. Plays an alarm sound if fire or smoke is detected.

## License

This project is licensed under the MIT License.