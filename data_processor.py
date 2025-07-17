import sys
from calculations import perform_calculations

def read_input_file(file_path):
    # Reads a file and returns a list of float numbers.
    try:
        with open(file_path, 'r') as file:
            numbers = [float(line.strip()) for line in file if line.strip()]
        return numbers
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        sys.exit(1)
    except ValueError:
        print("Error: Non-numeric data found in input file.")
        sys.exit(1)

def write_output_file(output_path, results):
    # Writes results to an output file.
    try:
        with open(output_path, 'w') as file:
            file.write("Processed Results:\n")
            file.write(f"Sum: {results['Sum']}\n")
            file.write(f"Difference (Max - Min): {results['Difference (Max - Min)']}\n")
            file.write(f"Average: {results['Average']}\n\n")

            file.write("Squares:\n")
            for val in results["Squares"]:
                file.write(f"{val}\n")

            file.write("\nSquare Roots:\n")
            for val in results["Square Roots"]:
                file.write(f"{val}\n")
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)

def main():
    # Main execution function
    if len(sys.argv) < 2:
        print("How to use standalone: python data_processor.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "output_data.txt"

    data = read_input_file(input_file)
    results = perform_calculations(data)
    write_output_file(output_file, results)

    print(f"Processing complete. Results written to {output_file}")

if __name__ == "__main__":
    main()
