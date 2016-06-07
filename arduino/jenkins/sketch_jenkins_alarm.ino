
/* JenkinsStatus will turn the LED at pin 13 on/off depending
 * on the value serially read.
 */
#include <Servo.h>
 
const int BUILD_SUCCESS = 'b';
const int BUILD_FAILURE = 'r';
const int BUILD_INSTABLE = 'y';

int inByte;
int currentPinValue = 0;
int gyroled = 6;
Servo servoLeft; 

void setup() {
  Serial.begin(9600);

  servoLeft.attach(gyroled);
  servoLeft.writeMicroseconds(0);
}

void loop() {
  if (Serial.available() > 0) {
      inByte = Serial.read();
      if (inByte == BUILD_INSTABLE) {
       servoLeft.writeMicroseconds(1000);
      } else{
        servoLeft.writeMicroseconds(0);
      }
  } else {
    currentPinValue = digitalRead(13);
    if (currentPinValue == HIGH) {
      delay(1000);
      digitalWrite(13, LOW);
      delay(1000);
      digitalWrite(13, HIGH);      
    }
  }
}


