#include <Servo.h>
#include <Keypad.h> 
#include <SPI.h>
#include <MFRC522.h> // библиотека "RFID".
#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);
unsigned long uidDec, uidDecTemp;
// для храниения номера метки в десятичном формате
Servo servo;
String outpu;
String UID;
int cout = 0;
const byte ROWS = 4; // 4 строки
const byte COLS = 4;// 4 столбца
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
}; 
byte rowPins[ROWS] = {7, 8, 5, A1}; 
byte colPins[COLS] = {3, 2, A0, 4}; 
Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );
void setup() {
  
  Serial.begin(9600);
  SPI.begin();  //  инициализация SPI / Init SPI bus.
  mfrc522.PCD_Init();     // инициализация MFRC522 / Init MFRC522 card.
  servo.attach(6);
  servo.write(90);  // устанавливаем серву в закрытое сосотояние
}
void loop() {
  if (cout==0){
  // Поиск новой метки
    outpu="";
    if ( ! mfrc522.PICC_IsNewCardPresent()) {
      return;
    }
    // Выбор метки
    if ( ! mfrc522.PICC_ReadCardSerial()) {
      return;
    }
    uidDec = 0;
    // Выдача серийного номера метки.
    for (byte i = 0; i < mfrc522.uid.size; i++)
    {
      uidDecTemp = mfrc522.uid.uidByte[i];
      uidDec = uidDec * 256 + uidDecTemp;
    }
    UID=(String)uidDec;// Выводим UID метки в консоль.
    outpu=outpu+UID+(String)"|";
    cout=1;
    //смена светодиода
  }
  else if ((cout==1)||(cout==2)){
    char key = keypad.getKey();
    if (key){
      if (key=='#'){
        
        if (cout==1){
          cout=2;
          //смена светодиода
        }
        else{
          cout=0;
          Serial.println(outpu);
        }
      }
      else if (key=='*'){
        cout=0;
      }
      else{
        outpu=outpu+(String)key;
      }
    }
  }
}
