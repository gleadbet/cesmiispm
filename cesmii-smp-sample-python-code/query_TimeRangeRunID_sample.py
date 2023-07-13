import os

import dotenv

import SMplatform as smp

dotenv.load_dotenv()
endpoint_url = str(os.environ.get("endpoint_url"))
header = smp.SMP_auth()
print(endpoint_url)
print(header)

runID = "SIM-0126"

StartandEnd = smp.getStartandEndTime(runID, endpoint_url, header)

print("\nRunID selected: " + runID)
print("\nStart of Run: " + StartandEnd[0])
print("End of Run: " + StartandEnd[1] + "\n")

# below are examples on how to use runID:
# searching for multiple/all runID's
runID = "0"
# search for multiple runs with similar/same names
# my_query = smp.build_RunIDts_Query(f"startsWith: \"{runID}\" ")
my_query = smp.build_RunIDts_Query(f'notEqualTo: "{runID}" ')
result = smp.request(my_query, endpoint_url, header)  # Execute the query

runID_List = result["data"]["getRawHistoryDataWithSampling"]

# for x in runID_List:
#    print(x)
