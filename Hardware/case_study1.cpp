// ------------------------------------------------------
// SMART MULTI-ASSIST SYSTEM (5-MODULE VERSION)
// ------------------------------------------------------

// ---------- MODULE SELECT (Choose which device) ----------
#define DEVICE_MODE 1  
// Change 1 → 2 → 3 → 4 → 5 for different person/device


// ------------------------------------------------------
// COMMON PINS (USED BY ALL MODULES)
// ------------------------------------------------------
#define LED_PIN 6
#define VIBRATION_MOTOR 5
#define LDR_PIN A0
#define POT_PIN A1

// BUZZER (used for advanced alerts)
#define BUZZER 3

// SOS Emergency Button
#define SOS_BUTTON 7

// ------------------------------------------------------
// MODULE 1 → BASIC ULTRASONIC
// ------------------------------------------------------
#if DEVICE_MODE == 1
#define TRIG 9
#define ECHO 10
#endif

// ------------------------------------------------------
// MODULE 2 → DIRECTIONAL ULTRASONIC (LEFT–RIGHT)
// ------------------------------------------------------
#if DEVICE_MODE == 2
#define TRIG_FRONT 9
#define ECHO_FRONT 10

#define TRIG_LEFT 11
#define ECHO_LEFT 12
#endif

// ------------------------------------------------------
// MODULE 3 → WATER DETECTION SENSOR
// ------------------------------------------------------
#if DEVICE_MODE == 3
#define WATER_SENSOR A2   // Analog water sensing
#endif

// ------------------------------------------------------
// MODULE 4 → TEMPERATURE WARNING SYSTEM
// ------------------------------------------------------
#if DEVICE_MODE == 4
#define TEMP_SENSOR A3    // LM35 or thermistor
#endif

// ------------------------------------------------------
// MODULE 5 → SOS EMERGENCY ALERT SYSTEM
// ------------------------------------------------------
#if DEVICE_MODE == 5
// Uses common LED, buzzer, vibration
#endif


// ------------------------------------------------------
// BASIC FUNCTIONS
// ------------------------------------------------------
long getDistanceCustom(int trigPin, int echoPin) {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH);
  long distance = duration * 0.034 / 2;
  return distance;
}


// ------------------------------------------------------
// SETUP
// ------------------------------------------------------
void setup() {
  Serial.begin(9600);

  pinMode(LED_PIN, OUTPUT);
  pinMode(VIBRATION_MOTOR, OUTPUT);
  pinMode(BUZZER, OUTPUT);
  pinMode(SOS_BUTTON, INPUT_PULLUP);

#if DEVICE_MODE == 1
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
#endif

#if DEVICE_MODE == 2
  pinMode(TRIG_FRONT, OUTPUT);
  pinMode(ECHO_FRONT, INPUT);
  pinMode(TRIG_LEFT, OUTPUT);
  pinMode(ECHO_LEFT, INPUT);
#endif

#if DEVICE_MODE == 3
  pinMode(WATER_SENSOR, INPUT);
#endif

#if DEVICE_MODE == 4
  pinMode(TEMP_SENSOR, INPUT);
#endif
}


// ------------------------------------------------------
// MAIN LOOP
// ------------------------------------------------------
void loop() {

  int ldrValue = analogRead(LDR_PIN);
  int potValue = analogRead(POT_PIN);
  int threshold = map(potValue, 0, 1023, 20, 120);

  // ---------- NIGHT LED ----------
  digitalWrite(LED_PIN, (ldrValue < 400));

  // ---------- SOS BUTTON ----------
  if (digitalRead(SOS_BUTTON) == LOW) {
    sosAlert();
  }

  // ---------------- MODULE 1 ----------------
#if DEVICE_MODE == 1

  long dist = getDistanceCustom(TRIG, ECHO);
  Serial.print("Distance: "); Serial.println(dist);
  vibrationFeedback(dist, threshold);

#endif



// ---------------- MODULE 2 ----------------
#if DEVICE_MODE == 2

  long dFront = getDistanceCustom(TRIG_FRONT, ECHO_FRONT);
  long dLeft = getDistanceCustom(TRIG_LEFT, ECHO_LEFT);

  Serial.print("Front: "); Serial.print(dFront);
  Serial.print(" | Left: "); Serial.println(dLeft);

  if (dFront < threshold) {
    tone(BUZZER, 1500, 80);
  }
  if (dLeft < threshold) {
    tone(BUZZER, 900, 80);
  }

#endif



// ---------------- MODULE 3 ----------------
#if DEVICE_MODE == 3

  int waterValue = analogRead(WATER_SENSOR);
  Serial.print("Water Sensor: "); Serial.println(waterValue);

  if (waterValue > 600) {  // Wet floor
    digitalWrite(VIBRATION_MOTOR, HIGH);
    tone(BUZZER, 700);
    delay(200);
    noTone(BUZZER);
    digitalWrite(VIBRATION_MOTOR, LOW);
  }

#endif



// ---------------- MODULE 4 ----------------
#if DEVICE_MODE == 4

  int tempValue = analogRead(TEMP_SENSOR);
  float temperature = tempValue * 0.488;  // LM35 = 10mV/°C

  Serial.print("Temperature: ");
  Serial.println(temperature);

  if (temperature > 45) {
    tone(BUZZER, 1000);
    digitalWrite(VIBRATION_MOTOR, HIGH);
  } else {
    noTone(BUZZER);
    digitalWrite(VIBRATION_MOTOR, LOW);
  }

#endif



// ---------------- MODULE 5 ----------------
#if DEVICE_MODE == 5

  if (digitalRead(SOS_BUTTON) == LOW) {
    sosAlert();
  }

#endif

  delay(60);
}



// ------------------------------------------------------
// FUNCTIONS
// ------------------------------------------------------
void vibrationFeedback(long distance, int threshold) {

  if (distance > threshold || distance <= 0) {
    digitalWrite(VIBRATION_MOTOR, LOW);
    return;
  }

  if (distance > 50) { pulse(200); }
  else if (distance > 30) { pulse(120); }
  else if (distance > 15) { pulse(70); }
  else { digitalWrite(VIBRATION_MOTOR, HIGH); }
}

void pulse(int ms) {
  digitalWrite(VIBRATION_MOTOR, HIGH);
  delay(ms);
  digitalWrite(VIBRATION_MOTOR, LOW);
  delay(ms);
}

void sosAlert() {
  Serial.println("SOS Activated!");

  for (int i = 0; i < 5; i++) {
    digitalWrite(LED_PIN, HIGH);
    tone(BUZZER, 2000);
    digitalWrite(VIBRATION_MOTOR, HIGH);
    delay(200);

    digitalWrite(LED_PIN, LOW);
    noTone(BUZZER);
    digitalWrite(VIBRATION_MOTOR, LOW);
    delay(200);
  }
}
