"""
Boys script can be used for finding path on Ott server to male samples
and their fetal fraction which was calculated by bayindir (if it was calculated).
"""
"""
pathtoboys.txt - path to samples which have known fetal fraction
maybe_boys.txt - path to samples which have not known fetal fraction
bayindir.txt - for known fetal fraction
"""


import os
import csv


boys_set = set()
bayindir = set()
bayindir_boys = set()
maybe_boys = set()

strange_dir = {"20190116", "20190131", "20190927", "20191207", "20191030", "20190621", "20200125", "20190612", "20191031", "20190301", "20190312"}

all_dir = os.listdir("/home/ott/NIPT/DATA")
for name_dir in all_dir:
    if (name_dir[:4] == '2019' or name_dir[:4] == '2020') and (name_dir[:8] not in strange_dir):
        pathto = "/backups/" + name_dir + "/FINALBAM/"
        that_boys = set()
        with open("/home/ott/NIPT/DATA/" + name_dir + "/RESULTS/" + name_dir + ".gender.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == 'M' and os.path.exists(pathto + row[1] + ".dedup.bam"):
                    maybe_boys.add(pathto + row[1] + ".dedup.bam")
                    that_boys.add("FINALBAM/" + row[1] + ".dedup.bam")
        if os.path.exists("/home/ott/NIPT/DATA/" + name_dir + "/RESULTS/" + name_dir + ".bayindir.ff"):
            with open("/home/ott/NIPT/DATA/" + name_dir + "/RESULTS/" + name_dir + ".bayindir.ff") as f:
                reader = f.read().split("\n")
                bayindir.add(name_dir + " : " + reader[0])
                if len(reader[0]) > 6:
                    for i in range(0, len(reader), 2):
                        if len(reader[i]) != 0:
                            if reader[i][0] == '[':
                                if (reader[i][5:-1] in that_boys) and (len(reader[i+1]) > 7) and (len(reader[i+1]) < 15):
                                    bayindir_boys.add(reader[i][14:-11] + " " + reader[i+1][4:] + " " + 'Male')
                                    boys_set.add(pathto + reader[i][14:-1])
                            else:
                                if (reader[i] in that_boys) and (len(reader[i+1]) > 7) and (len(reader[i+1]) < 15):
                                    bayindir_boys.add(reader[i][9:-10] + ":" + reader[i+1] + " " + 'Male')
                                    boys_set.add(pathto + reader[i][9:])
        else:
            bayindir.add(name_dir + " : " + "Not exist")


f = open('pathtoboys'+'.txt', 'w')
for el in boys_set:
    f.write(el + '\n')
f.close()

f = open('maybe_boys.txt', 'w')
f.write(str(len(maybe_boys.difference(boys_set))) + '\n')
for el in maybe_boys.difference(boys_set):
    f.write(el + '\n')
f.close()

number_of_file = int(len(boys_set)/30)
for i in range(number_of_file):
    f = open('pathtoboys'+str(i)+'.txt', 'w')
    for j in range(30):
        f.write(boys_set.pop() + '\n')
    f.close()
f = open('pathtoboys'+str(number_of_file)+'.txt', 'w')
for el in boys_set:
    f.write(el + '\n')
f.close()


f = open('bayindir.txt', 'w')
f.write(str(len(bayindir_boys)) + '\n')
for el in bayindir_boys:
    f.write(el + '\n')
f.close()

