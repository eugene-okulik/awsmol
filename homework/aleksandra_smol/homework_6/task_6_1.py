text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, "
        "dignissim vitae libero")

words = text.split()
fin_text = []

for word in words:
    if word[-1] in {".", ","}:
        fin_text.append(word[:-1] + "ing" + word[-1])
    else:
        fin_text.append(word + "ing")

print(" ".join(fin_text))
