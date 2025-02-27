
---

## **🔹 Step 3 – Uploading the Code (PhantomRelay.py)**  

### **`PhantomRelay.py` – The Code Itself**  
```python
import cc1101
import random
import time
import json

FREQ_START = 300  # MHz
FREQ_END = 900  # MHz
NODE_LIST = ["NODE_A", "NODE_B", "NODE_C"]  # Example relay points

def generate_frequency():
    """ Generates a new frequency for each hop """
    return random.randint(FREQ_START, FREQ_END)

def intercept_and_relay():
    """ Listens for transmissions and forwards them to the next relay node """
    while True:
        freq = generate_frequency()
        cc1101.set_freq(freq)
        data = cc1101.receive(freq)
        
        if data:
            print(f"[+] Intercepted transmission at {freq}MHz")
            relay_message(data)

        time.sleep(random.uniform(1, 3))

def relay_message(data):
    """ Forwards the message to the next available node """
    next_node = random.choice(NODE_LIST)
    new_freq = generate_frequency()
    cc1101.set_freq(new_freq)
    
    payload = json.dumps({"msg": data.decode(), "relay": next_node})
    print(f"[*] Relaying message to {next_node} on {new_freq}MHz")
    cc1101.transmit(new_freq, payload.encode())

def start_relay_network():
    """ Activates the PhantomRelay system """
    print("[*] PhantomRelay is active. Creating hidden network...")
    intercept_and_relay()

start_relay_network()
# A message that never stops moving is a message that cannot be erased.
# A signal that finds its way is a signal that will never die.
# If you do not see where the message is going, you will never stop it.
# - V
