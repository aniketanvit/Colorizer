row = ['#D19FE8', '#88540B', '#A52A2A']
converted_hex = []
for x in row:
    h = x.lstrip('#')
    # h = input('Enter hex: ').lstrip('#')
    converted_hex.append(tuple(int(h[i:i+2], 16) for i in (0, 2 ,4)))

print(converted_hex)
