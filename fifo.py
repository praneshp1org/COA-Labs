from collections import deque

def fifo_main():
    NUM_PAGES = 4
    pages = deque([-1] * NUM_PAGES)
    page_hits = 0
    page_faults = 0

    page_references = [2,3,2,1,5,2,4,5,3,2,3,2,6,7,8,9]
    num_page_references = len(page_references)

    for page in page_references:
        if page in pages:
            page_hits += 1
        else:
            pages.popleft()
            pages.append(page)
            page_faults += 1

    hit_ratio = page_hits / num_page_references
    fault_ratio = page_faults / num_page_references

    print("FIFO - Page hits:", page_hits)
    print("FIFO - Page faults:", page_faults)
    print("FIFO - Hit ratio: {:.2f}".format(hit_ratio))
    print("FIFO - Fault ratio: {:.2f}".format(fault_ratio))


if __name__ == "__main__":
    fifo_main()
