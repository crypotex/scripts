import sys
import xml.etree.ElementTree as ET

inp_f = sys.argv[1]
out_f = sys.argv[2]

with open(inp_f) as f:
    data = f.readlines()

cleaned = []

for i in data:
    try:
        cleaned.append(ET.fromstring(i).text)
    except ET.ParseError:
        pass

with open(out_f, "w") as f:
    for i in cleaned:
        f.write("%s\n" % i)
    
    
