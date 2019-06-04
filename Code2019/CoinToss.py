# Write a program to generate boolean outcome like flipping coin

import random
Outcome = random.choice([True, False])

try:
     while True:
         
         if (Outcome == "True"):
            print("Outcome: Heads")
         else:
             print("Outcome: Tails")
             
except KeyboardInterrupt:
    print("exit")

