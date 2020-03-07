import requests

# ~~~~~~~~~~~~~~~~~~~~~~~ Replace These 3 Lines ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
FILENAME = "Survivor"
url_raw = 'https://stream-5-1.loadshare.org/stream3/VideoID-iiX3ZVR2/ekQTaZA6p205SHh8WeRhHj6Lh84-5b7g9CM7IFoakxc4WNZ_woX4XHuJO5EBLGsYQcRHHfsuu8mdIv0xCilUPZZ7GkzlIIoicNYbOWVXMcGiLVT8OJ4wiK0XTjhun9HfmcANkK_YdJfLUy7wAeNxxg/seg-!!!!-f2-v1-a1.ts?token=ip=198.0.97.237~st=1583543364~exp=1583557764~acl=/*~hmac=b00d2a075836d1ae8f68bfc0f07515cfa96d48faf64cb4eca1f9d240973666bb'

file = open(FILENAME + '.ts', 'ba')
segment = 0

while True:
	print("Getting Segment: " + str(segment))
	url = url_raw.replace("!!!!", str(segment))
	myfile = requests.get(url)
	if myfile.status_code == 404:
		break
	file.write(myfile.content)
	segment += 1

print("done!")