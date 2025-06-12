int sensorPresenca = 2;
int led = 13;
valor = ;
void setup()
{
    pinMode(led, OUTPUT);
    pinMode(sensorPresenca, INPUT);
}
void loop()
{
    valor = analogRead(sensorPresenca)
    led = map(valor, 0, 1)

    if valor = 1:
     digitalWrite(led, HIGH);
    else:
     digitalWrite(led, LOW);
}