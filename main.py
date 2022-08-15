import io
import sys
from PIL import Image
import numpy as np
import matplotlib.image as img


def image_to_byteio(image: Image):
    output = io.BytesIO()

    image.save(output, "JPEG")

    return output


def convert_to_jpg(image: Image):
    return image_to_byteio(image)


def convert_to_greyscale(image: Image):
    return image.convert("L")


def is_power_of_2(num):
    return num and (not (num & (num - 1)))


def prev_power_of_2(num):
    prev = 2 << 1

    for i in range(2, 16):
        current = 2 << i

        if current > num:
            return prev

        prev = current

    return prev


def next_power_of_2(num):
    for i in range(2, 16):
        current = 2 << i

        if current > num:
            return current

    return num


def get_resize_img_dim(image: Image):
    width, height = image.size

    min_dim = width if width < height else height

    if is_power_of_2(min_dim):
        return min_dim, min_dim

    prev_pow_2 = prev_power_of_2(min_dim)
    next_pow_2 = next_power_of_2(min_dim)

    if min_dim - prev_pow_2 < min_dim - next_pow_2:
        return prev_pow_2

    return next_pow_2


def resize_image(image: Image):
    print(get_resize_img_dim(image))  # TODO: remove this

    dim = get_resize_img_dim(image)

    return image.resize((dim, dim))


def get_image_matrix(image: Image):
    return img.imread(image_to_byteio(image), format="JPEG")


def save_result_image(result_matrix, output_path):
    img.imsave(output_path, result_matrix, cmap="gray")


def flip_matrix(size):
    matrix = np.zeros((size, size))

    j = size - 1

    for i in range(size):
        matrix[i][j] = 1
        j -= 1

    return matrix


def call_operation(op: str, matrix: np.array):
    dim = matrix.shape[0]

    if op == "flip":
        return np.matmul(matrix, flip_matrix(dim))

    if op == "rotate_90_deg_left":
        return np.matmul(np.transpose(matrix), flip_matrix(dim))

    if op == "test":
        return np.matmul(matrix, np.ones((dim, dim)))

    return matrix


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Correct usage: python3 main.py <INPUT_FILE_PATH> <OUTPUT_FILE_PATH>")
        exit(0)

    file_path = sys.argv[1]
    output_path = sys.argv[2]

    converted_img = convert_to_greyscale(Image.open(file_path))

    if not file_path.endswith(".jpg"):
        converted_img = convert_to_jpg(converted_img)

    resized_img = resize_image(converted_img)

    img_matrix = get_image_matrix(resized_img)

    result = call_operation("flip", img_matrix)

    save_result_image(result, output_path)
