login_attempts = ["alice", "bob", "eve", "alice", "mallory", "frank", "eve"]
authorized_users = {"alice", "bob", "frank", "grace"}
def identify_intruders(attempts,authorised):
    intruders=set()
    
    for i in attempts:
        if i not in authorised:
            intruders.add(i)
    return intruders
print(identify_intruders(login_attempts,authorized_users))

            