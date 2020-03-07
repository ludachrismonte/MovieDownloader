# MovieDownloader
Downloads short .ts files (10 second movie clips) and outputs a full movie.

This was written to interface with the website gomovies.digital

To use:
1. Find a movie on the website that you want to download.
1. Start streaming the movie. 
1. Use devtools to find the .ts files that are being streamed.
1. Copy the source URL of the .ts file. (this contains your site token and the movie ID)
1. Paste the URL into the script, and replace the segment piece with !!!!, so that the script can switch in values to download every segment. 
1. Change the name of the output file. 
1. Run the script. (python3 get.py)
