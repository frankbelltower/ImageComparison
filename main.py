import tensorflow as tf
import matplotlib.image as mpimg
import requests


control_positive = 'control/positive.jpg'
control_negative = 'control/negative.jpg'
image_to_download = 'https://drive.google.com/uc?export=download&id=1q5u3Sr8D2VWi_qjm4wdo8KlJrfmaMWck'
image_downloaded = 'test.jpg'


def main():
    # Reads an image saved in the control folder
    # Pass in control_negative for the negative case
    # Pass in control_positive for the positive case
    img = mpimg.imread(control_positive)
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
