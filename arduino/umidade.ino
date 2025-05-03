int sensor = A0; 

void setup() {
  Serial.begin(9600);     
}
void loop() {
  int leituraSensor = analogRead(sensor);
  float porcentagem = map(leituraSensor, 694, 0, 0, 100);  
  Serial.print(" | Umidade: ");
  Serial.print(porcentagem);
  Serial.println("%");
  delay(1000);  
}
// sensor: vcc = 3.3v
// sensor: gnd = gnd
// sensor: A0 = A0


