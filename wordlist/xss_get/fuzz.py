import wfuzz

f = open("xss_get.txt", "r")
host = "192.168.0.38"
dic = "./output.txt"
line = None
while line != "":
    line = f.readline()
    if line != "":
        for r in wfuzz.fuzz(url="http://"+host+line, hc=[404], payloads=[("file",dict(fn=dic))]):
            print(r)