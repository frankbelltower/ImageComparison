import tensorflow as tf
import matplotlib.image as mpimg
import requests

from utils import log_tensor as log
from utils import check_difference_location
from utils import define_differences


control_positive = 'control/positive.jpg'
control_negative = 'control/negative.jpg'
image_to_download = 'https://drive.google.com/uc?export=download&id=1q5u3Sr8D2VWi_qjm4wdo8KlJrfmaMWck'
image_downloaded = 'test.jpg'


def main():
    # Reads an image saved in the control folder
    # Pass in control_negative for the negative case
    # Pass in control_positive for the positive case
    img = mpimg.imread(control_negative)
    # Transform the image in a Tensor
    img_tf = tf.constant(img)

    # Download the image to be compared with the previous one
    download_image(image_to_download, image_downloaded)
    img_to_compare = mpimg.imread(image_downloaded)
    # Transform the second image in a Tensor
    img_to_compare_tf = tf.constant(img_to_compare)
    # Check equality between the two matrices
    equality = tf.equal(img_tf, img_to_compare_tf)
    # Reduce equality to True or False
    reduced_equality = tf.reduce_all(equality)
    difference_locators = check_difference_location(equality, reduced_equality)
    define_differences(image_downloaded, difference_locators)
    print("Are the images equal?", reduced_equality)


def download_image(image_url, filename):
    """
    Downloads an image from a URL and saves it with the given filename.
    """
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Raise an exception for bad status codes

        with open(filename, 'wb') as f:
            f.write(response.content)

        print(f"Downloaded image: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")


if __name__ == "__main__":
    main()
