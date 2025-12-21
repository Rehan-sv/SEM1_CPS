compounds = {
    "P-401": {
        "condition": "Hypertension",
        "phase": "Phase 3",
        "investigator": "Dr. Anya Sharma",
        "efficacy": 78,
        "side_effects": ["Headache", "Nausea"]
    },
    "D-115": {
        "condition": "Type 2 Diabetes",
        "phase": "Phase 2",
        "investigator": "Dr. Ben Carter",
        "efficacy": 65,
        "side_effects": ["Fatigue", "Dizziness", "Rash"]
    },
    "C-708": {
        "condition": "Chronic Pain",
        "phase": "Phase 3",
        "investigator": "Dr. Anya Sharma",
        "efficacy": 85,
        "side_effects": ["Constipation"]
    },
    "A-550": {
        "condition": "Migraine",
        "phase": "Phase 1",
        "investigator": "Dr. Chen Li",
        "efficacy": 55,
        "side_effects": ["Nausea", "Dizziness"]
    },
    "B-205": {
        "condition": "Asthma",
        "phase": "Phase 2",
        "investigator": "Dr. David Kim",
        "efficacy": 72,
        "side_effects": ["Dry Mouth"]
    }
}

# Identify compound with highest efficacy
def highest_efficacy(c):
    max_eff = 0
    comp = ""
    for i in c:
        if c[i]["efficacy"] > max_eff:
            max_eff = c[i]["efficacy"]
            comp = i
    return comp



# Create a set of all side effects
def all_side_effects(c):
    s = set()
    for i in c:
        for e in c[i]["side_effects"]:
            s.add(e)
    return s



# List compounds in a given trial phase
def compounds_by_phase(c, phase):
    result = []
    for i in c:
        if c[i]["phase"] == phase:
            result.append(i)
    return result


# Investigator details
def investigator_info(c, name):
    count = 0
    conditions = []
    for i in c:
        if c[i]["investigator"] == name:
            count += 1
            conditions.append(c[i]["condition"])
    return count, conditions


# Side effects reported by more than one compound
def common_side_effects(c):
    effect_count = {}
    for i in c:
        for e in c[i]["side_effects"]:
            effect_count[e] = effect_count.get(e, 0) + 1

    result = []
    for e in effect_count:
        if effect_count[e] > 1:
            result.append(e)
    return result

    
print("1. Compound with highest efficacy:", highest_efficacy(compounds))
print("2. All side effects:", all_side_effects(compounds))

phase = input("3. Enter trial phase (e.g., Phase 2): ")
print("   Compounds in", phase, ":", compounds_by_phase(compounds, phase))

name = input("4. Enter investigator name: ")
count, cond = investigator_info(compounds, name)
print("   Number of compounds:", count)
print("   Target conditions:", cond)

print("5. Common side effects:", common_side_effects(compounds))
