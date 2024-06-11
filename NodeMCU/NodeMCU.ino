#include <SoftwareSerial.h>
#include <ESP8266WiFi.h>
#include <Wire.h>
#include "FirebaseESP8266.h"

char FIREBASE_AUTH[] = "*******************"; // Your Firebase Web API Key
char FIREBASE_HOST[] = "**************"; // Your Firebase Host URL
char WIFI_SSID[] = "*********";     // Your WIFI SSID
char WIFI_PASSWORD[] = "***********"; // Your WIFI Password

SoftwareSerial mySerial(D2, D3);
String sensorValueString;
FirebaseData firebaseData;

void setup() {
  Serial.begin(115200);
  mySerial.begin(9600);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");

}

void loop() {
  // Read data from Arduino and publish
  if (mySerial.available()) {
    String data = mySerial.readStringUntil('\n');
    sensorValueString = data.substring(data.indexOf(":") + 2);
    Serial.print("Received sensor value: ");
    Serial.println(sensorValueString);

    // Convert sensorValueString to integer
    int sensorValue = sensorValueString.toInt();

    // Send sensorValue as a number to Firebase
    Firebase.setInt(firebaseData, "/MQ4", sensorValue);
  }
}
