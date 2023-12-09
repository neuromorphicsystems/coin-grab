import actuator
import neuromorphic_drivers as nd

grabber = actuator.Grabber(port="/dev/cu.usbmodem14201")

configuration = nd.prophesee_evk4.Configuration(
    biases=nd.prophesee_evk4.Biases(
        diff_off=170,
        diff_on=130,
    )
)

with nd.open(configuration=configuration) as device:
    for status, packet in device:
        if "dvs_events" in packet:
            events = packet["dvs_events"]
            # events is a structured numpy array
            # with dtype [("t", "<u8"), ("x", "<u2"), ("y", "<u2"), ("on", "?")])
            #
            # call grabber.close() at the right time!
