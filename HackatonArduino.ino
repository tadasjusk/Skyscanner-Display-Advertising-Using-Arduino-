#include "LiquidCrystal.h"

// initialize the library by providing the nuber of pins to it
LiquidCrystal lcd(8,9,4,5,6,7);
char str[100];
int k=0;

void setup() {
 lcd.begin(16,2);
 Serial.begin(115200);
}
void loop()
{
 if(Serial.available() > 0) {
   while(Serial.available() > 0){
   char data = Serial.read();
   str[k] = data;
   k++;
   }
   for(int i=0; i<k; i++){
     Serial.print(str[i]);
   }
   k=0;
  lcd.setCursor(0,0);
 lcd.print("Skyscanner: Cheapest weekend getaway!");
 lcd.setCursor(0,1);
 lcd.print(str);
 }
for (int positionCounter = 0; positionCounter < 16; positionCounter++) {
  lcd.scrollDisplayLeft();
  delay(300);
}
}
