import requests

# ~~~~~~~~~~~~~~~~~~~~~~~ Replace These 2 Lines ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
FILENAME = "PLACEHOLDER"
url_raw = ""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

file = open(FILENAME + ".ts", "ba")
segment = 0

while True:
	print("Getting Segment: " + str(segment))
	response = requests.get(url_raw.replace("!!!!", str(segment)))
	if response.status_code == 404:
		print("done!")
		break
	file.write(response.content)
	segment += 1
