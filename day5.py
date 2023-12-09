from aoc_common import read_file
import regex as re


def get_maps(data):
    """Parse puzzle input to get all mapping patterns.

    Args:
        data (list): List of lines from the puzzle input.

    Returns:
        dict: Dictionary of mapping patterns for each conversion.
    """    
    maps = {}
    current_map = ''
    for line in data[1:]:
        # Update current map if line starts with text
        if re.match(r'[a-zA-Z]', line):
            current_map = line.split()[0]
            maps[current_map] = []
        # Append map numbers to current map if line starts with numbers
        elif re.match(r'\d', line):
            map_numbers = [int(num) for num in line.split()]
            maps[current_map].append(map_numbers)

    return maps


def get_seeds(data):
    """Extract seed ids from the first line of the input data.

    Args:
        data (list): List of lines from the puzzle input.

    Returns:
        list: List of ids
    """    
    seeds = [int(seed_id) for seed_id in re.findall(r'\d+', data[0])]
    return seeds


def convert_id(id, map_subset):
    """Converts an id based on the provided mapping pattern.

    Args:
        id (int): Starting id.
        map_subset (list): List of mapping parameters.

    Returns:
        int: Destination id.
    """    
    # Output defaults to input if not mapped
    destination_id = id

    for map_numbers in map_subset:
        source_start = map_numbers[1]
        source_stop = map_numbers[1]+map_numbers[2]
        # Calculate new id if mapped
        if id >= source_start and id < source_stop:
            destination_id = (id-source_start) + map_numbers[0]
            break

    return destination_id


def get_all_ids(seeds, maps):
    """Converts all provided soil ids to location ids 
    according to the mapping patterns.
    Stores all intermediary ids during mapping and 
    returns a list with all ids for each initial seed id.

    Args:
        seeds (list): List of seed ids.
        maps (dict): Dict with mapping patterns converting from soil to location.

    Returns:
        list: List with list of all intermediary ids for each starting seed id. 
    """    
    ids = []
    for seed_id in seeds:
        soil_id = convert_id(seed_id, maps['seed-to-soil'])
        fertilized_id = convert_id(soil_id, maps['soil-to-fertilizer'])
        water_id = convert_id(fertilized_id, maps['fertilizer-to-water'])
        light_id = convert_id(water_id, maps['water-to-light'])
        temperature_id = convert_id(light_id, maps['light-to-temperature'])
        humidity_id = convert_id(
            temperature_id, maps['temperature-to-humidity'])
        location_id = convert_id(humidity_id, maps['humidity-to-location'])
        ids.append([seed_id, soil_id, fertilized_id, water_id, light_id,
                    temperature_id, humidity_id, location_id])

    return ids


def solution1(ids):
    ids.sort(key=lambda x: x[-1])
    closest_location = ids[0][-1]

    return closest_location


if __name__ == "__main__":
    data = read_file(5)
    all_maps = get_maps(data)
    all_seeds = get_seeds(data)
    all_ids = get_all_ids(all_seeds, all_maps)

    print(f'Solution to part 1: {solution1(all_ids)}')

    # Skipping part 2 for now
    # Brute force with all seeds takes too long
