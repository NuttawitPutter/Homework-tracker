homeworks = []
done_homeworks = []

print("-Homework Tracker\n")
print("-Enter your homework's subject/name/page")
print("-To note a homework, type its name once")
print("-If you want to move a homework to DONE, type its name again (case doesn't matter)")
print("-Type 'DONE' to see your homework that are done")
print("-Type ' NOT DONE' to see your Not Done homework")
print("-Type 'EXIT' to quit the program.\n")

while True:
    hw = input("- ").strip()
    if not hw:
        continue

    hw_lower = hw.lower()

    if hw_lower == "done":
        print("\nDone:", done_homeworks if done_homeworks else "None")
        continue

    if hw_lower == "not done":
        print("\nNot done:", homeworks if homeworks else "None")
        continue

    if hw_lower == "exit":
        print("\nFinal Lists:")
        print("Not done:", homeworks if homeworks else "None")
        print("Done:", done_homeworks if done_homeworks else "None")
        break




    if hw.capitalize() in homeworks:
        homeworks.remove(hw.capitalize())
        done_homeworks.append(hw.capitalize())
        print("Added/Moved" , hw.capitalize(), "to 'DONE' list.")
    
    else:
        homeworks.append(hw.capitalize())
        print("Added/Moved", hw.capitalize(), "to 'Not Done' list.")





