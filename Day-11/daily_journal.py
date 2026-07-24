print("==== Daily Journal ====")


entry = input("How was your day?\n >")

with open("journal.txt ","a") as file:
    file.write("====Journal Entry====\n")
    file.write(entry + "\n")
    file.write("=======================\n\n")

print("\n Journal saved successfully !")




