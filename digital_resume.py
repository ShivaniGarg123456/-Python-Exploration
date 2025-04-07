resume = {
    "Name": "Shivani",
    "Age": 18,
    "Profession": "Student",
    "Dream job role": "Data analyst",
    "Skills": ["Python", "Excel", "Power BI", "Communication"],
    "Habits": ["Travelling", "Music", "Logical problem solving"],
    "Projects": ["Calculator", "Number guessing game", "Quiz game"]
}

print("<<< My Digital Resume >>>")
print(f"👩‍💻 Name : {resume['Name']}")
print(f"🎂 Age : {resume['Age']}")
print(f"📚 Profession : {resume['Profession']}")
print(f"💼 Dream job role : {resume['Dream job role']}")

print("💡 Skills")
for skill in resume["Skills"]:
    print(f"⭐ {skill}")

print("🎯 Habits")
for habit in resume["Habits"]:
    print(f"✨ {habit}")

print("🚀 Projects")
for project in resume["Projects"]:
    print(f"📁 {project}")
