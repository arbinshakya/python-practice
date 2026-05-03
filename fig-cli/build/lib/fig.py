import pyfiglet
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: fig <text>")
        return

    text = " ".join(sys.argv[1:]) 

    f = pyfiglet.Figlet(font='slant')
    print(f.renderText(text))

if __name__ == "__main__":
    main()