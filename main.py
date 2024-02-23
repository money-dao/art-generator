from PIL import Image
import os
import json
import argparse

import settings


def enforce_trait_order(traits_list, order_rules, special_rules=None):
    """
    Sorts a list of trait dictionaries based on specified ordering rules and optional special rules.

    This function organizes a list of character traits according to a predefined order. It allows
    for customization of trait sorting order through 'order_rules' and can handle exceptions or
    special cases defined in 'special_rules'. The sorting primarily depends on the trait type,
    but can be further refined based on specific trait values through special rules.

    Parameters:
    - traits_list (list): A list of dictionaries, where each dictionary represents a trait with
                          at least 'trait_type' and 'value' keys.
    - order_rules (dict): A dictionary mapping trait types to integers that represent their sorting
                          order. Lower numbers indicate higher priority in the sorting order.
    - special_rules (list, optional): A list of tuples, each containing three elements:
        1. trait_type (str): The type of the trait to which the special rule applies.
        2. value (str): A substring of the trait value that triggers the special sorting rule.
        3. order (int): An integer representing the sorting order for traits matching the rule.
                       This allows for placing certain traits at specific positions in the list,
                       overriding the default order specified by 'order_rules'.

    The sorting logic first checks if a trait matches any of the special rules based on its type
    and value. If so, the trait is assigned the corresponding order from the special rule. If no
    special rule applies, the function uses the general 'order_rules' to determine the trait's
    position in the sorted list. Traits not explicitly mentioned in either 'order_rules' or
    'special_rules' are placed at the end of the list.

    Returns:
    - list: A new list of traits sorted according to the combined logic of 'order_rules' and
            'special_rules'.

    Note:
    - This function does not modify the original 'traits_list'; it returns a new sorted list.
    - If 'special_rules' is not provided or is empty, the sorting will rely entirely on 'order_rules'.
    """
    if special_rules is None:
        special_rules = []

    # Build a dictionary for quick lookup of special rules
    special_order_lookup = {(rule[0], rule[1]): rule[2] for rule in special_rules}

    def sort_key(trait):
        # Check for special ordering rules first
        if (trait['trait_type'], trait['value']) in special_order_lookup:
            return special_order_lookup[(trait['trait_type'], trait['value'])]

        # Default to the order specified in order_rules, with a fallback
        return order_rules.get(trait['trait_type'], len(order_rules))

    return sorted(traits_list, key=sort_key)


def assemble_character_image_from_traits(base_path: str, id: int|str, trait_list: list):
    """
    Assembles a character image by layering trait images on top of a background image.

    This function iterates through a list of traits, identifying the background trait and
    other character traits such as eyes, mouth, etc. Each trait image is layered on top of
    the background image to assemble the final character image. The assembled image is
    saved to a specified directory.

    Parameters:
    - base_path (str): The base directory path where trait images are stored. Each trait type
                       is expected to have its own subdirectory within this base path.
    - id (int | str): An identifier for the assembled image. This is used to name the output image file.
    - trait_list (list): A list of dictionaries, where each dictionary represents a trait. Each
                         dictionary should have a 'trait_type' key indicating the type of the trait
                         (e.g., 'background', 'eyes') and a 'value' key indicating the specific trait
                         image filename (without the extension).

    The function checks for the presence of a background trait in the trait list. If not found,
    it prints an error message and returns without creating an image. For other traits, it looks
    for corresponding PNG images within subdirectories of the base path, layers them on top of
    the background, and saves the final composite image in the 'generated_images' subdirectory
    within the base path, using the provided id as the filename.

    The function expects PNG images for compatibility with alpha transparency for proper layering.

    Returns:
    None. The final image is saved to the filesystem, and an error message is printed to the console
    if the background trait is not specified or if any trait image file is not found.
    """
    background = None
    traits = {}

    for trait in trait_list:
        if trait['trait_type'] == 'background':
            background = trait['value']
        else:
            trait_type = trait['trait_type']
            traits[trait_type] = trait['value']

    if not background:
        print("Error: Background not specified.")
        return

    background_path = os.path.join(base_path, "background", f"{background}.png")
    base_image = Image.open(background_path).convert("RGBA")

    for trait_type, trait_value in traits.items():
        trait_image_path = os.path.join(base_path, trait_type, f"{trait_value}.png")

        if os.path.isfile(trait_image_path):
            trait_image = Image.open(trait_image_path).convert("RGBA")
            # Resize trait image to match base image size
            trait_image_resized = trait_image.resize(base_image.size)
            base_image = Image.alpha_composite(base_image, trait_image_resized)
        else:
            print(f"Trait image not found: {trait_image_path}")

    output_path = os.path.join(base_path, 'generated_images')
    final_image_path = os.path.join(output_path, f"{id}.png")
    base_image.save(final_image_path)
    # base_image.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate image from layered traits.")
    parser.add_argument("metadata_path", type=str, help="Path to metadata.")
    parser.add_argument("base_assets_path", type=str, help="Path to layer assets.")

    args = parser.parse_args()

    with open(args.metadata_path, 'r') as fp:
        metadata = json.load(fp)

    for id, traits in metadata.items():
        trait_list = enforce_trait_order(
            traits_list=traits,
            order_rules=settings.order_rules,
            special_rules=settings.special_rules
        )
        assemble_character_image_from_traits(args.base_assets_path, id, trait_list)
