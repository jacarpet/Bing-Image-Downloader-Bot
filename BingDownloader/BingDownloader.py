
import sys
import subprocess
import pkg_resources



from bing_image_downloader import downloader

args = sys.argv
numArgs = len(args)
searchAmount = args[numArgs - 1]
searchQuery = ""
for x in range(numArgs - 1):
    if(x > 0 and x != numArgs - 1):
        searchQuery += args[x] + " "
    

def SearchBing(query, amount):
    downloader.download(query, limit = int(amount), adult_filter_off = True)
    
SearchBing(searchQuery,searchAmount)
print("Download Succesful")