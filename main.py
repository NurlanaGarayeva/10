with open("metn.txt", "r") as soz:
    text = soz.read()
    text = text.upper()

with open("yenitext.txt", "w") as yeni_soz:
    yeni_soz.write(text)
