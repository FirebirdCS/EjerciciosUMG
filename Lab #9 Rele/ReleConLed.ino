int relePin = 8; 
int ledPin = 13;  

void setup() {
  pinMode(relePin, OUTPUT); 
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Encender relé
  digitalWrite(relePin, HIGH);
  delay(2000);
  // Apagar el relé y encender el LED por un segundo
  digitalWrite(relePin, LOW);
  digitalWrite(ledPin, HIGH);
  delay(1000); 
  digitalWrite(ledPin, LOW);     
  // Repetir luego de 2 segundos
  delay(2000);
}