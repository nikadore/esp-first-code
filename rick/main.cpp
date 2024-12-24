#include <Arduino.h>

const int dacPin = D1; // GPIO 5 on ESP8266
const int sampleRate = 12000;

const unsigned int sampleCount = 631343;
const signed char samples[] = {0}; // You should provide your own waveform data here.

void setup() {
    Serial.begin(115200);

    analogWriteRange(255); // Set analog write range to 8-bit resolution
    analogWriteFreq(sampleRate); // Set PWM frequency

    pinMode(dacPin, OUTPUT);
}

void loop() {
    for (unsigned int i = 0; i < sampleCount; i++) {
        int waveValue = 128 + samples[i];
        analogWrite(dacPin, waveValue);
        delayMicroseconds(1000000 / sampleRate);
    }

    Serial.println("CYCLE!");

    delay(1000);
}


