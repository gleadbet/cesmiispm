import calendar
import json
import os
import time

import dotenv

import SMplatform as smp

dotenv.load_dotenv()
endpoint_url = str(os.environ.get("endpoint_url"))
header = smp.SMP_auth()
print(endpoint_url)
print(header)

process_start = "2020-12-1T09:54:00-05:00"
process_end = "2020-12-18T10:26:30-05:00"
# process_end = "now"
# process_tags = '''["5776","5767","5759", "5765"]''' #example of requesting multiple values at once
process_tags = """["5776"]"""  # example of only one data point

my_query = smp.build_tsData_Query(process_tags, process_start, process_end)
print(my_query)
result = smp.request(my_query, endpoint_url, header)  # Execute the query
# print (result)

tagList = result["data"]

filename = "data"
timestamp = calendar.timegm(time.localtime())

with open(f"{filename}_{timestamp}.json", "w") as f:
    json.dump(result, f)
