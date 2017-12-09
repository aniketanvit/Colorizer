import csv

results = []
with open("color_categories.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)
# print(results[0])
row = results[0]
# row = ['#D19FE8', '#88540B', '#A52A2A']
converted_hex = []
for x in row:
    h = x.lstrip('#')
    # h = input('Enter hex: ').lstrip('#')
    converted_hex.append(tuple(int(h[i:i+2], 16) for i in (0, 2 ,4)))

with open('color_categories_rgb.csv', 'a') as the_file:
    for row in converted_hex:
        the_file.write(str(row).strip("() ") + '\n')
        # the_file.write('\n')
print(converted_hex)
