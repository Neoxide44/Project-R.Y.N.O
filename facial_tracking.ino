String x,vertical,horizontal;
void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
 
}

void loop() {
  
  while(!Serial.available());
  x = Serial.readString();
  if(x.length()==2)
  {
    vertical = x[0];
    horizontal = x[1];
    
    Serial.print("vertical = " + vertical);
    Serial.println(", horizontal = " + horizontal);
  }
  

 }
