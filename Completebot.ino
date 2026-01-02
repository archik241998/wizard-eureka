#include <Servo.h>
//#include <Ultrasonic.h> // Correct library for Teensy 4
#include <Encoder.h>
//#include <NewPing.h>

// --- Encoder Configuration ---
#define TICKS_PER_REVOLUTION 280

// --- Servo and Ultrasonic Pin Definitions ---
Servo myServo;
const int ULTRASONIC_TRIG_PIN = 34
const int ULTRASONIC_ECHO_PIN = 35
#define SERVO_PIN 9

// --- Motor Pin Definitions ---
#define MOTOR_C_IN1_PIN 11
#define MOTOR_C_IN2_PIN 10
#define MOTOR_C_ENA_PIN 12 
#define MOTOR_C_ENCODER_CH_A 24
#define MOTOR_C_ENCODER_CH_B 25
Encoder_C = Encoder(MOTOR_C_ENCODER_CH_A, MOTOR_C_ENCODER_CH_B);

#define MOTOR_A_IN3_PIN 2;
#define MOTOR_A_IN4_PIN 3;
#define MOTOR_A_ENB_PIN 4;

// --- IR Sensor Pin Definitions ---//
const int irPins[6] = {22, 21, 20, 17, 16, 15};
int irValues[6];

// --- Bot Movement Constants ---
int FORWARD_SPEED = 180;
int REVERSE_SPEED = 120; // A slower speed for backing up
int TURN_SPEED = 50;
int REVERSE_DURATION = 1000; // Time to reverse in milliseconds (1 second)

// --- Ultrasonic Scan Constants ---
int AVOID_DISTANCE_CM = 40; // Avoidance distance in centimeters
int SCAN_ANGLE_RANGE = 90;
int SCAN_STEP = 15;
//NewPing sonar(ULTRASONIC_TRIG_PIN, ULTRASONIC_ECHO_PIN, 400); // 400cm max distance


// --- IR Sensor Constants ---
// A digital IR sensor typically outputs LOW when an object is detected.
//#define OBSTACLE_DETECTED_STATE "0"
int NUM_IR_SENSORS = 6;
int irSensorValues[NUM_IR_SENSORS];

// --- Global Variables for Encoder Readings ---
long encoderC_steps = 0;
float encoderC_revolutions = 0.0;
float encoderC_degrees = 0.0;

// --- Function Declarations ---
void stopAllMotors();
int scan_sensor();
void moveForward(int speed);
void reverse(int speed, int duration);
void turnLeft(int speed);
void turnRight(int speed);
void setServoAngle(int angle);
void updateAllEncoderValues();
void resetAllEncoders();
void readIRSensors();
bool detectLowObstacle();
void scanEnvironment();

// --- Setup Function (Runs once when the Teensy starts) ---
void setup() {
  Serial.begin(9600);
  while (!Serial);

  myServo.attach(SERVO_PIN);
  setServoAngle(90);
  delay(1000);

  pinMode(ULTRASONIC_TRIG_PIN, OUTPUT);
  pinMode(ULTRASONIC_ECHO_PIN, INPUT);
  
  pinMode(MOTOR_C_IN1_PIN, OUTPUT);
  pinMode(MOTOR_C_IN2_PIN, OUTPUT);
  pinMode(MOTOR_C_ENA_PIN, OUTPUT);
  pinMode(MOTOR_A_IN3_PIN, OUTPUT);
  pinMode(MOTOR_A_IN4_PIN, OUTPUT);
  pinMode(MOTOR_A_ENB_PIN, OUTPUT);

  // Set IR sensor pins as inputs.
  for (int i = 0; i < 6; i++) {
    pinMode(irPins[i], INPUT);
  }
  Serial.println("Initializing bot...");
  Serial.println("Starting integrated obstacle avoidance mode.");
  resetAllEncoders();
}

// --- Main Loop (Runs continuously after setup()) ---
void loop() {
  delay(100);
  digitalWrite(ULTRASONIC_TRIG_PIN, LOW);
  delayMicroseconds(2);
  // Read IR sensor values first to check for low-lying obstacles
  readIRSensors();
  
  if (detectLowObstacle()) {
      Serial.println("Low-lying obstacle detected by IR! Reversing.");
      reverse(REVERSE_SPEED, REVERSE_DURATION);
  } else {
      // If no IR obstacle, check the ultrasonic sensor for obstacles ahead
      //int currentDistanceCM = sonar.ping_cm();
      int currentDistanceCM = scan_sensor();
      
      if (currentDistanceCM == 0 || currentDistanceCM > 400) {
          // 0 means timeout (no obstacle detected), assume a safe path
          // > 400 is the max range, also assume safe
          Serial.println("Path clear, moving forward.");
          moveForward(FORWARD_SPEED);
      } else if (currentDistanceCM < AVOID_DISTANCE_CM) {
          Serial.println("Obstacle detected by Ultrasonic! Initiating scan.");
          stopAllMotors();
          delay(500);
          scanEnvironment();
      } else {
          Serial.println("Path clear, moving forward.");
          moveForward(FORWARD_SPEED);
      }
  }
}

// -----------------------------------------------------------------------------
// --- Helper Functions ---
// -----------------------------------------------------------------------------

void stopAllMotors() {
  analogWrite(MOTOR_C_ENA_PIN, 0);
  analogWrite(MOTOR_A_ENB_PIN, 0);
  Serial.println("All motors are stopped");
  resetAllEncoders();
}

