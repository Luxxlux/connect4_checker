import sys
#I want to print all of the x's here:
# for x in lines:
#     print(x)
#

# rule n1 = read a file COMPLETE
# rule n2 = parse it (to make it easier to analyze) INCOMPLETE
# rule n3 = code the checks
#   check horizontal
#   check vertical
#   check diagonal

f = sys.argv[1]


def main():

    with open(sys.argv[1], 'r') as f:
        global lines
        lines = f.read()
        print(lines)

def replace_char(test: str, x: str, y: str):
    print(lines)
    replaced_text1 = lines.replace('   ', '.')
    print(replaced_text1)

    replaced_text2 = replaced_text1.replace('|','')
    print(replaced_text2)

    replaced_text3 = replaced_text2.replace('  ','')
    replaced_text4 = replaced_text3.replace(' ','')
    print(replaced_text4)




main()
replace_char(lines,' ','x')









