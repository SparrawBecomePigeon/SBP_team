#include <AccelStepper.h>
#include <SoftwareSerial.h>
#include <TFMPlus.h>  // Include TFMini Plus Library v1.5.0
TFMPlus tfmP;         // Create a TFMini Plus object
#include <SoftwareSerial.h>

#define sm1_pin1 2
#define sm1_pin2 3
#define sm1_pin3 4
#define sm1_pin4 5

#define sm2_pin1 6
#define sm2_pin2 7
#define sm2_pin3 8
#define sm2_pin4 9

#define aroundInterval 12900

AccelStepper stepper1(4, sm1_pin1, sm1_pin3, sm1_pin2, sm1_pin4);
AccelStepper stepper2(4, sm2_pin1, sm2_pin3, sm2_pin2, sm2_pin4);

int16_t tfDist = 0;    // Distance to object in centimeters
int16_t tfFlux = 0;    // Strength or quality of return signal
int16_t tfTemp = 0;    // Internal temperature of Lidar sensor chip
char dist[11];
unsigned long currentMillis;
unsigned long previousMillis;

void setup() {
  Serial.begin(9600);
  Serial1.begin(115200);  // Initialize TFMPLus device serial port.
  delay(20);               // Give port time to initalize
  tfmP.begin(&Serial1);   // Initialize device library object and...
  // pass device serial port to the object.

  // Send some example commands to the TFMini-Plus
  // - - Perform a system reset - - - - - - - - - - -
  Serial.print( "Soft reset: ");
  if( tfmP.sendCommand( SOFT_RESET, 0))
  {
    Serial.print( "passed.\r\n");
  }
  else tfmP.printReply();

  delay(500);  // added to allow the System Rest enough time to complete

  // - - Display the firmware version - - - - - - - - -
  Serial.print( "Firmware version: ");
  if( tfmP.sendCommand( GET_FIRMWARE_VERSION, 0))
  {
    Serial.print(tfmP.version[ 0]); // print three single numbers
    Serial.print(tfmP.version[ 1]); // each separated by a dot
    Serial.print(tfmP.version[ 2]);
    Serial.println();
  }
  else tfmP.printReply();
  // - - Set the data frame-rate to 20Hz - - - - - - - -
  Serial.print( "Data-Frame rate: ");
  if( tfmP.sendCommand( SET_FRAME_RATE, FRAME_20))
  {
    Serial.print(FRAME_20);
    Serial.println();
  }
  else tfmP.printReply();
  
  delay(2000);

  currentMillis = millis();
  previousMillis = millis();
  int currentDist = 0, maxDist = 0;
  unsigned long maxDistMillis;
  while(true){
    currentMillis = millis();
    if(currentMillis - previousMillis > aroundInterval) break;
    RightRound();
    currentDist = getDataAround();
    if(currentDist > maxDist){
      maxDist = currentDist;
      maxDistMillis = currentMillis - previousMillis;
    }
  }
  Stop();
  previousMillis = millis();
  while(true){
    currentMillis = millis();
    if(currentMillis - previousMillis > maxDistMillis) break;
    RightRound();
  }
  Stop();
}

int getDataAround(){
  if( tfmP.getData( tfDist, tfFlux, tfTemp)) // Get data from the device.
  {
    Serial.print( "Dist : ");   // display distance,
    Serial.print(tfDist);
    Serial.println( "cm");
  }
  else                  // If the command fails...
  {
    tfmP.printFrame();  // display the error and HEX dataa
  }
  return tfDist;
}

void loop() {
  
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

void RightAround(){
  currentMillis = millis();
  previousMillis = millis();
  while(true){
    currentMillis = millis();
    if(currentMillis - previousMillis > aroundInterval) break;
    RightRound();
  }
  Stop();
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
