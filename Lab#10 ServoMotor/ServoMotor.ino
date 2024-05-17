#include <Servo.h>

Servo servoMotor;

void setup() {
  servoMotor.attach(4);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char comando = Serial.read();
    if (comando == 'I') {
      servoMotor.write(0);
      Serial.println("Girando a la izquierda");
    } else if (comando == 'D') {
      servoMotor.write(180);
      Serial.println("Girando a la derecha");
    } else if (comando == 'C') {
      // Centro
      servoMotor.write(90);
      Serial.println("Centro");
    } 
  }
  delay(15);
}
