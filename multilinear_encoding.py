# This file defines a skeleton MLE class.
# Notice that this is TOTALLY insecure in practice, I'm not even attempting to hide values.
# This framework, or one like it, will be fleshed out with a scheme like 
# Coron et. al. '13, https://eprint.iacr.org/2013/183.pdf

# TODO: Include __mul__, __add__, __sub__, reference to parent class?
# Not clear how this will phase out.
class MLE_ENC_ELEM:
	def __init__( self, x, S ):
		self.x = x
		self.S = S
	def __repr__( self ):
		return "Enc_{" + repr( self.S )[5:-2] + "}( " + repr( self.x ) + " )"

class MLE_dummy:
	def __init__( self, full ):
		self.full = full
	def encode( self, x, S ):
		assert S.issubset( self.full )
		return MLE_ENC_ELEM( x, S )
	def add( self, e1, e2 ):
		assert e1.S == e2.S
		return MLE_ENC_ELEM( e1.x + e2.x, e1.S )
	def sub( self, e1, e2 ):
		# For now, just defined in terms of add.
		return self.add( e1, MLE_ENC_ELEM( -1 * e2.x, e2.S ) )
	def mul( self, e1, e2 ):
		assert len( e1.S & e2.S ) > 0
		return MLE_ENC_ELEM( e1.x * e2.x, e1.S | e2.S )
	def zerotest( self, e ):
		assert e.S == self.full
		return e.x == 0

# TODO: Base class?
# TODO: Decorator based Wrapper around integer based MLEs to provide translation from arbitrary keys in full


mle = MLE_dummy( set(range(10)) )

X = mle.encode( 3, set([2,3]) )
Y = mle.encode( 2, set([2,3]) )
Z = mle.encode( 0, set([0,1,2,3,4,5,6,7,8,9]) )

print X, Y 
print mle.add( X, Y )
print mle.sub( X, Y )
print mle.mul( X, Y )
print mle.zerotest( Z )
