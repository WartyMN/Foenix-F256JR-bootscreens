# Python program to read
# json file
  
  
import json
  
# Opening JSON file
f = open('screens/Untitled Screen.json', 'rb')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

# arrays to hold chars and processed attribute values
chars = bytearray()
attrs = bytearray()

# Iterating through the json
# list
for layer in data['layers']:
	if layer['label'] == 'F256JR the 2nd':
		for frame in layer["frames"]:
			for data in frame["data"]:
				for cell in data:
					tile = cell["t"]
					fore_color = cell["fc"]
					back_color = cell["bc"]
					
					if back_color == -1:
						back_color = 2 # dark blue
										
					if fore_color == -1:
						fore_color = 2 # dark blue
						
					the_attribute_value = ((fore_color << 4) | back_color);

					chars.append(tile)
					attrs.append(the_attribute_value)
  
# Closing file
f.close()

# write out data to 2 .bin binary files
with open('f256jr2_boot_chars.bin', 'wb') as f:
	f.write(chars)


with open('f256jr2_boot_attrs.bin', 'wb') as f:
	f.write(attrs)

