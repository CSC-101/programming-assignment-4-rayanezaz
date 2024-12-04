import sys
import pickle
import os

def dataset_loaded(filePath):
    try:
        with open(filePath, 'rb') as f:
            data = pickle.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: File '{filePath}' cannot be found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error with loading data: {e}")
        sys.exit(1)

def display(data):
    for i in data:
        print(i)
    print(f"Total entries: {len(data)}")


#The purpose of this function is to filter the counties through abbreviating them
def filterST(data, stateAbbrev):
    filt = [county for county in data if county.get("State") == stateAbbrev]
    print(f"Filter: state == {stateAbbrev} ({len(filt)} entries)")
    return filt

#The purpose of this function is to filter the counties by greater field value
def filterGT(data, field, val):

    filt = [county for county in data if county.get(field, 0) > val]
    print(f"Filter: {field} gt {val} ({len(filt)} entries)")
    return filt

#The purpose of this function is to filter the counties by less field value
def filterLT(data, field, val):
    filt = [county for county in data if county.get(field, 0) < val]
    print(f"Filter: {field} lt {val} ({len(filt)} entries)")
    return filt

#The purpose of this function is to print every counties 2014 population
def population_total(data):
    total_pop = sum(county.get("2014 Population", 0) for county in data)
    print(f"2014 population: {total_pop}")

#The purpose of this function is to print the total sup-population for a percentage-based field
def populationField(data, field):
    total = sum(
        county.get("2014 Population", 0) * (county.get(field, 0) / 100)
        for county in data
    )
    print(f"2014 {field} population: {total}")

#The purpose of this function is to print the percentage of the total population in a sup-population for a field
def percentField(data, field):
    total_pop = sum(county.get("2014 Population", 0) for county in data)
    if total_pop == 0:
        print(f"2014 {field} percentage: 0")
        return
    sub_pop = sum(
        county.get("2014 Population", 0) * (county.get(field, 0) / 100)
        for county in data
    )
    perc = (sub_pop / total_pop) * 100
    print(f"2014 {field} percentage: {perc}")

#The purpose of this function is to read the operations file and execute commands
def process_ops(file_path, data):
    try:
        with open(file_path, 'r') as f:
            operations = f.readlines()
    except FileNotFoundError:
        print(f"Error: Cannot find operations file '{file_path}'.")
        sys.exit(1)

    for lineNum, line in enumerate(operations, 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        try:
            parts = line.split(":")
            command = parts[0]

            if command == "display":
                display(data)
            elif command == "filter-state":
                stateAbbrev = parts[1]
                data = filterST(data, stateAbbrev)
            elif command == "filter-gt":
                field, val = parts[1], float(parts[2])
                data = filterGT(data, field, val)
            elif command == "filter-lt":
                field, val = parts[1], float(parts[2])
                data = filterLT(data, field, val)
            elif command == "population-total":
                population_total(data)
            elif command == "population":
                field = parts[1]
                populationField(data, field)
            elif command == "percent":
                field = parts[1]
                percentField(data, field)
            else:
                print(f"Error: Line {lineNum}: {line} with unknown command")
        except (IndexError, ValueError) as e:
            print(f"Error: Line {lineNum}: {line} ({e}) with malformed operation")
            continue

#The purpose of this function is to check for command-line arguments
def main():
    if len(sys.argv) != 2:
        print("Usage: python hw4.py <operations_file>")
        sys.exit(1)

    dataset_path = "county_demographics.data"
    if not os.path.exists(dataset_path):
        print(f"Error: Cannot find dataset file '{dataset_path}'.")
        sys.exit(1)

    data = dataset_loaded(dataset_path)
    print(f"Number of entries: {len(data)}")

    ops_file = sys.argv[1]
    process_ops(ops_file, data)

if __name__ == "__main__":
    main()