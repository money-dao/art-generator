from PIL import Image, ImageChops, ImageEnhance
import numpy as np
import argparse


def glitch_image_png(input_image_path: str, output_gif_path: str, frames: int = 10, displacement: float = 5, intensity: float = 0.5):
    """
    Create a glitchy GIF from a PNG image, potentially with an alpha channel.

    Parameters:
    - input_image_path: Path to the input PNG image.
    - output_gif_path: Path to save the output GIF.
    - frames: Number of frames in the GIF.
    - displacement: Maximum pixel displacement for the glitch effect.
    - intensity: Intensity of the color shift, between 0 and 1.
    """
    original = Image.open(input_image_path).convert("RGBA")
    width, height = original.size

    glitch_frames = []

    for frame in range(frames):
        # Split into RGBA channels (if applicable)
        channels = original.split()
        if len(channels) == 4:
            r, g, b, a = channels
            # We'll apply the glitch effect to RGB channels only
            has_alpha = True
        else:
            r, g, b = channels
            has_alpha = False

        # Apply displacement to the RGB channels
        displacement_val = np.random.randint(-displacement, displacement)
        r = ImageChops.offset(r, displacement_val, 0)
        g = ImageChops.offset(g, 0, displacement_val)
        b = ImageChops.offset(b, -displacement_val, 0)

        # Merge the channels back, including the alpha channel if present
        if has_alpha:
            glitched = Image.merge("RGBA", (r, g, b, a))
        else:
            glitched = Image.merge("RGB", (r, g, b))

        # Convert back to RGB if it was originally RGBA to avoid issues saving as GIF
        glitched = glitched.convert("RGB")

        # Enhance the color to make it more trippy
        enhancer = ImageEnhance.Color(glitched)
        glitched = enhancer.enhance(1 + intensity)

        glitch_frames.append(glitched)

    glitch_frames[0].save(output_gif_path, save_all=True, append_images=glitch_frames[1:], optimize=False, duration=100,
                          loop=0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create a glitchy GIF from an image.")
    parser.add_argument("input_image_path", type=str, help="Path to the input image.")
    parser.add_argument("output_gif_path", type=str, help="Path to save the output GIF.")
    parser.add_argument("--frames", type=int, default=10, help="Number of frames in the GIF.")
    parser.add_argument("--displacement", type=int, default=5, help="Maximum pixel displacement for the glitch effect.")
    parser.add_argument("--intensity", type=float, default=0.5, help="Intensity of the color shift, between 0 and 1.")

    args = parser.parse_args()

    print(f'loading image to glitch from {args.input_image_path}')

    glitch_image_png(
        input_image_path=args.input_image_path,
        output_gif_path=args.output_gif_path,
        frames=args.frames,
        displacement=args.displacement,
        intensity=args.intensity
    )

    print(f'GIF saved to {args.output_gif_path}')