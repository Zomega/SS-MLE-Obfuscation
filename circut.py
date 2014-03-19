#Implement (acyclic) circuts -- need to support NOT and AND nodes

# Support spice-like serialization and parsing? Initial way to code.

class input:
	def __init__( self, name, circut ):
		self.name = name
		self.circut = circut

		self.circut.register_input( self )
	def compute( self ):
		return self.circut.input_value( self )

class output:
	def __init__( self, name, input, circut ):
		self.name = name
		self.input = input
		self.circut = circut

		self.circut.register_output( self )

	def compute( self ):
		return self.input.compute()

class inverter:
	def __init__( self, input ):
		self.input = input
	def compute( self ):
		return not self.input.compute()

class and_gate:
	def __init__( self, input_1, input_2 ):
		self.input_1 = input_1
		self.input_2 = input_2
	def compute( self ):
		return self.input_1.compute() and self.input_2.compute()


### circut class
class circut:
		def __init__( self ):
			self.names = set()
			self.inputs = {}
			self.outputs = {}

		# Registration functions
		def register_name( self, name ):
			assert name not in self.names
			self.names.add( name )

		def register_input( self, input ):
			self.register_name( input.name )
			self.inputs[ input.name ] = input

		def register_output( self, output ):
			self.register_name( output.name )
			self.outputs[ output.name ] = output

		# For inefficient computation (primarily for testing and verification)
		def compute( self, input_vals ):
			#Validate input_vals keys...
			self.input_vals = input_vals
			self.output_vals = {}
			for output_name in self.outputs:
				output = self.outputs[ output_name ]
				self.output_vals[ output_name ] = output.compute()
			return self.output_vals

		def input_value( self, input ):
			assert self.input_vals
			assert input.name in self.inputs
			return self.input_vals[ input.name ]



# Returns only the pruned circut used to compute output
# The way circuts are implemented, just need to walk backwards.
def pick( circut, output ):
		raise NotImplementedError

# Simplifies the circut, with an emphasis on circut depth.
# There are no hard guarntees.
# TODO: Simplify with arbitrary elements?
def simplify( circut ):
	return circut # For now, do no harm.

c = circut()

i = input( "x0", c )
inv = inverter( i )

output( "y0", inv, c )

test_inputs = {
	"x0": True,
}

print c.compute( test_inputs )