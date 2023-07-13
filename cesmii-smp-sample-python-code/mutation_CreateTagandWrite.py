import csv
import os

import dotenv

import SMplatform as smp

dotenv.load_dotenv()
endpoint_url = str(os.environ.get("endpoint_url"))
header = smp.SMP_auth()
print(endpoint_url)
print(header)
Connector_Identifier = "Demo"

# for example only
my_query = smp.build_CreateTag_Mutation("RSB_Test")
# result = smp.request(my_query, endpoint_url, header)
my_query = smp.build_CreateTag_Mutation("RSB_Test_int", "INT", "This is only a test")
# result = smp.request(my_query, endpoint_url, header)


my_query = smp.build_TagList_Query("RSB")
result = smp.request(my_query, endpoint_url, header)
tagList = result["data"]["tags"]

# print (my_query)
tagID: str = ""

# tag I want to use and check if present
# tagName = "CCAM_CVI_SIM.ProcessTool_STATE"
tagName = "RSB_Test_Float"

# search for tag in list
for i in tagList:
    if i["displayName"] == tagName:
        tagID = i["id"]

# if tag not present create tag
if tagID == "":
    print("\ntag not in list and will be added\n")
    my_mutation = smp.build_CreateTag_Mutation(tagName, "FLOAT", "This is only a test")
    print(my_mutation)
    result = smp.request(my_mutation, endpoint_url, header)
    print(result)

    # after tag added rebuild tag list:
    result = smp.request(my_query, endpoint_url, header)
    tagList = result["data"]["tags"]

    for i in tagList:
        if i["displayName"] == tagName:
            tagID = i["id"]


print(f"\n{tagName} tagID: {tagID}\n")

# log update to my tag now
# my_mutation=smp.build_UpdateTagTS_Mutation(tagID, "3.14")
# result = smp.request(my_mutation, endpoint_url, header)
# print(result)

# log update to my tag at a specific time
# my_mutation=smp.build_UpdateTagTS_Mutation(tagID, "3.14", "2021-01-06T14:20:30-05:00")
# result = smp.request(my_mutation, endpoint_url, header)

# log all values saved in csv to tag
with open("Book1.csv", newline="") as f:
    reader = csv.reader(f)
    data = list(reader)

for x in data:
    if x[0] != "":
        my_mutation = smp.build_UpdateTagTS_Mutation(tagID, x[0], x[1])
        print(my_mutation)
        result = smp.request(my_mutation, endpoint_url, header)
        print(result)
