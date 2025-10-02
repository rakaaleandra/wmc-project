#include <Arduino.h>
#include <WiFi.h>
#include <WiFiUdp.h>
#include <iostream>
#include <algorithm>
#define ENA 2
#define IN1 4
#define IN2 5
#define IN3 18
#define IN4 19
#define ENB 21
using namespace std;

const char* ssid = "kost putra jeruk bawah";
const char* password = "jerukmanis02";

WiFiUDP Udp;
unsigned int localUdpPort = 4210;

char incomingPacket[255];

int Speed = 4095;

void setup() {
  Serial.begin(9600);

  Serial.println("UDP Receiver");

  WiFi.begin(ssid, password);  // ESP32 jadi Access Point
  Serial.println("ESP32 AP Started");
  Serial.print("IP Address: ");
  
  Udp.begin(localUdpPort);

  pinMode(LED_BUILTIN, OUTPUT);

  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENB, OUTPUT);
}

void carForward();
void carBackward();
void carLeft();
void carRight();
void carStop();

void loop() {
  Serial.println(WiFi.localIP());
  int packetSize = Udp.parsePacket();
  if (packetSize) {
    int len = Udp.read(incomingPacket, 255);
    if (len > 0) incomingPacket[len] = 0;
    Serial.printf("Received: %s\n", incomingPacket);
    switch(atoi(incomingPacket)){
      case 1:
        digitalWrite(LED_BUILTIN, HIGH);
        carForward();
        break;
      case 2:
        digitalWrite(LED_BUILTIN, LOW);
        carBackward();
        break;
      case 3:
        digitalWrite(LED_BUILTIN, HIGH);
        carLeft();
        break;
      case 4:
        digitalWrite(LED_BUILTIN, LOW);
        carRight();
        break;
      case 5:
        digitalWrite(LED_BUILTIN, HIGH);
        carStop();
        break;
      default:
        digitalWrite(LED_BUILTIN, LOW);
        carStop();
        break;
    }
    // if (atoi(incomingPacket) == 1){
    //   digitalWrite(LED_BUILTIN, HIGH);
    //   carForward();
    // } else if (atoi(incomingPacket) == 2){
    //   digitalWrite(LED_BUILTIN, LOW);
    //   carBackward();
    // } e
  }
}

void carForward() {
  analogWrite(ENA, Speed);
  analogWrite(ENB, Speed);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void carBackward() {
  analogWrite(ENA, Speed);
  analogWrite(ENB, Speed);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

void carLeft() {
  analogWrite(ENA, Speed);
  analogWrite(ENB, Speed);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void carRight() {
  analogWrite(ENA, Speed);
  analogWrite(ENB, Speed);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

void carStop() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}