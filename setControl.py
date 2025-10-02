from pyPS4Controller.controller import Controller
import socket

class ConfigureController(Controller):
    esp32_ip = ""
    esp32_port = 0
    sock = None

    def __init__(self, esp32_ip, esp32_port, **kwargs):
        Controller.__init__(self, **kwargs)
        self.esp32_ip = esp32_ip
        self.esp32_port = esp32_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
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
        self.sock.sendto(b'1', (self.esp32_ip, self.esp32_port))

    def on_circle_release(self):
        self.sock.sendto(b'2', (self.esp32_ip, self.esp32_port))
    
    def on_R2_press(self, value):
        # super().on_R2_press(self, value)
        self.sock.sendto(str(value).encode(), (self.esp32_ip, self.esp32_port))

    def on_left_arrow_press(self):
        # super(self)
        message = "left"
        self.sock.sendto(message.encode(), (self.esp32_ip, self.esp32_port))

    def on_right_arrow_press(self):
        # super(self)
        message = "right"
        self.sock.sendto(message.encode(), (self.esp32_ip, self.esp32_port))

    def on_left_right_arrow_release(self):
        # super(self)
        self.sock.sendto("right_release".encode(), (self.esp32_ip, self.esp32_port))

    def on_down_arrow_press(self):
        # super(self)
        self.sock.sendto(b"down", (self.esp32_ip, self.esp32_port))

    def on_up_arrow_press(self):
        # super(self)
        self.sock.sendto("up".encode(), (self.esp32_ip, self.esp32_port))
    
    def on_up_down_arrow_release(self):
        print("up_down_release")
        self.sock.sendto(b"up_down_release", (self.esp32_ip, self.esp32_port))