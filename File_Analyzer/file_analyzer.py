import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import re # reg-exp

# Function to open and display file 1 content
def open_file1():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text_content = file.read()
        file1_text_box.delete('1.0', tk.END)  # Clear the text box
        file1_text_box.insert(tk.END, text_content)  # Insert file content into the text box
        result_label.config(text=f"File Path: {file_path}")
    # get the file name from the file path using reg-exp
    file1_name = re.findall('.*/(.+txt)$', file_path)
    # file 1 label
    file1_name_label.config(text=f"File 1:  {file1_name[0]}")
# ************************************************************************ # 

# Function to open and display file 2 content
def open_file2():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text_content = file.read()
        file2_text_box.delete('1.0', tk.END)  # Clear the text box
        file2_text_box.insert(tk.END, text_content)  # Insert file content into the text box
        result_label.config(text=f"File Path: {file_path}")
    # get the file name from the file path using reg-exp
    file2_name = re.findall('.*/(.+txt)$', file_path)
    # file 1 label
    file2_name_label.config(text=f"File 2:  {file2_name[0]}")
# ************************************************************************ #

# Function to open and display the file content
def compare_files():
    # Remove any existing highlights
    file1_text_box.tag_remove('highlight', '1.0', tk.END)  
    # read the files content from the text box
    file1_content = file1_text_box.get('1.0', tk.END).strip()
    file2_content = file2_text_box.get('1.0', tk.END).strip()
    # if both files are empty
    if len(file1_content) == 0 and len(file2_content) == 0:
        result_text = 'The two Files are Empty'
    # if one of the files are empty
    elif len(file1_content) == 0 or len(file2_content) == 0:
        result_text = 'File 1 is Empty' if len(file1_content) == 0 else 'File 2 is Empty'
    # if the files are the same
    elif file1_content == file2_content:
        result_text = 'The two Files are Identical'
    # if the files are not the same
    else:
        result_text = 'The two Files are Different'
    # display the compare result
    result_label.config(text=result_text)
# ************************************************************************ #

# Function to count the words in the file
def count_words():
    # Remove any existing highlights
    file1_text_box.tag_remove('highlight', '1.0', tk.END)  
    word_count = None
    # get the content from the text box
    content = file1_text_box.get('1.0', tk.END).strip()
    if len(content) != 0: # if the text box are not empty
        lines = content.splitlines()
        for line in lines:
            words = line.split()
            word_count = len(words) if word_count is None else word_count + len(words)
            
        result_label.config(text=f'Word Count= {word_count}')
    else: # if the text box are empty
        result_label.config(text=f'Word Count= 0')
# ************************************************************************ #

# Function to count the distinct/unique words in the text
def count_unique_words():
    # Remove any existing highlights
    file1_text_box.tag_remove('highlight', '1.0', tk.END)
    u_dict = dict()
    tmp_lst = list()
    mostWords_list = list()
    # get the content from the text box
    content = file1_text_box.get('1.0', tk.END).strip()
    if len(content) != 0: # if the text box are not empty
        lines = content.splitlines()
        for line in lines:
            # replace any of these chars in the line with a space
            line = re.sub(r'[-,;:\"\&\.\[\]\{\}\(\)\_\\]', ' ', line)
            words = line.split()
            # count with dictionary
            for word in words:
                u_dict[word] = u_dict.get(word, 0) + 1
        # dictionary length is the no. of unique words
        text1 = f'Unique Word Count: {len(u_dict)}\n'
        # sort the list of tuples by value/count
        tmp_lst =  [ (v, k) for (k, v) in u_dict.items() ] # return list of (count, word)
        tmp_lst = sorted(tmp_lst, reverse=True) # sorting descending order (H2L)
        mostWord = tmp_lst[0][1] # the first element word as it's sorted
        mostCount = tmp_lst[0][0] # the first element count as it's sorted
        # to get all the words that has the mostCount
        for (count, word) in tmp_lst:
            if count == mostCount: 
                mostWords_list.append(word)
        text2 = f'Most Occurred Word/s:  {mostWords_list}\nwith Count=  {mostCount}\n'
        result_label.config(text= text1 + text2)
    else:
        result_label.config(text= 'Unique Word Count= 0')
# ************************************************************************ #

