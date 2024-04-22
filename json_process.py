import pandas as pd
import json

def load_and_process_jsonl(file_path):
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Convert each line to a dictionary
                json_record = json.loads(line.strip())
                
                # Flatten 'arca' dictionary into the main dictionary, if it exists
                if 'arca' in json_record:
                    for key, value in json_record['arca'].items():
                        json_record['arca_' + key] = value
                    del json_record['arca']
                
                data.append(json_record)
        
        # Create a DataFrame from the list of dictionaries
        return pd.DataFrame(data)
    except Exception as e:
        print(f"Error processing file: {e}")
        return None
