#include<Servo.h>

Servo servo1;
int servopin = 4;
void setup() {

  servo1.attach(servopin);
  // put your setup code here, to run once:

}

void loop() {
  servo1.write(75);
  delay(300);
  servo1.write(0);
  delay(300);
  // put your main code here, to run repeatedly:

}
