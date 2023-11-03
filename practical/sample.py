import threading
import time

class ShopQueue:
    def __init__(self):
        self.customer_queue = []
        self.customer_counter = 0
        self.lock = threading.Lock()
        self.running = True

    def add_customer(self):
        with self.lock:
            self.customer_counter += 1
            self.customer_queue.append(self.customer_counter)
            print(f"Customer with ticket {self.customer_counter} is added to the queue.")

    def see_next_customer(self):
        with self.lock:
            if self.customer_queue:
                next_customer = self.customer_queue.pop(0)
                print("Sales Assistant is ready to see the next customer.")
                print(f"The customer with ticket number {next_customer} will be seen now.")
            else:
                print("No customers in the queue.")

    def display_queue(self):
        with self.lock:
            print(f"The customers with the following tickets are in the queue: {self.customer_queue}")

    def stop(self):
        self.running = False

def new_customers(shop):
    while shop.running:
        shop.add_customer()
        shop.display_queue()
        time.sleep(3)

def see_customers(shop):
    while shop.running:
        shop.see_next_customer()
        shop.display_queue()
        time.sleep(5)

def main():
    print("Welcome to my SHOP.")
    print("Press any key to quit the program.")

    shop = ShopQueue()

    add_customers_thread = threading.Thread(target=new_customers, args=(shop,))
    see_customers_thread = threading.Thread(target=see_customers, args=(shop,))

    add_customers_thread.start()
    see_customers_thread.start()

    input("Press Enter to quit the program")

    shop.stop()  # Stop the threads

    add_customers_thread.join()
    see_customers_thread.join()

if __name__ == "__main__":
    main()

