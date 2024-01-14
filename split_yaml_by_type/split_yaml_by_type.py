import yaml
import os

def create_yaml_files(input_file):
    with open(input_file, 'r') as file:
        data = yaml.safe_load(file)

    # Create a dictionary to store entries based on 'type'
    type_entries = {}

    # Organize entries based on 'type'
    for entry in data['references']:
        entry_type = entry.get('type')
        if entry_type not in type_entries:
            type_entries[entry_type] = []
        type_entries[entry_type].append(entry)

    # Create a new YAML file for each 'type'
    for entry_type, entries in type_entries.items():
        output_file = f"{entry_type}_entries.yaml"
        with open(output_file, 'w') as file:
            yaml.dump(entries, file)

    print("YAML files created successfully.")

# Replace 'your_input_file.yaml' with the actual name of your YAML file
create_yaml_files('boehm.yaml')
