/*
    1e6/(F*N_Samp) (us)
*/
#include <SPI.h>
#define SAMPLES 16
#define FREQUENCY 1000
#define CS_PIN 10
const uint32_t PERIOD = 1e6 / (FREQUENCY * SAMPLES);
uint32_t next = 0;

uint16_t phase = 0;

uint16_t SIN_LUT[SAMPLES] = {};

void setup() {
  // Populate lookup table @ ~1V_pp
  for (int k = 0; k < SAMPLES; k++) {
    SIN_LUT[k] = ((2048 / 2) * (sin(2 * PI * (float)k / SAMPLES) + 1));
  }

  SPI.begin();

  // Set CS pin high to deselect the DAC
  digitalWrite(CS_PIN, HIGH);
}

void loop() {
  uint32_t now = micros();

  if (now > next) {
    writeDAC(SIN_LUT[phase], 0);

    phase = (phase + 1) % SAMPLES;
    next += PERIOD;
  }
}

void writeDAC(uint16_t value, int channel) {
  uint16_t command = 0x3000;  // Default command bits (0b0011 0000 0000 0000)

  if (channel == 1) {
    command |= 0x8000;  // Set bit 15 to select channel B
  }

  command |= (value & 0x0FFF);  // Mask the value to 12 bits and combine with the command

  // Select the DAC by pulling CS low
  digitalWrite(CS_PIN, LOW);

  // Send the command via SPI
  SPI.transfer16(command);

  // Deselect the DAC by pulling CS high
  digitalWrite(CS_PIN, HIGH);
}
