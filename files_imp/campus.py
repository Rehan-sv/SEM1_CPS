campuses = {
    "Dubai": {
        "programs": ["Engineering", "Business", "Arts"],
        "students": 4200,
        "year": 2015
    },
    "Singapore": {
        "programs": ["Computer Science", "Business", "Media Studies"],
        "students": 5800,
        "year": 2008
    },
    "London": {
        "programs": ["Law", "Arts", "History", "Economics"],
        "students": 6100,
        "year": 1999
    },
    "Sydney": {
        "programs": ["Science", "Engineering", "Business"],
        "students": 3900,
        "year": 2018
    },
    "Berlin": {
        "programs": ["Arts", "Computer Science", "Media Studies"],
        "students": 5500,
        "year": 2012
    }
}

# -------- TASK 1 --------
# Determine the newest campus
def newest_campus(c):
    latest_year = 0
    campus_name = ""
    for i in c:
        if c[i]["year"] > latest_year:
            latest_year = c[i]["year"]
            campus_name = i
    return campus_name


# -------- TASK 2 --------
# Create a set of all programs
def all_programs(c):
    s = set()
    for i in c:
        for p in c[i]["programs"]:
            s.add(p)
    return s


# -------- TASK 3 --------
# Campuses exceeding a minimum population
def population_above(c, limit):
    result = []
    for i in c:
        if c[i]["students"] > limit:
            result.append(i)
    return result


# -------- TASK 4 --------
# Count campuses offering a given program
def count_program(c, program):
    count = 0
    for i in c:
        if program in c[i]["programs"]:
            count += 1
    return count


# -------- TASK 5 --------
# Programs offered by exactly one campus
def unique_programs(c):
    prog_count = {}
    for i in c:
        for p in c[i]["programs"]:
            prog_count[p] = prog_count.get(p, 0) + 1

    result = []
    for p in prog_count:
        if prog_count[p] == 1:
            result.append(p)
    return result


# -------- OUTPUT SECTION --------
print("1. Newest Campus:", newest_campus(campuses))
print("2. All Programs:", all_programs(campuses))

limit = int(input("3. Enter minimum student population: "))
print("   Campuses exceeding population:", population_above(campuses, limit))

program = input("4. Enter program name: ")
print("   Number of campuses offering", program, ":", count_program(campuses, program))

print("5. Programs offered by exactly one campus:", unique_programs(campuses))
