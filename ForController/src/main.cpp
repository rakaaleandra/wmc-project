#include <Arduino.h>
#include <WiFi.h>
#include <WiFiUdp.h>
#include <iostream>
#include <algorithm>
using namespace std;

const char* ssid = "kost putra jeruk bawah";
const char* password = "jerukmanis02";

WiFiUDP Udp;
unsigned int localUdpPort = 4210;

char incomingPacket[255];

void setup() {
  Serial.begin(9600);

  Serial.println("UDP Receiver");

  WiFi.begin(ssid, password);  // ESP32 jadi Access Point
  Serial.println("ESP32 AP Started");
  Serial.print("IP Address: ");
  
  Udp.begin(localUdpPort);

  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  Serial.println(WiFi.localIP());
  int packetSize = Udp.parsePacket();
  if (packetSize) {
    int len = Udp.read(incomingPacket, 255);
    if (len > 0) incomingPacket[len] = 0;
    Serial.printf("Received: %s\n", incomingPacket);
    if (atoi(incomingPacket) == 1){
      digitalWrite(LED_BUILTIN, HIGH);
    } else if (atoi(incomingPacket) == 2){
      digitalWrite(LED_BUILTIN, LOW);
    }
  }
}