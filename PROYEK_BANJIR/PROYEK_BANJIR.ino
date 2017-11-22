#define RELAY_ON 1
#define RELAY_OFF 0
#define RELAY_1 2
const int trig =11;
const int echo =12;
int durasi;
int jarak; 
int titiknol; 
int naik;
void setup() {
  // put your setup code here, to run once:
  pinMode(RELAY_1, OUTPUT);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  digitalWrite(RELAY_1, RELAY_OFF);
  Serial.begin(9600);
}
void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  durasi = pulseIn(echo, HIGH);
  jarak = (durasi*0.034)/2;
  titiknol = jarak - 35;
  naik = titiknol * -1;
  Serial.println(naik);
  delay(500);
  if (naik == 28){ //banjir
    digitalWrite(RELAY_1, RELAY_ON);
    delay(1000);
    digitalWrite(RELAY_1,RELAY_OFF);
    delay(200);
  }else if (naik == 26){ //siap siap
    digitalWrite(RELAY_1, RELAY_ON);
    delay(2000);
    digitalWrite(RELAY_1,RELAY_OFF);
    delay(500);
  }else if (naik == 21){ //siaga 1
    digitalWrite(RELAY_1, RELAY_ON);
    delay(3000);
    digitalWrite(RELAY_1,RELAY_OFF);
    delay(1000);
  }else if (naik == 16){ //siaga 2
    digitalWrite(RELAY_1, RELAY_ON);
    delay(4000);
    digitalWrite(RELAY_1,RELAY_OFF);
    delay(3000);
  }else if (naik == -2){ //surut
    digitalWrite(RELAY_1, RELAY_ON);
    delay(1000);
    digitalWrite(RELAY_1,RELAY_OFF);
    delay(200);
  }else{
    digitalWrite(RELAY_1, RELAY_OFF);
  }
}

