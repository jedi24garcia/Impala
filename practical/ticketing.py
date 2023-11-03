#!/usr/bin/env python3

import sys
import time
import threading
from threading import Timer

class TicketStructure: # structure
  def __init__(self): # initializing the queue
    self.customer_queue = [] # create an empty list to store the queue
    self.running = True # 
    self.lock = threading.Lock()
    self.customer_counter = 0

# function to add customers in the ticketing system
  def addOn_customer(self):
    with self.lock:
      self.customer_counter += 1
      self.customer_queue.append(self.customer_counter) # adds new customer
      print(f"Customer with ticket {self.customer_counter} is added to the queue.")

# function to see customers in the ticketing system
  def seeOn_customer(self):
    with self.lock:
      if self.customer_queue:
        customer_number = self.customer_queue.pop(0) # removes and gets first customer from the queue
        print("Sales Assistant is ready to see the next customer.")
        print(f"The customer with ticket number {customer_number} will be seen now.")
      else:
        print("No customers in the queue.")
  
  # displays current state of the queue
  def queue_display(self):
    with self.lock:
      print(f"The customers with the following tickets are in the queue: {self.customer_queue}")

  # indicates the program should stop as self.running is set to False
  def exit(self):
    self.running = False

ticket_structure = TicketStructure() # create an instance of the ticketStructure class

def NewCustomers(store):
  global ticket_structure # global variable for ticket_structure
  while store.running:
    time.sleep(3) # adds new customers to data structure for every 3 seconds
    store.addOn_customer() # way to add new customer
    store.queue_display() # way to display the queue

def SeeCustomers(store):
  global ticket_structure # global variable for ticket_structure
  while store.running:
    time.sleep(5) # sees new customers to data structure for every 5 seconds
    store.seeOn_customer() # way to see next customer 
    store.queue_display() # way to display the queue

def main():
  print("Welcome to my SHOP.")
  print("Press any key to quit the program")

  AddCustomer_thread = threading.Thread(target=NewCustomers, args=(ticket_structure,))
  SeeCustomer_thread = threading.Thread(target=SeeCustomers, args=(ticket_structure,))

  AddCustomer_thread.start() # starts thread new customers
  SeeCustomer_thread.start() # starts thread sales 

  sys.stdin.read(1) # pressing any keys will quit the program
  ticket_structure.exit()  # Stop the threads

  AddCustomer_thread.join() # waits for new customers to finish thread
  SeeCustomer_thread.join() # waits for sales to finish thread

if __name__ == "__main__":
  main()

# ANALYSIS
# Why did you select that specific data structure?
# This is because a list is a practical choice for representing in this scenario. It is
# effective due to a supported ordered data, access control and its simplicity.
# How was that data structure suited to the task?
# The list data structure is an applicable and fitting choice of simulating queueing the shop
# because it provides the functional necessities to handle the order of arrival, add, remove
# customers, and to show the state of the queue.
# Could another data structure be used to complete the same task? If so, how would your solution differ?
# Yes, you can use deque from the collections module in Python 3. If said data structure is
# is implemented instead of a list, the solution would be of similar functionality but 
# potentially or significantly improved performance as the deque provides a more 
# efficient append. This would allow adding the customers by the end of the queue.