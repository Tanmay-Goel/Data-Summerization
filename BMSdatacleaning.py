import re
import string

f=open(r"C:\Users\goelt\Downloads\AboutBMSCE\AboutBMSCE.txt")

input_str=f.read()


#removing excess inbetween whitespace
_RE_COMBINE_WHITESPACE = re.compile(r"(?a:\s+)")
_RE_STRIP_WHITESPACE = re.compile(r"(?a:^\s+|\s+$)")
input_str = _RE_COMBINE_WHITESPACE.sub(" ", input_str)
input_str = _RE_STRIP_WHITESPACE.sub("", input_str)

#removing trailing and leading white space
input_str = input_str.strip()  

#removing double quotes
x=re.compile(r'"')
s=1
while s==1:
    m=re.search(x,input_str)
    if m==None:
        s=0
    else:
        input_str=re.sub(x, "", input_str)
        
#deleting punctuation except fullstop, comma and apostrophe
b=''
to_delete = set(string.punctuation) - {".", ",", "'", "-", "/"} 
input_str = [x for x in input_str if x not in to_delete]
for a in input_str:
    b+=a
input_str=b

#restoring B.M.S

y=re.compile(r"B\.M\.S.")
s=1
while s==1:
    m=re.search(y,input_str)
    if m==None:
        s=0
    else:
        input_str=re.sub(y, "BMS ", input_str)

#restoring B.E.
y=re.compile(r"B\.E")
s=1
while s==1:
    m=re.search(y,input_str)
    if m==None:
        s=0
    else:
        input_str=re.sub(y, "BE ", input_str)
        
y=re.compile(r"i\.e\.")
s=1
while s==1:
    m=re.search(y,input_str)
    if m==None:
        s=0
    else:
        input_str=re.sub(y, ",that is", input_str)
        
        
y=re.compile(r'â€“')
s=1
while s==1:
    m=re.search(y,input_str)
    if m==None:
        s=0
    else:
        input_str=re.sub(y, "-", input_str)
        
y=re.compile(r'â€™')
s=1
while s==1:
    m=re.search(y,input_str)
    if m==None:
        s=0
    else:
        input_str=re.sub(y, "'", input_str)
        
y=re.compile(r'(\d{1,2})\.(\d{1,2})\.(\d{4})')
s=1
while s==1:
    m=re.search(y,input_str)
    if m==None:
        s=0
    else:
        input_str=re.sub(y, '\\1/\\2/\\3', input_str)
        
y=re.compile(r'(Sri)\. (\w{1})\. (\w{1})\.')
s=1
while s==1:
    m=re.search(y,input_str)
    if m==None:
        s=0
    else:
        input_str=re.sub(y, '\\1 \\2 \\3', input_str)



print(input_str)
