def main():
    bacteria_types_count = int(input())
    bacteria_viable_temperatures = tuple(tuple(map(int, input().split())) for _ in range(bacteria_types_count))
    for planet_temperature in map(int, input().split()):
        result_count_planet = 0
        for bacteria_viable_temperature in bacteria_viable_temperatures:
            result_count_planet += bacteria_viable_temperature[0] <= planet_temperature <= bacteria_viable_temperature[
                1]
        print(result_count_planet)


if __name__ == "__main__":
    main()
