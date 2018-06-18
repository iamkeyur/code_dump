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

    csv = open('data.csv','w')
    columnTitleRow = "issue_id|added|removed\n"
    csv.write(columnTitleRow)

    commits = split_by_regex(lines,r)
    pattern = r"CAMEL\-[0-9]{4,6}"
    camel_pattern = re.compile(pattern)
    for commit in commits:
        commit_id = re.search(camel_pattern,str(commit))
        if commit_id:
            for i in range(len(commit)):
                added = re.match(log_add_pattern,str(commit[i]))
                deleted = re.match(log_del_pattern,str(commit[i-1]))
                if added and deleted:
                    row = commit_id[0] + "|" + commit[i][1:].strip() + "|" + commit[i-1][1:].strip() + "\n"
                    csv.write(row)

