import re
import string
import os
import codecs
    

def clean_wiki():
    dir = input("Enter text file directory : ")
    all_files = os.listdir(dir)   

    req_files = []
    for i in all_files:
        if i[-4::] == ".txt":
            req_files.append(i)
            
    for i in req_files:
        with codecs.open(i, 'r', encoding='utf8') as f:
            input_str = f.read()
        #encoding part not required for university.txt    required for ai,ml,computer.txt
        

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
    #new_file_name = i[:-4]+"_cleaned.txt"
    #print(new_file_name)
    with codecs.open(i, 'w', encoding='utf8') as f:
        f.write(input_str)
        
    print("Data Pre-processing completed...")

    
        
def clean_bms():
    dir = input("Enter text file directory : ")
    all_files = os.listdir(dir)   

    req_files = []
    for i in all_files:
        if i[-4::] == ".txt":
            req_files.append(i)
    
    for i in req_files:
        with codecs.open(i, 'r', encoding='utf8') as f:
            input_str = f.read()
        
    #lowercase
    input_str = input_str.lower() 
    
    y=re.compile(r'â€“')
    s=1
    while s==1:
        m=re.search(y,input_str)
        if m==None:
            s=0
        else:
            input_str=re.sub(y, "-", input_str)
    
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
    
    #restoring b.m.s
    y=re.compile(r"b\.M\.S")
    s=1
    while s==1:
        m=re.search(y,input_str)
        if m==None:
            s=0
        else:
            input_str=re.sub(y, "b.m.s.", input_str)
    
    #restoring b.e
    y=re.compile(r"b\.E")
    s=1
    while s==1:
        m=re.search(y,input_str)
        if m==None:
            s=0
        else:
            input_str=re.sub(y, "b.e.", input_str)
    
    
    #restoring some hyphen       
    y=re.compile(r'â€“')
    s=1
    while s==1:
        m=re.search(y,input_str)
        if m==None:
            s=0
        else:
            input_str=re.sub(y, " ", input_str)


        
    print("Data Pre-processing completed...")
    
def pdf_extraction():
    pass     
 
def website_extraction():
    pass

def summerization():
    website_ext=['.com','.in','.org','.net', '.info']
    url=input("Enter file or url: ")
    if url.find('.pdf')>=0:
      pdf_extraction()  #should return extracted directory
    else:
        for i in website_ext:
            if url.find(i)>=0:
                website_extraction()  #should return extracted directory
                break
                    
    #required code(if any)
    
    #data cleaning part
    
    #model for summerization
    
    #required code(if any)
    
summerization()
    