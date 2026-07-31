import re

# ==========================================
# ၁။ ဒီနေရာမှာ မိမိရဲ့ Input File Path ကို ပြင်ပေးပါ
# ==========================================
input_file_path = "/data/myPOS/otest.1k.nopipe.txt"  # မိမိ file path ကို ပြောင်းပါ
mode = 's'   # 's' = syllable tagging, 'c' = character tagging
n = 4        # Tag အမျိုးအစား (2, 3, သို့မဟုတ် 4)

# ==========================================
# Tagging Logic များနှင့် Regular Expression
# ==========================================
myConsonant = r"က-အ"
enChar = r"a-zA-Z0-9"
otherChar = r"ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s"
ssSymbol = r'္'
aThat = r'်'

BreakPattern = re.compile(r"((?<!" + ssSymbol + r")["+ myConsonant + r"](?![" + aThat + ssSymbol + r"])" + r"|[" + enChar + otherChar + r"])")

def segment_into_syllables(text):
    line = re.sub(BreakPattern, " "+r"\1", text)
    return line.split()

def make_word_ls(line, chk='s'):
    word_ls = []
    if chk == 's':
        words = line.split()
        for word in words:
            word_ls.append(list(segment_into_syllables(word)))
    else:
        word_ls = [list(c) for c in line.split()]
    return word_ls
    
def two_tagger(word_ls):
    for word in word_ls:
        n_of_element = len(word)
        if n_of_element == 1:
            print(f"{word[0]}\t|")
        else:
            for i in range(0, n_of_element-1):
                print(f"{word[i]}\t-")
            print(f"{word[n_of_element-1]}\t|")
            
def three_tagger(word_ls):
    for word in word_ls:
        n_of_element = len(word)
        if n_of_element >= 3:
            print(f"{word[0]}\t<")
            for i in range(1, n_of_element-1):
                print(f"{word[i]}\t-")
            print(f"{word[n_of_element-1]}\t|")
        elif n_of_element == 2:
            print(f"{word[0]}\t<")
            print(f"{word[1]}\t|")
        else:
            print(f"{word[0]}\t|")
            
def four_tagger(word_ls):
    for word in word_ls:
        n_of_element = len(word)
        if n_of_element >= 4:
            print(f"{word[0]}\t<")
            for i in range(1, n_of_element-2):
                print(f"{word[i]}\t-")
            print(f"{word[n_of_element-2]}\t>")
            print(f"{word[n_of_element-1]}\t|")
        elif n_of_element == 3:
            print(f"{word[0]}\t<")
            print(f"{word[1]}\t>")
            print(f"{word[2]}\t|")
        elif n_of_element == 2:
            print(f"{word[0]}\t<")
            print(f"{word[1]}\t|")
        else:
            print(f"{word[0]}\t|")

# ==========================================
# Main Execution
# ==========================================
try:
    with open(input_file_path, 'r', encoding='utf-8') as file:
        if n == 2:
            for line in file:
                two_tagger(make_word_ls(line, mode))
                print()
        elif n == 3:
            for line in file:
                three_tagger(make_word_ls(line, mode))
                print()
        elif n == 4:
            for line in file:
                four_tagger(make_word_ls(line, mode))
                print()
        else:
            print("Only 2 to 4 accepted.")
except FileNotFoundError:
    print(f"File '{input_file_path}' not found. Please check your path.")
except Exception as e:
    print(f"An error occurred: {e}")
