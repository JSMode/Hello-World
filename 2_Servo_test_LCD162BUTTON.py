  #!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#  2_Servo_Test_LCD162BUTTON.py
#  16x2 LCD Test Script [& 16 CH PWM Controller Test]
#
# Author : Matt Hawkins
# Date   : 06/04/2015
             # edit by JSMode Jan 2017
#
# http://www.raspberrypi-spy.co.uk/
#
# Copyright 2015 Matt Hawkins
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Note from editor -
# This program combines a few functions into one, to make a semi-challenging 
# experiment for the intermediate level beginner.  It involves some electrical
# knowlege and skill.  I know maybe 2% of Python and I'm gifted with electric
# -al skills.  You can do it! ~J
#
# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#--------------------------------------

# The wiring for the LCD is as follows:
# 1 : GND
# 2 : 5V
# 3 : Contrast (0-5V)*
# 4 : RS (Register Select)
# 5 : R/W (Read Write)       - GROUND THIS PIN
# 6 : Enable or Strobe
# 7 : Data Bit 0             - NOT USED
# 8 : Data Bit 1             - NOT USED
# 9 : Data Bit 2             - NOT USED
# 10: Data Bit 3             - NOT USED
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD Backlight +5V**
# 16: LCD Backlight GND

#import
from __future__ import division
import RPi.GPIO as GPIO
import time
import Adafruit_PCA9685
import os

buttonPin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN)
GPIO.setup(18,GPIO.IN)


# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685(0x40)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Define GPIO to LCD mapping
LCD_RS = 26
LCD_E  = 19
LCD_D4 = 13
LCD_D5 = 6
LCD_D6 = 5
LCD_D7 = 11


# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

 
def main():
 

  # Initialise display
  lcd_init()
  print('Refer to 16x2 LCD for servo status, press Ctrl-C to quit...')
  while True:
    #take a reading
    input = GPIO.input(17)

    
    #if the last reading was low and this one high, print
    if (input):
      pwm.set_pwm(2, 0, 600)
      pwm.set_pwm(3, 0, 0)
      time.sleep(.05)
      pwm.set_pwm(2, 0, 0)
      pwm.set_pwm(3, 0, 600)
      time.sleep(.05)
      pwm.set_pwm(2, 0, 600)
      pwm.set_pwm(3, 0, 0)
      time.sleep(.05)
      pwm.set_pwm(3, 0, 600)
      time.sleep(.05)
      lcd_string("Servo [1]",LCD_LINE_1)
      lcd_string("0   Degrees",LCD_LINE_2)
      pwm.set_pwm(0, 0, 150)
      time.sleep(.5)
      lcd_string("Servo  1 ",LCD_LINE_1)
      time.sleep(.5)
      pwm.set_pwm(2, 0, 600)
      pwm.set_pwm(3, 0, 0)
      time.sleep(.05)
      pwm.set_pwm(2, 0, 0)
      pwm.set_pwm(3, 0, 600)
      time.sleep(.05)
      pwm.set_pwm(2, 0, 600)
      pwm.set_pwm(3, 0, 0)
      time.sleep(.05)
      pwm.set_pwm(3, 0, 600)
      time.sleep(.05)
      lcd_string("Servo [2]",LCD_LINE_1)
      lcd_string("0   Degrees",LCD_LINE_2)
      pwm.set_pwm(1, 0, 150)
      time.sleep(.5)
      lcd_string("Servo  2 ",LCD_LINE_1)
      time.sleep(.5)
      pwm.set_pwm(2, 0, 600)
      pwm.set_pwm(3, 0, 0)
      time.sleep(.05)
      pwm.set_pwm(2, 0, 0)
      pwm.set_pwm(3, 0, 600)
      time.sleep(.05)
      pwm.set_pwm(2, 0, 600)
      pwm.set_pwm(3, 0, 0)
      time.sleep(.05)
      pwm.set_pwm(3, 0, 600)
      time.sleep(.05)
      lcd_string("Servo [1]",LCD_LINE_1)
      lcd_string("180 Degrees",LCD_LINE_2)
      pwm.set_pwm(0, 0, 600)
      time.sleep(.5)
      lcd_string("Servo  1 ",LCD_LINE_1)
      time.sleep(.5)
      pwm.set_pwm(2, 0, 600)
      pwm.set_pwm(3, 0, 0)
      time.sleep(.05)
      pwm.set_pwm(2, 0, 0)
      pwm.set_pwm(3, 0, 600)
      time.sleep(.05)
      pwm.set_pwm(2, 0, 600)
      pwm.set_pwm(3, 0, 0)
      time.sleep(.05)
      pwm.set_pwm(3, 0, 600)
      time.sleep(.05)
      lcd_string("Servo [2]",LCD_LINE_1)
      lcd_string("180 Degrees",LCD_LINE_2)
      pwm.set_pwm(1, 0, servo_max)
      time.sleep(.5)
      lcd_string("Servo  2 ",LCD_LINE_1)
      time.sleep(.5)
      pwm.set_pwm(2, 0, 600)
      pwm.set_pwm(3, 0, 0)
      time.sleep(.05)
      pwm.set_pwm(2, 0, 0)
      pwm.set_pwm(3, 0, 600)
      time.sleep(.05)
      pwm.set_pwm(2, 0, 600)
      pwm.set_pwm(3, 0, 0)
      time.sleep(.05)
      pwm.set_pwm(3, 0, 600)
      time.sleep(.05)
      lcd_string("Servo [1]",LCD_LINE_1)
      lcd_string("0   Degrees",LCD_LINE_2)
      pwm.set_pwm(0, 0, 150)
      time.sleep(.5)
      lcd_string("Servo  1 ",LCD_LINE_1)
      time.sleep(.5)
      pwm.set_pwm(2, 0, 600)
      pwm.set_pwm(3, 0, 0)
      time.sleep(.05)
      pwm.set_pwm(2, 0, 0)
      pwm.set_pwm(3, 0, 600)
      time.sleep(.05)
      pwm.set_pwm(2, 0, 600)
      pwm.set_pwm(3, 0, 0)
      time.sleep(.05)
      pwm.set_pwm(3, 0, 600)
      time.sleep(.05)
      lcd_string("Servo [2]",LCD_LINE_1)
      lcd_string("0   Degrees",LCD_LINE_2)
      pwm.set_pwm(1, 0, 150)
      time.sleep(.5)
      lcd_string("Servo  2 ",LCD_LINE_1)
      time.sleep(.5)
      pwm.set_pwm(2, 0, 600)
      pwm.set_pwm(3, 0, 0)
      time.sleep(.05)
      pwm.set_pwm(2, 0, 0)
      pwm.set_pwm(3, 0, 600)
      time.sleep(.05)
      pwm.set_pwm(2, 0, 600)
      pwm.set_pwm(3, 0, 0)
      time.sleep(.05)
      pwm.set_pwm(3, 0, 600)
      time.sleep(.05)
      lcd_string("Servo [1]",LCD_LINE_1)
      lcd_string("180 Degrees",LCD_LINE_2)
      pwm.set_pwm(0, 0, 600)
      time.sleep(.5)
      lcd_string("Servo  1 ",LCD_LINE_1)
      time.sleep(.5)
      pwm.set_pwm(2, 0, 600)
      pwm.set_pwm(3, 0, 0)
      time.sleep(.05)
      pwm.set_pwm(2, 0, 0)
      pwm.set_pwm(3, 0, 600)
      time.sleep(.05)
      pwm.set_pwm(2, 0, 600)
      pwm.set_pwm(3, 0, 0)
      time.sleep(.05)
      pwm.set_pwm(3, 0, 600)
      time.sleep(.05)
      lcd_string("Servo [2]",LCD_LINE_1)
      lcd_string("180 Degrees",LCD_LINE_2)
      pwm.set_pwm(1, 0, servo_max)
      time.sleep(.5)
      lcd_string("Servo  2 ",LCD_LINE_1)
      time.sleep(.5)
      lcd_string("     JSMode",LCD_LINE_1)
      lcd_string("      2017",LCD_LINE_2)
      pwm.set_pwm(1, 0, servo_min)
      pwm.set_pwm(0, 0, servo_min)
      time.sleep(.3)
      pwm.set_pwm(1, 0, 200)
      pwm.set_pwm(0, 0, 200)
      time.sleep(.3)
      pwm.set_pwm(1, 0, 233)
      pwm.set_pwm(0, 0, 233)
      time.sleep(.3)
      pwm.set_pwm(1, 0, 290)
      pwm.set_pwm(0, 0, 290)
      time.sleep(.3)
      pwm.set_pwm(1, 0, 350)
      pwm.set_pwm(0, 0, 350)
      time.sleep(.3)
      pwm.set_pwm(1, 0, 400)
      pwm.set_pwm(0, 0, 400)
      time.sleep(.3)
      pwm.set_pwm(1, 0, 500)
      pwm.set_pwm(0, 0, 500)
      time.sleep(.3)
      pwm.set_pwm(1, 0, 600)
      pwm.set_pwm(0, 0, 600)
      time.sleep(.3)
      pwm.set_pwm(1, 0, 350)
      pwm.set_pwm(0, 0, 350)
      time.sleep(.3)
      
      
    else:
      lcd_string("Servo Standby",LCD_LINE_1)
      lcd_string("Push Button.",LCD_LINE_2)
      pwm.set_pwm(2, 0, 600)
      pwm.set_pwm(3, 0, 0)
      time.sleep(.00001)
      lcd_string("Servo Standby",LCD_LINE_1)
      lcd_string("Push Button .",LCD_LINE_2)
      time.sleep(.00001)
      pwm.set_pwm(2, 0, 0)
      pwm.set_pwm(3, 0, 0) 
      lcd_string("Servo Standby",LCD_LINE_1)
      lcd_string("Push Button  .",LCD_LINE_2)
      time.sleep(.00001)
      lcd_string("Servo Standby",LCD_LINE_1)
      lcd_string("Push Button   .",LCD_LINE_2)
      time.sleep(.00001)
      pwm.set_pwm(2, 0, 0)
      pwm.set_pwm(3, 0, 600) 
      lcd_string("Servo Standby",LCD_LINE_1)
      lcd_string("Push Button    .",LCD_LINE_2)
      time.sleep(.00001)
      lcd_string("Servo Standby",LCD_LINE_1)
      lcd_string("Push Button   .",LCD_LINE_2)
      time.sleep(.00001)
      pwm.set_pwm(2, 0, 0)
      pwm.set_pwm(3, 0, 0) 
      lcd_string("Servo Standby",LCD_LINE_1)
      lcd_string("Push Button  .",LCD_LINE_2)
      time.sleep(.00001)
      lcd_string("Servo Standby",LCD_LINE_1)
      lcd_string("Push Button .",LCD_LINE_2)
      time.sleep(.00001)
