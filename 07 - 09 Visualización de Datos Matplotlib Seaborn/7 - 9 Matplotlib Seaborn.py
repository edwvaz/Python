fbk = ['Facebook', 2449, True, 2006]
twt = ['Twitter', 339, False, 2006]
ig = ['Instagram', 1000, True, 2010]
yt = ['YouTube', 2000, False, 2005]
lkn = ['LinkedIn', 663, False, 2003]
wsp = ['WhatsApp', 1600, True, 2009]

df['fbk']
# Sample list of lists
data_list = [[1, 'a', 'x'], [2, 'b', 'y'], [3, 'c', 'z']]

# Define column names
columns = ['Column1', 'Column2', 'Column3']

# Initialize empty list
data_rows = []

# Iterate through the list of lists
for row_list in data_list:
    row_dict = {}  # Create a dictionary for each row
    for i, value in enumerate(row_list):
        row_dict[columns[i]] = value  # Assign value to corresponding column
    data_rows.append(row_dict)  # Append row dictionary to the list

# Display the constructed rows
for row in data_rows:
    print(row)