import time
import struct
import threading

class Input:
    states = {'A':False, 'B':False, 'X':False, 'Y':False, 'LB':False, 'RB':False, 'LT':False, 'RT':False, 'L_Axis_x':0, 'L_Axis_y':0, 'R_Axis_x':0, 'R_Axis_y':0, 'Cross_x':0, 'Cross_y':0}
    def __init__(self, joystick_name):
        self.joystick_name = joystick_name

    def get_key(self, key_name) -> bool:
        return self.states[key_name]
    
    def update(self):
        with open("/dev/input/js0", "rb") as gamepad:
            while True:
                input = gamepad.read(8)
                time, value, digital_analog, index = struct.unpack("<Ihbb", input)  # 4 bytes, 2 bytes, 1 byte, 1 byte
                DA = {'Digital':1, 'Analog':2}
                digital_button = {'A':0, 'B':1, 'X':2, 'Y':3, 'LB':4, 'RB':5}
                analog_button =  {'L_Axis_x':0, 'L_Axis_y':1, 'LT':2, 'R_Axis_x':3, 'R_Axis_y':4, 'RT':5, 'Cross_x':6, 'Cross_y':7}
                if(digital_analog == DA['Digital'] and index == digital_button['A'] and value == 1):
                    print('A ', end='', flush=True)
                
                if(digital_analog == DA['Digital'] and index == digital_button['B'] and value == 1):
                    print('B ', end='', flush=True)
                
                if(digital_analog == DA['Digital'] and index == digital_button['X'] and value == 1):
                    print('X ', end='', flush=True)

                if(digital_analog == DA['Digital'] and index == digital_button['Y'] and value == 1):
                    print('Y ', end='', flush=True)
                
                if(digital_analog == DA['Digital'] and index == digital_button['LB'] and value == 1):
                    print('LB ', end='', flush=True)
                
                if(digital_analog == DA['Digital'] and index == digital_button['RB'] and value == 1):
                    print('RB ', end='', flush=True)

                if(digital_analog == DA['Analog'] and index == analog_button['Cross_x'] and value >= 15000):
                    print('→ ', end='', flush=True)
                
                if(digital_analog == DA['Analog'] and index == analog_button['Cross_x'] and value <= -15000):
                    print('← ', end='', flush=True)
                
                if(digital_analog == DA['Analog'] and index == analog_button['Cross_y'] and value >= 15000):
                    print('↓ ', end='', flush=True)
                
                if(digital_analog == DA['Analog'] and index == analog_button['Cross_y'] and value <= -15000):
                    print('↑ ', end='', flush=True)

                if(digital_analog == DA['Analog'] and index == analog_button['RT'] and value >= 15000):
                    print('RT ', end='', flush=True)

                if(digital_analog == DA['Analog'] and index == analog_button['LT'] and value >= 15000):
                    print('LT ', end='', flush=True)
                
                if(digital_analog == DA['Analog'] and index == analog_button['L_Axis_x'] and value >= 15000):
                    print('⇒ ', end='', flush=True)
                
                if(digital_analog == DA['Analog'] and index == analog_button['L_Axis_x'] and value <= -15000):
                    print('⇐ ', end='', flush=True)

                if(digital_analog == DA['Analog'] and index == analog_button['L_Axis_y'] and value >= 15000):
                    print('⇓ ', end='', flush=True)

                if(digital_analog == DA['Analog'] and index == analog_button['L_Axis_y'] and value <= -15000):
                    print('⇑ ', end='', flush=True)

                if(digital_analog == DA['Analog'] and index == analog_button['R_Axis_x'] and value >= 15000):
                    print('⇉ ', end='', flush=True)
                
                if(digital_analog == DA['Analog'] and index == analog_button['R_Axis_x'] and value <= -15000):
                    print('⇇ ', end='', flush=True)

                if(digital_analog == DA['Analog'] and index == analog_button['R_Axis_y'] and value >= 15000):
                    print('⇊ ', end='', flush=True)

                if(digital_analog == DA['Analog'] and index == analog_button['R_Axis_y'] and value <= -15000):
                    print('⇈ ', end='', flush=True)
                # print("time(ms): {:10d}, value: {:6d}, digital analog: {:1d}, index: {:1d}".format(time, value, digital_analog, index))

                # print(input)

def main():
    input = Input('Xbox Wireless Controller')
    update_task = threading.Thread(target=input.update)
    update_task.start()
    update_task.join()

if __name__ == '__main__':
    main()