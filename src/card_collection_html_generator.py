#!/usr/bin/env python3

import json
import html

# Read the JSON file
with open('output/card_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Start the HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Card Collection</title>
    <style>
        .hidden { display: none; }
    </style>
    <script>
        function filterCards() {
            var filter = document.querySelector('input[name="filter"]:checked').value;
            var cards = document.querySelectorAll('.card');
            cards.forEach(function(card) {
                if (filter === 'all' || card.classList.contains(filter)) {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            });
        }
    </script>
</head>
<body>
    <h1>Card Data</h1>
    <div>
        <label><input type="radio" name="filter" value="all" checked onclick="filterCards()"> All</label>
        <label><input type="radio" name="filter" value="U" onclick="filterCards()"> Blue</label>
        <label><input type="radio" name="filter" value="R" onclick="filterCards()"> Red</label>
        <label><input type="radio" name="filter" value="G" onclick="filterCards()"> Green</label>
        <label><input type="radio" name="filter" value="B" onclick="filterCards()"> Black</label>
        <label><input type="radio" name="filter" value="W" onclick="filterCards()"> White</label>
    </div>
"""

# Process each card in the data
for card in data['data']:
    try:
        colors = ' '.join(card['colors'])
        html_content += f"""
        <div class="card {html.escape(colors)}">
            <h2>{html.escape(card['name'])}</h2>
            <p><strong>ID:</strong> {html.escape(card['id'])}</p>
            <p><strong>Oracle ID:</strong> {html.escape(card['oracle_id'])}</p>
            <p><strong>Released At:</strong> {html.escape(card['released_at'])}</p>
            <p><strong>Mana Cost:</strong> {html.escape(card['mana_cost'])}</p>
            <p><strong>CMC:</strong> {html.escape(str(card['cmc']))}</p>
            <p><strong>Type Line:</strong> {html.escape(card['type_line'])}</p>
            <p><strong>Oracle Text:</strong> {html.escape(card['oracle_text'])}</p>
            <p><strong>Colors:</strong> {html.escape(', '.join(card['colors']))}</p>
            <p><strong>Color Identity:</strong> {html.escape(', '.join(card['color_identity']))}</p>
            <img src="{html.escape(card['image_uris']['normal'])}" alt="{html.escape(card['name'])}">
        </div>
        """
    except KeyError:
        continue

# End the HTML content
html_content += """
</body>
</html>
"""

# Write the HTML content to a file with utf-8 encoding
with open('output/card_data.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

print("HTML file has been generated.")