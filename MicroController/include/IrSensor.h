// #include <PinDefinitionsAndMore.h>


// #if !defined(IR_SEND_PIN)
// #define IR_SEND_PIN 3
// #endif

// #define DECODE_DISTANCE_WIDTH 
// #if !defined(RAW_BUFFER_LENGTH)
// #  if RAMEND <= 0x4FF || RAMSIZE < 0x4FF
// #define RAW_BUFFER_LENGTH  120
// #  elif RAMEND <= 0xAFF || RAMSIZE < 0xAFF // 0xAFF for LEONARDO
// #define RAW_BUFFER_LENGTH  400 
// #  else
// #define RAW_BUFFER_LENGTH  750
// #  endif
// #endif

// #define DELAY_BETWEEN_REPEATS_MILLIS 70

// #ifndef __IRSENSOR__
//     #define IRSENSOR
    
//     class IrSensor{
        
//         public:
//             void send(char cmd);
        
//         private:
//             #define POWER_ON 'h' //high
//             #define POWER_OFF 'l' //low
//     };
// #endif