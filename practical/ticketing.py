#!/usr/bin/env python3

import time
import threading

class TicketStructure:
  def __init__(self): # initializing the queue
    self.customer_queue = [] # create an empty list to store the queue
    self.running = True
    self.lock = threading.Lock()
    self.customer_counter = 0

  def add_customer(self):
    with self.lock:
      self.customer_counter += 1
      self.customer_queue.append(self.customer_counter)
      print(f"Customer with ticket {self.customer_counter} is added to the queue.")

  def see_customer(self):
    with self.lock:
      if self.customer_queue:
        customer_number = self.customer_queue.pop(0)
        print(f"Sales Assistant is ready to see the next customer.")
        print(f"The customer with ticket number {customer_number} will be seen now.")
      else:
        print("No customers in the queue.")

  def queue_display(self):
    with self.lock:
      print(f"The customers with the following tickets are in the queue: {self.customer_queue}")

  def stop(self):
    self.running = False

def NewCustomers(store):
  while store.running:
    store.add_customer()
    store.queue_display()
    time.sleep(3)

def SeeCustomers(store):
  while store.running:
    store.see_customer()
    store.queue_display()
    time.sleep(5)

def main():
  print("Welcome to my SHOP.")

  ticket_structure = TicketStructure()

  add_customer_thread = threading.Thread(target=NewCustomers, args=(ticket_structure,))
  see_customer_thread = threading.Thread(target=SeeCustomers, args=(ticket_structure,))

  add_customer_thread.start()
  see_customer_thread.start()

  input("Press Enter to quit the program")
  ticket_structure.stop()  # Stop the threads

  add_customer_thread.join()
  see_customer_thread.join()

if __name__ == "__main__":
  main()