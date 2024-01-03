#include <WiFi.h>
const char *ssid = "Shubhodip Pal";
const char *password = "19122003#";
WiFiServer server(80);
int a;
#define relay 27
#define bluein 2
#define red 12
#define green 13
#define blue 14
void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
    Serial.println("Connecting to WiFi...");
    pinMode(red, HIGH);
  }
  pinMode(red, LOW);
  Serial.println("Connected to WiFi");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
  pinMode(relay, OUTPUT);
  server.begin();
  Serial.println("Server started");
}

void loop() {
  WiFiClient client = server.available();
  if (client) {
    Serial.println("New client connected");
    String request = client.readStringUntil('\r');
    Serial.println("Received data: " + request);
    int receivedValue = request.toInt();
    Serial.println("Converted to integer: " + String(receivedValue));
    if (receivedValue == 97) {
      digitalWrite(relay, HIGH);
    } else {
      digitalWrite(relay, LOW);
    }
    client.print("Received: ");
    client.println(receivedValue);
    client.stop();
    Serial.println("Client disconnected");
  }
  
}
