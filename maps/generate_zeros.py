
def main():
    width = 600
    height = 600
    wsize = 40
    hsize = 40
    wratio = width // wsize
    hratio = height // hsize
    for i in range(wratio + 1):
        if (i == 0): print("[",end="")
        elif (i == wratio): print("]")
        for j in range(hratio + 1):
            if (j == 0): print("[",end="")
            elif (j == hratio): print("0]")
            else: print("0,",end="")


if __name__ == "__main__":
    main()
