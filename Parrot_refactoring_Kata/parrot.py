from enum import Enum



class Parrot:

    def __init__(self, number_of_coconuts, voltage, nailed):
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed
            
    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])

    def _load_factor(self):
        return 9.0

    def _base_speed(self):
        return 12.0
    

class EuropeanParrot(Parrot):
    def __init__(self, number_of_coconuts, voltage, nailed):
        super().__init__(number_of_coconuts, voltage, nailed)

    def cry(self):
        return "Sqoork!"
    def speed(self):
        return self._base_speed()
    
    

class AfricanParrot(Parrot):
    def __init__(self, number_of_coconuts, voltage, nailed):
     super().__init__(number_of_coconuts, voltage, nailed)

    
    def cry(self):
       return "Sqaark!"
    def speed(self):
        return max(0, self._base_speed() - self._load_factor() * self._number_of_coconuts)

class NorwegianBlueParrot(Parrot):
    def __init__(self, number_of_coconuts, voltage, nailed):
        super().__init__(number_of_coconuts, voltage, nailed)


    def cry(self):
        return "Bzzzzzz" if self._voltage > 0 else "..."
    def speed(self):
        return 0 if self._nailed else self._compute_base_speed_for_voltage(self._voltage)