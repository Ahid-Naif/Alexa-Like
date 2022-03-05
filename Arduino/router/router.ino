// Include the Wire library for I2C
#include <Wire.h>
 
void setup() {
  // Join I2C bus as slave with address 8
  Wire.begin(0x8);
  
  // Call receiveEvent when data received                
  Wire.onReceive(receiveEvent);

  Serial.begin(9600);
}
 
// Function that executes whenever data is received from master
void receiveEvent(int howMany) {
  while (Wire.available()) { // loop through all but the last
    char c = Wire.read(); // receive from raspberry
    Serial.write(c); // send to computer
  }
}
void loop() {
  delay(100);
}
