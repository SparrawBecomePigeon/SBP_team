#include <StackArray.h>
#include <SoftwareSerial.h>
#include <AccelStepper.h>
#include <TFMPlus.h>  // Include TFMini Plus Library v1.5.0
TFMPlus tfmP;         // Create a TFMini Plus object
#include <ArduinoJson.h>
#include "WiFiEsp.h"

#define sm1_pin1 2
#define sm1_pin2 3
#define sm1_pin3 4
#define sm1_pin4 5

#define sm2_pin1 6
#define sm2_pin2 7
#define sm2_pin3 8
#define sm2_pin4 9

#define aroundInterval 13000  // 한바퀴 도는 시간
#define LIDARDATASIZE 72      // 한바퀴 동안 측정할 데이터 개수 현재 360 / 72 = 5도 마다 측정

char ssid[] = "AndroidHotspot2409";            // your network SSID (name)
char pass[] = "12345678";        // your network password
int status = WL_IDLE_STATUS;     // the Wifi radio's status
char server[] = "54.180.142.70";  // server IP address
int server_port = 3000;           // server port number

// Initialize the Ethernet client object
WiFiEspClient client;

AccelStepper stepper1(4, sm1_pin1, sm1_pin3, sm1_pin2, sm1_pin4);
AccelStepper stepper2(4, sm2_pin1, sm2_pin3, sm2_pin2, sm2_pin4);

int16_t tfDist = 0;    // Distance to object in centimeters
unsigned long currentMillis;
unsigned long previousMillis;

void setup() {
  Serial.begin(9600);
  Serial1.begin(9600); // initialize serial for ESP module
  Serial2.begin(115200);  // Initialize TFMPLus device serial port.
  delay(20);               // Give port time to initalize
  tfmP.begin(&Serial2);   // Initialize device library object and...
  // pass device serial port to the object.

  // initialize ESP module
  WiFi.init(&Serial1);

  // check for the presence of the shield
  if (WiFi.status() == WL_NO_SHIELD) {
    Serial.println("WiFi shield not present");
    // don't continue
    while (true);
  }
  
  // attempt to connect to WiFi network
  while ( status != WL_CONNECTED) {
    Serial.print("Attempting to connect to WPA SSID: ");
    Serial.println(ssid);
    // Connect to WPA/WPA2 network
    status = WiFi.begin(ssid, pass);
  }
  
  Serial.println("You're connected to the network");
  printWifiStatus();

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
  
  delay(1000);
}

int cur_x = 0; int cur_y = 0;
int cur_rot = 90;

StackArray<int> st_x;
StackArray<int> st_y;
StackArray<unsigned long> st_rot;

void loop() {
  String jsonstr = ""; // json string 선언
  LidarDetectAround(jsonstr); // 반시계방향으로 360도 돌면서 거리 측정 및 좌표로 환산
  SendDataWeb(jsonstr); // 측정된 좌표 웹에 전송
  delay(3000);

  if(st_x.isEmpty()){
    Serial.println("FINISH!!!");
    delay(10000);
  }

  // 다음 측정 위치로 이동을 위한 좌표 및 방위각 설정
  int nt_x = st_x.pop();
  int nt_y = st_y.pop();
  unsigned long nt_rot = st_rot.pop();
  int nt_dist;

  Serial.print("Rotation : ");
  Serial.println(360 * nt_rot / aroundInterval - 90);

  // 이동 방위각 회전
  previousMillis = millis();
  while(true){
    currentMillis = millis();
    if(currentMillis - previousMillis >= nt_rot) break;
    LeftRound();
  }
  Stop();
  //(360 * (currentMillis - previousMillis) / aroundInterval)
  cur_rot += 360 * nt_rot / aroundInterval;
  cur_rot = cur_rot % 360;
  nt_dist = getDataLidar();
  Serial.print("nt_dist = ");
  Serial.println(nt_dist);
  delay(1000);

  // 이동
  unsigned long lidarInterval = aroundInterval / LIDARDATASIZE;
  previousMillis = millis();
  while(true){
    currentMillis = millis();
    if(currentMillis - previousMillis >= lidarInterval){
      int currentLidar = getDataLidar();
      if(currentLidar < 50 && currentLidar != 0) break;
      lidarInterval += lidarInterval;
    }
    Go();
  }
  Stop();
  cur_x = int((nt_dist - getDataLidar()) * (cos(radians(cur_rot))));
  cur_y = int((nt_dist - getDataLidar()) * (sin(radians(cur_rot))));

  // 이동 후 방위각 90도로 다시 돌아옴
  previousMillis = millis();
  while(true){
    currentMillis = millis();
    if(currentMillis - previousMillis >= nt_rot) break;
    RightRound();
  }
  
  Serial.print("Current Point [x, y] = ");
  Serial.print(cur_x);
  Serial.print(" , ");
  Serial.println(cur_y);
  delay(2000);
}

