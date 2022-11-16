/**
 * @copyright (C) 2017 Melexis N.V.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */
#include <Wire.h>
#include <Arduino.h>

//#include "mbed.h"
#include "MLX90641_I2C_Driver.h"

//I2C i2c(p9, p10);

void MLX90641_I2CInit()
{   
   // i2c.stop();
}

int MLX90641_I2CRead(uint8_t slaveAddr, uint16_t startAddress, uint16_t nMemAddressRead, uint16_t *data)
{
   
    /*
    char cmd[2] = {0,0};
    char i2cData[1664] = {0};
    uint16_t *p;
    
    p = data;
     cmd[0] = startAddress >> 8;
    cmd[1] = startAddress & 0x00FF;
    
    uint8_t sa;                           
    int ack = 0;                               
    int cnt = 0;
    int i = 0;
    sa = (slaveAddr << 1);
    
    i2c.stop();
    wait_us(5);    
    ack = i2c.write(sa, cmd, 2, 1);
    
    if (ack != 0x00)
    {
        return -1;
    }
             
    sa = sa | 0x01;
    ack = i2c.read(sa, i2cData, 2*nMemAddressRead, 0);
    
    if (ack != 0x00)
    {
        return -1; 
    }          
    i2c.stop();   
    
    for(cnt=0; cnt < nMemAddressRead; cnt++)
    {
        i = cnt << 1;
        *p++ = (uint16_t)i2cData[i]*256 + (uint16_t)i2cData[i+1];
    }*/
    
    uint16_t bytesRemaining = nMemAddressRead * 2;
    uint16_t dataSpot = 0; //Start at beginning of array
    //Setup a series of chunked I2C_BUFFER_LENGTH byte reads
    while (bytesRemaining > 0) {
        Wire.beginTransmission(slaveAddr);
        Wire.write(startAddress >> 8); //MSB
        Wire.write(startAddress & 0xFF); //LSB
        if (Wire.endTransmission(false) != 0) { //Do not release bus
            //Serial.println("No ack read");
            return (0); //Sensor did not ACK
        }

        uint16_t numberOfBytesToRead = bytesRemaining;
        if (numberOfBytesToRead > I2C_BUFFER_LENGTH) {
            numberOfBytesToRead = I2C_BUFFER_LENGTH;
        }

        Wire.requestFrom((uint8_t)slaveAddr, numberOfBytesToRead);
        if (Wire.available()) {
            for (uint16_t x = 0 ; x < numberOfBytesToRead / 2; x++) {
                //Store data into array
                data[dataSpot] = Wire.read() << 8; //MSB
                data[dataSpot] |= Wire.read(); //LSB

                dataSpot++;
            }
        }else
            return -1;

        bytesRemaining -= numberOfBytesToRead;

        startAddress += numberOfBytesToRead / 2;
    }

    return 0;   
} 

void MLX90641_I2CFreqSet(int freq)
{
//    i2c.frequency(1000*freq);
    Wire.setClock((long)1000 * freq);
}

int MLX90641_I2CWrite(uint8_t slaveAddr, uint16_t writeAddress, uint16_t data)
{
    /*
    uint8_t sa;
    int ack = 0;
    char cmd[4] = {0,0,0,0};
    static uint16_t dataCheck;
    

    sa = (slaveAddr << 1);
    cmd[0] = writeAddress >> 8;
    cmd[1] = writeAddress & 0x00FF;
    cmd[2] = data >> 8;
    cmd[3] = data & 0x00FF;

    i2c.stop();
    wait_us(5);    
    ack = i2c.write(sa, cmd, 4, 0);
    
    if (ack != 0x00)
    {
        return -1;
    }         
    i2c.stop();   
    
    MLX90641_I2CRead(slaveAddr,writeAddress,1, &dataCheck);
    
    if ( dataCheck != data)
    {
        return -2;
    }    */
    Wire.beginTransmission((uint8_t)slaveAddr);
    Wire.write(writeAddress >> 8); //MSB
    Wire.write(writeAddress & 0xFF); //LSB
    Wire.write(data >> 8); //MSB
    Wire.write(data & 0xFF); //LSB
    if (Wire.endTransmission() != 0) {
        //Sensor did not ACK
        //Serial.println("Error: Sensor did not ack");
        return (-1);
    }

    uint16_t dataCheck;
    MLX90641_I2CRead(slaveAddr, writeAddress, 1, &dataCheck);
    if (dataCheck != data) {
        //Serial.println("The write request didn't stick");
        return -2;
    }
    return 0;
}

