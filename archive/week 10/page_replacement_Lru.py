pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_size = 3
print(" Least Recently Used (LRU) Page Replacement Simulation")

frames = []            
recent = {}            
page_fault = 0         # penghitung page fault
time = 0               # penanda waktu akses

for page in pages:     # loop membaca setiap halaman
    time += 1          # waktu bertambah setiap akses

    if page not in frames:          # kondisi PAGE FAULT
        page_fault += 1

        if len(frames) < frame_size:
            frames.append(page)     # jika frame belum penuh
        else:
            # mencari halaman yang paling lama tidak digunakan
            lru_page = min(frames, key=lambda x: recent[x])
            frames.remove(lru_page)
            frames.append(page)

        print(f"Page {page} -> Fault | Frames: {frames}")
    else:
        print(f"Page {page} -> Hit   | Frames: {frames}")

    recent[page] = time             # update waktu terakhir halaman dipakai

print("Total Page Fault:", page_fault)

