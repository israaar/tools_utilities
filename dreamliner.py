"""
Created on Thu Jan 28 06:25:08 EST 2021
@author: mt_collaboration_team



"""

import PySimpleGUI as sg
import sys

# Global lists
bambara_bfe = list()
francais_bfe = list()
english_bfe = list()
bambara_bf = list()
francais_bf = list()
bambara_be = list()
english_be = list()

# Constants
ML_WIDTH = 75
ML_HEIGHT = 5


def usage():
    print("Usage:")
    print("$ python3 dreamliner.py filename")
    print("Assuming you have [bam_, fr_,en_]filename.txt")

# input files to read in

if len(sys.argv) < 2:
    usage()
    sys.exit(1)
elif len(sys.argv) == 2:
    path = sys.argv[1]
else:
    usage()
    sys.exit(1)


path_to_file = "bam_" + path + ".txt"
text = open(path_to_file, "rb").read().decode(encoding="utf-8")
lines_bam = text.splitlines()

path_to_file = "fr_" + path + ".txt"
text = open(path_to_file, "rb").read().decode(encoding="utf-8")
lines_fr = text.splitlines()

path_to_file = "en_" + path + ".txt"
text = open(path_to_file, "rb").read().decode(encoding="utf-8")
lines_en = text.splitlines()


# Start from the begining
line_no_1 = -1
line_no_2 = -1
line_no_3 = -1

if len(lines_bam):
    text1 = lines_bam[line_no_1]
else:
    text1 = ""
if len(lines_fr):
    text2 = lines_fr[line_no_2]
else:
    text2 = ""
if len(lines_en):
    text3 = lines_en[line_no_3]
else:
    text3 = ""

def save_aligned_bfe(*args):
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

def save_aligned_bf(*args):
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

def save_aligned_be(*args):
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
        text1 = lines_bam[line_no_1]
        text2 = lines_fr[line_no_2]
        text3 = lines_en[line_no_3]

        # Update and display the index
        window["-TXT_BM_IDX-"].update(line_no_1)
        window["-TXT_FR_IDX-"].update(line_no_2)
        window["-TXT_EN_IDX-"].update(line_no_3)

        # Update and display the text
        window["-BM_ML-"].update(text1)
        window["-FR_ML-"].update(text2)
        window["-EN_ML-"].update(text3)


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
        text1 = lines_bam[line_no_1]
        text2 = lines_fr[line_no_2]
        text3 = lines_en[line_no_3]

        # Update and display the index
        window["-TXT_BM_IDX-"].update(line_no_1)
        window["-TXT_FR_IDX-"].update(line_no_2)
        window["-TXT_EN_IDX-"].update(line_no_3)

        # Update and display the text
        window["-BM_ML-"].update(text1)
        window["-FR_ML-"].update(text2)
        window["-EN_ML-"].update(text3)


    except ValueError:
        pass

# Flow Control
# Next buttons
def next1(*args):
    try:
        global line_no_1
        line_no_1 = line_no_1 + 1
        text1 = lines_bam[line_no_1]

        # Update and display the index
        window["-TXT_BM_IDX-"].update(line_no_1)
        # Update and display the text
        window["-BM_ML-"].update(text1)

    except ValueError:
        pass

def next2(*args):
    try:
        global line_no_2
        line_no_2 = line_no_2 + 1
        text2 = lines_fr[line_no_2]

        # Update and display the index
        window["-TXT_FR_IDX-"].update(line_no_2)
        # Update and display the text
        window["-FR_ML-"].update(text2)


    except ValueError:
        pass

def next3(*args):
    try:
        global line_no_3
        line_no_3 = line_no_3 + 1
        text3 = lines_en[line_no_3]

        # Update and display the index
        window["-TXT_EN_IDX-"].update(line_no_3)
        # Update and display the text
        window["-EN_ML-"].update(text3)

    except ValueError:
        pass

# Previous buttons
def prev1(*args):
    try:
        global line_no_1
        line_no_1 = line_no_1 - 1
        text1 = lines_bam[line_no_1]

        # Update and display the index
        window["-TXT_BM_IDX-"].update(line_no_1)
        # Update and display the text
        window["-BM_ML-"].update(text1)


    except ValueError:
        pass

def prev2(*args):
    try:
        global line_no_2
        line_no_2 = line_no_2 - 1
        text2 = lines_fr[line_no_2]

        # Update and display the index
        window["-TXT_FR_IDX-"].update(line_no_2)
        # Update and display the text
        window["-FR_ML-"].update(text2)

    except ValueError:
        pass

def prev3(*args):
    try:
        global line_no_3
        line_no_3 = line_no_3 - 1
        text3 = lines_en[line_no_3]

        # Update and display the index
        window["-TXT_EN_IDX-"].update(line_no_3)
        # Update and display the text
        window["-EN_ML-"].update(text3)
    except ValueError:
        pass

# Define the layout of the program
layout = [[sg.Text(line_no_1, key="-TXT_BM_IDX-"), sg.Multiline(text1, size=(ML_WIDTH, ML_HEIGHT), key="-BM_ML-"), sg.Button(">", key="-BM_NXT_BTN-"),
sg.Button("<", key="-BM_PRV_BTN-")],
        [sg.Text(line_no_2, key="-TXT_FR_IDX-"), sg.Multiline(text2, size=(ML_WIDTH, ML_HEIGHT), key="-FR_ML-"), sg.Button(">", key="-FR_NXT_BTN-"),
        sg.Button("<", key="-FR_PRV_BTN-")],
        [sg.Text(line_no_3, key="-TXT_EN_IDX-"), sg.Multiline(text3, size=(ML_WIDTH, ML_HEIGHT), key="-EN_ML-"), sg.Button(">", key="-EN_NXT_BTN-"),
        sg.Button("<", key="-EN_PRV_BTN-")],
        [sg.Button("Aling B-F-E", key="-ALGN_ALL_BTN-"),
        sg.Button("Aling B-F", key="-ALGN_BM_FR_BTN-"),
        sg.Button("Aling B-E", key="-ALGN_BM_EN_BTN-"),
        sg.T(), sg.Button(">>>", key="-ALL_NXT_BTN-"),
        sg.Button("<<<", key="-ALL_PRV_BTN-")],
        [sg.Button("Save", key="-SAVE_BTN-"),
        sg.Button("Continue Saving", key="-CNT_SAVE_BTN-"), sg.Quit()]]

window = sg.Window("Translation Aligner Bamanankan - Français - English", layout)
event, values = window.read()

# Button Functions

while True: # Event loop

    event, values = window.read()

    if event in ("Quit", sg.WIN_CLOSED):
        break

    elif event == "-BM_NXT_BTN-":
        next1()

    elif event == "-BM_PRV_BTN-":
        prev1()

    elif event == "-FR_NXT_BTN-":
        next2()

    elif event == "-FR_PRV_BTN-":
        prev2()

    elif event == "-EN_NXT_BTN-":
        next3()

    elif event == "-EN_PRV_BTN-":
        prev3()

    elif event == "-ALL_NXT_BTN-":
        next_bfe()

    elif event == "-ALL_PRV_BTN-":
        prev_bfe()

    elif event == "-ALGN_BM_FR_BTN-":
        save_aligned_bf()

    elif event == "-ALGN_BM_EN_BTN-":
        save_aligned_be()

    elif event == "-ALGN_ALL_BTN-":
        save_aligned_bfe()

    elif event == "-SAVE_BTN-":
        save()

    elif event == "-CNT_SAVE_BTN-":
        continue_saving()
