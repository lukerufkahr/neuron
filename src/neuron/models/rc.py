import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

from neuron import plotting
from neuron.models.pulse import pulse


def run() -> None:
	R = 50
	C = 2e-6
	t = np.linspace(0, 10, 1000)
	signal = sp.signal.square(t * 1 * 2 * np.pi, duty=0.5)
	vc = np.exp(-1 * t)
	response = np.convolve(vc, signal, mode="full")
	fig, ani = plotting.animate_rc(t, response)
	plt.show()


if __name__ == "__main__":
	run()
