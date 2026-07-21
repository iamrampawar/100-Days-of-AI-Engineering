print("==== Student Club Membership System ====")

python_club = {"Ram","Amit","Neha","Priya"}
ai_club = {"Ram","Anjali","Neha","Rahul"}

print("\n Python Club :",python_club)
print("AI Club :",ai_club)


all_students = python_club | ai_club
print("All Club Membres :",all_students)


common_students = python_club & ai_club
print("\nStudent in both Clubs :",common_students)

only_python = python_club - ai_club
print("\n  OnlyPython Club Members :",only_python)

only_one = python_club ^ ai_club
print("\n Students in only one club :",only_one)





