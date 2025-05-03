int sensor = A0; 
void setup() {
    Serial.begin(9600);
    pinMode(sensor, INPUT);
    Serial.println("Sensor de Fogo");
    Serial.println("Lendo dados...");
}
void loop() {
    int leituraSensor = analogRead(sensor);
    float porcentagem = map(leituraSensor, 694, 0, 0, 100);
    Serial.print(porcentagem);
}