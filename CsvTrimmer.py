import csv
import os
import sys
from typing import Dict, List, Optional

cwd = os.path.join(os.getcwd())

RELEVANT_KEYS = []  # TODO: Ask the user to fill those in


def extract_data_from_csv(
        csv_file_path: str,
        delimiter: str = ";",
        relevant_keys: Optional[List[str]] = None
) -> Dict[str, Dict[str, str]]:
    with open(csv_file_path, mode="r") as infile:
        reader = csv.reader(infile, delimiter=delimiter)
        all_keys = next(reader)

        if relevant_keys is not None:
            keys = []
            indices = []
            for i, key in enumerate(all_keys):
                if key in relevant_keys:
                    keys.append(key)
                    indices.append(i)
        else:
            keys = all_keys
            indices = range(len(all_keys))

        relevant_data = {}
        for row in reader:
            relevant_data[row[0]] = dict(zip(keys, [row[i] for i in indices]))
        return relevant_data


def parse_to_csv(data: Dict[str, Dict[str, str]]):
    with open("result.csv", mode="w", newline="") as outfile:
        writer = csv.DictWriter(
            outfile,
            fieldnames=RELEVANT_KEYS,
            delimiter=';',
            quoting=csv.QUOTE_ALL
        )
        writer.writeheader()
        for v in data.values():
            writer.writerow(v)


if __name__ == "__main__":
    infile = os.path.join(cwd, sys.argv[1])

    relevant_data = extract_data_from_csv(infile, relevant_keys=RELEVANT_KEYS)
    parse_to_csv(relevant_data)
