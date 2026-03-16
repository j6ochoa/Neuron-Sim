import classes
import functions

def test_neuron_class():
    # test default vals
    test_neuron = classes.Neuron()
    assert test_neuron.voltage == -70.0
    assert test_neuron.input_resistance == 10.0
    assert test_neuron.threshold == -55.0
    assert test_neuron.history == [-70.0]

    # test non default vals
    test_neuron = classes.Neuron(input_resistance=20.0, threshold=-50.0)
    assert test_neuron.voltage == -70.0
    assert test_neuron.input_resistance == 20.0
    assert test_neuron.threshold == -50.0
    assert test_neuron.history == [-70.0]


def test_add_current():
    test_neuron = classes.Neuron()

    # adding 0 current when it starts at rest
    test_neuron.add_current(0)
    assert test_neuron.voltage == -70.0
    assert test_neuron.history == [-70.0, -70.0]

    # adding a small amount of current
    test_neuron.add_current(0.0000001)
    assert test_neuron.voltage > -70.0
    assert test_neuron.history == [-70.0, -70.0, -69.999999]

    # reset the current for test
    test_neuron = classes.Neuron()
    # adding a large amount of current (should cause an AP and reset voltage to rest)
    test_neuron.add_current(100000)
    assert test_neuron.voltage == -70.0
    assert test_neuron.history == [-70.0, 30.0, -80.0, -70.0]


def test_current_clamp():
    # test with 0
    test_neuron = classes.Neuron()
    functions.current_clamp(test_neuron, amt_current=0.0, amt_time=0)
    assert test_neuron.voltage == -70.0
    assert test_neuron.history == [-70.0]

    # testing history change and with default vals
    test_neuron = classes.Neuron()
    functions.current_clamp(test_neuron)
    assert test_neuron.voltage == -70.0
    assert test_neuron.history == [-70.0, -60.0, 30, -80,
                                   -70.0, -60.0, 30, -80,
                                   -70.0, -60.0, 30, -80,
                                   -70.0, -60.0, 30, -80,
                                   -70.0, -60.0, 30, -80,
                                   -70.0]

    # test with non default vals, large current val
    test_neuron = classes.Neuron()
    functions.current_clamp(test_neuron, amt_current=10.0, amt_time=1)
    assert test_neuron.voltage == -70.0
    assert test_neuron.history == [-70.0, 30, -80, -70]

    # additional test with small current
    test_neuron = classes.Neuron()
    functions.current_clamp(test_neuron, amt_current=0.1, amt_time=5)
    assert test_neuron.voltage == -65.7018378125
    assert test_neuron.history == [-70.0, -69.0,
                                   -68.05, -67.1475,
                                   -66.29012499999999, -65.47561875]


def test_decay():
    # test without current change (already at -70.0, decay should not do anything to voltage)
    test_neuron = classes.Neuron()
    test_neuron.decay()
    assert test_neuron.voltage == -70.0

    # test with a voltage thats not -70.0
    test_neuron = classes.Neuron()
    test_neuron.add_current(1.0)
    test_neuron.decay()
    assert test_neuron.voltage == -60.5

def test_plot():
    #Tests that the plot function executes without errors
    test_neuron = classes.Neuron()
    test_neuron.history = [-70.0]

    try:
        functions.plot(test_neuron)
        plot_passed = True
    except Exception:
        plot_passed = False
        
    assert plot_passed == True