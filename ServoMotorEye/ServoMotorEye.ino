#include<Servo.h>

Servo servo1, servo2;
int servopin1 = 4, servopin2 = 5;
void setup() {

  servo1.attach(servopin1);
  servo2.attach(servopin2);
  // put your setup code here, to run once:

}

void loop() {
  servo1.write(80);
  delay(500);
  servo1.write(30);
  delay(500);
  servo2.write(0);
  delay(500);
  servo1.write(80);
  delay(500);
  servo1.write(30);
  delay(500);
  servo2.write(60);
  delay(500);
  // put your main code here, to run repeatedly:

}
