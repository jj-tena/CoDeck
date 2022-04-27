const int switchPin1 = 4;
int switchState1 = 0;

const int switchPin2 = 5;
int switchState2 = 0;

const int switchPin3 = 6;
int switchState3 = 0;

void setup() {
  
    Serial.begin(9600);

    pinMode(switchPin1, INPUT);
    digitalWrite(switchPin1, HIGH);

    pinMode(switchPin2, INPUT);
    digitalWrite(switchPin2, HIGH);

    pinMode(switchPin3, INPUT);
    digitalWrite(switchPin3, HIGH);
}

void loop() {

  switchState1 = digitalRead(switchPin1);
  switchState2 = digitalRead(switchPin2);
  switchState3 = digitalRead(switchPin3);

  
  if (switchState1 == LOW) {
    Serial.println("1");
    delay(800);
  }
  if (switchState2 == LOW) {
    Serial.println("2");
    delay(800);
  }
  if (switchState3 == LOW) {
    Serial.println("3");
    delay(800);
  }
  
}
