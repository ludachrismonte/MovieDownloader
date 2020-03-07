# MovieDownloader
Downloads short .ts files (10 second movie clips) and outputs a full movie.

This was written to interface with the website gomovies.digital

## To use get.py:
1. Find a movie on gomovies.digital that you want to download.
1. Start streaming the movie. 
1. Use chrome devtools (the network analyzer) to find the .ts files that are being streamed.
1. Copy the source URL of the .ts file into get.py (this contains your site token and the movie ID). Example URL: https://stream-5-1.loadshare.org/stream3/VideoID-blahblahblah/blahblahblah-blahblahblah/seg-1-f2-v1-a1.ts?token=ip=0.0.0.0~st=blahblahblah~exp=blahblahblah~acl=/*~hmac=blahblahblah
1. Paste the URL into line 5 in the script, and replace the number in the URL after "/seg-" with "!!!!", so that the script knows where to insert new segment values to download every segment. Example: "/seg-1-f2-v1-a1.ts?" becomes "/seg-!!!!-f2-v1-a1.ts?"
1. Edit line 4 to be the desired name of your output file.
1. Run the script with `python3 get.py`
