import matplotlib.pyplot as plt


def current_clamp(neuron, amt_current=1.0, amt_time=10):
    """
    Simulates a current clamp experiment, where a certain amount of current
    is constantly injected for a certain amount of time, allowing us to
    view the voltage freely change. Natural decay is also accounted for.

    Voltage values are logged automatically, and can be plotted later

    Parameters
    ------
    amt_current: float
        amount of current we want to constantly inject
        default is 1.0
    amt_time: int
        how long we want to inject current for
        default is 10
    """
    for time in range(amt_time):
        neuron.add_current(amt_current)
        neuron.decay()

# plots neurons history
def plot(neuron):
    """
    Visualizes a neurons previous voltage changes. Appears as a line plot.
    Voltage is graphed on the y axis, time is on the x axis, there is
    also a dashed line showing the neurons threshold

    Parameters
    ------
    neuron: obj
        neuron whos history we want to plot
    """
    plt.plot(neuron.history)
    plt.ylabel("Voltage (mV)")
    plt.xlabel("Time Increment")
    plt.title("Neuron Simulation")
    plt.grid(True)
    plt.axhline(y=neuron.threshold, color="r", linestyle="dashed", label="Threshold")
    plt.legend()
    plt.show()
