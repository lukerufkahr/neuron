from neuron.models import lif, projectile, pulse, rc

MODELS = {
	"projectile": projectile.run,
	"pulse": pulse.run,
	"rc": rc.run,
	"lif": lif.run,
}
