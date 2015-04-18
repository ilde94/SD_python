//declaramos los pines donde estar conectado cada sensor
const int sensorTemp = A0;
const int sensorLDR = A1;
const int sensorMOV = 6; //el de movimiento es digital
//el sensor de movmiento devuelve 0 si no hay movmiento y 1 si si lo hay.

int valor_actual_ldr;
int valor_actual_temp;
int valor_actual_mov;

void setup()
{
  //iniciacion del puerto serial
  Serial.begin(9600);
  
  valor_actual_ldr = 0;
  valor_actual_temp = 0;
  valor_actual_mov = 0;
  
  //Iniciacion pin del sensor de movimiento:
  pinMode(sensorMOV, INPUT);
  pinMode(5, OUTPUT);
  
}

void loop()
{
  //leemos los valores de cada sensor y lo asignamos a una variable
  int sensorVal_temp;
  int sensorVal_ldr;
  int sensorVal_mov;
  
  sensorVal_temp = analogRead(sensorTemp);
  sensorVal_ldr = analogRead(sensorLDR);
  sensorVal_mov = digitalRead(sensorMOV);
  /*
  Serial.print(" El valor del sensor en bruto: ");
  Serial.println(sensorVal);
 
  Serial.print("Valor del sensor MOV: ");
  Serial.println(sensorVal_mov);
  */
  //Convertir la ADC a voltage
  
  float voltaje_ldr = sensorVal_ldr *0.0049;
  float voltaje_temp = (sensorVal_temp/1024.0) * 5.0;
  
  //convertimos a grados el voltaje de la temperatura:
  float temp = (sensorVal_temp *5.0 *100.0)/1024.0; //temperatura en centigrados
  
  
  //solo escriberemos por pantalla en caso de que se produzca un cambio
  if(voltaje_ldr != valor_actual_ldr || temp != valor_actual_temp || sensorVal_mov != valor_actual_mov)
  {
    valor_actual_ldr = voltaje_ldr;
    valor_actual_temp = temp;
    valor_actual_mov = sensorVal_mov;
    if(sensorVal_mov == 1){
    digitalWrite(5, HIGH);
    }
    // actualizamos el nuevo valor
    //escribimos en el puerto serial los resultados:
    delay(500);
    Serial.println(temp - 50.0);
    delay(500);
    Serial.println(voltaje_ldr);
    delay(500);
    Serial.println(sensorVal_mov);
    delay(500);

  }
  digitalWrite(5, LOW);
  //pequeño delay de 15 segundos para no sobrecargar demsaiado
  //delay(3000);    
}