# Function to count the characters (including any special-chars/spaces) in the file
def count_characters():
    # Remove any existing highlights
    file1_text_box.tag_remove('highlight', '1.0', tk.END)
    character_count = None
    # get the content from the text box
    content = file1_text_box.get('1.0', tk.END)
    if len(content) != 0:
        lines = content.splitlines()
        for line in lines:  
            character_count = len(line) if character_count is None else character_count + len(line)
        result_label.config(text=f'Character Count= {character_count}')
    else:
        result_label.config(text=f'Character Count= 0')
# ************************************************************************ #

# Function to search for a specific term in the text
def search_text():
    # Remove any existing highlights
    file1_text_box.tag_remove('highlight', '1.0', tk.END)
    occurrences = 0
    line_numbers = list()
    # get the search term from the search entry box
    search_term = search_entry.get().strip()
    # get the content from the text box
    content = file1_text_box.get('1.0', tk.END).strip()
    # make sure that user entered a file and a search text
    if len(search_term) != 0 and len(content) !=0 :
        lines = content.splitlines()
        for (line_num, line) in enumerate(lines, start=1):
            occurrences += line.count(search_term)
            # store the line numbers containing the search term
            if line.count(search_term) > 0:
                line_numbers.append( line_num )
                
        text1 = f'Occurrences of "{search_term}":  {occurrences}\n'
        text2 = f'Lines:  {line_numbers}'
        # display and highlight the search term
        if occurrences > 0:
            highlight_text(search_term) 
            result_label.config(text= text1 + text2)
        else:
            result_label.config(text= text1)
    # the user did not enter a file
    elif len(content) == 0: 
        result_label.config(text=f'Please Open a File')
    # the user did not enter a search text
    elif len(search_term) == 0: 
        result_label.config(text=f'Please Enter a Search Text')
# ************************************************************************ #

# Function to search for a specific term in the text
def search_word():
    # Remove any existing highlights
    file1_text_box.tag_remove('highlight', '1.0', tk.END)
    occurrences = 0
    line_numbers = list()
    # get the search word from the search entry box
    search_term = search_entry.get().strip()
    # get the content from the text box
    content = file1_text_box.get('1.0', tk.END).strip()
    # reg-exp patterns that used below
    pattern = fr'{search_term}'
    non_alphabet = r'[^a-zA-Z]'
    # make sure that user entered a file and a search word
    if len(search_term) != 0 and len(content) !=0 :
        lines = content.splitlines()
        for (line_num, line) in enumerate(lines, start=1):
            words = line.split()
            word_found = False
            for word in words:
                # the word is the same as the search word 
                if word == search_term:
                    occurrences += 1
                    word_found = True
                # the word starts with search_term after that non-alphabet char 
                # or ends with search_term before that non-alphabet char or in between
                # ex: (X-any, any-X, any-X-any) 
                elif len(word) > len(search_term): 
                    if re.search(f'^{pattern}{non_alphabet}+|{non_alphabet}+{pattern}$|{non_alphabet}+{pattern}{non_alphabet}+', word):
                        occurrences = occurrences + 1
                        word_found = True
            # store the line numbers containing the search term
            if  word_found:
                line_numbers.append( line_num )
                
        text1 = f'Occurrences of "{search_term}":  {occurrences}\n'
        text2 = f'Lines:  {line_numbers}'
        # display and highlight the search term
        if occurrences > 0:
            highlight_word(search_term)
            result_label.config(text= text1 + text2)
        else:
            result_label.config(text= text1)
    # the user did not enter a file
    elif len(content) == 0: 
        result_label.config(text=f'Please Open a File')
    # the user did not enter a search word
    elif len(search_term) == 0: 
        result_label.config(text=f'Please Enter a Search Word')
# ************************************************************************ #
        
# Function to highlight searched word
def highlight_word(term):
    # Remove any existing highlights
    file1_text_box.tag_remove('highlight', '1.0', tk.END)
    # Use regular expression to find whole words
    pattern = r'\b' + re.escape(term) + r'\b'
    content = file1_text_box.get('1.0', tk.END)  # Get all text from the text box
    for match in re.finditer(pattern, content):
        start_idx = file1_text_box.index(f"1.0 + {match.start()} chars")
        end_idx = file1_text_box.index(f"1.0 + {match.end()} chars")
        # Add tag for highlighting
        file1_text_box.tag_add('highlight', start_idx, end_idx)
    # Configure the appearance of the highlight
    file1_text_box.tag_config('highlight', background='yellow')