void SendDataWeb(const String& jsonstr){
  Serial.println("Starting connection to server...");
  previousMillis = millis();
  while(true){
    currentMillis = millis();
    // if you get a connection, report back via serial
    if (client.connect(server, server_port)) {
      Serial.println("Connected to server");
      
      // Make a HTTP request
      client.print(F("POST /send HTTP/1.1\r\n"));
      client.print(F("Connection: keep-alive\r\n"));
      client.print(F("Content-Type: application/json; charset=utf-8\r\n"));
      client.print(F("Host: 54.180.142.70:3000\r\n"));
      client.print(F("Accept: */*\r\n"));
      client.print(F("Content-Length: "));
      client.println(jsonstr.length());
      client.println();
      client.println(jsonstr);
  
      Serial.println("Post success!!!");
      break;
    }
    else {
      // if you couldn't make a connection
      Serial.println("Connection failed and retry");
      delay(100);
    }
    if(currentMillis - previousMillis >= 2000){
      Serial.println("Conection failed and end");
      break;
    }
  }
  client.flush();
  client.stop(); // 클라이언트 접속 종료
  // close the connection:
  Serial.println("Client disconnected");
}

int getDataLidar(){
  tfmP.getData( tfDist); // Get data from the device.
  Serial.print( "Dist : ");   // display distance,
  Serial.print(tfDist);
  Serial.println( "cm");
  return tfDist;
}

void LidarDetectAround(String& jsonstr){
  unsigned long lidarInterval = aroundInterval / LIDARDATASIZE;
  unsigned long lidarRunMillis = millis();
  
  DynamicJsonDocument doc(2048);
  JsonObject root = doc.to<JsonObject>();
  JsonArray Lidar_Location = root.createNestedArray("Lidar_Location");
  Lidar_Location[0] = cur_x;
  Lidar_Location[1] = cur_y;
  JsonArray LidarData_x = root.createNestedArray("LidarData_x");
  JsonArray LidarData_y = root.createNestedArray("LidarData_y");
  int dataCount = 0; int previousDist = -1;
  previousMillis = millis();
  while(true){
    currentMillis = millis();
    if(currentMillis - previousMillis >= aroundInterval) break;
    if((currentMillis - lidarRunMillis)>= lidarInterval){
      lidarRunMillis += lidarInterval;
      if(dataCount > LIDARDATASIZE - 1){
        Serial.println("ERROR: Lidar data Overflow!!!");
        break;
      }
      int currentDist = getDataLidar();
      if(previousDist < 0) { previousDist = currentDist; }
      if(currentDist == 0 || currentDist - previousDist > 2 * previousDist ){
        st_x.push(cur_x);
        st_y.push(cur_y);
        st_rot.push(currentMillis - previousMillis);
      }
      previousDist = currentDist;
      LidarData_x[dataCount] = int(currentDist * (cos(radians(cur_rot + (360 * (currentMillis - previousMillis) / aroundInterval)))));
      LidarData_y[dataCount] = int(currentDist * (sin(radians(cur_rot + (360 * (currentMillis - previousMillis) / aroundInterval)))));
      dataCount++;
    }
    LeftRound();
  }
  Serial.println("==============");
  serializeJsonPretty(doc, jsonstr);
  Serial.println(jsonstr);
  Serial.println("==============");
  return jsonstr;
}

void printWifiStatus()
{
  // print the SSID of the network you're attached to
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());
  
  // print your WiFi shield's IP address
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // print the received signal strength
  long rssi = WiFi.RSSI();
  Serial.print("Signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
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
