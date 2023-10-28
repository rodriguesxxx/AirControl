#include <IrSensor.h>
#include <IRremote.hpp>



void IrSensor::send(char cmd){
    
    IRRawDataType sDecodedRawDataArray[RAW_DATA_ARRAY_SIZE];
    DistanceWidthTimingInfoStruct sDistanceWidthTimingInfo;
    uint8_t sNumberOfBits = 120;
    int qtyRawData = 0;
    uint32_t tRawData[qtyRawData];
    
    switch (cmd)
    {
        case POWER_ON:
            Serial.print("entre");
            sDecodedRawDataArray[RAW_DATA_ARRAY_SIZE] = { 0x6C56 }; 
            sDistanceWidthTimingInfo = { 8350, 4150, 550, 1500, 550, 550 }; 
            qtyRawData = 4;
            tRawData[0] = 0x6C56;
            tRawData[1] = 0x1A40;
            tRawData[2] = 0xC0C000C;
            tRawData[3] = 0x6B0C1;
            break;
        
        case POWER_OFF:
            sDecodedRawDataArray[RAW_DATA_ARRAY_SIZE] = { 0x7856 }; 
            sDistanceWidthTimingInfo = { 8400, 4100, 500, 1550, 500, 550 }; 
            qtyRawData = 4;
            tRawData[0] = 0x7856;
            tRawData[1] = 0xC010;
            tRawData[2] = 0x220C000C;
            tRawData[3] = 0x550C24;
            break;

        default:
            break;
    }

    IrSender.sendPulseDistanceWidthFromArray(38, &sDistanceWidthTimingInfo, tRawData, sNumberOfBits, PROTOCOL_IS_LSB_FIRST, 100, 0);

    delay(DELAY_BETWEEN_REPEATS_MILLIS); 
}