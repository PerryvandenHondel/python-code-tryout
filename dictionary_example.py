#
# PYTHON SCRIPT example of dictionary usage (Marketplace Solution)
#
# See: https://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python/

#
# Generate some example data:
#

our_key_value_list = {
    'key_one': 'value_one',
    'key_two': 'value_two',
    'key_three': 'value_three',
}

#
# Adding a key-value pair:
#
our_key_value_list['key_four'] = 'value_four'


#
# Print complete dictionary:
#
print("\n", our_key_value_list, "\n")


#
# Print value of specific key:
#
print("key_four", ":", our_key_value_list.get("key_four"), "\n")

#
# Get length of dictionary:
#
print("Dictionary length:", len(our_key_value_list), "\n")

#
# Print all keys in the list:
#
for key in our_key_value_list:
    print(key)

# Print empty line:
print("\n")

#
# Print all values in the list:
#
for key,val in our_key_value_list.items():
    print(val)

# Print empty line:
print("\n")

#
# Print all key-value pairs:
#
for key,val in our_key_value_list.items():
    print(key, ":", val)


# Print empty line:
print("\n")


#
# Writing contents of dictionary to a file (JSON):
#
# See: https://stackoverflow.com/questions/36965507/writing-a-dictionary-to-a-text-file

import json

json = json.dumps(our_key_value_list)
f = open("dict.json","w")
f.write(json)
f.close()

#
# Reading contents of JSON-file into dictionary:
#
import json

with open('dict.json') as json_file:
    imported_key_value_list = json.load(json_file)



# Print empty line:
print("\n")

# Print notification:
print("IMPORTED FROM JSON...", "\n")


#
# Print all key-value pairs:
#
for key, val in imported_key_value_list.items():
        print(key, ":", val)
