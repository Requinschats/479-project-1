from pathlib import Path
import os

def main():
    for fileName in os.listdir("reuters21578"):
        if fileName != "reut2-017.sgm":
            file_content = Path('reuters21578/' + fileName).read_text()
            print(file_content)


if __name__ == '__main__':
    main()
