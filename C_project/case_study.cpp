// ============================================================
// SMART CITY MONITORING SYSTEM - SINGLE PICO COMBINED VERSION
// Raspberry Pi Pico - Arduino IDE - Wokwi Compatible
// Modules:
// 1. Smart Street Light
// 2. Smart Waste Monitoring
// 3. Smart Parking
// 4. Smart Traffic Management
// 5. Fire/Smoke/Environment Monitoring
// ============================================================

#include <DHT.h>

#define DHTPIN 16
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

// ---------------- PIN DEFINITIONS ----------------

// Waste Ultrasonic
const int trigPin = 2;
const int echoPin = 3;

// LEDs
const int greenLED = 10;
const int yellowLED = 11;
const int redLED = 12;
const int whiteLED = 13;

// Buzzer
const int buzzerPin = 14;

// Traffic button
const int buttonPin = 15;

// Street light sensor
const int ldrPin = 26;     // ADC

// Parking sensor (potentiometer used as simulated input)
const int parkingPin = 27; // ADC

// Smoke / fire sensor (potentiometer used as simulated input)
const int smokePin = 28;   // ADC

// ---------------- VARIABLES ----------------

unsigned long lastPrint = 0;

// ---------------- FUNCTIONS ----------------

float getDistanceCM() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH, 30000); // timeout 30ms

  if (duration == 0) {
    return 999.0;
  }

  float distance = duration * 0.0343 / 2.0;
  return distance;
}

void allLedsOff() {
  digitalWrite(greenLED, LOW);
  digitalWrite(yellowLED, LOW);
  digitalWrite(redLED, LOW);
  digitalWrite(whiteLED, LOW);
}

void beepShort() {
  digitalWrite(buzzerPin, HIGH);
  delay(100);
  digitalWrite(buzzerPin, LOW);
}

void setup() {
  Serial.begin(115200);
  delay(1500);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  pinMode(greenLED, OUTPUT);
  pinMode(yellowLED, OUTPUT);
  pinMode(redLED, OUTPUT);
  pinMode(whiteLED, OUTPUT);

  pinMode(buzzerPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);

  dht.begin();

  Serial.println("==================================================");
  Serial.println(" SMART CITY MONITORING SYSTEM - SINGLE PICO NODE ");
  Serial.println("==================================================");
}

void loop() {
  // ----------- READ SENSORS -----------
  int ldrValue = analogRead(ldrPin);
  float wasteDistance = getDistanceCM();
  int parkingValue = analogRead(parkingPin);
  int smokeValue = analogRead(smokePin);

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  bool pedestrianRequest = (digitalRead(buttonPin) == LOW);

  // ----------- STATUS VARIABLES -----------
  String streetStatus;
  String wasteStatus;
  String parkingStatus;
  String trafficStatus;
  String envStatus;

  // ----------- MODULE 1: STREET LIGHT -----------
  bool streetOn = false;
  if (ldrValue < 1500) {
    streetOn = true;
    streetStatus = "LIGHTS ON";
  } else {
    streetOn = false;
    streetStatus = "LIGHTS OFF";
  }

  // ----------- MODULE 2: WASTE MONITORING -----------
  if (wasteDistance > 20) {
    wasteStatus = "BIN EMPTY";
  } else if (wasteDistance > 10) {
    wasteStatus = "BIN HALF";
  } else {
    wasteStatus = "BIN FULL";
  }

  // ----------- MODULE 3: PARKING -----------
  if (parkingValue < 1000) {
    parkingStatus = "SLOTS AVAILABLE";
  } else if (parkingValue < 2500) {
    parkingStatus = "LIMITED PARKING";
  } else {
    parkingStatus = "PARKING FULL";
  }

  // ----------- MODULE 4: TRAFFIC -----------
  if (pedestrianRequest) {
    trafficStatus = "PEDESTRIAN CROSSING ACTIVE";
  } else if (parkingValue > 2500) {
    trafficStatus = "HEAVY TRAFFIC";
  } else {
    trafficStatus = "NORMAL TRAFFIC";
  }

  // ----------- MODULE 5: ENVIRONMENT -----------
  bool danger = false;
  bool warning = false;

  if (!isnan(temperature)) {
    if (temperature > 45 || smokeValue > 3000) {
      danger = true;
    } else if (temperature > 35 || smokeValue > 1800) {
      warning = true;
    }
  } else {
    if (smokeValue > 3000) {
      danger = true;
    } else if (smokeValue > 1800) {
      warning = true;
    }
  }

  if (danger) {
    envStatus = "DANGER";
  } else if (warning) {
    envStatus = "WARNING";
  } else {
    envStatus = "SAFE";
  }

  // ----------- OUTPUT LOGIC -----------
  allLedsOff();
  digitalWrite(buzzerPin, LOW);

  // Environment has highest priority
  if (danger) {
    digitalWrite(redLED, HIGH);
    digitalWrite(buzzerPin, HIGH);
  } 
  else if (warning) {
    digitalWrite(yellowLED, HIGH);
  } 
  else if (String(wasteStatus) == "BIN FULL") {
    digitalWrite(redLED, HIGH);
    beepShort();
  } 
  else if (pedestrianRequest) {
    digitalWrite(whiteLED, HIGH);
    beepShort();
  } 
  else if (streetOn) {
    digitalWrite(whiteLED, HIGH);
    digitalWrite(greenLED, HIGH);
  } 
  else if (parkingStatus == "SLOTS AVAILABLE") {
    digitalWrite(greenLED, HIGH);
  } 
  else if (parkingStatus == "LIMITED PARKING") {
    digitalWrite(yellowLED, HIGH);
  } 
  else {
    digitalWrite(redLED, HIGH);
  }

  // ----------- SERIAL MONITOR DASHBOARD -----------
  if (millis() - lastPrint > 2000) {
    lastPrint = millis();

    Serial.println();
    Serial.println("============== SMART CITY DASHBOARD ==============");
    Serial.print("LDR Value            : ");
    Serial.println(ldrValue);

    Serial.print("Waste Distance       : ");
    Serial.print(wasteDistance);
    Serial.println(" cm");

    Serial.print("Parking Sensor       : ");
    Serial.println(parkingValue);

    Serial.print("Smoke Value          : ");
    Serial.println(smokeValue);

    Serial.print("Temperature          : ");
    if (isnan(temperature)) Serial.println("Sensor Error");
    else {
      Serial.print(temperature);
      Serial.println(" C");
    }

    Serial.print("Humidity             : ");
    if (isnan(humidity)) Serial.println("Sensor Error");
    else {
      Serial.print(humidity);
      Serial.println(" %");
    }

    Serial.print("Street Light Status  : ");
    Serial.println(streetStatus);

    Serial.print("Waste Status         : ");
    Serial.println(wasteStatus);

    Serial.print("Parking Status       : ");
    Serial.println(parkingStatus);

    Serial.print("Traffic Status       : ");
    Serial.println(trafficStatus);

    Serial.print("Environment Status   : ");
    Serial.println(envStatus);

    Serial.println("==================================================");
  }

  delay(200);
}