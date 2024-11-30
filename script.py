# Ashar Nadeem (21L-5336)
# Abdul Moiz (21L-5203)
import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Grid Analysis with Streamlit")
uploaded_file = st.file_uploader("Upload a custom image (optional):", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    input_image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    st.write("Using uploaded image.")
else:
    input_image_path = "input/input.jpg"
    input_image = cv2.imread(input_image_path)
    st.write("Using predefined input image.")
input_image_rgb = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
st.subheader("Input Image")
st.image(input_image_rgb, caption="Original Input Image", use_container_width=False, width=200)
binary_threshold = 128
binary_image = np.zeros_like(input_image)
binary_image[input_image >= binary_threshold] = 255
binary_image_rgb = cv2.cvtColor(binary_image, cv2.COLOR_BGR2RGB)
# Grid settings
height, width, _ = binary_image.shape
rows, cols = 10, 4
h_spacing = height // rows
v_spacing = width // cols
# Horizontal lines
for i in range(1, rows):
    y = i * h_spacing
    cv2.line(input_image, (0, y), (width, y), (0, 255, 0), 2)
# Vertical lines
for i in range(1, cols):
    x = i * v_spacing
    cv2.line(input_image, (x, 0), (x, height), (255, 0, 0), 2)
# Grid analysis
checked_threshold = 0.3
grid_analysis = []
for row in range(rows):
    row_analysis = []
    for col in range(cols):
        cell = binary_image[row * h_spacing:(row + 1) * h_spacing, col * v_spacing:(col + 1) * v_spacing]
        black_pixels = np.sum(cell == 0)
        total_pixels = cell.size
        ratio = black_pixels / total_pixels
        is_black_dominant = ratio > checked_threshold
        row_analysis.append(is_black_dominant)
        if is_black_dominant:
            top_left = (col * v_spacing, row * h_spacing)
            bottom_right = ((col + 1) * v_spacing, (row + 1) * h_spacing)
            cv2.rectangle(input_image, top_left, bottom_right, (0, 0, 255), 5)
    grid_analysis.append(row_analysis)
choices = ["A", "B", "C", "D"]
answers = ["A", "C", "B", "D", "A", "B", "C", "D", "A", "B"]
results = []
for row_index, row in enumerate(grid_analysis):
    true_columns = [col_index for col_index, is_true in enumerate(row) if is_true]

    if len(true_columns) > 1:
        detected_choices = [choices[col_index] for col_index in true_columns]
        results.append(f"Q{row_index + 1}: Multiple Choices Found: {', '.join(detected_choices)}")
    elif len(true_columns) == 1:
        selected_choice = choices[true_columns[0]]
        correct_answer = answers[row_index]
        if selected_choice == correct_answer:
            results.append(f"Q{row_index + 1}: Choice made: {selected_choice} (Correct)")
        else:
            results.append(f"Q{row_index + 1}: Choice made: {selected_choice} (Incorrect, Correct Answer: {correct_answer})")
    else:
        results.append(f"Q{row_index + 1}: No Choice Found")
st.subheader("Image Results")
col1, col2, col3 = st.columns(3)
with col1:
    st.image(input_image_rgb, caption="Input Image", use_container_width=True)
with col2:
    st.image(binary_image_rgb, caption="Binary Image", use_container_width=True)
with col3:
    st.image(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB), caption="Grid with Analysis", use_container_width=True)
st.subheader("Question Results")
for result in results:
    st.write(result)