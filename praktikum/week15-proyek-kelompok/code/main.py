# main.py
# Mini Simulasi Sistem Operasi
# Menu utama: FCFS Scheduling & FIFO Page Replacement

from fcfs import simulasi_fcfs
from fifo import simulasi_fifo


def tampilkan_menu():
    print("\n=== MINI SIMULASI SISTEM OPERASI ===")
    print("1. Simulasi CPU Scheduling (FCFS)")
    print("2. Simulasi Memory Management (FIFO)")
    print("3. Keluar")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1/2/3): ").strip()

        if pilihan == "1":
            print("\n--- SIMULASI FCFS ---")
            simulasi_fcfs("dataset_cpu.csv")

        elif pilihan == "2":
            print("\n--- SIMULASI FIFO ---")
            try:
                frame = int(input("Masukkan jumlah frame RAM: "))
                simulasi_fifo("dataset_memory.txt", frame)
            except ValueError:
                print("Input harus berupa angka!")

        elif pilihan == "3":
            print("Keluar dari program. Terima kasih.")
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")


if __name__ == "__main__":
    main()
