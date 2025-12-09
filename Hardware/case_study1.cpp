#include <WiFi.h>
#include <HTTPClient.h>

// ---------------------- PIN DEFINITIONS ----------------------
#define TRIG 5
#define ECHO 18
#define LED_PIN 25
#define BUZZER 21
#define LDR_PIN 34
#define POT_PIN 35
#define SOS_BUTTON 23

// ---------------------- WIFI DETAILS FOR WOKWI ----------------------
const char* ssid     = "Wokwi-GUEST";
const char* password = "";  // No password

// ---------------------- WOKWI BUILT-IN TEST SERVER ----------------------
// 100% reliable, never busy, supports GET requests
String webhookURL = "http://wokwi-http-request.wokwi.com/?msg=";

// ---------------------- SETUP ----------------------
void setup() {
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER, OUTPUT);
  pinMode(SOS_BUTTON, INPUT_PULLUP);

  Serial.begin(115200);

  // Connect to WiFi
  Serial.print("Connecting to WiFi...");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi connected!");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
}

// ---------------------- DISTANCE FUNCTION ----------------------
long getDistance() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  long duration = pulseIn(ECHO, HIGH, 30000);
  return duration * 0.034 / 2;
}

// ---------------------- SEND MESSAGE TO WOKWI SERVER ----------------------
void sendTestMessage(String msg) {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi disconnected. Cannot send message.");
    return;
  }

  HTTPClient http;

  String finalURL = webhookURL + msg;
  Serial.println("Sending GET request to:");
  Serial.println(finalURL);

  http.begin(finalURL);
  int httpCode = http.GET();

  Serial.print("HTTP Response Code: ");
  Serial.println(httpCode);

  if (httpCode > 0) {
    String payload = http.getString();
    Serial.println("Server Response:");
    Serial.println(payload);
  }

  http.end();
}

// ---------------------- MAIN LOOP ----------------------
void loop() {
  long distance = getDistance();
  int ldrValue = analogRead(LDR_PIN);
  int potValue = analogRead(POT_PIN);

  int threshold = map(potValue, 0, 4095, 20, 100);

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.print(" cm | Threshold: ");
  Serial.print(threshold);
  Serial.print(" | LDR: ");
  Serial.println(ldrValue);

  // LED activates in low light
  if (ldrValue < 1500)
    digitalWrite(LED_PIN, LOW);
  else
    digitalWrite(LED_PIN, HIGH);

  // SOS button → send message to test server
  if (digitalRead(SOS_BUTTON) == LOW) {
    delay(50);

    if (digitalRead(SOS_BUTTON) == LOW) {

      String message = "Emergency alert from Rahul!! Location: 10.9020,76.9036";
      sendTestMessage(message);

      sosAlert();

      while (digitalRead(SOS_BUTTON) == LOW) delay(50);
      delay(200);
    }
  }

  // Distance → buzzer logic
  if (distance > threshold || distance <= 0) {
    noTone(BUZZER);
  }
  else if (distance > 50) {
    alertPattern(200, 1000);
  }
  else if (distance > 30) {
    alertPattern(120, 1500);
  }
  else if (distance > 15) {
    alertPattern(70, 2000);
  }
  else {
    tone(BUZZER, 2500);
  }

  delay(50);
}

// ---------------------- ALERT PATTERN ----------------------
void alertPattern(int speed, int toneFreq) {
  tone(BUZZER, toneFreq);
  delay(speed);
  noTone(BUZZER);
  delay(speed);
}

// ---------------------- SOS ALERT ----------------------
void sosAlert() {
  for (int i = 0; i < 5; i++) {
    digitalWrite(LED_PIN, HIGH);
    tone(BUZZER, 3000);
    delay(200);
    digitalWrite(LED_PIN, LOW);
    noTone(BUZZER);
    delay(200);
  }
}