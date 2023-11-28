int solenoid = 13; 

void setup() {
  pinMode(solenoid, OUTPUT);
  Serial.begin(9600);

void loop() {
  if (Serial.available() > 0) {
    char receivedChar = Serial.read();
    if (receivedChar == '1') {
      digitalWrite(solenoid, HIGH); 
    } else if (receivedChar == '0') {
      digitalWrite(solenoid, LOW); 
    }
  }
}
