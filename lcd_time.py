#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#  lcd_16x2.py
#  16x2 LCD Test Script
#
# Author : Matt Hawkins
# Date   : 06/04/2015
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





GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

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
  # Main program block
  

  # Initialise display
  lcd_init()
  print('CLOCK DISPLAYED ON 16X2 LCD')
  print('clock started at ' + time.ctime())

  
  while True:

    # Send some test
    lcd_string(time.strftime("%a %b %-d %Y"),LCD_LINE_1)
    lcd_string(time.strftime("  %-I:%M:%S %p"),LCD_LINE_2)
    time.sleep(.1)
    
    if time.strftime("%-I") == "1":
        
        pwm.set_pwm(0, 0, 600)
        pwm.set_pwm(1, 0, 0)
        pwm.set_pwm(2, 0, 0)
        pwm.set_pwm(3, 0, 0)
        pwm.set_pwm(4, 0, 0)
        pwm.set_pwm(5, 0, 0)
        pwm.set_pwm(6, 0, 0)
        pwm.set_pwm(7, 0, 0)
        pwm.set_pwm(8, 0, 0)
        pwm.set_pwm(9, 0, 0)
        pwm.set_pwm(10, 0, 0)
        pwm.set_pwm(11, 0, 0)
        time.sleep(.1)
        
    if time.strftime("%-I") == "2":

        pwm.set_pwm(1, 0, 600)
        pwm.set_pwm(0, 0, 600)
        time.sleep(.1)
        
    if time.strftime("%-I") == "3":

        pwm.set_pwm(2, 0, 600)
        time.sleep(.1)

    if time.strftime("%-I") == "4":

        pwm.set_pwm(3, 0, 600)
        time.sleep(.1)

    if time.strftime("%-I") == "5":

        pwm.set_pwm(4, 0, 600)
        time.sleep(.1)

    if time.strftime("%-I") == "6":

        pwm.set_pwm(5, 0, 600)
        time.sleep(.1)

    if time.strftime("%-I") == "7":

        pwm.set_pwm(6, 0, 600)
        time.sleep(.1)

    if time.strftime("%-I") == "8":

        pwm.set_pwm(7, 0, 600)
        time.sleep(.1)

    if time.strftime("%-I") == "9":

        pwm.set_pwm(8, 0, 600)
        time.sleep(.1)

    if time.strftime("%-I") == "10":

        pwm.set_pwm(9, 0, 600)
        time.sleep(.1)

    if time.strftime("%-I") == "11":

        pwm.set_pwm(10, 0, 600)
        time.sleep(.1)

    if time.strftime("%-I") == "12":

        pwm.set_pwm(11, 0, 600)
        time.sleep(.1)



    
    if  time.strftime("%S") + time.strftime("%M") == "0000":
                                            
        GPIO.output(23,1)
        time.sleep(.75)
        GPIO.output(23,0)
        
    if  time.strftime("%M") + time.strftime("%S") == "3000":
                                            
        GPIO.output(23,1)
        time.sleep(.25)
        GPIO.output(23,0)                                        

    if time.strftime("%S") == "00":
                                            
        GPIO.output(25,1)
        time.sleep(.75)
        GPIO.output(25,0)
    
        
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
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)
    lcd_string("    Goodbye!",LCD_LINE_1)
    lcd_string("* * * *  * * * *",LCD_LINE_2)
    
    GPIO.cleanup()
