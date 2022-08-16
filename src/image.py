import io
from PIL import Image
import numpy as np
import matplotlib.image as img
from strassen import strassen, brute_force

def image_to_byteio(image: Image):
    output = io.BytesIO()

    image.save(output, "JPEG")

    return output


def convert_to_jpg(image: Image):
    return Image.open(image_to_byteio(image))


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
        return min_dim

    prev_pow_2 = prev_power_of_2(min_dim)
    next_pow_2 = next_power_of_2(min_dim)

    if min_dim - prev_pow_2 < min_dim - next_pow_2:
        return prev_pow_2

    return next_pow_2


def resize_image(image: Image):
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

def matrix_dim(matrix):
    return matrix.shape[0]

def get_mult_func(use_numpy):
    if use_numpy:
        return np.matmul

    return strassen

def flip_image(matrix, use_numpy):
    mat_mul = get_mult_func(use_numpy)

    return mat_mul(matrix, flip_matrix(matrix_dim(matrix)))

def rotate_90_deg_image(matrix, use_numpy):
    mat_mul = get_mult_func(use_numpy)

    return mat_mul(np.transpose(matrix), flip_matrix(matrix_dim(matrix)))
