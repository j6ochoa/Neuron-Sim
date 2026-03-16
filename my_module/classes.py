class Neuron:
    """
    Simulates model of a neuron, using V=IR for voltage calculations

    Attributes
    ------
    voltage: float
        the current membrane potential (in mV)
    input_resistance: float
        membrane resistance (in megaohms)
        default is -10.0
    threshold: float
        the threshold for an action potential (in mV)
        default is -55.0
    history: list
        keeps track of voltage changes of a neuron over time
    """

    # voltage starts at rest (-70mV)
    def __init__(self, input_resistance=10.0, threshold=-55.0):
        self.voltage = -70.0
        self.input_resistance = input_resistance
        self.threshold = threshold
        self.history = [self.voltage]

    # simulates the input of current, translates into a voltage change in membrane potential
    def add_current(self, amount):
        """
        Simulates the input of current, translates into a voltage change in membrane potential using V=IR
        when the converted voltage passes the threshold, spike is called (allowing for an Action Potential)

        Parameters
        ------
        amount: float
            the amount of current to be injected (in nA)

        """
        self.voltage += amount * self.input_resistance

        if self.voltage >= self.threshold:
            self.voltage = self.threshold
            self.spike()
        else:
            self.history.append(self.voltage)

    def check_voltage(self):
        """
        Checks the current voltage of the neuron

        Returns
        ------
        a str with current voltage
        """
        return str(self.voltage)

    # Decays voltage to rest
    def decay(self):
        """
        Simulates natural leak of current in a neuron
        when the voltage is above rest, decays the voltage by 5%
        """
        if self.voltage > -70.0:
            change = self.voltage + 70.0  # accounts for negative numbers
            self.voltage = self.voltage - (change * 0.05)
            
            # cant go under -70
            if self.voltage < -70.0:
                self.voltage = -70.0
            
    # This is the Action Potential
    def spike(self):
        """
        Simulates the Action Potential by logging a set sequence of voltage changes
        """
        # print("Voltage: " + self.check_voltage())
        # print("Threshold Reached, Spike Initiated")

        self.history.extend(
            [30, -80, -70]
        )
        self.voltage = -70.0
