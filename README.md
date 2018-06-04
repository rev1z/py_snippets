# py_snippets
useful snippets in python


Final class realisation (can not be inherited from)

<pre><code>
class Final(type):
    def __new__(cls, name, bases, classdict):
        for b in bases:
            if isinstance(b, Final):
                raise TypeError("type '{0}' is not an acceptable base type".format(b.__name__))
        return type.__new__(cls, name, bases, dict(classdict))

class FinalClass(metaclass=Final): pass

class DummyClass(FinalClass): pass 
# will cause TypeError 
</code></pre>
