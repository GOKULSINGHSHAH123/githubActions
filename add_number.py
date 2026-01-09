# add_number.py

def main():
    with open("input.txt", "r") as f:
        num = int(f.read().strip())

    result = num + 2   # change this to +4 later

    with open("output.txt", "w") as f:
        f.write(str(result))

    print(f"Input: {num}, Output: {result}")

if __name__ == "__main__":
    main()
