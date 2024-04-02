const int ledPin13 = 13;
const int ledPin12 = 12;
const int ledPin11 = 11;
const int ledPin10 = 9;
const int ledPin9 = 10;
const int ledPin8 = 8;
const int ledPin3 = 3;
const int ledPin2 = 2;
const int buttonPin1 = 7;
const int buttonPin2 = 6;
const int buttonPin3 = 5;  
const int buttonPin4 = 4;  

bool lastButtonState1 = HIGH;
bool lastButtonState2 = HIGH;
bool lastButtonState3 = HIGH;  
bool lastButtonState4 = HIGH;  
unsigned long lastDebounceTime1 = 0;
unsigned long lastDebounceTime2 = 0;
unsigned long lastDebounceTime3 = 0;  
unsigned long lastDebounceTime4 = 0;  
unsigned long debounceDelay = 50;

bool grupo1Enabled = false;
bool grupo2Enabled = false;
bool grupo3Enabled = false;
bool grupo4Enabled = false;

void setup() {
  pinMode(ledPin13, OUTPUT);
  pinMode(ledPin12, OUTPUT);
  pinMode(ledPin11, OUTPUT);
  pinMode(ledPin10, OUTPUT);
  pinMode(ledPin9, OUTPUT);
  pinMode(ledPin8, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(buttonPin1, INPUT_PULLUP);
  pinMode(buttonPin2, INPUT_PULLUP);
  pinMode(buttonPin3, INPUT_PULLUP);  
  pinMode(buttonPin4, INPUT_PULLUP);  
  Serial.begin(9600);
}

void loop() {
    if (!grupo1Enabled && !grupo2Enabled && !grupo3Enabled && !grupo4Enabled) {
    digitalWrite(ledPin13, LOW);
    digitalWrite(ledPin12, LOW);
    digitalWrite(ledPin11, LOW);
    digitalWrite(ledPin10, LOW);
    digitalWrite(ledPin9, LOW);
    digitalWrite(ledPin8, LOW);
    digitalWrite(ledPin3, LOW);
    digitalWrite(ledPin2, LOW);
  }

  if (Serial.available() > 0) {
    char monitorSerial = Serial.read();
    if (monitorSerial == '1') {
      grupo1Enabled = true;
      grupo2Enabled = false;
      grupo3Enabled = false;
      grupo4Enabled = false;
      digitalWrite(ledPin11, LOW); 
      digitalWrite(ledPin10, LOW); 
      digitalWrite(ledPin9, LOW); 
      digitalWrite(ledPin8, LOW); 
      digitalWrite(ledPin3, LOW);
      digitalWrite(ledPin2, LOW);
      Serial.println("Grupo 1 permitido encender");
    } else if (monitorSerial == '2') {
      grupo1Enabled = false;
      grupo2Enabled = true;
      grupo3Enabled = false;
      grupo4Enabled = false;
      digitalWrite(ledPin13, LOW); 
      digitalWrite(ledPin12, LOW);
      digitalWrite(ledPin9, LOW); 
      digitalWrite(ledPin8, LOW); 
      digitalWrite(ledPin3, LOW); 
      digitalWrite(ledPin2, LOW); 
      Serial.println("Grupo 2 permitido encender");
    } else if (monitorSerial == '3') {
      grupo1Enabled = false;
      grupo2Enabled = false;
      grupo3Enabled = true;
      grupo4Enabled = false;
      digitalWrite(ledPin13, LOW); 
      digitalWrite(ledPin12, LOW);
      digitalWrite(ledPin11, LOW); 
      digitalWrite(ledPin10, LOW);
      digitalWrite(ledPin3, LOW); 
      digitalWrite(ledPin2, LOW);
      Serial.println("Grupo 3 permitido encender");
    } else if (monitorSerial == '4') {
      grupo1Enabled = false;
      grupo2Enabled = false;
      grupo3Enabled = false;
      grupo4Enabled = true;
      digitalWrite(ledPin13, LOW); 
      digitalWrite(ledPin12, LOW); 
      digitalWrite(ledPin11, LOW); 
      digitalWrite(ledPin10, LOW); 
      digitalWrite(ledPin9, LOW); 
      digitalWrite(ledPin8, LOW); 
      Serial.println("Grupo 4 permitido encender");
    } else if (monitorSerial == '5') {
      grupo1Enabled = false;
      grupo2Enabled = false;
      grupo3Enabled = false;
      grupo4Enabled = false;
      Serial.println("Todos los grupos apagados");
    }
  }

  static bool ledState1 = LOW;
  int buttonState1 = digitalRead(buttonPin1);
  if (buttonState1 != lastButtonState1 && (millis() - lastDebounceTime1) > debounceDelay) {
      lastDebounceTime1 = millis();
      if (grupo1Enabled) {
          if(buttonState1 == LOW){
              ledState1 = !ledState1;
              digitalWrite(ledPin13, ledState1 ? HIGH : LOW);
              digitalWrite(ledPin12, ledState1 ? HIGH : LOW);
              Serial.println(ledState1 ? "Prende LEDs del primer grupo" : "Apaga LEDs del primer grupo");
          }
      }
      lastButtonState1 = buttonState1;
  }

  static bool ledState2 = LOW;
  int buttonState2 = digitalRead(buttonPin2);
  if (buttonState2 != lastButtonState2 && (millis() - lastDebounceTime2) > debounceDelay) {
    lastDebounceTime2 = millis();
    if (grupo2Enabled) {
      if(buttonState2 == LOW){
        ledState2 = !ledState2;
        digitalWrite(ledPin11, ledState2 ? HIGH : LOW);
        digitalWrite(ledPin10, ledState2 ? HIGH : LOW);
        Serial.println(ledState2 ? "Prende LEDs del segundo grupo" : "Apaga LEDs del segundo grupo");
      }
    }
    lastButtonState2 = buttonState2;
  }
  static bool ledState3 = LOW;
  int buttonState3 = digitalRead(buttonPin3);
  if (buttonState3 != lastButtonState3 && (millis() - lastDebounceTime3) > debounceDelay) {
    lastDebounceTime3 = millis();
    if (grupo3Enabled) {
      if(buttonState3 == LOW){
          ledState3 = !ledState3;
          digitalWrite(ledPin9, ledState3 ? HIGH : LOW);
          digitalWrite(ledPin8, ledState3 ? HIGH : LOW);
          Serial.println(ledState3 ? "Prende LEDs del tercer grupo" : "Apaga LEDs del tercer grupo");
      }
    }
    lastButtonState3 = buttonState3;
  }
  static bool ledState4 = LOW;
  int buttonState4 = digitalRead(buttonPin4);
  if (buttonState4 != lastButtonState4 && (millis() - lastDebounceTime4) > debounceDelay) {
    lastDebounceTime4 =  millis();
    if (grupo4Enabled) {
      if(buttonState4 == LOW){
        ledState4 = !ledState4;
        digitalWrite(ledPin3, ledState4 ? HIGH : LOW);
        digitalWrite(ledPin2, ledState4 ? HIGH : LOW);
        Serial.println(ledState4 ? "Prende LEDs del cuarto grupo" : "Apaga LEDs del cuarto grupo");
      }
    }
    lastButtonState4 = buttonState4;
  }
}
