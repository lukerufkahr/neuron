from collections.abc import Callable

import numpy as np


def euler(
	f: Callable[[float, np.ndarray], np.ndarray],
	y0: np.ndarray,
	t: np.ndarray,
	reset: Callable[[np.ndarray], np.ndarray] | None = None,
) -> np.ndarray:
	y = np.empty((len(t), *np.shape(y0)))
	y[0] = y0
	for i in range(1, len(t)):
		dt = t[i] - t[i - 1]
		y[i] = y[i - 1] + f(t[i - 1], y[i - 1]) * dt
		if reset is not None:
			y[i] = reset(y[i])
	return y


if __name__ == "__main__":
	print("cannot be run directly")
