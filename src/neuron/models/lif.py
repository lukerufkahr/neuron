"""
Leaky Integrate and Fire Neuron Model
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

from neuron import plotting
from neuron.helper import euler
from neuron.params import LIFParams


def fire(u: np.ndarray, p: LIFParams) -> np.ndarray:
	return np.where(u >= p.threshold_V, p.u_r, u)


def current(t: float, p: LIFParams) -> np.ndarray:
	if t >= (p.n_pulses / p.frequency):
		signal = np.array([0])
	else:
		signal = p.I * ((sp.signal.square(2 * np.pi * t * p.frequency, duty=0.5) + 1) / 2)
	return signal


def membrane(t: float, u: np.ndarray, p: LIFParams) -> np.ndarray:
	# f(t, u) = (1/C)I(t) - dU/RC
	f = (p.R / p.tm) * current(t, p) - (u - p.u_r) * (1 / p.tm)
	return f


def run(p: LIFParams = LIFParams()) -> None:
	t = np.linspace(0, p.n_periods / p.frequency, 10000)
	u0 = np.array([p.u_r])

	u = euler(lambda ti, ui: membrane(ti, ui, p), u0, t, reset=lambda ui: fire(ui, p))

	plotting.lif(t, u, p.threshold_V)
	plt.show()


if __name__ == "__main__":
	run()
