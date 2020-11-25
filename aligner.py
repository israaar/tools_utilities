# -*- coding: utf-8 -*-
"""
Created on Tue May 12 23:28:20 2020

@author: Michael

Modified by mt_collaboration_team
"""

from tkinter import *
from tkinter import ttk

# starts from the begining
# line_no_1 = -1
# line_no_2 = -1
# line_no_3 = -1

# starts from a custom start point
line_no_1 = 696
line_no_2 = 971
line_no_3 = 949

bambara_bfe = list()
francais_bfe = list()
english_bfe = list()
bambara_bf = list()
francais_bf = list()
bambara_be = list()
english_be = list()

def save_aligned_BFE(*args):
    """
    Append corresponding aligned Bambara, French, and English to their lists
    """

    try:
        global bambara_bfe
        global francais_bfe
        global english_bfe
        bambara_bfe.append(lines_bam[line_no_1])
        francais_bfe.append(lines_fr[line_no_2])
        english_bfe.append(lines_en[line_no_3])
    except ValueError:
        pass

def save_aligned_BF(*args):
    """
    Append corresponding aligned Bambara and French to their lists
    """

    try:
        global bambara_bf
        global francais_bf
        bambara_bf.append(lines_bam[line_no_1])
        francais_bf.append(lines_fr[line_no_2])
    except ValueError:
        pass

def save_aligned_BE(*args):
    """
    Append corresponding aligned Bambara and English to their lists
    """

    try:
        global bambara_be
        global english_be
        bambara_be.append(lines_bam[line_no_1])
        english_be.append(lines_en[line_no_3])
    except ValueError:
        pass

def save(*args):
    """
    Create corresponding aligned Bambara, French, and English and clear lists
    depending on the corresponding conditoin
    """

    try:
        global bambara_bfe
        global francais_bfe
        global english_bfe
        global bambara_bf
        global francais_bf
        global bambara_be
        global english_be

        # if len(bambara_bfe) > 0 and len(bambara_bf) > 0 and len(bambara_be) > 0:
        #     pass

        if len(bambara_bfe) > 0:
            with open("bambara_bfe.txt", "w", encoding="utf-8") as f:
                for item in bambara_bfe:
                    f.write("%s\n" % item)
                bambara_bfe = list()

            with open("francais_bfe.txt", "w", encoding="utf-8") as f:
                for item in francais_bfe:
                    f.write("%s\n" % item)
                francais_bfe = list()

            with open("english_bfe.txt", "w", encoding="utf-8") as f:
                for item in english_bfe:
                    f.write("%s\n" % item)
                english_bfe = list()

        if len(bambara_bf) > 0:
            with open("bambara_bf.txt", "w", encoding="utf-8") as f:
                for item in bambara_bf:
                    f.write("%s\n" % item)
                bambara_bf = list()

            with open("francais_bf.txt", "w", encoding="utf-8") as f:
                for item in francais_bf:
                    f.write("%s\n" % item)
                francais_bf = list()

        if len(bambara_be) > 0:
            with open("bambara_be.txt", "w", encoding="utf-8") as f:
                for item in bambara_be:
                    f.write("%s\n" % item)
                bambara_be = list()

            with open("english_be.txt", "w", encoding="utf-8") as f:
                for item in english_be:
                    f.write("%s\n" % item)
                english_be = list()

    except ValueError:
        pass

def continue_saving(*args):
    """
    Append corresponding aligned Bambara, French, and English and clear lists
    depending on the corresponding conditoin
    """

    try:
        global bambara_bfe
        global francais_bfe
        global english_bfe
        global bambara_bf
        global francais_bf
        global bambara_be
        global english_be

        # if len(bambara_bfe) > 0 and len(bambara_bf) > 0 and len(bambara_be) > 0:
        #     pass

        if len(bambara_bfe) > 0:
            with open("bambara_bfe.txt", "a", encoding="utf-8") as f:
                for item in bambara_bfe:
                    f.write("%s\n" % item)
                bambara_bfe = list()

            with open("francais_bfe.txt", "a", encoding="utf-8") as f:
                for item in francais_bfe:
                    f.write("%s\n" % item)
                francais_bfe = list()

            with open("english_bfe.txt", "a", encoding="utf-8") as f:
                for item in english_bfe:
                    f.write("%s\n" % item)
                english_bfe = list()

        if len(bambara_bf) > 0:
            with open("bambara_bf.txt", "a", encoding="utf-8") as f:
                for item in bambara_bf:
                    f.write("%s\n" % item)
                bambara_bf = list()

            with open("francais_bf.txt", "a", encoding="utf-8") as f:
                for item in francais_bf:
                    f.write("%s\n" % item)
                francais_bf = list()

        if len(bambara_be) > 0:
            with open("bambara_be.txt", "a", encoding="utf-8") as f:
                for item in bambara_be:
                    f.write("%s\n" % item)
                bambara_be = list()

            with open("english_be.txt", "a", encoding="utf-8") as f:
                for item in english_be:
                    f.write("%s\n" % item)
                english_be = list()

    except ValueError:
        pass

def next_bfe(*args):
    try:
        global line_no_1
        global line_no_2
        global line_no_3
        line_no_1 = line_no_1 + 1
        line_no_2 = line_no_2 + 1
        line_no_3 = line_no_3 + 1
        text1 = str(line_no_1) + ": " + lines_bam[line_no_1]
        text2 = str(line_no_2) + ": " + lines_fr[line_no_2]
        text3 = str(line_no_3) + ": " + lines_en[line_no_3]
        clrStr = "                                                                                                                                                  "
        ttk.Label(mainframe, text=clrStr).grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, text=text1).grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, text=clrStr).grid(column=1, row=2, sticky=W)
        ttk.Label(mainframe, text=text2).grid(column=1, row=2, sticky=W)
        ttk.Label(mainframe, text=clrStr).grid(column=1, row=3, sticky=W)
        ttk.Label(mainframe, text=text3).grid(column=1, row=3, sticky=W)

    except ValueError:
        pass

