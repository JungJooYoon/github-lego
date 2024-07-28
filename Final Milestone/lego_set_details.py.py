import sqlite3
import pandas as pd

# Connect to the LEGO database
conn = sqlite3.connect('C:\\Users\\5akfl.MINI\\Downloads\\CSC370\\LEGO.db')
cursor = conn.cursor()

# Function to get the list of parts for a set
def get_parts_for_set(set_num):
    query = """
    SELECT p.part_num, p.name, ip.quantity, c.name as color
    FROM inventory_parts ip
    JOIN inventories i ON ip.inventory_id = i.id
    JOIN parts p ON ip.part_num = p.part_num
    JOIN colors c ON ip.color_id = c.id
    WHERE i.set_num = ?
    """
    cursor.execute(query, (set_num,))
    return cursor.fetchall()

# Function to get the list of minifigs for a set
def get_minifigs_for_set(set_num):
    query = """
    SELECT m.fig_num, m.name, im.quantity
    FROM inventory_minifigs im
    JOIN inventories i ON im.inventory_id = i.id
    JOIN minifigs m ON im.fig_num = m.fig_num
    WHERE i.set_num = ?
    """
    cursor.execute(query, (set_num,))
    return cursor.fetchall()

# Example set number to test the functions
example_set_num = '75252-1'

# Get parts and minifigs for the example set
parts_list = get_parts_for_set(example_set_num)
minifigs_list = get_minifigs_for_set(example_set_num)

# Display the results
parts_df = pd.DataFrame(parts_list, columns=['Part Number', 'Part Name', 'Quantity', 'Color'])
minifigs_df = pd.DataFrame(minifigs_list, columns=['Minifig Number', 'Minifig Name', 'Quantity'])

# Print the dataframes
print("Parts List for Set", example_set_num)
print(parts_df)

print("\nMinifigs List for Set", example_set_num)
print(minifigs_df)
