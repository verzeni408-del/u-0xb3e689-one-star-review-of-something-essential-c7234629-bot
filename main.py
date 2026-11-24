"""One-star review of something essential: sleep, rated honestly."""
import os

TEXT = "Sleep takes a third of my life and still charges me a stiff neck every morning."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

if __name__ == "__main__":
    main()
