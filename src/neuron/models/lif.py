"""
Leaky Integrate and Fire Neuron Model
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

from neuron import plotting
from neuron.helper import euler

# Constants
I = 2e-9  # noqa: E741
R = 10e6
C = 1e-9
tm = R * C
u_r = -0.065
threshold_V = -0.05
frequency = 10
n_pulses = 2
n_periods = 4


def fire(u: np.ndarray) -> np.ndarray:
	return np.where(u >= threshold_V, u_r, u)


def current(t: float) -> np.ndarray:
	if t >= (n_pulses / frequency):
		signal = np.array([0])
	else:
		signal = I * ((sp.signal.square(2 * np.pi * t * frequency, duty=0.5) + 1) / 2)
	return signal


def membrane(t: float, u: np.ndarray) -> np.ndarray:
	# f(t, u) = (1/C)I(t) - dU/RC
	f = (R / tm) * current(t) - (u - u_r) * (1 / tm)
	return f


def run() -> None:
	t = np.linspace(0, n_periods / frequency, 10000)
	u0 = np.array([u_r])

	u = euler(membrane, u0, t, reset=fire)

	plotting.lif(t, u, threshold_V)
	plt.show()


if __name__ == "__main__":
	run()
