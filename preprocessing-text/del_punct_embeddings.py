import sys
import re
import string

punc_to_remove = string.punctuation[0:6] + string.punctuation[7:]

rgx = re.compile('[%s]' % punc_to_remove)

data = []
with open(sys.argv[1]) as f:
    for i in f:
        row = rgx.sub("", i.strip())
        data.append("%s\n" % row)

with open(sys.argv[2], "w") as g:
    g.writelines(data)
