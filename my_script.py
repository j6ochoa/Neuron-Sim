from my_module import classes
from my_module import functions

# adding current, then shows natural decay
neuron = classes.Neuron()
neuron.add_current(1.4)
for x in range(20):
    neuron.decay()
    neuron.history.append(neuron.voltage)
functions.plot(neuron)

# current clamp experiment (1 nA for 10ms)
neuron = classes.Neuron()
functions.current_clamp(neuron)
functions.plot(neuron)

# current clamp experiment (.3 nA for 10ms)
neuron = classes.Neuron()
functions.current_clamp(neuron, amt_current=0.3, amt_time=10)
functions.plot(neuron)

# adding current, then shows natural decay
neuron = classes.Neuron()
functions.current_clamp(neuron, amt_current=0.3, amt_time=5)
functions.current_clamp(neuron, amt_current=0, amt_time=20)
functions.plot(neuron)

print('Success!')