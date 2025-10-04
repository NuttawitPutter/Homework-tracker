homeworks = []

print("Homework Tracker\n")
print("Enter your homework's subject/name/page")
print("To note a homework, type its name once")
print("If you want to remove a homework, type its name again (case doesn't matter)")
print("Type 'done' to see your current list")
print("Type 'exit' to quit the program.\n")

while True:
    homework = input("- ").strip()

    if not homework:
        print("Please enter something.")
        continue

    hw_lower = homework.lower()
    lower_map = {h.lower(): h for h in homeworks}

    if hw_lower == 'done':
        print("\nYour current homework list:")
        if homeworks:
            for i, hw in enumerate(homeworks, 1):
                print(f"Homework{i}: {hw.capitalize()}")
        else:
            print("No homeworks added.")
        print()
        continue

    elif hw_lower == 'exit':
        print("\nFinal homework list:")
        if homeworks:
            for i, hw in enumerate(homeworks, 1):
                print(f"Homework{i}: {hw.capitalize()}")
        else:
            print("No homeworks added.")
        break

    if hw_lower in lower_map:
        original = lower_map[hw_lower]
        homeworks.remove(original)
        print(f"Removed '{original.capitalize()}' from the list.")
    else:
        capitalized = homework.capitalize()
        homeworks.append(capitalized)
        print(f"Added '{capitalized}' to the list.")













