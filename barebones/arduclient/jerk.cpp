#include <Wire.h>
#include <math.h>
#include <Arduino.h>
#include "jerk.h"

const int MPU_addr=0x68;
int16_t AcX,AcY,AcZ,Tmp,GyX,GyY,GyZ;

void init_imu(){
  Wire.begin();
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x6B);  // PWR_MGMT_1 register
  Wire.write(0);     // set to zero (wakes up the MPU-6050)
  Wire.endTransmission(true);
  Wire.begin();
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x1C);
  Wire.write(0x08);
  Wire.endTransmission(true);
}

uint32_t accel_mag(){
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
  Wire.endTransmission(false);
  Wire.requestFrom(MPU_addr,14,true);  // request a total of 14 registers
  AcX=Wire.read()<<8|Wire.read();  // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)
  AcY=Wire.read()<<8|Wire.read();  // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
  AcZ=Wire.read()<<8|Wire.read();  // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)

  uint32_t mag = sqrt((uint32_t)(AcX*AcX + AcY*AcY + AcZ*AcZ)); //calculate magnitude
  return mag;
}

uint32_t accel_jerk(int mag1, int mag2, int time){
	int my_delay=50;
	uint32_t jerk = abs(mag2-mag1)/my_delay;
	return jerk;
}

uint32_t jerkometer(){
    static uint mag1 = 0;
    static uint mag2 = 0;
	uint32_t jerk;
	for (int i=0; i<5; i++){
		mag1 = accel_mag();
		int my_delay=50;
    	jerk = accel_jerk(mag1, mag2, my_delay);
		delay(my_delay);
		mag2 = mag1;
	}
	return jerk;
}
