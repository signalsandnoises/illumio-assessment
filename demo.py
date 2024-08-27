# Part 1
protocols = {}

with open("protocols.csv", "r") as file:
    for i, line in enumerate(file):
        protocols[str(i)] = line.strip().split(',')[1].lower()
        # We're using str(i) as the key because that's how it's represented in the flow log


lookup = dict()

with open("input_lookup.csv", "r") as file:
    file.readline() # skip the first line
    for i, line in enumerate(file):
        contents = line.split(",")
        port_protocol = ",".join(contents[:2])
        tag = contents[2].strip().lower()
        
        lookup[port_protocol] = tag


# Part 2
from collections import defaultdict

count_port_protocols = defaultdict(int)
count_tags = {tag: 0 for tag in lookup.values()}
count_tags["Untagged"] = 0

with open("input_flowlog.txt", "r") as file:
    for line in file:
        # Get the port_protocol
        contents = line.split()
        port_protocol = ",".join((contents[6], protocols[contents[7]]))
        
        # Count the port_protocol
        count_port_protocols[port_protocol] += 1

        # Get and count the tag
        if port_protocol in lookup:
            tag = lookup[port_protocol]
            count_tags[tag] = count_tags[tag] + 1
        else:
            count_tags["Untagged"] += 1


# Part 3
with open("output_tag_counts.csv", "w") as file:
    file.write('Tag,Count\n')
    for key, value in count_tags.items():
        file.write(f'{key},{value}\n')

with open("output_port_protocol_combination_counts.csv", "w") as file:
    file.write('Port,Protocol,Count\n')
    for key, value in count_port_protocols.items():
        file.write(f'{key},{value}\n')