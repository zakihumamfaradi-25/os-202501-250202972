import csv


def simulasi_fcfs(nama_file):
    proses = []

    with open(nama_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            proses.append({
                "nama": row["Process"],
                "arrival": int(row["ArrivalTime"]),
                "burst": int(row["BurstTime"])
            })

    # Urutkan berdasarkan arrival time (FCFS)
    proses.sort(key=lambda x: x["arrival"])

    waktu = 0
    total_waiting = 0
    total_turnaround = 0

    print("\nProses | Arrival | Burst | Waiting | Turnaround")
    print("-" * 50)

    for p in proses:
        if waktu < p["arrival"]:
            waktu = p["arrival"]

        waiting = waktu - p["arrival"]
        turnaround = waiting + p["burst"]

        waktu += p["burst"]

        total_waiting += waiting
        total_turnaround += turnaround

        print(f"{p['nama']:6} | {p['arrival']:7} | {p['burst']:5} | {waiting:7} | {turnaround:10}")

    n = len(proses)
    print("\nRata-rata Waiting Time :", round(total_waiting / n, 2))
    print("Rata-rata Turnaround Time :", round(total_turnaround / n, 2))
