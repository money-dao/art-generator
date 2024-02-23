
traits_names_lookup = {
    'background': 'background',
    'face': 'body',
    'shirt': 'shirt',
    'necklace': 'chain',
    'eyes': 'eyes',
    'head': 'head',
    'mouth': 'mouth'
}

trait_values_lookup = {
    'background': {
        'orange': 'orange',
        'yellow': 'yellow',
        'lavender': 'lavender',
        'green': 'green',
        'white': 'grey',
        'teal': 'teal',
        'purple': 'purple',
        'blue': 'blue',
        'pink': 'red'
    },
    'face': {
        'orange': 'orange',
        'yellow': 'yellow',
        'dark': 'brown',
        'lavender': 'lavender',
        'green': 'green',
        'light': 'light',
        'white': 'grey',
        'teal': 'teal',
        'purple': 'purple',
        'blue': 'blue',
        'pink': 'red'
    },
    'shirt': {
        'backpackgreen': 'backpack_green',
        'hoodielavender': 'hoodie_lavender',
        'robeking': 'robe_king',
        'backpackrainbow': 'backpack_multi',
        'jacketorangeyellow15': 'jacket_orange_yellow',
        'hoodieblue': 'hoodie_blue',
        'jackettealpink': 'jacket_teal_pink',
        'robegreenyellow': 'robe_green',
        'robeblueteal': 'robe_blue',
        'collartealpink': 'polo_teal_pink',
        'jacketgreen': 'jacket_green',
        'backpackpink': 'backpack_red',
        'collargreen': 'polo_green',
        'collargold': 'polo_yellow',
        'jacketyellowpurple': 'jacket_yellow_purple',
        'hoodiepurple': 'hoodie_purple',
        'collargreenorange': 'polo_green_orange',
        'robepinkyellow': 'robe_pink_multi',
        'backpackking': 'backpack_orange',
        'backpackorangeteal': 'backpack_teal',
        'robegold': 'robe_orange',
        'collarrainbow2': 'polo_multi_1',
        'jacketgold': 'jacket_yellow',
        'hoodiegreen': 'hoodie_green',
        'collaryellowlavender': 'polo_yellow_purple',
        'backpackblue': 'backpack_purple',
        'backpackpurpleyellow': 'backpack_purple_multi',
        'collarrainbow1': 'polo_multi_2',
        'jacketpurplegreen': 'jacket_lavender_green'
    },
    'necklace': {
        'ng': 'goldchain',
        'transparent1': 'none'
    },
    'eyes': {
        'angry': 'angry',
        'awake': 'awake',
        'chill': 'chill'
    },
    'head': {
        'dropblue': 'head_slime_blue',
        'darkdrop2': 'hole',
        'droppink': 'head_slime_pink',
        'dripteal': 'top_slime_teal',
        'droppurple': 'head_slime_purple',
        'crown': 'crown',
        'hatgreen': 'cap_green',
        'hatblue': 'cap_blue',
        'dripblue': 'top_slime_blue',
        'halo': 'halo_black',
        'drippurple': 'top_slime_purple',
        'haloteal': 'halo_green',
        'halopurple': 'halo_white',
        'hatpink': 'cap_pink',
        'hatpurple': 'cap_purple',
        'dripgreen': 'top_slime_green',
        'bald': 'none',
        'hatorange': 'cap_orange',
        'droporange': 'head_slime_orange',
        'darkdrop': 'hole',
        'dripgold': 'top_slime_yellow'
    },
    'mouth': {
        'smokeyellow': 'smoke_yellow',
        'zigmouthpurple': 'slime_purple',
        'smokegreen': 'smoke_green',
        'smokegreenorange': 'smoke_green_orange',
        'zigmouthgold': 'slime_yellow',
        'smile': 'smile',
        'darkmask3': 'hole',
        'tonguegold': 'tounge_yellow',
        'nomouth': 'none',
        'grinpink': 'red_smile',
        'moneymouth': 'money_mouth',
        'skullmouth': 'skull',
        'smokepurple': 'smoke_purple',
        'smokepurpleteal': 'smoke_multi',
        'grin100': 'white_smile',
        'gringreen': 'green_smile',
        'zigmouthteal': 'slime_teal',
        'smokeorangeteal': 'smoke_orange_teal',
        'smokepink': 'smoke_pink',
        'tongue': 'tounge_pink',
        'tonguegreen': 'tounge_green',
        'darkmask2': 'slime',
        'smoketeallavender': 'smoke_teal_orange',
        'gringold': 'yellow_smile',
        'darkmask1': 'slime'
    }
}


def update_traits_with_lookups(json_data, traits_names_lookup, trait_values_lookup):
    """
    Updates a collection of traits within a JSON-like dictionary structure based on provided lookup tables.

    This function iterates over a dictionary of traits, updating each trait's type and value according to
    provided lookup tables. The `traits_names_lookup` table is used to update the type of each trait,
    while the `trait_values_lookup` table is used to update the value of each trait. If a trait type or
    value does not have a corresponding entry in the lookup tables, the original type or value is retained.

    Parameters:
    - json_data (dict): A dictionary where each key maps to a list of trait dictionaries. Each trait
                        dictionary should have at least 'trait_type' and 'value' keys.
    - traits_names_lookup (dict): A dictionary mapping original trait types to their new types. If a trait
                                  type is not present in this lookup, its type remains unchanged.
    - trait_values_lookup (dict): A nested dictionary where the outer key is the trait type, and the inner
                                  dictionary maps original trait values to their new values for that type.
                                  If a trait value is not present in this lookup for its type, its value
                                  remains unchanged.

    Returns:
    - dict: A new dictionary structured like `json_data` but with trait types and values updated according
            to the lookup tables.

    Example:
    json_data = {
        "0": [{"trait_type": "eye_color", "value": "blue"}, {"trait_type": "hair_color", "value": "blonde"}],
        "1": [{"trait_type": "eye_color", "value": "green"}]
    }
    traits_names_lookup = {"eye_color": "color_of_eyes", "hair_color": "color_of_hair"}
    trait_values_lookup = {
        "color_of_eyes": {"blue": "deep_blue", "green": "emerald"},
        "color_of_hair": {"blonde": "golden"}
    }
    updated_json_data = update_traits_with_lookups(json_data, traits_names_lookup, trait_values_lookup)
    # `updated_json_data` will have "blue" updated to "deep_blue", "green" to "emerald", and
    # "blonde" to "golden", with trait types updated according to `traits_names_lookup`.
    """
    updated_data = {}

    for key, traits in json_data.items():
        updated_traits = []
        for trait in traits:
            updated_trait_type = traits_names_lookup.get(trait['trait_type'], trait['trait_type'])

            updated_value = trait['value']
            if trait['trait_type'] in trait_values_lookup and trait['value'] in trait_values_lookup[
                trait['trait_type']]:
                updated_value = trait_values_lookup[trait['trait_type']][trait['value']]

            updated_traits.append({'trait_type': updated_trait_type, 'value': updated_value})

        updated_data[key] = updated_traits

    return updated_data
