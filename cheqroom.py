import os
import re

import pandas as pd
import openai
from dotenv import load_dotenv

# Load your OpenAI API key
load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")
client = openai.Client()

# Example prompt template with provided examples
example_prompt_template = (
    "I need to extract concise item names from detailed product descriptions like in these examples:\n"
    "1. Description: 'SAMSUNG 27\" T35F Series FHD 1080p Computer Monitor, 75Hz, IPS Panel, HDMI, VGA (D-Sub), 3-Sided Border-Less, FreeSync, LF27T350FHNXZA'. Name: 'Samsung 27\" Monitor'\n"
    "2. Description: 'Ray-Ban Meta - Wayfarer (Standard) Smart Glasses - Shiny Black, Clear'. Name: 'Ray-Ban Meta - Glasses'\n\n"
    "Here is another description from an online store: '{description}'. Based on these examples, extract the most relevant and concise item name."
)


# Function to generate item name using OpenAI
def generate_item_name(description):
    try:
        prompt = example_prompt_template.format(description=description)
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        # print(response)
        generated_text = response.choices[0].message.content

        # Remove "Name:" prefix if present
        generated_text = re.sub(r'^Name:\s*', '', generated_text).strip()
        print("Generated text:", generated_text)
        return generated_text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return None


# Read the CSV file
df = pd.read_csv('updated_inventory.csv')


# Generate item names
# df['Item Name'] = df['Item Description'].apply(generate_item_name)

# Function to remove quotes from item names
def remove_quotes(item_name):
    print(item_name.strip("'\""))
    return item_name.strip("'\"")


# Remove quotes from the item names
df['Item Name'] = df['Item Name'].apply(remove_quotes)

# Save the DataFrame back to CSV
df.to_csv('updated_inventory.csv', index=False)
