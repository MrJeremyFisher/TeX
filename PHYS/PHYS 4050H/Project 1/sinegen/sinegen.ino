#include <SPI.h>
#define SAMPLES 16
#define FREQUENCY 1000
#define CS_PIN 10
const uint32_t PERIOD = 1e6 / (FREQUENCY * SAMPLES);
uint32_t next = 0;

uint16_t phase = 0;

uint16_t SIN_LUT[SAMPLES] = {};

void setup()
{
  // Populate lookup table @ ~1V_pp
  for (int k = 0; k < SAMPLES; k++)
  {
    SIN_LUT[k] = ((2048 / 2) * (sin(2 * PI * (float)k / SAMPLES) + 1));
  }

  SPI.begin();

  // Chip select pin active low, this will deselect the DAC
  digitalWrite(CS_PIN, HIGH);
}

void loop()
{
  uint32_t now = micros();

  if (now > next)
  {
    writeDAC(SIN_LUT[phase]);

    phase = (phase + 1) % SAMPLES;
    next += PERIOD;
  }
  // Could we delayMicroseconds(PERIOD);??
}

void writeDAC(uint16_t value)
{
  uint16_t command = 0x3000; // 0011...,
  // 0 -> Write Channel A
  // 0 -> DC
  // 1 -> V_o=V_r * value/4096
  // 1 -> Output shutdown, operating on HI
  // See datasheet for more

  // AND here forces to 12 bit
  // OR command w/value, gives
  // 0011 value
  command |= (value & 0x0FFF);

  digitalWrite(CS_PIN, LOW);

  SPI.transfer16(command);

  digitalWrite(CS_PIN, HIGH);
}
