import cv2
import numpy as np

input_image = cv2.imread('input/input.jpg')

binary_threshold = 128
binary_image = np.zeros_like(input_image)
binary_image[input_image >= binary_threshold] = 255

cv2.imwrite('output/binary_image.jpg', binary_image)

height, width, _ = binary_image.shape

rows, cols = 10, 4
h_spacing = height // rows
v_spacing = width // cols

for i in range(1, 10):
    y = i * h_spacing
    cv2.line(input_image, (0, y), (width, y), (0, 255, 0), 2)

for i in range(1, 4):
    x = i * v_spacing
    cv2.line(input_image, (x, 0), (x, height), (255, 0, 0), 2)


cv2.imwrite('output/grid_image.jpg', input_image)

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

cv2.imwrite('output/grid_with_analysis.jpg', input_image)

choices = ["A", "B", "C", "D"]
answers = ["A", "C", "B", "D", "A", "B", "C", "D", "A", "B"]

for row_index, row in enumerate(grid_analysis):
    true_columns = [col_index for col_index, is_true in enumerate(row) if is_true]
    
    if len(true_columns) > 1:
        detected_choices = [choices[col_index] for col_index in true_columns]
        print(f"Q{row_index + 1}: Multiple Choices Found: {', '.join(detected_choices)}")
    elif len(true_columns) == 1:
        selected_choice = choices[true_columns[0]]
        correct_answer = answers[row_index]
        if selected_choice == correct_answer:
            print(f"Q{row_index + 1}: Choice made: {selected_choice} (Correct)")
        else:
            print(f"Q{row_index + 1}: Choice made: {selected_choice} (Incorrect, Correct Answer: {correct_answer})")
    else:
        print(f"Q{row_index + 1}: No Choice Found")