from aoc_common import read_file
import regex as re


def get_maps(data):
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
    seeds = [int(seed_id) for seed_id in re.findall(r'\d+', data[0])]
    return seeds


def convert_ids(id, map_subset):
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
    ids = []
    for seed_id in seeds:
        soil_id = convert_ids(seed_id, maps['seed-to-soil'])
        fertilized_id = convert_ids(soil_id, maps['soil-to-fertilizer'])
        water_id = convert_ids(fertilized_id, maps['fertilizer-to-water'])
        light_id = convert_ids(water_id, maps['water-to-light'])
        temperature_id = convert_ids(light_id, maps['light-to-temperature'])
        humidity_id = convert_ids(
            temperature_id, maps['temperature-to-humidity'])
        location_id = convert_ids(humidity_id, maps['humidity-to-location'])
        ids.append([seed_id, soil_id, fertilized_id, water_id, light_id,
                    temperature_id, humidity_id, location_id])

    return ids


def solution1(ids):
    ids.sort(key=lambda x: x[-1])
    closest_location = ids[0][-1]

    return closest_location


data = read_file(5)
all_maps = get_maps(data)
all_seeds = get_seeds(data)
all_ids = get_all_ids(all_seeds, all_maps)

print(solution1(all_ids))

# Skipping part 2 for now
# Brute force with all seeds takes too long
