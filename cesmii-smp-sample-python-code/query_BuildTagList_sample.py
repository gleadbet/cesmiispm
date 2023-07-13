import os

import dotenv

import SMplatform as smp

# SMP header setup
dotenv.load_dotenv()
endpoint_url = str(os.environ.get("endpoint_url"))
header = smp.SMP_auth()
print(endpoint_url)
print(header)
Connector_Identifier = "MQTT_Connector"

indentifier = "CCAM_CVI_Sim"
my_query = smp.build_TagList_Query(indentifier)
result = smp.request(my_query, endpoint_url, header)

tagList = result["data"]["tags"]
print(
    f"\nThere is a total of {len(tagList)} tags in the tag list asscociated with {indentifier}:\n"
)
for x in tagList:
    print(x["displayName"])

# timestamp = calendar.timegm(time.localtime())

# with open(f'{indentifier}_{timestamp}.json', 'w') as f:
#    json.dump(result, f)
