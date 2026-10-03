import argparse

import matplotlib

from neuron.models import MODELS


def main() -> None:
	parser = argparse.ArgumentParser(prog="neuron")
	parser.add_argument("model", choices=MODELS, help="model to use")
	args = parser.parse_args()

	matplotlib.use("TkAgg")
	MODELS[args.model]()
