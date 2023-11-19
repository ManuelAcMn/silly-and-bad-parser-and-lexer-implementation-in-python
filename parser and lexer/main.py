import parsers
import lexers

def main():
    filea = input("Dame el nombre del archivo (.lg)")

    if filea.endswith(".lg") == False:
        filea = filea + ".lg"

    parsers.getFile(filea)

main()