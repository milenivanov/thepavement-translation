#!/usr/local/bin/python3

def buildfilename(text, num):
    filename = text.strip()
    if not filename:
        raise RuntimeError("empty file name")
    return "{:0>3}-{}".format(num, filename)

def writeitem(dest, text):
    with open(dest, "a") as f:
        f.write(text)

with open("999-remaining.txt") as f:
    linecount = 0
    para = ""
    newname = "BADNAME"
    filenum = 29
    for line in f:
        linecount += 1

        if 1 == linecount:
            newname = buildfilename(line, filenum)
        else:
            para += line

        if "\n" == line:
            writeitem(newname, para)
            linecount = 0
            para = ""
            filenum += 1

