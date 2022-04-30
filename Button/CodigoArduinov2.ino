// Array para los pines y el estado de cada switch
int switchPin[12] = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13};
int switchState[12] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

int i;



void setup() {
  
  Serial.begin(9600);

  // Inicializamos los pines como input y mandamos señal en high para detectar cuando se cierre el circuito
  // (los switches son normalmente cerrados) y activar la resistencia interna de cada pin
  for (i = 0; i < 12; ++i)
    {
      pinMode(switchPin[i], INPUT);
      digitalWrite(switchPin[i], HIGH);
    }
}

void loop() {
  // Con este for leemos los valores en cada pin constantemente para comprobar si alguno se activa
  for (i = 0; i < 12; ++i)
    {
      switchState[i] = digitalRead(switchPin[i]);
      if (switchState[i] == LOW) {
        Serial.println(switchPin[i]-1);
        delay(800);
      }
    }
  
}
