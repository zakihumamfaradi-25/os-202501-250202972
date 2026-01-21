def simulasi_fifo(nama_file, jumlah_frame):
    try:
        with open(nama_file, "r") as file:
            pages = [p.strip() for p in file.read().split(",")]
    except FileNotFoundError:
        print("File dataset memory tidak ditemukan!")
        return

    frame = []
    page_fault = 0

    print("\nPage Reference | Frame RAM | Status")
    print("-" * 45)

    for page in pages:
        if page in frame:
            status = "Hit"
        else:
            status = "Fault"
            page_fault += 1

            if len(frame) < jumlah_frame:
                frame.append(page)
            else:
                frame.pop(0)   # FIFO
                frame.append(page)

        print(f"{page:13} | {str(frame):15} | {status}")

    print("-" * 45)
    print(f"Total Page Fault: {page_fault}")