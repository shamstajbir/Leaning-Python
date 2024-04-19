def read_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [int(line.strip()) for line in file]
            return numbers
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

def write_sum_to_file(filename, total):
    with open(filename, 'w') as file:
        file.write(str(total))

def main():
    input_filename = "numbers.txt"
    output_filename = "sum.txt"


    numbers = read_numbers_from_file(input_filename)


    total = sum(numbers)


    write_sum_to_file(output_filename, total)

    print(f"Sum of numbers has been written to '{output_filename}'.")

if __name__ == "__main__":
    main()
