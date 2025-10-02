from pyPS4Controller.controller import Controller
import socket
import time
import threading

ESP32_IP = "192.168.100.15"
ESP32_IP_2 = "192.168.100.19"
ESP32_PORT = 4210

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        
    def on_L3_up(self, value):
        # print("on_L3_up: {}".format(value))
        pass

    def on_L3_down(self, value):
        # print("on_L3_down: {}".format(value))
        pass

    def on_L3_left(self, value):
        # print("on_L3_left: {}".format(value))
        pass

    def on_L3_right(self, value):
        # print("on_L3_right: {}".format(value))
        pass

    def on_L3_y_at_rest(self):
        pass

    def on_L3_x_at_rest(self):
        pass

    def on_R3_up(self, value):
        # print("on_R3_up: {}".format(value))
        pass

    def on_R3_down(self, value):
        # print("on_R3_down: {}".format(value))
        pass

    def on_R3_left(self, value):
        # print("on_R3_left: {}".format(value))
        pass

    def on_R3_right(self, value):
        # print("on_R3_right: {}".format(value))
        pass

    def on_R3_y_at_rest(self):
        """R3 joystick is at rest after the joystick was moved and let go off"""
        # print("on_R3_y_at_rest")
        pass

    def on_R3_x_at_rest(self):
        """R3 joystick is at rest after the joystick was moved and let go off"""
        # print("on_R3_x_at_rest")
        pass

    def on_circle_press(self):
        sock.sendto(b'1', (ESP32_IP, ESP32_PORT))

    def on_circle_release(self):
        sock.sendto(b'2', (ESP32_IP, ESP32_PORT))
    
    def on_R2_press(self, value):
        # super().on_R2_press(self, value)
        sock.sendto(str(value).encode(), (ESP32_IP, ESP32_PORT))

    def on_left_arrow_press(self):
        # super(self)
        message = "left"
        sock.sendto(message.encode(), (ESP32_IP, ESP32_PORT))

    def on_right_arrow_press(self):
        # super(self)
        message = "right"
        sock.sendto(message.encode(), (ESP32_IP, ESP32_PORT))

    def on_left_right_arrow_release(self):
        # super(self)
        sock.sendto("right_release".encode(), (ESP32_IP, ESP32_PORT))

    def on_down_arrow_press(self):
        # super(self)
        sock.sendto(b"down", (ESP32_IP, ESP32_PORT))

    def on_up_arrow_press(self):
        # super(self)
        sock.sendto("up".encode(), (ESP32_IP, ESP32_PORT))
    
    def on_up_down_arrow_release(self):
        print("up_down_release")
        sock.sendto(b"up_down_release", (ESP32_IP, ESP32_PORT))

class MySecondController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        
    def on_L3_up(self, value):
        # print("on_L3_up: {}".format(value))
        pass

    def on_L3_down(self, value):
        # print("on_L3_down: {}".format(value))
        pass

    def on_L3_left(self, value):
        # print("on_L3_left: {}".format(value))
        pass

    def on_L3_right(self, value):
        # print("on_L3_right: {}".format(value))
        pass

    def on_L3_y_at_rest(self):
        pass

    def on_L3_x_at_rest(self):
        pass

    def on_R3_up(self, value):
        # print("on_R3_up: {}".format(value))
        pass

    def on_R3_down(self, value):
        # print("on_R3_down: {}".format(value))
        pass

    def on_R3_left(self, value):
        # print("on_R3_left: {}".format(value))
        pass

    def on_R3_right(self, value):
        # print("on_R3_right: {}".format(value))
        pass

    def on_R3_y_at_rest(self):
        """R3 joystick is at rest after the joystick was moved and let go off"""
        # print("on_R3_y_at_rest")
        pass

    def on_R3_x_at_rest(self):
        """R3 joystick is at rest after the joystick was moved and let go off"""
        # print("on_R3_x_at_rest")
        pass

    def on_circle_press(self):
        sock2.sendto(b'1', (ESP32_IP_2, ESP32_PORT))

    def on_circle_release(self):
        sock2.sendto(b'2', (ESP32_IP_2, ESP32_PORT))
    

    def on_R2_press(self, value):
        # super().on_R2_press(self, value)
        sock2.sendto(str(value).encode(), (ESP32_IP_2, ESP32_PORT))

    def on_left_arrow_press(self):
        # super(self)
        message = "left"
        sock2.sendto(message.encode(), (ESP32_IP_2, ESP32_PORT))

    def on_right_arrow_press(self):
        # super(self)
        message = "right"
        sock2.sendto(message.encode(), (ESP32_IP_2, ESP32_PORT))

    def on_left_right_arrow_release(self):
        # super(self)
        sock2.sendto("right_release".encode(), (ESP32_IP_2, ESP32_PORT))

    def on_down_arrow_press(self):
        # super(self)
        sock2.sendto(b"down", (ESP32_IP_2, ESP32_PORT))

    def on_up_arrow_press(self):
        # super(self)
        sock2.sendto("up".encode(), (ESP32_IP_2, ESP32_PORT))
    
    def on_up_down_arrow_release(self):
        print("up_down_release")
        sock2.sendto(b"up_down_release", (ESP32_IP_2, ESP32_PORT))

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller2 = MySecondController(interface="/dev/input/js1", connecting_using_ds4drv=False)
# controller.listen()
# controller2.listen()

# Run both listen loops in parallel threads
t1 = threading.Thread(target=controller.listen, daemon=True)
t2 = threading.Thread(target=controller2.listen, daemon=True)

t1.start()
t2.start()

# Keep main thread alive
t1.join()
t2.join()