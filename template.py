def main(data):
    print("Start")
    # Enter code here

if __name__ == "__main__":
    with open("dayX_input.txt", 'r') as file:
        data = file.read().splitlines()
    main(data)
