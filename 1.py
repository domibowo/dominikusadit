import json

person = {
    "name" : "Dominikus Adhitya Prabowo",
    "age" : 23,
    "address" : "Wismamas Blok B1 No 21 Cinangka, Sawangan, Depok 16516",
    "hobbies" : ("Cooking","Online Gaming","Eating"),
    "is_married" : False,
    "list_school" : [
        {"Sekolah" : "Surya University", "year_in" : 2014, "year_out" : 2019, "major" : "Biology"},
        {"Sekolah" : "SMA Charitas", "year_in" : 2011, "year_out" : 2014, "major" : "Life Science"}
    ],
    "skills" : [
        {"skill_name" : "MS Word", "level" : "Advance"},
        {"skill_name" : "MS Excel", "level" : "Advance"},
        {"skill_name" : "Power Point", "level" : "Advance"},
        {"skill_name" : "English Passive", "level" : "Advance"},
    ],
    "interest_in_coding" : True
}

print (json.dumps(person))
