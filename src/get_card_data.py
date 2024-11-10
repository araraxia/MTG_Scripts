#!/usr/bin/env python3

import requests

def get_card_data(card_name):
    url = f"https://api.scryfall.com/cards/named?fuzzy={card_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def main():
    card_name = input("Enter a card name: ")
    card_data = get_card_data(card_name)
    
    if card_data:
        print(f"Card name: {card_data['name']}")
        print(f"Set: {card_data['set_name']}")
        print(f"Type: {card_data['type_line']}")
    else:
        print("Card not found.")
        
if __name__ == "__main__":
    main()
    