def lcd_init():
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  GPIO.setup(LCD_E, GPIO.OUT)  # E
  GPIO.setup(LCD_RS, GPIO.OUT) # RS
  GPIO.setup(LCD_D4, GPIO.OUT) # DB4
  GPIO.setup(LCD_D5, GPIO.OUT) # DB5
  GPIO.setup(LCD_D6, GPIO.OUT) # DB6
  GPIO.setup(LCD_D7, GPIO.OUT) # DB7
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command

  GPIO.output(LCD_RS, mode) # RS

  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin
  lcd_toggle_enable()

  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin
  lcd_toggle_enable()

def lcd_toggle_enable():
  # Toggle enable
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)

def lcd_string(message,line):
  # Send string to display



  message = message.ljust(LCD_WIDTH," ")

  lcd_byte(line, LCD_CMD)

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)


if __name__ == '__main__':

  try:
      main()
  except:
      pass
   
  finally: 
    lcd_byte(0x01, LCD_CMD)
    lcd_string("All Servos",LCD_LINE_1)
    lcd_string("Shutting Down",LCD_LINE_2)
    pwm.set_pwm(2, 0, 600)
    time.sleep(.5)
    pwm.set_pwm(0, 0, 165)
    time.sleep(0)
    pwm.set_pwm(2, 0, 0)
    time.sleep(0)
    pwm.set_pwm(3, 0, 600)
    lcd_string("Shutting Down.",LCD_LINE_2)
    time.sleep(.5)
    lcd_string("Shutting Down .",LCD_LINE_2)
    pwm.set_pwm(1, 0, 160)
    time.sleep(0)
    pwm.set_pwm(3, 0, 0)
    time.sleep(0)
    pwm.set_pwm(2, 0, 600)
    time.sleep(.5)
    lcd_string("Shutting Down  .",LCD_LINE_2)
    pwm.set_pwm(0, 0, 340)
    time.sleep(0)
    pwm.set_pwm(2, 0, 0)
    time.sleep(0)
    pwm.set_pwm(3, 0, 600)
    time.sleep(.2)
    lcd_string("Shutting Down .",LCD_LINE_2)
    pwm.set_pwm(2, 0, 600)
    time.sleep(0)
    pwm.set_pwm(3, 0, 0)
    time.sleep(.2)
    lcd_string("Shutting Down.",LCD_LINE_2)
    pwm.set_pwm(2, 0, 0)
    time.sleep(0)
    pwm.set_pwm(3, 0, 600)
    time.sleep(.2)
    lcd_string("Shutting Down .",LCD_LINE_2)
    pwm.set_pwm(2, 0, 600)
    time.sleep(0)
    pwm.set_pwm(3, 0, 0)
    time.sleep(.2)
    lcd_string("Shutting Down  .",LCD_LINE_2)
    time.sleep(.2)
    pwm.set_pwm(1, 0, servo_max)
    time.sleep(0)
    pwm.set_pwm(0, 0, 600)
    time.sleep(0)
    lcd_string("Servo Shut",LCD_LINE_1)
    lcd_string("Down Successful!",LCD_LINE_2)
    time.sleep(1)
    pwm.set_pwm(2, 0, 600)
    pwm.set_pwm(3, 0, 0)
    time.sleep(.05)
    pwm.set_pwm(2, 0, 0)
    pwm.set_pwm(3, 0, 600)
    time.sleep(.05)
    pwm.set_pwm(2, 0, 600)
    pwm.set_pwm(3, 0, 0)
    time.sleep(.05)
    pwm.set_pwm(2, 0, 0)
    pwm.set_pwm(3, 0, 600)
    time.sleep(.05)
    pwm.set_pwm(2, 0, 600)
    pwm.set_pwm(3, 0, 0)
    time.sleep(.05)
    pwm.set_pwm(2, 0, 0)
    pwm.set_pwm(3, 0, 600)
    time.sleep(.05)
    pwm.set_pwm(2, 0, 600)
    pwm.set_pwm(3, 0, 0)
    time.sleep(.05)
    pwm.set_pwm(2, 0, 0)
    pwm.set_pwm(3, 0, 600)
    time.sleep(.05)
    pwm.set_pwm(2, 0, 600)
    pwm.set_pwm(3, 0, 0)
    time.sleep(.05)
    pwm.set_pwm(2, 0, 0)
    pwm.set_pwm(3, 0, 600)
    time.sleep(.05)
    pwm.set_pwm(2, 0, 600)
    pwm.set_pwm(3, 0, 0)
    time.sleep(.05)
    pwm.set_pwm(2, 0, 0)
    pwm.set_pwm(3, 0, 600)
    time.sleep(.05)
    pwm.set_pwm(2, 0, 600)
    pwm.set_pwm(3, 0, 0)
    time.sleep(.05)
    pwm.set_pwm(3, 0, 600)
    time.sleep(.05)
    lcd_string(" Servos  Online",LCD_LINE_1)
    lcd_string("   [1]    [2]",LCD_LINE_2)
    
    print "All Servos Shut Down"
    GPIO.cleanup()
