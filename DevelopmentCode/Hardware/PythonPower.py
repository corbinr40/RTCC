import smbus
import time

# BUS VOLTAGE REGISTER (R)
_REG_BUSVOLTAGE             = 0x02

# CALIBRATION REGISTER (R/W) #Required
_REG_CALIBRATION            = 0x05

class BusVoltageRange:
    """Constants for ``bus_voltage_range``"""
    RANGE_16V               = 0x00      # set bus voltage range to 16V
    RANGE_32V               = 0x01      # set bus voltage range to 32V (default)


class INA219:
    def __init__(self, i2c_bus=1, addr=0x40):
        self.bus = smbus.SMBus(i2c_bus);
        self.addr = addr

        # Set chip to known config values to start #Required
        self._cal_value = 0

    def read(self,address):
        data = self.bus.read_i2c_block_data(self.addr, address, 2)
        return ((data[0] * 256 ) + data[1])
    
    def write(self,address,data):
        temp = [0,0]
        temp[1] = data & 0xFF
        temp[0] =(data & 0xFF00) >> 8
        self.bus.write_i2c_block_data(self.addr,address,temp)


    def set_calibration_32V_2A(self):

        #Required
        self._cal_value = 4096


        # Set Calibration register to 'Cal' calculated above #Required
        self.write(_REG_CALIBRATION,self._cal_value)



    def getBusVoltage_V(self):
        self.write(_REG_CALIBRATION,self._cal_value)
        self.read(_REG_BUSVOLTAGE)
        return (self.read(_REG_BUSVOLTAGE) >> 3) * 0.004

        
if __name__=='__main__':

    # Create an INA219 instance.
    ina219 = INA219(addr=0x43)
    while True:
        bus_voltage = ina219.getBusVoltage_V()             # voltage on V- (load side)
        p = (bus_voltage - 3)/1.2*100
        if(p > 100):p = 100
        if(p < 0):p = 0

        # INA219 measure bus voltage on the load side. So PSU voltage = bus_voltage + shunt_voltage
        print("Percent:       {:3.0f}%".format(p))
        print("")

        time.sleep(2)
