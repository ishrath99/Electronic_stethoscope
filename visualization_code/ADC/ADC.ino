

const int analogPin = A0; // The ADC pin

long int samplingFreq = 800;            // sampling frequency= 8kHz
long Delay = 1000000 / samplingFreq;    //sampling interval in microseconds
long t0, t1;

void setup() {
  Serial.begin(14400); // Initialize serial communication
}

void loop() {

  t0 = micros(); // time just before taking reading
  int sensorValue = analogRead(analogPin); // Read voltage from ADC pin
  Serial.println(sensorValue); // Send voltage value over serial
  t1 = micros(); // time just after transmitting data
  
  // set delay to preserve the 
  if (t1 - t0 < Delay) {
    delayMicroseconds(Delay + t0 - t1);
  }

}
