# S -> A|B
# A -> CC|B
# B -> x|y|z
# C -> 0D
# D -> 1|2|3



# S -> A|B
def S(tokens):
    try:
        A(tokens)
    except:
        try:
            B(tokens)
        except:
            print("FAILED")
            exit()

    if len(tokens) > 0:
        print("Failed, leftovers")
        exit()
    else:
        print("passed")
        exit()

# A -> CC|B
def A(tokens):
    try:
        C(tokens)
        C(tokens)
    except:
        B(tokens)



# B -> x|y|z
def B(tokens):
    if tokens[0] == 'x':
        tokens.pop(0)
    elif tokens[0] == 'y':
        tokens.pop(0)
    elif tokens[0] == 'z':
        tokens.pop(0)
    else:
        raise Exception("Failed")
# C -> 0D
def C(tokens):
    if tokens[0] != '0':
        raise Exception("Failed")
    tokens.pop(0)
    D(tokens)

# D -> 1|2|3
def D(tokens):
    if tokens[0] == '1':
        tokens.pop(0)
    elif tokens[0] == '2':
        tokens.pop(0)
    elif tokens[0] == '3':
        tokens.pop(0)


def main():
    sentence = "paul"

    tokens = [char for char in sentence]
    print(tokens)

    S(tokens)

if __name__ == '__main__':

    main()
