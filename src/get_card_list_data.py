#!/usr/bin/env python3

import requests, json, sys, txt_list_sort


with open('conf/scryfall_headers.json') as f:
    SCRYFALL_HEADERS = json.load(f)
    
REQUEST_BATCH_SIZE = 75
COLLECTION_ENDPOINT = "https://api.scryfall.com/cards/collection"
DEFAULT_OUTPUT = "output/card_data.json"
    
    
def get_collection_data(card_list):
    """
    Fetches collection data for a list of Magic: The Gathering cards from the Scryfall API.
    This function processes the card list in batches defined by REQUEST_BATCH_SIZE, sends a POST request
    to the Scryfall API for each batch, and aggregates the responses into a single response.
    Args:
        card_list (list): A list of card names to fetch data for.
    Returns:
        dict: A dictionary containing the aggregated response data from the Scryfall API.
    """
    
    full_response = None
    
    for i in range(0, len(card_list), REQUEST_BATCH_SIZE):
        batch = card_list[i:i + REQUEST_BATCH_SIZE]

        print(f"Processing batch {i // REQUEST_BATCH_SIZE + 1}: {batch}")
        
        body = {
            "identifiers": [{"name": card_name} for card_name in batch]
        }
    
        response = requests.post(COLLECTION_ENDPOINT, headers=SCRYFALL_HEADERS, json=body)
        
        if full_response:
            full_response["data"].extend(response.json()["data"])
        else:
            full_response = response.json()
            
    return full_response
    
def save_response(response, output_path=DEFAULT_OUTPUT):
    with open(output_path, "w") as file:
        json.dump(response, file, indent=4)    
    
def catch_arg():
    if len(sys.argv) < 2:
        print("No input file path provided. Exiting.")
        sys.exit(1)
    
    arg = sys.argv[1]
    if arg == "-h" or arg == "--help":
        print("Usage: python get_card_list_data.py <input_file_path>")
        print("Options:")
        print("  -h, --help: Show this help message and exit.")
        sys.exit(0)
        
    input_file_path = sys.argv[1]
    
    if input_file_path is None:
        print("No input file path provided. Exiting.")
        sys.exit(1)
        
    return input_file_path
    
def main():
    input_file_path = catch_arg()
    card_list = txt_list_sort.main(input_file_path)
    response = get_collection_data(card_list)
    
    save_response(response)

            
if __name__ == "__main__":
    main()
        
    