# ************************************************************************ #

# Function to highlight searched text
def highlight_text(term):
    # Remove any existing highlights
    file1_text_box.tag_remove('highlight', '1.0', tk.END)
    start_pos = '1.0'
    while True:
        start_pos = file1_text_box.search(term, start_pos, stopindex=tk.END)
        if not start_pos:
            break
        end_pos = f"{start_pos}+{len(term)}c"
        file1_text_box.tag_add('highlight', start_pos, end_pos)
        start_pos = end_pos
    file1_text_box.tag_config('highlight', background='orange')
# ************************************************************************ #

# Function to clear the search and highlights
def clear_search():
    search_entry.delete(0, tk.END)
    file1_text_box.tag_remove('highlight', '1.0', tk.END)
    result_label.config(text="Results will be displayed here..")
# ************************************************************************ #

# Function to reset the app
def reset_all():
    search_entry.delete(0, tk.END)
    result_label.config(text="Results will be displayed here..")
    file1_name_label.config(text="File 1")
    file2_name_label.config(text="File 2")
    file1_text_box.delete('1.0', tk.END)
    file2_text_box.delete('1.0', tk.END)
# ************************************************************************ #

# Tkinter Setup
root = tk.Tk()
root.title("Text File Analyzer")
root.geometry('800x600')
# ************************************************************************ #

# Widgets
frame_top = tk.Frame(root)
frame_top.grid(row=0, column=0, padx=10, pady=10)

# Buttons
open_file1_button = tk.Button(frame_top, text="Open File", command=open_file1, width=15, fg='black', bg='lightgrey')
open_file1_button.grid(row=0, column=0, padx=10)

open_file2_button = tk.Button(frame_top, text="Open Compare File", command=open_file2, width=20, fg='black', bg='lightgrey')
open_file2_button.grid(row=0, column=1, padx=10)

compare_files_button = tk.Button(frame_top, text="Compare Files", command=compare_files, width=15)
compare_files_button.grid(row=3, column=3, padx=10)

count_words_button = tk.Button(frame_top, text="Count Words", command=count_words, width=15)
count_words_button.grid(row=3, column=0, padx=10)

count_unique_words_button = tk.Button(frame_top, text="Count Unique Words", command=count_unique_words, width=20)
count_unique_words_button.grid(row=3, column=1, padx=10)

count_characters_button = tk.Button(frame_top, text="Count Characters", command=count_characters, width=15)
count_characters_button.grid(row=3, column=2, padx=10)

search_text_button = tk.Button(frame_top, text="Search Text", command=search_text, width=15)
search_text_button.grid(row=1, column=2, pady=10)

search_word_button = tk.Button(frame_top, text="Search Word", command=search_word, width=15)
search_word_button.grid(row=1, column=3, pady=10)

clear_button = tk.Button(frame_top, text="Clear Highlights", command=clear_search, width=15, fg='black', bg='lavender')
clear_button.grid(row=0, column=2, padx=10)

reset_button = tk.Button(frame_top, text="Reset All", command=reset_all, width=15, fg='black', bg='lavender')
reset_button.grid(row=0, column=3, padx=10)
# ************************************************************************ #

# Labels
search_label = tk.Label(frame_top, text="Search Term:")
search_label.grid(row=1, column=0, pady=10)

result_label = tk.Label(root, text="Results will be displayed here..", font=("Arial ", 11))
result_label.grid(row=0, column=1, padx=10, pady=10)

file1_name_label = tk.Label(root, text=f'File 1')
file1_name_label.grid(row=1, column=0, pady=10, padx=10)
    
file2_name_label = tk.Label(root, text=f'File 2')
file2_name_label.grid(row=1, column=1, pady=10, padx=10)
# ************************************************************************ #

# text boxes and search text entry
file1_text_box = scrolledtext.ScrolledText(root, height=31, width=80, wrap=tk.WORD)
file1_text_box.grid(row=5, column=0, padx=10)

file2_text_box = scrolledtext.ScrolledText(root, height=31, width=80, wrap=tk.WORD)
file2_text_box.grid(row=5, column=1, padx=10)

search_entry = tk.Entry(frame_top, width=30)
search_entry.grid(row=1, column=1, pady=10)
# ************************************************************************ #


# Run the application
root.mainloop()