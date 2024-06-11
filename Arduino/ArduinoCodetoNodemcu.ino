#include <SoftwareSerial.h>
#include <LiquidCrystal.h>

LiquidCrystal lcd(8, 9, 10, 11, 12, 13);
SoftwareSerial espSerial(2, 3); // RX, TX pins for communication with NodeMCU
int sensorValue;

void setup() {
  lcd.setCursor(0, 0);
  lcd.print("Decay Inspector");
  delay(2000);
  lcd.clear();
  Serial.begin(9600);
  espSerial.begin(9600);
  delay(1000);
}

void loop() {
  sensorValue = analogRead(A0);
  Serial.print("Sensor value: ");
  Serial.println(sensorValue);
  espSerial.print("Sensor value: "); // Send the string "Sensor value: " followed by the value
  espSerial.println(sensorValue);

  if (sensorValue > 75) {
    lcd.clear();
    lcd.setCursor(0, 1);   //<<<<<<<<
    lcd.print("   ");          //<<<<<<<<
    lcd.setCursor(0, 1);
    lcd.print(sensorValue);
    //lcd.setCursor(0, 1);
    lcd.print(" - Not Safe");
  } else {
    lcd.clear();
    lcd.setCursor(0, 0);   //<<<<<<<<
    lcd.print("   ");          //<<<<<<<<
    lcd.setCursor(0, 0);
    lcd.print(sensorValue);
    //lcd.setCursor(0, 1);
    lcd.print(" - Safe to Eat");
  }

  delay(1000);
}
