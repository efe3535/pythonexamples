import os

def main():
    if os.name == "posix":
        print("Linux user!")
    if os.name == "darwin":
        print("macOS user!")
    if os.name == "nt":
        print("Windows user!")
if __name__ == "__main__":
    main()