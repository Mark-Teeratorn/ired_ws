// blinking led by usb serial communication
const int ledPin = 13;  // pin number with built-in LED

void setup() {
  Serial.begin(115200);    // Serial communication initialization
  pinMode(ledPin, OUTPUT); // Set internal LED as output pin
  Serial.println("Arduino ready. Send command like: pm1:3");  
}

void loop() {
  if (Serial.available()) {
    String receivedString = Serial.readStringUntil('\n'); // read until newline

    // Print back what was received (echo)
    Serial.print("Received: ");
    Serial.println(receivedString);

    // Internal LED control when 'pm1' string is received
    if (receivedString.startsWith("pm1")) {
      int num = receivedString.substring(4).toInt(); // extract number
      Serial.print("Blinking LED ");
      Serial.print(num);
      Serial.println(" times...");

      blinkLED(num);

      Serial.println("Done blinking.");
    }
  }
}

void blinkLED(int times) {
  for (int i = 0; i < times; i++) {
    Serial.print("Blink #");
    Serial.println(i + 1);

    digitalWrite(ledPin, HIGH);
    delay(1000);
    digitalWrite(ledPin, LOW);
    delay(1000);
  }
}
