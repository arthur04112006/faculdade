int led = 13;
int ldr = A0;
int valorLdr = 0;

void setup()
{
    pinMode(led, OUTPUT);
    pinMode(ldr, INPUT); 
}
void loop()
{
    valorLdr = analogRead(ldr);
    Serial.begin(9600);
    Serial.print("luminosidade: ");
    Serial.println(valorLdr);
    if (valorLdr < 20)/
    {
        digitalWrite(led, HIGH);
        Serial.println("led ligado");
    }
    else
    {
        digitalWrite(led, LOW);
        Serial.println("led desligado");
    }
    delay(500);
}

// aqui estou usando um sensor ldr com resistor (laranja, laranja, marrom e dourado). 
// o sensor ligado no positivo 5v e negativo gnd com o resistor. o negativo é ligado na porta A0. e led ligado na porta 13.