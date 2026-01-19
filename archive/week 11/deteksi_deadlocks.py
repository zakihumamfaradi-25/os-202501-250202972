print("=== FILE BARU WFG DIJALANKAN ===")

processes = ['p1', 'p2', 'p3']

allocation = {
    'p1': ['r1'],
    'p2': ['r2'],
    'p3': ['r3']
}

request = {
    'p1': ['r2'],
    'p2': ['r3'],
    'p3': ['r1']
}

waitforgraph = {}

for p in processes: 
    waitforgraph[p] = []
    for other in processes:
        if request[p][0] in allocation[other]:
            waitforgraph[p].append(other)

print("waitforgraph:")
for p, edges in waitforgraph.items():
    print(f" {p} -> {edges}")

visited = set()
recstack = set()
deadlock_processes = set()

def detect_cycle(process):
    visited.add(process)
    recstack.add(process)

    for neighbor in waitforgraph[process]:
        if neighbor not in visited:
            if detect_cycle(neighbor):
                return True
        elif neighbor in recstack:
            deadlock_processes.update(recstack)
            return True

    recstack.remove(process)
    return False

for p in processes:
    if p not in visited:
        detect_cycle(p)

if deadlock_processes:
    print("ADA DEADLOCK TERDETEKSI:")
    print("Proses yang terlibat dalam deadlock:", ",".join(sorted(deadlock_processes)))
else:
    print("TIDAK ADA DEADLOCK TERDETEKSI")
