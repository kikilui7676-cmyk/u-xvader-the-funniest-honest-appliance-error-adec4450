import os

FAULT = {"appliance": "microwave", "hot": "the edges", "cold": "the middle"}
LINE = "Error: I heated {hot} and left {cold} frozen, as is tradition.".format(
    hot=FAULT["hot"], cold=FAULT["cold"]
)

def error_message():
    return LINE

def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(error_message())
        handle.write("\n")

if __name__ == "__main__":
    main()
