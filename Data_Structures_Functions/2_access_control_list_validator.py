def identify_intruders(attempts, authorized):
    intruders = set()

    for user in attempts:
        if user not in authorized:
            intruders.add(user)

    return intruders

def identify_intruders_v2(attempts, authorized):
    att = set(attempts)
    auth = set(authorized)
    intruders = att.difference(auth)
    return intruders

login_attempts = ["alice", "bob", "eve", "alice", "mallory", "frank", "eve"]
authorized_users = {"alice", "bob", "frank", "grace"}
print(identify_intruders(login_attempts, authorized_users))
print(identify_intruders_v2(login_attempts, authorized_users))
# Expected Output: {'eve', 'mallory'}