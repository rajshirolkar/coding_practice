def read_file(file_name):
    input_array = []
    with open(file_name, "r") as file:
        for line in file:
            input_array.append(line.strip())
        return input_array


lines = read_file("input.txt")


def mapper():
    pass


seeds = lines[0].split(":")[1].split()
seeds = list(map(int, seeds))
print(seeds)
i = 3
seed_to_soil = []
while len(lines[i].strip()) > 0:
    seed_to_soil.append(lines[i].strip())
    i += 1
print(seed_to_soil)

i += 2
soil_to_fertilizer = []
while len(lines[i].strip()) > 0:
    soil_to_fertilizer.append(lines[i].strip())
    i += 1
print(soil_to_fertilizer)

i += 2
fertilizer_to_water = []
while len(lines[i].strip()) > 0:
    fertilizer_to_water.append(lines[i].strip())
    i += 1
print(fertilizer_to_water)

i += 2
water_to_light = []
while len(lines[i].strip()) > 0:
    water_to_light.append(lines[i].strip())
    i += 1
print(water_to_light)

i += 2
light_to_temperature = []
while len(lines[i].strip()) > 0:
    light_to_temperature.append(lines[i].strip())
    i += 1
print(light_to_temperature)

i += 2
temperature_to_humidity = []
while len(lines[i].strip()) > 0:
    temperature_to_humidity.append(lines[i].strip())
    i += 1
print(temperature_to_humidity)

i += 2
humidity_to_location = []
while i < len(lines):
    humidity_to_location.append(lines[i].strip())
    i += 1
print(humidity_to_location)


def getRecord(num, mapping):
    for record in mapping:
        dst, src, val = list(map(int, record.split()))
        if num >= src and num <= src + val:
            # print(dst + num - src)
            return dst + num - src
    return num


def getLocationFromSoil(num):
    soil = getRecord(num, seed_to_soil)
    fertilizer = getRecord(soil, soil_to_fertilizer)
    water = getRecord(fertilizer, fertilizer_to_water)
    light = getRecord(water, water_to_light)
    temperature = getRecord(light, light_to_temperature)
    humidity = getRecord(temperature, temperature_to_humidity)
    location = getRecord(humidity, humidity_to_location)
    return location


locations = []
# for num in seeds:
#     print(getLocationFromSoil(num))
#     locations.append(getLocationFromSoil(num))

# print("seed ranges : ")
for i in range(0, len(seeds), 2):
    # print("seed ranges : ", seeds[i], seeds[i] + seeds[i + 1])
    for j in range(seeds[i], seeds[i] + seeds[i + 1]):
        # print("location : ", getLocationFromSoil(j))
        locations.append(getLocationFromSoil(j))


print(" min location : ", min(locations))
