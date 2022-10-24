import requests
import time

# Python code to
# demonstrate readlines()

# L = ["Geeks\n", "for\n", "Geeks\n"]

# # writing to file
# file1 = open('myfile.txt', 'w')
# file1.writelines(L)
# file1.close()

def get_redirected_url(url):
    #url = "https://lnkd.in/dBTsJbhz"
    url = url.strip()
    response = requests.get(url)
    if response.history:
        print("Request was redirected")
        #for resp in response.history:
        #    print(resp.status_code, resp.url)
        print("Final destination:")
        print(response.url)
        return(response.url)
    response.close()
    # else:
    #     print("Request was not redirected")

# Using readlines()
file1 = open('devops.txt', 'r')
Lines = file1.readlines()

formatted_text = []
# Strips the newline character
for line in Lines:
    #print(line)
    if "https" in line:
       print(line)
       
       #print(get_redirected_url(line))
       formatted_text.append(get_redirected_url(line))
    else:
        formatted_text.append(line)

with open('devops_formatted.txt', 'w') as f:
    for line in formatted_text:
        f.write("%s\n" % line)
	#print("Line{}: {}".format(count, line.strip()))

