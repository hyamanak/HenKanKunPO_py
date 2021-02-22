#へんかんくんぴーおー.py
# -*- coding: utf-8 -*-

import polib, sys, re, jaconv



##conver Zenkaku characters to Hankaku
def zenkaku2hankaku(content):
    if type(content) is not str:
        content = str(content)
    content = jaconv.z2h(content,digit=True, ascii=True, kana=False)
    return content

##Adds space between alphabet and Zenakaku
def addSpace(pair):
    global entry
    for item in pair:
            firstLt      = item[0]
            secondLt     = item[1]
            repl         = firstLt + " " + secondLt
            entry.msgstr = entry.msgstr.replace(item, repl)

##fix terminology problem such as コンピュータ vs コンピューター        
def yogoCheck(pair):
    global entry
    for term in terms:
        if term in entry.msgstr:
            correct_term = term + "ー"
            if not correct_term in entry.msgstr:
                entry.msgstr = entry.msgstr.replace(term, correct_term)
    

##opens files, first argument is for po file, the second is for yogo file.
with open(sys.argv[1], mode='r', encoding='utf-8') as f, open(sys.argv[2], mode='r', encoding='utf-8') as t:
    terms = t.read().splitlines()

    po = polib.pofile(sys.argv[1])
    for entry in po:
        entry.msgstr = zenkaku2hankaku(entry.msgstr)

        hanWithZen        = re.findall(r"[a-zA-Z0-9@:/\]\)*&_\-\+|~^%$#@!?\"\'][ぁ-んァ-ンー-龥]", entry.msgstr)
        zenWithHan        = re.findall(r"[ぁ-んァ-ンー-龥][a-zA-Z0-9@\[\(*&_\-\+|~^%$#@!?\"\']", entry.msgstr)
        numWithSpcialChar = re.findall(r"[a-zA-Z0-9][\(]", entry.msgstr)

        if re.search(r"[ぁ-んァ-ンー-龥]", entry.msgstr):
            
            addSpace(hanWithZen)
            addSpace(zenWithHan)
            addSpace(numWithSpcialChar)
            #print(entry.msgstr)
            yogoCheck(entry.msgstr)
            
po.save(sys.argv[3])

