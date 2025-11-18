states = {
    "Andhra Pradesh": {
        "official": ["Telugu", "English"],
        "spoken": ["Urdu","Hindi","Banjara","Tamil","Kannada","Marathi","Oriya"]
    },
    "Karnataka": {
        "official": ["Kannada","English"],
        "spoken": ["Urdu","Telugu","Tamil","Marathi"]
    },
    "Kerala": {
        "official": ["Malayalam","English"],
        "spoken": ["Hindi","Kannada","Tamil","Tulu"]
    },
    "Tamilnadu": {
        "official": ["Tamil","English"],
        "spoken": ["Telugu","Kannada","Urdu","Malayalam","Hindi"]
    },
    "Telangana": {
        "official": ["Telugu","Urdu"],
        "spoken": ["Hindi","Tamil","Kannada","Marathi","Oriya"]
    }
}


def max_languages(states):
    max_state = ""
    max_count = 0
    for s in states:
        total = len(states[s]["official"]) + len(states[s]["spoken"])
        if total > max_count:
            max_count = total
            max_state = s
    return max_state


def count_spoken(states, state_name):
    return len(states[state_name]["spoken"])


def where_spoken(states, lang):
    res = []
    for s in states:
        if lang in states[s]["spoken"]:
            res.append(s)
    return res


def unique_languages(states):
    all_langs = []
    for s in states:
        all_langs += states[s]["official"] + states[s]["spoken"]

    uniq = []
    for l in all_langs:
        if all_langs.count(l) == 1:
            uniq.append(l)
    return uniq
print("1. State with maximum languages")
print("2. Count spoken languages in a state")
print("3. States where a language is spoken")
print("4. Unique languages")
print("--------------------------------")

choice = int(input("Enter your choice (1-4): "))

# 1
if choice == 1:
    print("State with maximum languages:", max_languages(states))

# 2
elif choice == 2:
    st = input("Enter state name: ")
    print("Spoken languages count:", count_spoken(states, st))

# 3
elif choice == 3:
    lang = input("Enter language name: ")
    print("States where", lang, "is spoken:", where_spoken(states, lang))

# 4
elif choice == 4:
    print("Unique languages:")
    for x in unique_languages(states):
        print(x)

else:
    print("Invalid choice")
