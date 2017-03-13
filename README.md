# Jython talk

## Usages

```
alias jython-show-usages='xdg-open https://en.wikipedia.org/wiki/Jython
xdg-open https://en.wikipedia.org/wiki/Jython
```

## Install Jython

```
curl -O http://search.maven.org/remotecontent?filepath=org/python/jython-installer/2.7.0/jython-installer-2.7.0.jar
java -jar jython-installer-2.7.0.jar
```

## Use python code at jython

```
print 'Hello World!'
x = 'PythonVigo'
print 'Hello ' + x
```

## Performance

This is an extremly bad test, it's just to speak about performance.

```
time python2.7 fib35.py
# real    0m5.010s
time jython fib35.py
# real    0m5.890s
time pypy fib35.py
# real    0m0.900s

time python2.7 fib40.py
# real    0m55.441s
time jython fib40.py
# real    0m46.397s
time pypy fib35.py
# real    0m8.392s
```

## Use Java code from jython (also in real time)

```
from java.lang import System
System.out.println("Hello PythonVigo");
System.out.println("Hello " + x);
dir()

from java.util import Vector
v = Vector()
v.add('aaa')
v.add('bbb')
for val in v:
    print val

dir(v)
quit()
```

## Embed Jython code at Java

```
javac -cp .:jython.jar SimpleEmbedded.java
java -cp .:jython.jar SimpleEmbedded
```

Now dinamically:

```
javac -cp .:jython.jar SimpleEmbeddedFile.java
java -cp .:jython.jar SimpleEmbeddedFile
```

Change `hello.py` and execute again:

```
java -cp .:jython.jar SimpleEmbeddedFile
```
