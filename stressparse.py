#!/usr/bin/python3

""" A syllable is stressed iff:
1. first syllable in a polysyllabic word
2. monosyllabic word that isn't a function word
3. first syllable in second part of compound or proper name """

vowels = ['a','á','e','i','í','o','ó','u','ú','y','ý','æ','ø']
func = ['tann', 'tí', 'teir', 'ta', 'tær', 'tað', 'tey', 'hin', 'hitt', 'ein', 'eitt', 'eg', 'meg', 'mær', 'mín', 'vit', 'tú', 'teg', 'tín', 'tit', 'hann', 'hon', 'tess', 'seg', 'sær', 'sín', 'mítt', 'títt', 'sítt', 'hvør', 'hvønn', 'hvat', 'sjálv', 'er', 'ert', 'var', 'vart', 'fær', 'fært', 'læt', 'lætst', 'gekk', 'gekst', 'fekk', 'fekst', 'far', 'fer', 'fert', 'kann', 'kanst', 'má', 'mást', 'man', 'manst', 'skal', 'skalt', 'vil', 'vilt', 'varð', 'varðst', 'bleiv', 'bleivst', 'havt', 'verð', 'blív', 'gakk', 'fá', 'ver', 'lat', 'um', 'at', 'av', 'frá', 'hjá', 'nær', 'úr', 'á', 'í', 'við', 'upp', 'inn', 'mót', 'nú', 'tá', 'tó', 'enn', 'fram', 'út', 'har', 'her', 'ov', 'so', 'ei', 'til', 'sum', 'væl', 'og', 'men', 'ið', 'hví', 'sjálvt', 'helst', 'hvar']
    
def syl_count(line):
	count = 0
	found2lv = False
	for i in range(len(line)):
		char = line[i]
		if found2lv:
			found2lv = False
			continue
		if char.lower() == 'e':
			if len(line) > i+1 and line[i+1] in 'iy':
				found2lv = True
		elif char.lower() == 'o':
			if len(line) > i+1 and line[i+1] == 'y':
				found2lv = True
		if char.lower() in vowels:
			count += 1
	return count
      
        
filename = ''
lines = []
with open("parse.txt", "w") as f2:
    with open(filename) as f:
	    for line in f:
		    lines.append(line)
    for line in lines:
	    if line[0] == '#':
		    continue
	    words = line.split()
	    parse = ""
	    for word in words:
		    if word.isdigit():
			    continue
		    count = syl_count(word)
		    if word.lower() in func:
			    parse += "x"
		    else:
			    parse += "X"
			    for i in range(count-1):
				    parse += "x"
		    parse += " "
	    print(line + parse)
	    f2.write('\n' + '' + line + parse)       
