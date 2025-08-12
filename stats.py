def word_count(text):
    words = text.split()
    return len(words)  




def c_count(text):
    c_dict = {}
    for char in text.lower():
        if char in c_dict:
            c_dict[char] += 1
        else:
            c_dict[char] = 1
    return c_dict

def print_sorted_counts(c_dict):
    sorted_items = sorted(c_dict.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_items:
        print(f"{char}: {count}")
