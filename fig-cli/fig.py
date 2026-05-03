import pyfiglet
import sys

def main():

    text = " ".join(sys.argv[1:]) 

    f = pyfiglet.Figlet(font='slant')
    print(f.renderText(text))

if __name__ == "__main__":
    main()