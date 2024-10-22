options1 = {"easy":"simple", "medium":"complex", "hard":"Very complex"}


def view(description, strings):
    print(description)
    for x in strings:
        print(f"{x})  {strings[x]}")

def menu(title, prompt, options):
    view(title, options)
    action = input(prompt)
    if action in options:
       return action

opt1 = menu("Select a Difficulty", "Difficulty selected: ", options1)
print(f"You selected Difficulty: {opt1}")
print()

options2 = {"r":"Try again", "q":"Quit"}
opt2 = menu("What do you want to do?", "My choice: ", options2)
print(f"You selected option {opt2}) {options2[opt2]}")