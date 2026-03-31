wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

staff = {}
for dept, docs in wards.items():
    for doc in docs:
        staff[doc] = staff.get(doc, 0) + 1
print(staff)

     