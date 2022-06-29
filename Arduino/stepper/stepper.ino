#include <AccelStepper.h>
#include <SoftwareSerial.h>

#define sm1_pin1 2
#define sm1_pin2 3
#define sm1_pin3 4
#define sm1_pin4 5

#define sm2_pin1 6
#define sm2_pin2 7
#define sm2_pin3 8
#define sm2_pin4 9

AccelStepper stepper1(4, sm1_pin1, sm1_pin3, sm1_pin2, sm1_pin4);
AccelStepper stepper2(4, sm2_pin1, sm2_pin3, sm2_pin2, sm2_pin4);


void setup() {
  Serial.begin(9600);
}

void loop() {
  Go();
  
}

void Stop(){
  stepper1.setSpeed(0);
  stepper2.setSpeed(0);
}

void Go(){
  stepper1.setSpeed(-1000);
  stepper2.setSpeed(1000);
  stepper1.runSpeed();
  stepper2.runSpeed();
}

void RightRound(){
  stepper1.setSpeed(500);
  stepper2.setSpeed(500);
  stepper1.runSpeed();
  stepper2.runSpeed();
}

void LeftRound(){
  stepper1.setSpeed(-500);
  stepper2.setSpeed(-500);
  stepper1.runSpeed();
  stepper2.runSpeed();
}
