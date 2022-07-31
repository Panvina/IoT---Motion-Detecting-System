int calibrationTime = 40;  
int pir = 2; 
int buzzer = 3;            
int oldState = LOW;             
int curState = 0;                

void setup() {
  pinMode(buzzer, OUTPUT);
  pinMode(pir, INPUT);    // initialize sensor as an input
  Serial.begin(9600);        // initialize serial
  //prepping the time for the PIR sensor to start working properly
    Serial.println("PREPARING THE SENSOR...");
    for(int i = 0; i < calibrationTime; i++){
      delay(1000);
      }
    Serial.println("SENSOR ACTIVE");
}

void loop(){
  curState = digitalRead(pir);   // read sensor value
  if (curState == HIGH) {           // check if the sensor is HIGH
    delay(100);                
          //ensuring that the serial prints data only once if detected
    if (oldState == LOW) {
      Serial.println(curState); 
      oldState = HIGH;       // update variable state to HIGH
    }
  } 
  else {
      delay(100);             
      if (oldState == HIGH){
        Serial.println(curState);
        oldState = LOW;       // update variable state to LOW
    }
  }

  // if there's data being sent from Raspberry Pi
  if (Serial.available()){
    char data = '0';
    //read the data as long as it is available
    while(Serial.available() > 0){
       data = Serial.read();
    //if the data being sent is == to 1 which is indicating that the user is turning on the buzzer
    if (data == '1'){
      tone(buzzer, 1000);
    } else{
      noTone(buzzer);
    }   
    }
  }
}
