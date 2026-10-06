"""
Testing model for an RC circuit
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

from neuron import plotting


def run() -> None:
	R = 50
	C = 2e-6
	frequency = 1000

	t = np.linspace(0, 3 * (1 / frequency), 1000)
	signal = (sp.signal.square(2 * np.pi * frequency * t, duty=0.5) + 1) / 2
	vc = (R * C) ** (-1) * np.exp(-1 * t / (R * C))

	dt = t[1] - t[0]
	response = np.convolve(signal, vc, mode="full")[: len(t)] * dt

	plotting.rc(t, response)
	plt.show()


if __name__ == "__main__":
	run()
