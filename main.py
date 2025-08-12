import sys
from stats import word_count, c_count, print_sorted_counts



def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")

    cmd_line = sys.argv[1]
    
    print(f"Analyzing book found at {cmd_line}...")

    text = get_book_text(cmd_line)

    print("----------- Word Count ----------")
    total_words = word_count(text)  
    print(f"Found {total_words} total words")  

    print("--------- Character Count -------")
    c_dict = c_count(text)
    print_sorted_counts(c_dict)

    print("============= END ===============")




def get_book_text(files):
    with open(files, "r") as the_files:
        return the_files.read()



main()