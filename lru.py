def lru_main():
    NUM_PAGES = 4
    pages = [-1] * NUM_PAGES
    page_hits = 0
    page_faults = 0
    current_time = 1

    page_references = [2,3,2,1,5,2,4,5,3,2,3,2,6,7,8,9]
    num_page_references = len(page_references)

    for page in page_references:
        page_hit = False
        for i in range(NUM_PAGES):
            if pages[i] == page:
                page_hit = True
                break

        if page_hit:
            page_hits += 1
        else:
            least_recent_time = current_time
            least_recent_page_index = 0

            for i in range(NUM_PAGES):
                if pages[i] == -1:
                    least_recent_page_index = i
                    break

                if pages[i] < least_recent_time:
                    least_recent_time = pages[i]
                    least_recent_page_index = i

            pages[least_recent_page_index] = current_time
            page_faults += 1

        current_time += 1

    hit_ratio = page_hits / num_page_references
    fault_ratio = page_faults / num_page_references

    print("LRU - Page hits:", page_hits)
    print("LRU - Page faults:", page_faults)
    print("LRU - Hit ratio: {:.2f}".format(hit_ratio))
    print("LRU - Fault ratio: {:.2f}".format(fault_ratio))


if __name__ == "__main__":
    lru_main()
