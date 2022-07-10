import csv
import os
import re
import sys

from englishToKanaConverter import EnglishToKanaConverter
from englishToKanaConverter.constants import ZENHAN_TABLE


if __name__ == "__main__":
    file = "HISS_dic\\main.csv"
    if not os.path.isfile(file):
        sys.stderr.write("File does not exist.\n")
        sys.exit(1)
    
    with open(file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
    # ヘッダ行は無視
    data = data[1:]
    c = EnglishToKanaConverter()
    failed = []
    for i in data:
        word = i[0]
        # すべて半角の大文字にする
        word = word.upper()
        word = word.translate(str.maketrans(ZENHAN_TABLE))
        if not re.match("[A-Z']+$", word):
            continue
        converted = c.process(word, False)
        if not re.search("[A-Z']", converted):
            continue
        ret = [word, i[1]]
        failed.append(ret)
    print("%d words" % len(failed))
    with open("failed.txt", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerows(failed)
    print("Done!")
