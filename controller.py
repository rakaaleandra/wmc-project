from setControl import ConfigureController
from setIP import ESP32_IP, ESP32_IP_2, ESP32_PORT
import time
import threading

MyController = ConfigureController(esp32_ip=ESP32_IP, esp32_port=ESP32_PORT,interface="/dev/input/js0", connecting_using_ds4drv=False)
MyController2 = ConfigureController(esp32_ip=ESP32_IP_2, esp32_port=ESP32_PORT, interface="/dev/input/js1", connecting_using_ds4drv=False)

# Run both listen loops in parallel threads
t1 = threading.Thread(target=MyController.listen, daemon=True)
t2 = threading.Thread(target=MyController2.listen, daemon=True)

t1.start()
t2.start()

# Keep main thread alive
t1.join()
t2.join()