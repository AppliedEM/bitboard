#ifndef JERK_H
#define JERK_H

void init_imu();
uint32_t accel_mag();
uint32_t accel_jerk(int mag1, int mag2, int time);
uint32_t jerkometer();

#endif
