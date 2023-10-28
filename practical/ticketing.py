#!/usr/bin/env python3

import time
import threading
#from threading import Time
#from collections import deque

class TicketStructure:
  def __init__(self):
    self.customer_queue = []
    print("Welcome to my SHOP")
  
  def NewCustomers(self):
    customer_number = 1
    while True:
      print(f"Customer with ticket {customer_number} is added to the queue.")
      self.customer_queue.append(customer_number)
      customer_number += 1
      time.sleep(3)

  def SeeCustomers(self):
    while True:
      if self.customer_queue:
        customer_number = self.customer_queue.pop(0)
        print(f"Sales Assistant is ready to see the next customer.")
        print(f"The customer with ticket number {customer_number} will be seen now.")
        print(f"The customers with the following tickets are in the queue: {self.customer_queue}")
      else:
        print("No customers in the queue.")
        time.sleep(5)

ticket_structure = TicketStructure()

NewCustomers_thread = threading.Thread(target=ticket_structure.NewCustomers)
SeeCustomers_thread = threading.Thread(target=ticket_structure.SeeCustomers)

NewCustomers_thread.start()
SeeCustomers_thread.start()