



int IRSensor1 = 2;

int LED = 13; // conect Led to arduino pin 13
int slot1;



void setup() 
{
  Serial.begin(9600);
  pinMode (IRSensor1, INPUT);
  pinMode (LED, OUTPUT); // Led pin OUTPUT
 
}

void loop()
{
  int slot1 = digitalRead (IRSensor1);
  
  if (slot1 == 1 ){
    digitalWrite(LED, LOW); // LED LOW
    Serial.println("Slot 1 : Available");
    delay(1000);
  }

  else
  {
    digitalWrite(LED, HIGH); // LED High
     Serial.println("Slot 1 : Not Available");
     delay(1000);
  }
  
}
