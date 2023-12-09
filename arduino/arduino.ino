#include <Servo.h>

constexpr byte servo_pin = 52;

Servo servo;

void setup() {
    Serial.begin(115200);
    servo.attach(servo_pin, 0, 3000);
    servo.writeMicroseconds(1500);
}

void loop() {
    if (Serial.available() > 1) {
        const uint8_t code_lsb = static_cast<uint8_t>(Serial.read());
        const uint8_t code_msb = static_cast<uint8_t>(Serial.read());
        const uint16_t target = ((static_cast<uint16_t>(code_msb) << 8) | static_cast<uint16_t>(code_lsb));
        servo.writeMicroseconds(target);
    }
}
