from dataclasses import dataclass


@dataclass
class LIFParams:
	# Constants
	I: float | int = 2e-9  # noqa: E741
	R: float | int = 10e6
	C: float | int = 1e-9
	u_r: float | int = -0.065
	threshold_V: float | int = -0.05
	frequency: float | int = 10.0
	n_pulses: int = 2
	n_periods: int = 4

	@property
	def tm(self) -> float:
		return self.R * self.C
