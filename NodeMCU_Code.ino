#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>

// Set these to run example.
#define FIREBASE_HOST "fir-2d0b5-default-rtdb.firebaseio.com"
#define FIREBASE_AUTH "lQBZhHYuzftTNO5tDLKDW0UYfKnKc4p4EtsALjtt"
#define WIFI_SSID "iPhone"
#define WIFI_PASSWORD "12345678"

#include <SoftwareSerial.h>
SoftwareSerial mySerial(D1, D2);

void setup() {
 Serial.begin(115200);
 mySerial.begin(9600);
 WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("connecting");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.print("connected: ");
  Serial.println(WiFi.localIP());
  
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
}

void loop() {
  String slot1 = mySerial.readStringUntil('\n');
  String slot2 = mySerial.readStringUntil('\n');
  Firebase.setString("SLOT1", slot1);
  Firebase.setString("SLOT2", slot2);
  Serial.println(slot1);
  Serial.println(slot2);
}
