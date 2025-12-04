#define TRIG 9
#define ECHO 10

#define VIBRATION_MOTOR 5
#define LED_PIN 6
#define BUZZER 4
#define LDR_PIN A0
#define POT_PIN A1
#define SOS_BUTTON 7

void setup() {
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  pinMode(VIBRATION_MOTOR, OUTPUT);
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER, OUTPUT);
  pinMode(SOS_BUTTON, INPUT_PULLUP);
  Serial.begin(9600);
}

long getDistance() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  long duration = pulseIn(ECHO, HIGH);
  return duration * 0.034 / 2;
}

void loop() {
  long distance = getDistance();
  int ldrValue = analogRead(LDR_PIN);
  int potValue = analogRead(POT_PIN);
  int threshold = map(potValue, 0, 1023, 20, 100);

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.print(" cm | Threshold: ");
  Serial.println(threshold);

  if (ldrValue < 400) digitalWrite(LED_PIN, HIGH);
  else digitalWrite(LED_PIN, LOW);

  if (digitalRead(SOS_BUTTON) == LOW) {
    sosAlert();
  }

  if (distance > threshold || distance <= 0) {
    digitalWrite(VIBRATION_MOTOR, LOW);
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
    digitalWrite(VIBRATION_MOTOR, HIGH);
    tone(BUZZER, 2500);
  }

  delay(50);
}

void alertPattern(int speed, int toneFreq) {
  digitalWrite(VIBRATION_MOTOR, HIGH);
  tone(BUZZER, toneFreq);
  delay(speed);
  digitalWrite(VIBRATION_MOTOR, LOW);
  noTone(BUZZER);
  delay(speed);
}

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
