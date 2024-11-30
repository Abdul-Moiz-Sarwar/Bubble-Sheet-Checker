# Bubble Sheet Checker

This project processes an input image to:
1. Convert it into a binary image using a threshold value.
2. Divide the image into a grid of 10x4 (10 rows and 4 columns).
3. Calculate the black-to-white pixel ratio for each cell and analyze the results.
4. Identify and validate choices based on detected pixel patterns in the grid.

The project is designed for tasks such as detecting marked answers on grids, with added functionality for error detection and choice validation.

## Features
- Convert images to binary with a custom thresholding algorithm.
- Analyze images by dividing them into a grid.
- Calculate pixel ratios and determine marked cells.
- Output results for multiple-choice grids, including errors or identified choices.

---

## Installation and Setup

Follow these steps to get the project running on your local machine:

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

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

4. Run the main script:
    ```bash
    python script.py
    ```

---

## Usage
1. Place the input image in the project directory.
2. Update the image path in the script if necessary.
3. Execute the script to generate:
    - A binary image (`binary_image.jpg`).
    - A grid image (`grid_image.jpg`).
    - A results image (`grid_with_analysis.jpg`).
    - Analysis results printed to the console.

---

## Example Output
- **Binary Image**: Saved as `binary_image.jpg`.
- **Grid Image**: Saved as `grid_image.jpg`.
- **Analysis Image**: Saved as `grid_with_analysis.jpg`.
- **Console Output**:
    ```
    Q1: Choice made: A (Correct)
    Q2: Multiple Choices Found: A, C
    Q3: Choice made: A (Incorrect, Correct Answer: B)
    Q4: No Choice Found
    ```

---

## Collaborators

This project was developed as a group effort. The contributors are:
- **Asher Nadeem** ([View Profile](https://github.com/asharnadeem002))
- **Abdul Moiz Sarwar** ([View Profile](https://github.com/Abdul-Moiz-Sarwar))
---