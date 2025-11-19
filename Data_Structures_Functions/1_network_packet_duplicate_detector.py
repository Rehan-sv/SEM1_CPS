def find_duplicate_packets(packet_sequence_numbers):
    packet_count = {}
    duplicates = {}

    for seq_num in packet_sequence_numbers:
        if seq_num in packet_count:
            packet_count[seq_num] += 1
        else:
            packet_count[seq_num] = 1

    for seq_num, count in packet_count.items():
        if count > 1:
            duplicates[seq_num] = count

    return duplicates

packets = [1001, 1002, 1003, 1002, 1004, 1005, 1001, 1003, 1002]
print(find_duplicate_packets(packets))
# Expected Output: {1001: 2, 1002: 3, 1003: 2}