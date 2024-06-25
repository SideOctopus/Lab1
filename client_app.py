import requests

def main():
    while True:
        print("1) Send POST request")
        print("2) Send GET request")
        print("3) Exit")
        choice = int(input("Your choice: "))

        if choice == 1:
            message = input("Enter your message: ")
            response = requests.post('http://localhost:5000/data', data=message)
            print('Response:', response.json())
        elif choice == 2:
            response = requests.get('http://localhost:5000/data')
            print('Response:', response.json())
        elif choice == 3:
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
