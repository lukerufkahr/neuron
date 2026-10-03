import matplotlib.pyplot as plt
import numpy as np

from neuron import plotting

G = -9.81


def height(t: np.ndarray, v0: float, g: float = G) -> np.ndarray:
	return g * t**2 / 2 + v0 * t


def run() -> None:
	t = np.linspace(0, 3, 40)

	v0 = 12
	z = height(t, v0)

	v02 = 5
	z2 = height(t, v02)

	# keep a reference to the animation, or it gets garbage collected
	# and stops

	fig, ani = plotting.animate_trajectories(t, v0, z, v02, z2)
	plt.show()


if __name__ == "__main__":
	run()
