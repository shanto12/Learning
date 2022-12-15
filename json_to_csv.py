import json
import csv

json_file_path = r"C:/Users/shant/Downloads/splunk_run_query_result.json"
csv_file = r"C:/Users/shant/Downloads/splunk_run_query_result.csv"


# Opening JSON file and loading the data
# into the variable data
with open(json_file_path) as json_file:
    data = json.load(json_file)

keys = data[0].keys()

with open(csv_file, 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)



import os

# os.path.splitext('/home/user/somefile.txt')[0]
print(os.path.splitext("/home/user/somefile.txt")[0] + ".jpg")

