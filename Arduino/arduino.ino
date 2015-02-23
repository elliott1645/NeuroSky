int incomingByte = 0;   // for incoming serial data
boolean flag = false;
int ledPin = 13;

void setup() {
        Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
        pinMode(ledPin,OUTPUT);
}

void loop() {

        // send data only when you receive data:
        while (Serial.available() > 0) 
        {
                // read the incoming byte:
                incomingByte = Serial.read();
                flag=true;
        }
        if(flag)
        {
           digitalWrite(ledPin,HIGH);
           delay(250);
           digitalWrite(ledPin,LOW);
           flag=false;
        }
}
 
