#define LED1 13
#define LED2 12

void setup() {
  Serial.begin(9600);
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(13,OUTPUT);
}

void loop() {
 
  delay(1000);
  int a = digitalRead(2);
  int b = digitalRead(3);
  String st,ts;
  if(a==1)
  {
    digitalWrite(LED1,LOW);
    Serial.println("Available");
  }
  else{
    digitalWrite(LED1,HIGH);
    Serial.println("Not Available");
  }
  if(b==1)
  {
    digitalWrite(LED1,LOW);
    Serial.println("Not Available");
  }
  else{
    digitalWrite(LED2,HIGH);
    Serial.println(" Available");
  }
  delay(500);
}
