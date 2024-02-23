from PIL import Image


def create_gif(image_paths: list[str], output_path: str, duration: int = 500):
    """
    Creates an animated GIF from a list of image paths.

    This function takes a list of paths to image files, loads them, and combines them into a single
    animated GIF. All images are resized to match the size of the first image in the list to ensure
    consistency. The images are then converted to RGB mode for GIF compatibility. The resulting GIF
    is saved to the specified output path.

    Parameters:
    - image_paths (list[str]): A list of file paths to the images that will be included in the GIF.
                               Each path should be a string.
    - output_path (str): The file path where the resulting GIF should be saved. This includes the
                         filename and its extension (e.g., 'output/animated.gif').
    - duration (int, optional): The duration each frame should be displayed for, in milliseconds.
                                Defaults to 500ms.

    Returns:
    None. The function saves the resulting GIF to the filesystem at the specified `output_path`.

    Note:
    - All images are resized to the dimensions of the first image in `image_paths`. Aspect ratio
      may be altered if the original images have different dimensions.
    - This function requires the Pillow library (PIL fork) to run. Make sure to install it via pip
      using `pip install Pillow`.
    - Ensure the image paths exist and are accessible to avoid runtime errors.

    Example usage:
    create_gif(['path/to/image1.png', 'path/to/image2.png'], 'path/to/output.gif', duration=1000)
    """
    images = [Image.open(image_path).convert("RGBA") for image_path in image_paths]

    base_size = images[0].size
    resized_images = [image.resize(base_size, Image.Resampling.LANCZOS) for image in images]

    # Convert images to RGB mode for GIF compatibility
    rgb_images = [image.convert("RGB") for image in resized_images]

    rgb_images[0].save(output_path, save_all=True, append_images=rgb_images[1:], optimize=False, duration=duration,
                       loop=0)
