import re
import sys
import os
import codecs

r = re.compile(r"^commit\s(?P<hash>\b[0-9a-f]{5,40}\b)")

log_add_pattern = re.compile(r'^\+(?!\+)(?!(\s)*//)(.)*log(\w)*(\(\))?\.(fatal|error|warn|info|debug|trace|log|catching|throwing|entry|exit|printf)\(.*', 
        re.IGNORECASE)
    
log_del_pattern = re.compile(r'^-(?!-)(?!(\s)*//)(.)*log(\w)*(\(\))?\.(fatal|error|warn|info|debug|trace|log|catching|throwing|entry|exit|printf)\(.*', 
        re.IGNORECASE)

def findall_regex(l, r):
    found = list()
    for i in range(0, len(l)):
        k = r.match(l[i])
        if k:
            found.append(i)
            k = None

    return found

def split_by_regex(l, r):
    splits = list()
    indices = findall_regex(l, r)
    k = None
    for i in indices:
        if k is None:
            splits.append(l[0:i])
            k = i
        else:
            splits.append(l[k:i])
            k = i

    splits.append(l[k:])

    return splits

with codecs.open("sampleoutjava1.txt", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()
    try:
        lines = text.splitlines()
    except AttributeError:
        lines = text

    csv = open('new-data.csv','w')
    columnTitleRow = "issue_id|author|author_email|no. of line added|no. of line removed|file_name\n"
    csv.write(columnTitleRow)

    commits = split_by_regex(lines,r)
    churn_pattern = re.compile(r"^(?P<added>[0-9]{1,3})\s(?P<removed>[0-9]{1,3})\s(?P<file_name>(.*/)?(?:$|(.+?)(?:(\.[^.]*$)|$)))")
    author_pattern = re.compile('Author: (.*) <(.*)>')
    camel_pattern = re.compile(r"CAMEL\-[0-9]{4,6}")
    for commit in commits:
        commit_id = re.search(camel_pattern,str(commit))
        author = re.match(author_pattern,str(commit))
        if commit_id:
            for i in range(len(commit)):
                author = re.match(author_pattern,commit[i])       
                match = re.match(churn_pattern,commit[i])
                if(author):
                    name = author.group(1).strip()
                    email = author.group(2)
                if(match):
                    row = commit_id[0] + "|" + name + "|" + email + "|" + match.group(1) + "|" + match.group(2) + "|" + match.group(3) + "\n"
                    csv.write(row)



