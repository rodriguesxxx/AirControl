// #include <IrReceive.h>

// volatile  unsigned int irBuffer[maxLen];
// volatile unsigned int x = 0;

// IrReceive::IrReceive() {
//   attachInterrupt(digitalPinToInterrupt(rxPinIR), rxIR_Interrupt_Handler, CHANGE);//set up ISR for receiving IR signal
// }

// void IrReceive::readRawCode() {
//   // put your main code here, to run repeatedly:

//   Serial.println(F("Press the button on the remote now - once only"));
//   delay(5000); // pause 5 secs
//   if (x) { //if a signal is captured
//     Serial.println();
//     Serial.print(F("Raw: (")); //dump raw header format - for library
//     Serial.print((x - 1));
//     Serial.print(F(") "));
//     detachInterrupt(digitalPinToInterrupt(rxPinIR));//stop interrupts & capture until finshed here
//     for (int i = 1; i < x; i++) { //now dump the times
//       if (!(i & 0x1)) Serial.print(F("-"));
//       Serial.print(irBuffer[i] - irBuffer[i - 1]);
//       Serial.print(F(", "));
//     }
//     x = 0;
//     Serial.println();
//     Serial.println();
//     attachInterrupt(digitalPinToInterrupt(rxPinIR), rxIR_Interrupt_Handler, CHANGE);//re-enable ISR for receiving IR signal
//   }

// }

// void rxIR_Interrupt_Handler() {
//   if (x > maxLen) return; //ignore if irBuffer is already full
//   irBuffer[x++] = micros(); //just continually record the time-stamp of signal transitions

// }