#!/usr/bin/env python3

"""
Grabs a few word stimuli from KiloPerf, copies them into the `stims/`
directory, and creates a `.lab` file for each.
"""

import shutil
import random as rd
import pandas as pd

stim_dir = "/home/rachael/projects/kiloperf/media"
list_dir = "/home/rachael/projects/kiloperf-analyses/stim_data"

word_list = pd.read_csv(list_dir + "/word_list.csv")
words = list(set(word_list.loc[word_list.isWord == 1, "ORTH"]))

sample = rd.sample(words, 10)
print(sample)
while True:
    resp = input("Continue? [Y/n] ").lower()
    if resp in ["y", "yes", ""]:
        break
    elif resp in ["n", "no"]:
        sample = rd.sample(words, 10)
        print(sample)
        continue
    else:
        continue

for w in sample:
    # Copy the stim file to ../stims
    orig_path = "{}/words{}.wav".format(stim_dir, w)
    new_path = "../stims/{}.wav".format(w)
    shutil.copy(orig_path, new_path)

    # Create a matching .lab file with the word's orthography in uppercase.
    with open("../stims/{}.lab".format(w), "w") as f:
        f.write(w.upper())
