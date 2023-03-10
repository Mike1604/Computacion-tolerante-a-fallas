import threading
import time

def check_status():
    while True:
        print("Application is running...")
        time.sleep(2)

def main():
    t = threading.Thread(target=check_status)
    t.start()
    
    while True:
        user_input = input("Enter 'q' to quit: ")
        if user_input == "q":
            break
    
    t.join()

if __name__ == "__main__":
    main()