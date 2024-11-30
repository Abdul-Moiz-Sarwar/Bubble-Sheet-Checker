# Bubble Sheet Checker

This project processes an input image to:
1. Convert it into a binary image using a threshold value.
2. Divide the image into a grid of 10x4 (10 rows and 4 columns).
3. Calculate the black-to-white pixel ratio for each cell and analyze the results.
4. Identify and validate choices based on detected pixel patterns in the grid.
5. Optionally allows users to upload a custom image for processing and analysis.

The project is designed for tasks such as detecting marked answers on grids, with added functionality for error detection, choice validation, and an interactive user interface.

---

## Features
- **Streamlit Interface**: 
  - Displays input images, binary images, and grid analysis images side by side.
  - Includes an optional image uploader for processing custom images.
- **Binary Conversion**: Convert images to binary with a custom thresholding algorithm.
- **Grid Analysis**: 
  - Divide the image into a grid.
  - Calculate pixel ratios and determine marked cells.
  - Overlay detected markings on the grid.
- **Answer Validation**: Output results for multiple-choice grids, including errors or identified choices.
- **Interactive Output**: View images and results directly in the browser.

---

## Installation and Setup

Follow these steps to get the project running on your local machine:

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Streamlit

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/Abdul-Moiz-Sarwar/Bubble-Sheet-Checker
    cd Bubble-Sheet-Checker
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux 
    venv\Scripts\activate  # On Windows
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run script.py
    ```

---

## Usage

### Upload Custom Image
1. Run the Streamlit app using `streamlit run script.py`.
2. Open the provided URL in a web browser (e.g., `http://localhost:8501`).
3. Upload a custom image using the file uploader, or use the default predefined image.
4. The app will:
   - Display the input image, binary image, and grid analysis image side by side.
   - Provide analysis results below the images, including detected choices and validation.

---

## Example Output

### Images
- **Input Image**: The original image (uploaded or predefined).
- **Binary Image**: Image converted into binary format.
- **Grid Analysis Image**: Grid overlay with detected markings highlighted.

### Results (Console Output in the Browser)
```
Q1: Choice made: A (Correct)
Q2: Multiple Choices Found: A, C
Q3: Choice made: A (Incorrect, Correct Answer: B)
Q4: No Choice Found
```

---

## Collaborators

This project was developed as a group effort. The contributors are:
- **Ashar Nadeem 21L-5336** ([View Profile](https://github.com/asharnadeem002))
- **Abdul Moiz Sarwar 21L-5203** ([View Profile](https://github.com/Abdul-Moiz-Sarwar))

---