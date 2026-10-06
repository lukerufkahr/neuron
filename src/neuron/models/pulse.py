"""
test modeling for a pulse waveform
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

from neuron import plotting


def pulse(
	t: np.ndarray,
	amplitude: float,
	frequency: float,
	duty: float,
):
	return amplitude * sp.signal.square(np.pi * frequency * t, duty=duty)


def run() -> None:

	freq = 1000  # HZ
	period = 1 / freq
	amplitude = 1
	duty = 0.5

	t = np.linspace(0, 2 * period, 10000)
	signal = pulse(t, amplitude, freq, duty)
	fig, ani = plotting.animate_pulse(t, signal)
	plt.show()


if __name__ == "__main__":
	run()
