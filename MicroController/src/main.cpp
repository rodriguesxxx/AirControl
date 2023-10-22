#include <Arduino.h>

#include <SoftwareSerial.h>

SoftwareSerial bt(10, 11); //rx, tx

void setup(){
    Serial.begin(9600);
    bt.begin(9600);
}

void loop(){
    if(bt.available()){
        Serial.println(bt.readString());
    }
}