def prev_bfe(*args):
    try:
        global line_no_1
        global line_no_2
        global line_no_3
        line_no_1 = line_no_1 - 1
        line_no_2 = line_no_2 - 1
        line_no_3 = line_no_3 - 1
        text1 = str(line_no_1) + ": " + lines_bam[line_no_1]
        text2 = str(line_no_2) + ": " + lines_fr[line_no_2]
        text3 = str(line_no_3) + ": " + lines_en[line_no_3]
        clrStr = "                                                                                                                                                  "
        ttk.Label(mainframe, text=clrStr).grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, text=text1).grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, text=clrStr).grid(column=1, row=2, sticky=W)
        ttk.Label(mainframe, text=text2).grid(column=1, row=2, sticky=W)
        ttk.Label(mainframe, text=clrStr).grid(column=1, row=3, sticky=W)
        ttk.Label(mainframe, text=text3).grid(column=1, row=3, sticky=W)

    except ValueError:
        pass



def next1(*args):
    try:
        global line_no_1
        line_no_1 = line_no_1 + 1
        text1 = str(line_no_1) + ": " + lines_bam[line_no_1]
        clrStr = "                                                                                                                                                  "
        ttk.Label(mainframe, text=clrStr).grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, text=text1).grid(column=1, row=1, sticky=W)

    except ValueError:
        pass

def next2(*args):
    try:
        global line_no_2
        line_no_2 = line_no_2 + 1
        text2 = str(line_no_2) + ": " + lines_fr[line_no_2]
        clrStr = "                                                                                                                                                  "
        ttk.Label(mainframe, text=clrStr).grid(column=1, row=2, sticky=W)
        ttk.Label(mainframe, text=text2).grid(column=1, row=2, sticky=W)

    except ValueError:
        pass

def next3(*args):
    try:
        global line_no_3
        line_no_3 = line_no_3 + 1
        text3 = str(line_no_3) + ": " + lines_en[line_no_3]
        clrStr = "                                                                                                                                                  "
        ttk.Label(mainframe, text=clrStr).grid(column=1, row=3, sticky=W)
        ttk.Label(mainframe, text=text3).grid(column=1, row=3, sticky=W)

    except ValueError:
        pass

def prev1(*args):
    try:
        global line_no_1
        line_no_1 = line_no_1 - 1
        text1 = str(line_no_1) + ": " + lines_bam[line_no_1]
        clrStr = "                                                                                                                                                  "
        ttk.Label(mainframe, text=clrStr).grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, text=text1).grid(column=1, row=1, sticky=W)

    except ValueError:
        pass

def prev2(*args):
    try:
        global line_no_2
        line_no_2 = line_no_2 - 1
        text2 = str(line_no_2) + ": " + lines_fr[line_no_2]
        clrStr = "                                                                                                                                                  "
        ttk.Label(mainframe, text=clrStr).grid(column=1, row=2, sticky=W)
        ttk.Label(mainframe, text=text2).grid(column=1, row=2, sticky=W)

    except ValueError:
        pass

def prev3(*args):
    try:
        global line_no_3
        line_no_3 = line_no_3 - 1
        text3 = str(line_no_3) + ": " + lines_en[line_no_3]
        clrStr = "                                                                                                                                                  "
        ttk.Label(mainframe, text=clrStr).grid(column=1, row=3, sticky=W)
        ttk.Label(mainframe, text=text3).grid(column=1, row=3, sticky=W)

    except ValueError:
        pass

root = Tk()
root.title("Translation Aligner Bamanankan - Français - English")

path_to_file = "comp_bam_dataset.txt"
text = open(path_to_file, "rb").read().decode(encoding="utf-8")
lines_bam = text.splitlines()

path_to_file = "comp_fr_dataset.txt"
text = open(path_to_file, "rb").read().decode(encoding="utf-8")
lines_fr = text.splitlines()

path_to_file = "comp_en_dataset.txt"
text = open(path_to_file, "rb").read().decode(encoding="utf-8")
lines_en = text.splitlines()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Button(mainframe, text=">>>", command=next_bfe).grid(column=1, row=4, sticky=E)
ttk.Button(mainframe, text="Aligned B-F-E", command=save_aligned_BFE).grid(column=2, row=4, sticky=W)
ttk.Button(mainframe, text="Aligned B-F", command=save_aligned_BF).grid(column=1, row=5, sticky=E)
ttk.Button(mainframe, text="Aligned B-E", command=save_aligned_BE).grid(column=2, row=5, sticky=W)
ttk.Button(mainframe, text="Save", command=save).grid(column=3, row=5, sticky=E)
ttk.Button(mainframe, text="Continue Saving", command=continue_saving).grid(column=4, row=5, sticky=W)

ttk.Button(mainframe, text=">", command=next1).grid(column=3, row=1, sticky=E)
ttk.Button(mainframe, text=">", command=next2).grid(column=3, row=2, sticky=E)
ttk.Button(mainframe, text=">", command=next3).grid(column=3, row=3, sticky=E)
ttk.Button(mainframe, text="<", command=prev1).grid(column=4, row=1, sticky=W)
ttk.Button(mainframe, text="<", command=prev2).grid(column=4, row=2, sticky=W)
ttk.Button(mainframe, text="<", command=prev3).grid(column=4, row=3, sticky=W)
ttk.Button(mainframe, text="<<<", command=prev_bfe).grid(column=3, row=4, sticky=E)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", save)
next_bfe()

root.mainloop()
