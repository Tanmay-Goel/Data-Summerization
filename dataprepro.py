import re
import string

f=open(r"C:\Users\tanmay\Downloads\university.txt") #enter file name

input_str=f.read()

#lowercase
input_str = input_str.lower() 

#capitalizing first letter of first word of each sentence
rtn = re.split('([.!?] *)', input_str)
input_str = ''.join([i.capitalize() for i in rtn])

#removing square brackets with text/numbers
wikiindex= re.compile(r'\[\w+\]')
s=1
while s==1:
    m=re.search(wikiindex,input_str)
    if m==None:
        s=0
    else:
        input_str=re.sub(wikiindex, "", input_str)
        
#removing excess whitespace in between sentances 
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
to_delete = set(string.punctuation) - {".", ",", "'"} 
input_str = [x for x in input_str if x not in to_delete]
for a in input_str:
    b+=a
input_str=b

print(input_str)
