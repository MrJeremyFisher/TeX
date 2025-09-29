const uint32_t SW_PERIOD_US = 2e3;  // 2s
int cur_pin = 2;

void setup() {
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  Serial.begin(9600);
}

void loop() {
    digitalWrite(cur_pin, LOW);

    cur_pin++;
    if (cur_pin > 5) {
      cur_pin = 2;
    }
    switch (cur_pin) {
      case 2:
        Serial.print("220Ω");
        Serial.print("\n");
        break;
      case 3:
        Serial.print("1kΩ");
        Serial.print("\n");
        break;
      case 4:
        Serial.print("3.6kΩ");
        Serial.print("\n");
        break;
      case 5:
        Serial.print("9.1kΩ");
        Serial.print("\n");
        break;
      default:
        break;
    }
    digitalWrite(cur_pin, HIGH);
    delay(SW_PERIOD_US);
}