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



"""
Output:

Parts List for Set 75252-1
    Part Number                                          Part Name  Quantity              Color
0         10202                       Tile 6 x 6 with Bottom Tubes         9  Light Bluish Gray
1         10247  Plate Special 2 x 2 with 1 Pin Hole [Complete ...         2                Red
2         11211         Brick Special 1 x 2 with 2 Studs on 1 Side         6                Tan
3         11212                                        Plate 3 x 3        18                Red
4         11212                                        Plate 3 x 3        12  Light Bluish Gray
..          ...                                                ...       ...                ...
478       99774                           Sports Ski without Hinge         3   Dark Bluish Gray
479       99780                     Bracket 1 x 2 - 1 x 2 Inverted         4  Light Bluish Gray
480       99781                              Bracket 1 x 2 - 1 x 2         2              White
481       99781                              Bracket 1 x 2 - 1 x 2        15  Light Bluish Gray
482       99784  Bar 1 x 12 with 1 x 2 Plate End with Hollow St...         1        Trans-Clear

[483 rows x 4 columns]

Minifigs List for Set 75252-1
  Minifig Number                                       Minifig Name  Quantity
0     fig-004467  Imperial Crew, Light Bluish Gray Uniform, Dark...         1
1     fig-004471  Imperial Officer / Lieutenant, Dark Bluish Gra...         1
"""

