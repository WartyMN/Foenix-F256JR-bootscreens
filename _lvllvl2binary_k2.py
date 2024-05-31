# Python program to read
# json file
  
  
import json
  
# Opening JSON file
f = open('screens/Untitled Screen.json', 'rb')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

# arrays to hold chars and processed attribute values
chars = []
attrs = []

# Iterating through the json
# list
for layer in data['layers']:
	if layer['label'] == 'F256K2':
		for frame in layer["frames"]:
			for data in frame["data"]:
				for cell in data:
					tile = cell["t"]
					fore_color = cell["fc"]
					back_color = cell["bc"]
					
					if back_color == -1:
						back_color = 1 # dark blue
										
					if fore_color == -1:
						fore_color = 1 # dark blue
						
					the_attribute_value = ((fore_color << 4) | back_color);

					#print(tile, fore_color, back_color, the_attribute_value)
					
					chars.append(tile)
					attrs.append(the_attribute_value)
  
# Closing file
f.close()

# write out data to 2 .bin binary files
with open('f256k2_boot_chars.bin', 'w') as f:
	for char in chars:
		f.write('{:c}'.format(char))


with open('f256k2_boot_attrs.bin', 'w') as f:
	for attr in attrs:
		f.write('{:c}'.format(attr))

