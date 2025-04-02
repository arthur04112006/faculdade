int led1 = 7;
int led2 = 6;
int led3 = 5;
int led4 = 4;
int led5 = 3;
int led6 = 2;
int pot = A5;

void setup() 
{
    pinMode(led1, OUTPUT);
    pinMode(led2, OUTPUT);
    pinMode(led3, OUTPUT);
    pinMode(led4, OUTPUT);
    pinMode(led5, OUTPUT);
    pinMode(led6, OUTPUT);
    pinMode(pot, INPUT);

}
void loop() 
{
    int valor = analogRead(pot);
    int nivel = map(valor, 0, 1023, 0, 1023);

    digitalWrite(led1, nivel =< 292 ? HIGH : LOW);
    digitalWrite(led2, nivel =< 438 ? HIGH : LOW);
    digitalWrite(led3, nivel =< 585 ? HIGH : LOW);
    digitalWrite(led4, nivel =< 731 ? HIGH : LOW);
    digitalWrite(led5, nivel =< 877 ? HIGH : LOW);
    digitalWrite(led6, nivel =< 1023 ? HIGH : LOW);
}