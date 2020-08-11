def asdf(a,b):
    a=a.split(' ')
    b=b.split(' ')
    c=0
    for i in a:
        for j in b:
            if i==j:
                c+=1
    return c

a='''Python now uses the same ABI whether it’s built in release or debug mode. On Unix, when Python is built in debug mode, it is now possible to load C extensions built in release mode and C extensions built using the stable ABI.

Release builds and debug builds are now ABI compatible: defining the Py_DEBUG macro no longer implies the Py_TRACE_REFS macro, which introduces the only ABI incompatibility. The Py_TRACE_REFS macro, which adds the sys.getobjects() function and the PYTHONDUMPREFS environment variable, can be set using the new ./configure --with-trace-refs build option. (Contributed by Victor Stinner in bpo-36465.)

On Unix, C extensions are no longer linked to libpython except on Android and Cygwin. It is now possible for a statically linked Python to load a C extension built using a shared library Python. (Contributed by Victor Stinner in bpo-21536.)

On Unix, when Python is built in debug mode, import now also looks for C extensions compiled in release mode and for C extensions compiled with the stable ABI. (Contributed by Victor Stinner in bpo-36722.)

To embed Python into an application, a new --embed option must be passed to python3-config --libs --embed to get -lpython3.8 (link the application to libpython). To support both 3.8 and older, try python3-config --libs --embed first and fallback to python3-config --libs (without --embed) if the previous command fails.

Add a pkg-config python-3.8-embed module to embed Python into an application: pkg-config python-3.8-embed --libs includes -lpython3.8. To support both 3.8 and older, try pkg-config python-X.Y-embed --libs first and fallback to pkg-config python-X.Y --libs (without --embed) if the previous command fails (replace X.Y with the Python version).

On the other hand, pkg-config python3.8 --libs no longer contains -lpython3.8. C extensions must not be linked to libpython (except on Android and Cygwin, whose cases are handled by the script); this change is backward incompatible on purpose. '''
a=a.lower()
a=a.split('.')
Search=input("Search:")

b=[]
for i in range(len(a)):
    b.append(asdf(Search,a[i]))
c=[i for i in sorted(zip(b,a),reverse=True)]
for i in c:
    if i[0]==0:
        break
    print(i)
