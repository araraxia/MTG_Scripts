#!/usr/bin/env python3
"""
This script processes a list of Magic: The Gathering card names from a text file, 
removing tags and empty lines, and then sorts the list.
Functions:
    import_file(file_path): Reads the file at the given path and returns a list of lines.
    strip_tags(card_list): Removes specific tags from each card name in the list.
    remove_empty(card_list): Removes empty lines from the list.
    main(input_file_path=None): Main function that processes the input file and prints the sorted list.
Usage:
    python txt_list_sort.py <input_file_path>
"""

import re, sys

TAG_STRIP_REGEX = r"[0-9]+x|\*.*$|\(.*$|\#.*$"
FIX_DUAL_CARD_REGEX = r"(\w+)\s?\/{1,2}\s?(\w+)"

def import_file(file_path):
    try:
        with open(file_path, 'r') as file:
            card_list = file.readlines()
            
    except FileNotFoundError:
        card_list = []
    
    return card_list

def save_file(file_path, card_list):
    with open(file_path, 'w') as file:
        for each_card in card_list:
            file.write(each_card + "\n")

def fix_card_list(card_list):
    new_list = []
    for each_card in card_list:
        
        if each_card is None or each_card == '':
            continue
        
        each_card = re.sub(TAG_STRIP_REGEX, '', each_card, flags=re.MULTILINE | re.DOTALL).strip()
        each_card = re.sub(FIX_DUAL_CARD_REGEX, r'\1 // \2', each_card)
        
        if each_card not in new_list:
            new_list.append(each_card)
            
    return sorted(new_list)
    
        
def main(ran_manual = False):
    if len(sys.argv) != 2:
        print("No input file path provided. Exiting.")
        sys.exit(1)

    input_file_path = sys.argv[1]
    card_list = import_file(input_file_path)
    
    if card_list:
        fixed_card_list = fix_card_list(card_list)
        
        if ran_manual:
            save_file(input_file_path, fixed_card_list)
            
        return fixed_card_list
    
    print("Error processing file, no list to output. Exiting.")
    return []

if __name__ == "__main__":
    print("Fixing text file and saving sorted list...")
    main(True)
