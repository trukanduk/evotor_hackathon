with open("pytorochka.txt") as f:
    with open("pytorochka_parsed.txt", "w") as fw:
        fw.write("\n".join(f.read().split("\n")[::2]))
