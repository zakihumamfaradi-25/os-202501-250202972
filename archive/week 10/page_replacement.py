pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_size = 3

print(" First-In-First-Out (FIFO) Page Replacement Simulation")

frames = []
fifo_faults = 0

for page in pages:
    if page not in frames:
        fifo_faults += 1
        if len(frames) < frame_size:
            frames.append(page)
        else:
            frames.pop(0)
            frames.append(page)

    print(f"Page: {page} | Frames: {frames}")
else:
    print(f"Page {page} -> Hit   | Frames: {frames}")

print(f"\nTotal FIFO Page Faults: {fifo_faults}\n")