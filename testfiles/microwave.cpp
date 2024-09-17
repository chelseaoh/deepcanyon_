#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h> // for system()

int main()
{
  wiringPiSetup();
  char val;
  {
    pinMode(28,INPUT);//microwave motion sensor connecting to PIN28 on raspberry pi
  }
  
  while(1)//if someone passes by
  { 
   val=digitalRead(28);
   if(val==0)
  {
  printf("someone is in the area \n");
  system("python /home/deepcanyonnrs/MicrowaveSensor/videos/testvideo.py");
   
   
   delay(100);//delay10MS

  }

 else//nobody passes by
  {
   printf("no one is in the area \n");
   delay(100); //delay 10MS  
 }
 
 }
 
 }