void moveForward(int speed) {
  digitalWrite(MOTOR_A_IN3_PIN, HIGH);
  digitalWrite(MOTOR_A_IN4_PIN, LOW);
  analogWrite(MOTOR_A_ENB_PIN, speed);

  digitalWrite(MOTOR_C_IN1_PIN, HIGH);
  digitalWrite(MOTOR_C_IN2_PIN, LOW);
  analogWrite(MOTOR_C_ENA_PIN, speed);
  updateAllEncoderValues();
}

void reverse(int speed, int duration) {
  // Set both motors to reverse direction
  digitalWrite(MOTOR_A_IN3_PIN, LOW);
  digitalWrite(MOTOR_A_IN4_PIN, HIGH);
  analogWrite(MOTOR_A_ENB_PIN, speed);

  digitalWrite(MOTOR_C_IN1_PIN, LOW);
  digitalWrite(MOTOR_C_IN2_PIN, HIGH);
  analogWrite(MOTOR_C_ENA_PIN, speed);

  delay(duration);
  stopAllMotors(); // Stop after reversing
}

void turnLeft(int speed) {
  digitalWrite(MOTOR_A_IN3_PIN, LOW); // Left motor reverse
  digitalWrite(MOTOR_A_IN4_PIN, HIGH);
  analogWrite(MOTOR_A_ENB_PIN, speed);

  digitalWrite(MOTOR_C_IN1_PIN, HIGH); // Right motor forward
  digitalWrite(MOTOR_C_IN2_PIN, LOW);
  analogWrite(MOTOR_C_ENA_PIN, speed);
  
  delay(1000);
  stopAllMotors();
}

void turnRight(int speed) {
  digitalWrite(MOTOR_A_IN3_PIN, HIGH); // Left motor forward
  digitalWrite(MOTOR_A_IN4_PIN, LOW);
  analogWrite(MOTOR_A_ENB_PIN, speed);

  digitalWrite(MOTOR_C_IN1_PIN, LOW); // Right motor reverse
  digitalWrite(MOTOR_C_IN2_PIN, HIGH);
  analogWrite(MOTOR_C_ENA_PIN, speed);
  
  delay(1000);
  stopAllMotors();
}

void setServoAngle(int angle) {
  myServo.write(angle);
  delay(100);
}

void updateAllEncoderValues() {
  encoderC_steps = Encoder_C.read();
  encoderC_revolutions = (float)encoderC_steps / TICKS_PER_REVOLUTION;
  encoderC_degrees = encoderC_revolutions * 360.0;
}

void resetAllEncoders() {
  Encoder_C.write(0);
  Serial.println("All encoder steps have been reset to 0.");
}

// -----------------------------------------------------------------------------
// --- IR Sensor Functions ---
// -----------------------------------------------------------------------------

/**
 * @brief Reads the digital values from all 6 IR line sensors.
 */
void readIRSensors() {
  for (int i = 0; i < 6; i++) {
    irValues[i] = digitalRead(irPins[i]);
    Serial.print(irValues[i]);
    Serial.print(" ");
  }

  Serial.println();

  delay(100); // Small 
}

/**
 * @brief Checks if any IR sensor detects a low-lying obstacle.
 * @return true if an obstacle is detected, false otherwise.
 */
bool detectLowObstacle() {
  for (int i = 0; i < NUM_IR_SENSORS; i++) {
    // Check if the sensor value is the digital state for an obstacle (typically LOW).
    if (irSensorValues[i] == HIGH) {
      return true;
    }
  }
  return false;
}

// -----------------------------------------------------------------------------
// --- Ultrasonic/Scan Functions ---
// -----------------------------------------------------------------------------
/**
 * @brief Scans the environment with the ultrasonic sensor to find the clearest path.
 */
void scanEnvironment() {
  int center_angle = 90;
  int half_scan_range = SCAN_ANGLE_RANGE / 2;
  int clear_angle = -1;
  int max_distance = 0;

  for (int angle = center_angle - half_scan_range; angle <= center_angle + half_scan_range; angle += SCAN_STEP) {
    setServoAngle(angle);
    delay(300); // Give servo time to move

    // int distance = sonar.ping_cm();
    int distance = scan_sensor();
    if (distance == 0 || distance > 400) { // If ping fails or is out of range, assume a far distance
      distance = 0; 
    }
    
    Serial.print("Angle: ");
    Serial.print(angle);
    Serial.print(", Distance: ");
    Serial.print(distance);
    Serial.println(" cm");

    if (distance > AVOID_DISTANCE_CM && distance > max_distance) {
      max_distance = distance;
      clear_angle = angle;
    }
  }

  setServoAngle(center_angle); // Return to center
  delay(300);

  if (clear_angle == -1) {
    Serial.println("No clear path found in scan, backing up and turning.");
    reverse(REVERSE_SPEED, REVERSE_DURATION);
    turnLeft(TURN_SPEED, 1000);
  } else {
    Serial.print("Clearest path at angle: ");
    Serial.print(clear_angle);
    Serial.print(" degrees with distance ");
    Serial.print(max_distance);
    Serial.println(" cm");

    if (clear_angle < 90) {
      Serial.println("Turning left.");
      turnLeft(TURN_SPEED, 1000);
    } else if (clear_angle > 90) {
      Serial.println("Turning right.");
      turnRight(TURN_SPEED, 1000);
    } else {
      Serial.println("Path clear after scan, moving forward.");
      moveForward(FORWARD_SPEED);
    }
  }
}

int scan_sensor() {
  while(1) {
    digitalWrite(ULTRASONIC_TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(ULTRASONIC_TRIG_PIN, LOW);
    long duration = pulseIn(ULTRASONIC_ECHO_PIN, HIGH);
    delay(500);
    int distance = duration * (0.034 / 2); // Sound speed in cm/micros = 0.034 cm/us
    return distance;
  }
}
