import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from matplotlib.figure import Figure


def animate_trajectories(
	t: np.ndarray,
	v0_scatter: float,
	z_scatter: np.ndarray,
	v0_line: float,
	z_line: np.ndarray,
) -> tuple[Figure, animation.FuncAnimation]:

	fig, ax = plt.subplots()

	scat = ax.scatter(t[0], z_scatter[0], c="b", s=5, label=f"v0 = {v0_scatter} m/s")
	line2 = ax.plot(t[0], z_line[0], label=f"v0 = {v0_line} m/s")[0]
	ax.set(xlim=(0, 3), ylim=(-4, 10), xlabel="Time [s]", ylabel="Z [m]")
	ax.legend()

	def update(frame):
		# for each frame, update the data stored on each artist.
		x = t[:frame]
		y = z_scatter[:frame]
		# update the scatter plot:
		data = np.stack([x, y]).T
		scat.set_offsets(data)
		# update the line plot:
		line2.set_xdata(t[:frame])
		line2.set_ydata(z_line[:frame])
		return (scat, line2)

	ani = animation.FuncAnimation(fig=fig, func=update, frames=len(t), interval=30)
	return fig, ani


def animate_pulse(t: np.ndarray, pulse: np.ndarray) -> tuple[Figure, animation.FuncAnimation]:
	fig, ax = plt.subplots()
	line = ax.plot(t[0], pulse[0])[0]
	ax.set(xlim=(0, (2 / 1000)), ylim=(-2, 2))

	def update(frame):
		x = t[:frame]
		y = pulse[:frame]
		data = np.stack([x, y]).T
		line.set_xdata(t[:frame])
		line.set_ydata(y[:frame])

	ani = animation.FuncAnimation(fig=fig, func=update, frames=len(t), interval=1)
	return fig, ani


def animate_rc(t: np.ndarray, response: np.ndarray) -> tuple[Figure, animation.FuncAnimation]:
	fig, ax = plt.subplots()
	line = ax.plot(t[0], response[0])[0]
	ax.set(xlim=(0, 10), ylim=(-2, 2))

	def update(frame):
		x = t[:frame]
		y = response[:frame]
		data = np.stack([x, y]).T
		line.set_xdata(t[:frame])
		line.set_ydata(y[:frame])

	ani = animation.FuncAnimation(fig=fig, func=update, frames=len(t), interval=0.001)
	return fig, ani
