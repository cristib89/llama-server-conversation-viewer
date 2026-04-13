import json
import os
import sys
from datetime import datetime

def split_llama_conversations(input_file):
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        return

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: '{input_file}' is not a valid JSON file.")
        return

    if not isinstance(data, list):
        print("Error: JSON root must be an array.")
        return

    for entry in data:
        conv = entry.get('conv', {})
        if not conv:
            continue

        try:
            # 1. Convert lastModified (ms) to formatted timestamp
            ms_timestamp = conv.get('lastModified', 0)
            dt_object = datetime.fromtimestamp(ms_timestamp / 1000.0)
            ts_str = dt_object.strftime('%Y-%m-%d_%H-%M-%S')

            # 2. Get first segment of UUID
            conv_id = conv.get('id', 'unknown-0000')
            uuid_segment = conv_id.split('-')[0]

            # 3. Clean and Truncate the 'name'
            raw_name = conv.get('name', 'untitled_conv')[:20]
            
            # Standardize formatting: lowercase and replace dashes
            clean_suffix = raw_name.lower().replace('-', '_').replace('—', '_').replace(' ', '_')
            
            # Remove non-alphanumeric (except underscores) for OS safety
            clean_suffix = "".join(c for c in clean_suffix if c.isalnum() or c == '_')
            
            # TRUNCATE: Limit to 20 characters and strip trailing underscores
            clean_suffix = clean_suffix.strip('_')

            # 4. Construct Filename
            file_name = f"{ts_str}_conv_{uuid_segment}_{clean_suffix}.json"

            # 5. Write individual file
            with open(file_name, 'w', encoding='utf-8') as out_f:
                json.dump(entry, out_f, indent=4)
            
            print(f"Generated: {file_name}")

        except Exception as e:
            print(f"Skipping entry due to error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split.py <filename.json>")
    else:
        split_llama_conversations(sys.argv[1])
