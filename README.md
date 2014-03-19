SS-MLE-Based Obfuscation
==================

A python scratchpad with a focus towards implementing a toy cryptographically strong program obfuscation scheme based off Multi-Linear Encodings as described in [Pass, Seth, and Telang 2014](https://eprint.iacr.org/2013/781.pdf).

Please don't use this stuff in production code. It's really not designed for that, it's just a place for me to play around with the ideas. If you'd like to join me, that would be super exciting and I'd love to work with you, but please read [PST'14](https://eprint.iacr.org/2013/781.pdf) at a bare minimum before contributing -- remember, the goal here is a state-of-the-art cryptographic iO obfuscator, not something that is fast enough to use in practice.

Also, if you're ignoring the warning above, keep in mind that this approach cannot obfuscate arbitrary programs, and may or may not even be diO (it's not even totally clear to me at time of writing that diO is even a thing). Specifically, if you are trying to obfuscate something that reduces to a PPT learnable function, you're out of luck, and you should check out the practical (but ultimantly insecure) obfuscation methods already in commercial use. But seriously, this is a toy. Don't use it in practice.

How does this work? (TL;DR)
===========================

[Read the paper.](https://eprint.iacr.org/2013/781.pdf)

But if you REALLY can't, [PST'14](https://eprint.iacr.org/2013/781.pdf) propose obfuscating [branching programs](http://en.wikipedia.org/wiki/Binary_decision_diagram), which can be represented as a multiplication of permutations (invertible matrices) drawn from [S5](http://en.wikipedia.org/wiki/Symmetric_group). These matricies are randomized while maintaining correctness.  A carefully engineered [Multi-Linear Encoding](https://eprint.iacr.org/2013/183.pdf) is then applied to the resulting set of matrices to produce the final program.

There is an additional little step in between where the program is switched against with an arbitrary program so that a Hybrid Argument can be applied to prove security based on SS-MLE (Extended property of MLE, which is strong, but somewhat reasonable), but it looks an awful lot like that shouldn't influence security (It looks to me that it's easy to obtain the unswitched program given the switched one, so presumably the unswitched program can't reveal any more information). The proof is a little technical here, so I need to read a little more before I'll be sure. In the meantime, there's plenty of grindstone coding to be done.

