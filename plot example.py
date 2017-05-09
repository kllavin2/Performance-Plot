Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
C:\Users\John>python -V
Python 2.7.11

C:\Users\John>python pip list
python: can't open file 'pip': [Errno 2] No such file or directory

C:\Users\John>pip

Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  search                      Search PyPI for packages.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --isolated                  Run pip in an isolated mode, ignoring
                              environment variables and user configuration.
  -v, --verbose               Give more output. Option is additive, and can be
                              used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be
                              used up to 3 times (corresponding to WARNING,
                              ERROR, and CRITICAL logging levels).
  --log <path>                Path to a verbose appending log.
  --proxy <proxy>             Specify a proxy in the form
                              [user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should
                              attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists:
                              (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
  --trusted-host <hostname>   Mark this host as trusted, even though it does
                              not have valid or any HTTPS.
  --cert <path>               Path to alternate CA bundle.
  --client-cert <path>        Path to SSL client certificate, a single file
                              containing the private key and the certificate
                              in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine
                              whether a new version of pip is available for
                              download. Implied with --no-index.

C:\Users\John>pip list
DEPRECATION: The default format will switch to columns in the future. You can use --format=(legacy|columns) (or define
 disable this warning.
pip (9.0.1)
psutil (5.0.0)
pypiwin32 (219)
setuptools (18.2)
wheel (0.29.0)

C:\Users\John>pip install matplotlib
Collecting matplotlib
  Downloading matplotlib-2.0.1-cp27-cp27m-win32.whl (8.5MB)
    100% |################################| 8.5MB 112kB/s
Collecting python-dateutil (from matplotlib)
  Downloading python_dateutil-2.6.0-py2.py3-none-any.whl (194kB)
    100% |################################| 194kB 922kB/s
Collecting numpy>=1.7.1 (from matplotlib)
  Downloading numpy-1.12.1-cp27-none-win32.whl (6.6MB)
    100% |################################| 6.6MB 138kB/s
Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=1.5.6 (from matplotlib)
  Downloading pyparsing-2.2.0-py2.py3-none-any.whl (56kB)
    100% |################################| 61kB 1.1MB/s
Collecting six>=1.10 (from matplotlib)
  Downloading six-1.10.0-py2.py3-none-any.whl
Collecting pytz (from matplotlib)
  Downloading pytz-2017.2-py2.py3-none-any.whl (484kB)
    100% |################################| 491kB 769kB/s
Collecting functools32 (from matplotlib)
  Downloading functools32-3.2.3-2.zip
Collecting cycler>=0.10 (from matplotlib)
  Downloading cycler-0.10.0-py2.py3-none-any.whl
Building wheels for collected packages: functools32
  Running setup.py bdist_wheel for functools32 ... done
  Stored in directory: C:\Users\John\AppData\Local\pip\Cache\wheels\3c\d0\09\cd78d0ff4d6cfecfbd730782a7815a4571cd2cd4d
2ed6e69d9
Successfully built functools32
Installing collected packages: six, python-dateutil, numpy, pyparsing, pytz, functools32, cycler, matplotlib
Successfully installed cycler-0.10.0 functools32-3.2.3.post2 matplotlib-2.0.1 numpy-1.12.1 pyparsing-2.2.0 python-date
util-2.6.0 pytz-2017.2 six-1.10.0

C:\Users\John>python
Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> np
<module 'numpy' from 'C:\Python27\lib\site-packages\numpy\__init__.pyc'>
>>> plt
<module 'matplotlib.pyplot' from 'C:\Python27\lib\site-packages\matplotlib\pyplot.pyc'>
>>> np.array([1,2,3,4,5])
array([1, 2, 3, 4, 5])
>>> x = np.array([1,2,3,4,5])
>>> y = np.array([6,7,8,9,10])
>>> x
array([1, 2, 3, 4, 5])
>>> y
array([ 6,  7,  8,  9, 10])
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x04AB3C10>]
>>> plt.show()
>>> plt.title('MY TITLE', fontsize=22)
<matplotlib.text.Text object at 0x04CB32D0>
>>> plt.xlabel('x-axis')
<matplotlib.text.Text object at 0x048A7E30>
>>> plt.ylabel('y axis', color = 'g')
<matplotlib.text.Text object at 0x04865E90>
>>> plt.show()
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x04E90290>]
>>> plt.title('MY TITLE', fontsize=22)
<matplotlib.text.Text object at 0x04D595B0>
>>> plt.xlabel('x-axis')
<matplotlib.text.Text object at 0x04ADEC70>
>>> plt.ylabel('y axis', color = 'g')
<matplotlib.text.Text object at 0x04D43250>
>>> plt.show()
>>> data = np.genfromtext(r'C:\Users\John\Documents\Kristi\test.csvC:\Users\John\Documents\Kristi\test.csv', delimiter
=',')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'genfromtext'
>>>
>>> data = np.genfromtxt(r'C:\Users\John\Documents\Kristi\test.csvC:\Users\John\Documents\Kristi\test.csv', delimiter=
',')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python27\lib\site-packages\numpy\lib\npyio.py", line 1510, in genfromtxt
    fhd = iter(np.lib._datasource.open(fname, 'rbU'))
  File "C:\Python27\lib\site-packages\numpy\lib\_datasource.py", line 151, in open
    return ds.open(path, mode)
  File "C:\Python27\lib\site-packages\numpy\lib\_datasource.py", line 499, in open
    return _file_openers[ext](found, mode=mode)
IOError: [Errno 22] invalid mode ('rbU') or filename: 'C:\\Users\\John\\Documents\\Kristi\\test.csvC:\\Users\\John\\Do
cuments\\Kristi\\test.csv'
>>>
>>> data = np.genfromtxt(r'C:\Users\John\Documents\Kristi\test.csvC:\Users\John\Documents\Kristi\test.csv', delimiter=
',')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python27\lib\site-packages\numpy\lib\npyio.py", line 1510, in genfromtxt
    fhd = iter(np.lib._datasource.open(fname, 'rbU'))
  File "C:\Python27\lib\site-packages\numpy\lib\_datasource.py", line 151, in open
    return ds.open(path, mode)
  File "C:\Python27\lib\site-packages\numpy\lib\_datasource.py", line 499, in open
    return _file_openers[ext](found, mode=mode)
IOError: [Errno 22] invalid mode ('rbU') or filename: 'C:\\Users\\John\\Documents\\Kristi\\test.csvC:\\Users\\John\\Do
cuments\\Kristi\\test.csv'
>>> data = np.genfromtxt(r'C:\Users\John\Documents\Kristi\test.csv', delimiter=',')
>>> data
array([[   nan,    nan,    nan,    nan],
       [   nan,  4.63 ,  4.63 , -3.353],
       [   nan,  4.63 ,  4.63 , -3.441],
       [   nan,  4.63 ,  4.63 , -3.221],
       [   nan,  4.63 ,  4.63 , -3.472],
       [   nan,  4.63 ,  4.63 , -3.263],
       [   nan,  4.63 ,  4.63 , -3.333],
       [   nan,  4.63 ,  4.63 , -3.421],
       [   nan,  4.63 ,  4.63 , -3.245],
       [   nan,  4.63 ,  4.63 , -3.316],
       [   nan,  4.63 ,  4.63 , -3.242],
       [   nan,  4.63 ,  4.63 , -3.156],
       [   nan,  4.63 ,  4.63 , -3.229],
       [   nan,  4.63 ,  4.63 , -3.299],
       [   nan,  4.63 ,  4.63 , -3.015],
       [   nan,  4.63 ,  4.63 , -3.289],
       [   nan,  4.63 ,  4.63 , -3.148],
       [   nan,  4.63 ,  4.63 , -3.148],
       [   nan,  4.63 ,  4.63 , -3.308],
       [   nan,  4.63 ,  4.63 , -3.167],
       [   nan,  4.63 ,  4.63 , -3.228],
       [   nan,  4.63 ,  4.63 , -3.295],
       [   nan,  4.63 ,  4.63 , -3.276],
       [   nan,  4.63 ,  4.63 , -3.089],
       [   nan,  4.63 ,  4.63 , -3.251],
       [   nan,  4.63 ,  4.63 , -3.136],
       [   nan,  4.63 ,  4.63 , -3.11 ],
       [   nan,  4.63 ,  4.63 , -3.215],
       [   nan,  4.63 ,  4.63 , -3.06 ],
       [   nan,  4.63 ,  4.63 , -3.238],
       [   nan,  4.63 ,  4.63 , -3.361],
       [   nan,  4.63 ,  4.63 , -3.299],
       [   nan,  4.63 ,  4.63 , -3.414],
       [   nan,  4.63 ,  4.63 , -3.202],
       [   nan,  4.63 ,  4.63 , -3.353],
       [   nan,  4.63 ,  4.63 , -3.345],
       [   nan,  4.63 ,  4.63 , -3.333],
       [   nan,  4.63 ,  4.63 , -3.373],
       [   nan,  4.63 ,  4.63 , -3.431],
       [   nan,  4.63 ,  4.63 , -3.318],
       [   nan,  4.63 ,  4.63 , -3.273]])
>>> data = np.genfromtxt(r'C:\Users\John\Documents\Kristi\test.csv', delimiter=',')
>>> data
array([[   nan,    nan,    nan,    nan],
       [   nan,  3.72 ,  0.57 , -3.353],
       [   nan,  3.78 ,  0.58 , -3.441],
       [   nan,  3.75 ,  0.57 , -3.221],
       [   nan,  3.78 ,  0.58 , -3.472],
       [   nan,  3.46 ,  0.54 , -3.263],
       [   nan,  3.67 ,  0.57 , -3.333],
       [   nan,  4.   ,  0.6  , -3.421],
       [   nan,  3.82 ,  0.58 , -3.245],
       [   nan,  3.39 ,  0.53 , -3.316],
       [   nan,  3.62 ,  0.56 , -3.242],
       [   nan,  4.   ,  0.6  , -3.156],
       [   nan,  0.   ,  0.   , -3.229],
       [   nan,  3.99 ,  0.6  , -3.299],
       [   nan,  2.69 ,  0.43 , -3.015],
       [   nan,  3.68 ,  0.57 , -3.289],
       [   nan,  3.38 ,  0.53 , -3.148],
       [   nan,  3.52 ,  0.55 , -3.148],
       [   nan,  3.69 ,  0.57 , -3.308],
       [   nan,  3.44 ,  0.54 , -3.167],
       [   nan,  3.75 ,  0.57 , -3.228],
       [   nan,  4.05 ,  0.61 , -3.295],
       [   nan,  3.9  ,  0.59 , -3.276],
       [   nan,  3.72 ,  0.57 , -3.089],
       [   nan,  3.6  ,  0.56 , -3.251],
       [   nan,  3.76 ,  0.57 , -3.136],
       [   nan,  3.67 ,  0.56 , -3.11 ],
       [   nan,  3.8  ,  0.58 , -3.215],
       [   nan,  3.33 ,  0.52 , -3.06 ],
       [   nan,  3.09 ,  0.49 , -3.238],
       [   nan,  3.79 ,  0.58 , -3.361],
       [   nan,  4.13 ,  0.62 , -3.299],
       [   nan,  3.96 ,  0.6  , -3.414],
       [   nan,  3.35 ,  0.52 , -3.202],
       [   nan,  4.21 ,  0.62 , -3.353],
       [   nan,  3.43 ,  0.53 , -3.345],
       [   nan,  3.74 ,  0.57 , -3.333],
       [   nan,  3.79 ,  0.58 , -3.373],
       [   nan,  3.94 ,  0.6  , -3.431],
       [   nan,  4.05 ,  0.61 , -3.318],
       [   nan,  3.19 ,  0.5  , -3.273]])
>>> data = np.genfromtxt(r'C:\Users\John\Documents\Kristi\test.csv', delimiter=',', skipheader=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: genfromtxt() got an unexpected keyword argument 'skipheader'
>>> data = np.genfromtxt(r'C:\Users\John\Documents\Kristi\test.csv', delimiter=',', skip_header=1)
>>> data
array([[   nan,  3.72 ,  0.57 , -3.353],
       [   nan,  3.78 ,  0.58 , -3.441],
       [   nan,  3.75 ,  0.57 , -3.221],
       [   nan,  3.78 ,  0.58 , -3.472],
       [   nan,  3.46 ,  0.54 , -3.263],
       [   nan,  3.67 ,  0.57 , -3.333],
       [   nan,  4.   ,  0.6  , -3.421],
       [   nan,  3.82 ,  0.58 , -3.245],
       [   nan,  3.39 ,  0.53 , -3.316],
       [   nan,  3.62 ,  0.56 , -3.242],
       [   nan,  4.   ,  0.6  , -3.156],
       [   nan,  0.   ,  0.   , -3.229],
       [   nan,  3.99 ,  0.6  , -3.299],
       [   nan,  2.69 ,  0.43 , -3.015],
       [   nan,  3.68 ,  0.57 , -3.289],
       [   nan,  3.38 ,  0.53 , -3.148],
       [   nan,  3.52 ,  0.55 , -3.148],
       [   nan,  3.69 ,  0.57 , -3.308],
       [   nan,  3.44 ,  0.54 , -3.167],
       [   nan,  3.75 ,  0.57 , -3.228],
       [   nan,  4.05 ,  0.61 , -3.295],
       [   nan,  3.9  ,  0.59 , -3.276],
       [   nan,  3.72 ,  0.57 , -3.089],
       [   nan,  3.6  ,  0.56 , -3.251],
       [   nan,  3.76 ,  0.57 , -3.136],
       [   nan,  3.67 ,  0.56 , -3.11 ],
       [   nan,  3.8  ,  0.58 , -3.215],
       [   nan,  3.33 ,  0.52 , -3.06 ],
       [   nan,  3.09 ,  0.49 , -3.238],
       [   nan,  3.79 ,  0.58 , -3.361],
       [   nan,  4.13 ,  0.62 , -3.299],
       [   nan,  3.96 ,  0.6  , -3.414],
       [   nan,  3.35 ,  0.52 , -3.202],
       [   nan,  4.21 ,  0.62 , -3.353],
       [   nan,  3.43 ,  0.53 , -3.345],
       [   nan,  3.74 ,  0.57 , -3.333],
       [   nan,  3.79 ,  0.58 , -3.373],
       [   nan,  3.94 ,  0.6  , -3.431],
       [   nan,  4.05 ,  0.61 , -3.318],
       [   nan,  3.19 ,  0.5  , -3.273]])
>>> dt = [('date','datetime64'),('LCLog', 'double'),('HCLog','double'),('slope','float')]
>>> dt
[('date', 'datetime64'), ('LCLog', 'double'), ('HCLog', 'double'), ('slope', 'float')]
>>> data = np.genfromtxt(r'C:\Users\John\Documents\Kristi\test.csv', delimiter=',', skip_header=1, dtype=dt)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python27\lib\site-packages\numpy\lib\npyio.py", line 1896, in genfromtxt
    rows = np.array(data, dtype=[('', _) for _ in dtype_flat])
ValueError: Cannot create a NumPy datetime other than NaT with generic units
>>>
>>> data = np.genfromtxt(r'C:\Users\John\Documents\Kristi\test.csv', delimiter=',', skip_header=1, dtype=dt)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python27\lib\site-packages\numpy\lib\npyio.py", line 1896, in genfromtxt
    rows = np.array(data, dtype=[('', _) for _ in dtype_flat])
ValueError: Cannot create a NumPy datetime other than NaT with generic units
>>>
>>> dt = [('date','datetime'),('LCLog', 'double'),('HCLog','double'),('slope','float')]
>>> data = np.genfromtxt(r'C:\Users\John\Documents\Kristi\test.csv', delimiter=',', skip_header=1, dtype=dt)
'datetime'Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python27\lib\site-packages\numpy\lib\npyio.py", line 1580, in genfromtxt
    replace_space=replace_space)
  File "C:\Python27\lib\site-packages\numpy\lib\_iotools.py", line 903, in easy_dtype
    ndtype = np.dtype(dict(formats=ndtype, names=names))
TypeError: data type "date" not understood
>>>
>>> dt = [('date','datetime64'),('LCLog', 'double'),('HCLog','double'),('slope','float')]
>>> data = np.genfromtxt(r'C:\Users\John\Documents\Kristi\test.csv', delimiter=',', skip_header=1, dtype=dt)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python27\lib\site-packages\numpy\lib\npyio.py", line 1896, in genfromtxt
    rows = np.array(data, dtype=[('', _) for _ in dtype_flat])
ValueError: Cannot create a NumPy datetime other than NaT with generic units
>>>
>>> from datetime import datetime
>>> data = np.genfromtxt(r'C:\Users\John\Documents\Kristi\test.csv', delimiter=',', skip_header=1)
>>> data
array([[   nan,  3.72 ,  0.57 , -3.353],
       [   nan,  3.78 ,  0.58 , -3.441],
       [   nan,  3.75 ,  0.57 , -3.221],
       [   nan,  3.78 ,  0.58 , -3.472],
       [   nan,  3.46 ,  0.54 , -3.263],
       [   nan,  3.67 ,  0.57 , -3.333],
       [   nan,  4.   ,  0.6  , -3.421],
       [   nan,  3.82 ,  0.58 , -3.245],
       [   nan,  3.39 ,  0.53 , -3.316],
       [   nan,  3.62 ,  0.56 , -3.242],
       [   nan,  4.   ,  0.6  , -3.156],
       [   nan,  0.   ,  0.   , -3.229],
       [   nan,  3.99 ,  0.6  , -3.299],
       [   nan,  2.69 ,  0.43 , -3.015],
       [   nan,  3.68 ,  0.57 , -3.289],
       [   nan,  3.38 ,  0.53 , -3.148],
       [   nan,  3.52 ,  0.55 , -3.148],
       [   nan,  3.69 ,  0.57 , -3.308],
       [   nan,  3.44 ,  0.54 , -3.167],
       [   nan,  3.75 ,  0.57 , -3.228],
       [   nan,  4.05 ,  0.61 , -3.295],
       [   nan,  3.9  ,  0.59 , -3.276],
       [   nan,  3.72 ,  0.57 , -3.089],
       [   nan,  3.6  ,  0.56 , -3.251],
       [   nan,  3.76 ,  0.57 , -3.136],
       [   nan,  3.67 ,  0.56 , -3.11 ],
       [   nan,  3.8  ,  0.58 , -3.215],
       [   nan,  3.33 ,  0.52 , -3.06 ],
       [   nan,  3.09 ,  0.49 , -3.238],
       [   nan,  3.79 ,  0.58 , -3.361],
       [   nan,  4.13 ,  0.62 , -3.299],
       [   nan,  3.96 ,  0.6  , -3.414],
       [   nan,  3.35 ,  0.52 , -3.202],
       [   nan,  4.21 ,  0.62 , -3.353],
       [   nan,  3.43 ,  0.53 , -3.345],
       [   nan,  3.74 ,  0.57 , -3.333],
       [   nan,  3.79 ,  0.58 , -3.373],
       [   nan,  3.94 ,  0.6  , -3.431],
       [   nan,  4.05 ,  0.61 , -3.318],
       [   nan,  3.19 ,  0.5  , -3.273]])
>>> with open(r'C:\Users\John\Documents\Kristi\test.csv', 'rb') as fIn:
...     for line in fIn:
...             print line
...
Date,LC LOG,HC LOG,Slope

2017-01-04,3.72,0.57,-3.353

2017-01-05,3.78,0.58,-3.441

2017-01-09,3.75,0.57,-3.221

2017-01-11,3.78,0.58,-3.472

2017-01-12,3.46,0.54,-3.263

2017-01-18,3.67,0.57,-3.333

2017-01-20,4.00,0.60,-3.421

2017-01-23,3.82,0.58,-3.245

2017-01-25,3.39,0.53,-3.316

2017-01-26,3.62,0.56,-3.242

2017-01-30,4.00,0.60,-3.156

2017-02-01,0.00,0.00,-3.229

2017-02-02,3.99,0.60,-3.299

2017-02-06,2.69,0.43,-3.015

2017-02-09,3.68,0.57,-3.289

2017-02-13,3.38,0.53,-3.148

2017-02-16,3.52,0.55,-3.148

2017-02-20,3.69,0.57,-3.308

2017-02-23,3.44,0.54,-3.167

2017-02-27,3.75,0.57,-3.228

2017-03-02,4.05,0.61,-3.295

2017-03-06,3.90,0.59,-3.276

2017-03-09,3.72,0.57,-3.089

2017-03-13,3.60,0.56,-3.251

2017-03-16,3.76,0.57,-3.136

2017-03-22,3.67,0.56,-3.110

2017-03-23,3.80,0.58,-3.215

2017-03-28,3.33,0.52,-3.060

2017-03-30,3.09,0.49,-3.238

2017-04-03,3.79,0.58,-3.361

2017-04-06,4.13,0.62,-3.299

2017-04-10,3.96,0.60,-3.414

2017-04-13,3.35,0.52,-3.202

2017-04-17,4.21,0.62,-3.353

2017-04-20,3.43,0.53,-3.345

2017-04-24,3.74,0.57,-3.333

2017-04-27,3.79,0.58,-3.373

2017-05-01,3.94,0.60,-3.431

2017-05-02,4.05,0.61,-3.318

2017-05-04,3.19,0.50,-3.273

>>> with open(r'C:\Users\John\Documents\Kristi\test.csv', 'rb') as fIn:
...     for line in fIn:
...             print line
...
Date,LC LOG,HC LOG,Slope

2017-01-04,3.72,0.57,-3.353

2017-01-05,3.78,0.58,-3.441

2017-01-09,3.75,0.57,-3.221

2017-01-11,3.78,0.58,-3.472

2017-01-12,3.46,0.54,-3.263

2017-01-18,3.67,0.57,-3.333

2017-01-20,4.00,0.60,-3.421

2017-01-23,3.82,0.58,-3.245

2017-01-25,3.39,0.53,-3.316

2017-01-26,3.62,0.56,-3.242

2017-01-30,4.00,0.60,-3.156

2017-02-01,0.00,0.00,-3.229

2017-02-02,3.99,0.60,-3.299

2017-02-06,2.69,0.43,-3.015

2017-02-09,3.68,0.57,-3.289

2017-02-13,3.38,0.53,-3.148

2017-02-16,3.52,0.55,-3.148

2017-02-20,3.69,0.57,-3.308

2017-02-23,3.44,0.54,-3.167

2017-02-27,3.75,0.57,-3.228

2017-03-02,4.05,0.61,-3.295

2017-03-06,3.90,0.59,-3.276

2017-03-09,3.72,0.57,-3.089

2017-03-13,3.60,0.56,-3.251

2017-03-16,3.76,0.57,-3.136

2017-03-22,3.67,0.56,-3.110

2017-03-23,3.80,0.58,-3.215

2017-03-28,3.33,0.52,-3.060

2017-03-30,3.09,0.49,-3.238

2017-04-03,3.79,0.58,-3.361

2017-04-06,4.13,0.62,-3.299

2017-04-10,3.96,0.60,-3.414

2017-04-13,3.35,0.52,-3.202

2017-04-17,4.21,0.62,-3.353

2017-04-20,3.43,0.53,-3.345

2017-04-24,3.74,0.57,-3.333

2017-04-27,3.79,0.58,-3.373

2017-05-01,3.94,0.60,-3.431

2017-05-02,4.05,0.61,-3.318

2017-05-04,3.19,0.50,-3.273

>>> data2 = []
>>> with open(r'C:\Users\John\Documents\Kristi\test.csv', 'rb') as fIn:
...
  File "<stdin>", line 2

    ^
IndentationError: expected an indented block
>>>
>>> import csv
>>> csv
<module 'csv' from 'C:\Python27\lib\csv.pyc'>
>>> with open(r'C:\Users\John\Documents\Kristi\test.csv', 'rb') as fIn:
...     reader = csv.reader(fIn)
...     for line in reader:
...             data2.append(line)
...
>>> data2
[['Date', 'LC LOG', 'HC LOG', 'Slope'], ['2017-01-04', '3.72', '0.57', '-3.353'], ['2017-01-05', '3.78', '0.58', '-3.4
41'], ['2017-01-09', '3.75', '0.57', '-3.221'], ['2017-01-11', '3.78', '0.58', '-3.472'], ['2017-01-12', '3.46', '0.54
', '-3.263'], ['2017-01-18', '3.67', '0.57', '-3.333'], ['2017-01-20', '4.00', '0.60', '-3.421'], ['2017-01-23', '3.82
', '0.58', '-3.245'], ['2017-01-25', '3.39', '0.53', '-3.316'], ['2017-01-26', '3.62', '0.56', '-3.242'], ['2017-01-30
', '4.00', '0.60', '-3.156'], ['2017-02-01', '0.00', '0.00', '-3.229'], ['2017-02-02', '3.99', '0.60', '-3.299'], ['20
17-02-06', '2.69', '0.43', '-3.015'], ['2017-02-09', '3.68', '0.57', '-3.289'], ['2017-02-13', '3.38', '0.53', '-3.148
'], ['2017-02-16', '3.52', '0.55', '-3.148'], ['2017-02-20', '3.69', '0.57', '-3.308'], ['2017-02-23', '3.44', '0.54',
 '-3.167'], ['2017-02-27', '3.75', '0.57', '-3.228'], ['2017-03-02', '4.05', '0.61', '-3.295'], ['2017-03-06', '3.90',
 '0.59', '-3.276'], ['2017-03-09', '3.72', '0.57', '-3.089'], ['2017-03-13', '3.60', '0.56', '-3.251'], ['2017-03-16',
 '3.76', '0.57', '-3.136'], ['2017-03-22', '3.67', '0.56', '-3.110'], ['2017-03-23', '3.80', '0.58', '-3.215'], ['2017
-03-28', '3.33', '0.52', '-3.060'], ['2017-03-30', '3.09', '0.49', '-3.238'], ['2017-04-03', '3.79', '0.58', '-3.361']
, ['2017-04-06', '4.13', '0.62', '-3.299'], ['2017-04-10', '3.96', '0.60', '-3.414'], ['2017-04-13', '3.35', '0.52', '
-3.202'], ['2017-04-17', '4.21', '0.62', '-3.353'], ['2017-04-20', '3.43', '0.53', '-3.345'], ['2017-04-24', '3.74', '
0.57', '-3.333'], ['2017-04-27', '3.79', '0.58', '-3.373'], ['2017-05-01', '3.94', '0.60', '-3.431'], ['2017-05-02', '
4.05', '0.61', '-3.318'], ['2017-05-04', '3.19', '0.50', '-3.273']]
>>> data = np.array(data2)
>>> data
array([['Date', 'LC LOG', 'HC LOG', 'Slope'],
       ['2017-01-04', '3.72', '0.57', '-3.353'],
       ['2017-01-05', '3.78', '0.58', '-3.441'],
       ['2017-01-09', '3.75', '0.57', '-3.221'],
       ['2017-01-11', '3.78', '0.58', '-3.472'],
       ['2017-01-12', '3.46', '0.54', '-3.263'],
       ['2017-01-18', '3.67', '0.57', '-3.333'],
       ['2017-01-20', '4.00', '0.60', '-3.421'],
       ['2017-01-23', '3.82', '0.58', '-3.245'],
       ['2017-01-25', '3.39', '0.53', '-3.316'],
       ['2017-01-26', '3.62', '0.56', '-3.242'],
       ['2017-01-30', '4.00', '0.60', '-3.156'],
       ['2017-02-01', '0.00', '0.00', '-3.229'],
       ['2017-02-02', '3.99', '0.60', '-3.299'],
       ['2017-02-06', '2.69', '0.43', '-3.015'],
       ['2017-02-09', '3.68', '0.57', '-3.289'],
       ['2017-02-13', '3.38', '0.53', '-3.148'],
       ['2017-02-16', '3.52', '0.55', '-3.148'],
       ['2017-02-20', '3.69', '0.57', '-3.308'],
       ['2017-02-23', '3.44', '0.54', '-3.167'],
       ['2017-02-27', '3.75', '0.57', '-3.228'],
       ['2017-03-02', '4.05', '0.61', '-3.295'],
       ['2017-03-06', '3.90', '0.59', '-3.276'],
       ['2017-03-09', '3.72', '0.57', '-3.089'],
       ['2017-03-13', '3.60', '0.56', '-3.251'],
       ['2017-03-16', '3.76', '0.57', '-3.136'],
       ['2017-03-22', '3.67', '0.56', '-3.110'],
       ['2017-03-23', '3.80', '0.58', '-3.215'],
       ['2017-03-28', '3.33', '0.52', '-3.060'],
       ['2017-03-30', '3.09', '0.49', '-3.238'],
       ['2017-04-03', '3.79', '0.58', '-3.361'],
       ['2017-04-06', '4.13', '0.62', '-3.299'],
       ['2017-04-10', '3.96', '0.60', '-3.414'],
       ['2017-04-13', '3.35', '0.52', '-3.202'],
       ['2017-04-17', '4.21', '0.62', '-3.353'],
       ['2017-04-20', '3.43', '0.53', '-3.345'],
       ['2017-04-24', '3.74', '0.57', '-3.333'],
       ['2017-04-27', '3.79', '0.58', '-3.373'],
       ['2017-05-01', '3.94', '0.60', '-3.431'],
       ['2017-05-02', '4.05', '0.61', '-3.318'],
       ['2017-05-04', '3.19', '0.50', '-3.273']],
      dtype='|S10')
>>> data = np.array(data2, dtype = dt)
>>> data
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python27\lib\site-packages\numpy\core\numeric.py", line 1898, in array_repr
    ', ', "array(")
  File "C:\Python27\lib\site-packages\numpy\core\arrayprint.py", line 463, in array2string
    separator, prefix, formatter=formatter)
  File "C:\Python27\lib\site-packages\numpy\core\arrayprint.py", line 336, in _array2string
    _summaryEdgeItems, summary_insert)[:-1]
  File "C:\Python27\lib\site-packages\numpy\core\arrayprint.py", line 533, in _formatArray
    summary_insert)
  File "C:\Python27\lib\site-packages\numpy\core\arrayprint.py", line 507, in _formatArray
    word = format_function(a[-i]) + separator
  File "C:\Python27\lib\site-packages\numpy\core\arrayprint.py", line 795, in __call__
    s += format_function(field) + ", "
  File "C:\Python27\lib\site-packages\numpy\core\arrayprint.py", line 748, in __call__
    casting=self.casting)
TypeError: Invalid datetime unit "generic" in metadata
>>> data2
[['Date', 'LC LOG', 'HC LOG', 'Slope'], ['2017-01-04', '3.72', '0.57', '-3.353'], ['2017-01-05', '3.78', '0.58', '-3.4
41'], ['2017-01-09', '3.75', '0.57', '-3.221'], ['2017-01-11', '3.78', '0.58', '-3.472'], ['2017-01-12', '3.46', '0.54
', '-3.263'], ['2017-01-18', '3.67', '0.57', '-3.333'], ['2017-01-20', '4.00', '0.60', '-3.421'], ['2017-01-23', '3.82
', '0.58', '-3.245'], ['2017-01-25', '3.39', '0.53', '-3.316'], ['2017-01-26', '3.62', '0.56', '-3.242'], ['2017-01-30
', '4.00', '0.60', '-3.156'], ['2017-02-01', '0.00', '0.00', '-3.229'], ['2017-02-02', '3.99', '0.60', '-3.299'], ['20
17-02-06', '2.69', '0.43', '-3.015'], ['2017-02-09', '3.68', '0.57', '-3.289'], ['2017-02-13', '3.38', '0.53', '-3.148
'], ['2017-02-16', '3.52', '0.55', '-3.148'], ['2017-02-20', '3.69', '0.57', '-3.308'], ['2017-02-23', '3.44', '0.54',
 '-3.167'], ['2017-02-27', '3.75', '0.57', '-3.228'], ['2017-03-02', '4.05', '0.61', '-3.295'], ['2017-03-06', '3.90',
 '0.59', '-3.276'], ['2017-03-09', '3.72', '0.57', '-3.089'], ['2017-03-13', '3.60', '0.56', '-3.251'], ['2017-03-16',
 '3.76', '0.57', '-3.136'], ['2017-03-22', '3.67', '0.56', '-3.110'], ['2017-03-23', '3.80', '0.58', '-3.215'], ['2017
-03-28', '3.33', '0.52', '-3.060'], ['2017-03-30', '3.09', '0.49', '-3.238'], ['2017-04-03', '3.79', '0.58', '-3.361']
, ['2017-04-06', '4.13', '0.62', '-3.299'], ['2017-04-10', '3.96', '0.60', '-3.414'], ['2017-04-13', '3.35', '0.52', '
-3.202'], ['2017-04-17', '4.21', '0.62', '-3.353'], ['2017-04-20', '3.43', '0.53', '-3.345'], ['2017-04-24', '3.74', '
0.57', '-3.333'], ['2017-04-27', '3.79', '0.58', '-3.373'], ['2017-05-01', '3.94', '0.60', '-3.431'], ['2017-05-02', '
4.05', '0.61', '-3.318'], ['2017-05-04', '3.19', '0.50', '-3.273']]
>>> for e1 in data2:
...     for n in range(0,len(e1)):
...             if n==0:
...
...
  File "<stdin>", line 5

    ^
IndentationError: expected an indented block
>>> data2.remove(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> data2.remove(data2[0])
>>> data2
[['2017-01-04', '3.72', '0.57', '-3.353'], ['2017-01-05', '3.78', '0.58', '-3.441'], ['2017-01-09', '3.75', '0.57', '-
3.221'], ['2017-01-11', '3.78', '0.58', '-3.472'], ['2017-01-12', '3.46', '0.54', '-3.263'], ['2017-01-18', '3.67', '0
.57', '-3.333'], ['2017-01-20', '4.00', '0.60', '-3.421'], ['2017-01-23', '3.82', '0.58', '-3.245'], ['2017-01-25', '3
.39', '0.53', '-3.316'], ['2017-01-26', '3.62', '0.56', '-3.242'], ['2017-01-30', '4.00', '0.60', '-3.156'], ['2017-02
-01', '0.00', '0.00', '-3.229'], ['2017-02-02', '3.99', '0.60', '-3.299'], ['2017-02-06', '2.69', '0.43', '-3.015'], [
'2017-02-09', '3.68', '0.57', '-3.289'], ['2017-02-13', '3.38', '0.53', '-3.148'], ['2017-02-16', '3.52', '0.55', '-3.
148'], ['2017-02-20', '3.69', '0.57', '-3.308'], ['2017-02-23', '3.44', '0.54', '-3.167'], ['2017-02-27', '3.75', '0.5
7', '-3.228'], ['2017-03-02', '4.05', '0.61', '-3.295'], ['2017-03-06', '3.90', '0.59', '-3.276'], ['2017-03-09', '3.7
2', '0.57', '-3.089'], ['2017-03-13', '3.60', '0.56', '-3.251'], ['2017-03-16', '3.76', '0.57', '-3.136'], ['2017-03-2
2', '3.67', '0.56', '-3.110'], ['2017-03-23', '3.80', '0.58', '-3.215'], ['2017-03-28', '3.33', '0.52', '-3.060'], ['2
017-03-30', '3.09', '0.49', '-3.238'], ['2017-04-03', '3.79', '0.58', '-3.361'], ['2017-04-06', '4.13', '0.62', '-3.29
9'], ['2017-04-10', '3.96', '0.60', '-3.414'], ['2017-04-13', '3.35', '0.52', '-3.202'], ['2017-04-17', '4.21', '0.62'
, '-3.353'], ['2017-04-20', '3.43', '0.53', '-3.345'], ['2017-04-24', '3.74', '0.57', '-3.333'], ['2017-04-27', '3.79'
, '0.58', '-3.373'], ['2017-05-01', '3.94', '0.60', '-3.431'], ['2017-05-02', '4.05', '0.61', '-3.318'], ['2017-05-04'
, '3.19', '0.50', '-3.273']]
>>> for e1 in data2:
...     for n in range(0,len(e1)):
...             if n==0:
...                     e1[n]=np.datetime64(e1[n]).astype(datetime)
...             else:
...                     e1[n]=float(e1[n])
...
>>> data2
[[datetime.date(2017, 1, 4), 3.72, 0.57, -3.353], [datetime.date(2017, 1, 5), 3.78, 0.58, -3.441], [datetime.date(2017
, 1, 9), 3.75, 0.57, -3.221], [datetime.date(2017, 1, 11), 3.78, 0.58, -3.472], [datetime.date(2017, 1, 12), 3.46, 0.5
4, -3.263], [datetime.date(2017, 1, 18), 3.67, 0.57, -3.333], [datetime.date(2017, 1, 20), 4.0, 0.6, -3.421], [datetim
e.date(2017, 1, 23), 3.82, 0.58, -3.245], [datetime.date(2017, 1, 25), 3.39, 0.53, -3.316], [datetime.date(2017, 1, 26
), 3.62, 0.56, -3.242], [datetime.date(2017, 1, 30), 4.0, 0.6, -3.156], [datetime.date(2017, 2, 1), 0.0, 0.0, -3.229],
 [datetime.date(2017, 2, 2), 3.99, 0.6, -3.299], [datetime.date(2017, 2, 6), 2.69, 0.43, -3.015], [datetime.date(2017,
 2, 9), 3.68, 0.57, -3.289], [datetime.date(2017, 2, 13), 3.38, 0.53, -3.148], [datetime.date(2017, 2, 16), 3.52, 0.55
, -3.148], [datetime.date(2017, 2, 20), 3.69, 0.57, -3.308], [datetime.date(2017, 2, 23), 3.44, 0.54, -3.167], [dateti
me.date(2017, 2, 27), 3.75, 0.57, -3.228], [datetime.date(2017, 3, 2), 4.05, 0.61, -3.295], [datetime.date(2017, 3, 6)
, 3.9, 0.59, -3.276], [datetime.date(2017, 3, 9), 3.72, 0.57, -3.089], [datetime.date(2017, 3, 13), 3.6, 0.56, -3.251]
, [datetime.date(2017, 3, 16), 3.76, 0.57, -3.136], [datetime.date(2017, 3, 22), 3.67, 0.56, -3.11], [datetime.date(20
17, 3, 23), 3.8, 0.58, -3.215], [datetime.date(2017, 3, 28), 3.33, 0.52, -3.06], [datetime.date(2017, 3, 30), 3.09, 0.
49, -3.238], [datetime.date(2017, 4, 3), 3.79, 0.58, -3.361], [datetime.date(2017, 4, 6), 4.13, 0.62, -3.299], [dateti
me.date(2017, 4, 10), 3.96, 0.6, -3.414], [datetime.date(2017, 4, 13), 3.35, 0.52, -3.202], [datetime.date(2017, 4, 17
), 4.21, 0.62, -3.353], [datetime.date(2017, 4, 20), 3.43, 0.53, -3.345], [datetime.date(2017, 4, 24), 3.74, 0.57, -3.
333], [datetime.date(2017, 4, 27), 3.79, 0.58, -3.373], [datetime.date(2017, 5, 1), 3.94, 0.6, -3.431], [datetime.date
(2017, 5, 2), 4.05, 0.61, -3.318], [datetime.date(2017, 5, 4), 3.19, 0.5, -3.273]]
>>> data = np.array(data2)
>>> data
array([[datetime.date(2017, 1, 4), 3.72, 0.57, -3.353],
       [datetime.date(2017, 1, 5), 3.78, 0.58, -3.441],
       [datetime.date(2017, 1, 9), 3.75, 0.57, -3.221],
       [datetime.date(2017, 1, 11), 3.78, 0.58, -3.472],
       [datetime.date(2017, 1, 12), 3.46, 0.54, -3.263],
       [datetime.date(2017, 1, 18), 3.67, 0.57, -3.333],
       [datetime.date(2017, 1, 20), 4.0, 0.6, -3.421],
       [datetime.date(2017, 1, 23), 3.82, 0.58, -3.245],
       [datetime.date(2017, 1, 25), 3.39, 0.53, -3.316],
       [datetime.date(2017, 1, 26), 3.62, 0.56, -3.242],
       [datetime.date(2017, 1, 30), 4.0, 0.6, -3.156],
       [datetime.date(2017, 2, 1), 0.0, 0.0, -3.229],
       [datetime.date(2017, 2, 2), 3.99, 0.6, -3.299],
       [datetime.date(2017, 2, 6), 2.69, 0.43, -3.015],
       [datetime.date(2017, 2, 9), 3.68, 0.57, -3.289],
       [datetime.date(2017, 2, 13), 3.38, 0.53, -3.148],
       [datetime.date(2017, 2, 16), 3.52, 0.55, -3.148],
       [datetime.date(2017, 2, 20), 3.69, 0.57, -3.308],
       [datetime.date(2017, 2, 23), 3.44, 0.54, -3.167],
       [datetime.date(2017, 2, 27), 3.75, 0.57, -3.228],
       [datetime.date(2017, 3, 2), 4.05, 0.61, -3.295],
       [datetime.date(2017, 3, 6), 3.9, 0.59, -3.276],
       [datetime.date(2017, 3, 9), 3.72, 0.57, -3.089],
       [datetime.date(2017, 3, 13), 3.6, 0.56, -3.251],
       [datetime.date(2017, 3, 16), 3.76, 0.57, -3.136],
       [datetime.date(2017, 3, 22), 3.67, 0.56, -3.11],
       [datetime.date(2017, 3, 23), 3.8, 0.58, -3.215],
       [datetime.date(2017, 3, 28), 3.33, 0.52, -3.06],
       [datetime.date(2017, 3, 30), 3.09, 0.49, -3.238],
       [datetime.date(2017, 4, 3), 3.79, 0.58, -3.361],
       [datetime.date(2017, 4, 6), 4.13, 0.62, -3.299],
       [datetime.date(2017, 4, 10), 3.96, 0.6, -3.414],
       [datetime.date(2017, 4, 13), 3.35, 0.52, -3.202],
       [datetime.date(2017, 4, 17), 4.21, 0.62, -3.353],
       [datetime.date(2017, 4, 20), 3.43, 0.53, -3.345],
       [datetime.date(2017, 4, 24), 3.74, 0.57, -3.333],
       [datetime.date(2017, 4, 27), 3.79, 0.58, -3.373],
       [datetime.date(2017, 5, 1), 3.94, 0.6, -3.431],
       [datetime.date(2017, 5, 2), 4.05, 0.61, -3.318],
       [datetime.date(2017, 5, 4), 3.19, 0.5, -3.273]], dtype=object)
>>> data = np.array(data2, dtype='datetime64,f,f,f')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: expected a readable buffer object
>>> data[:,0]
array([datetime.date(2017, 1, 4), datetime.date(2017, 1, 5),
       datetime.date(2017, 1, 9), datetime.date(2017, 1, 11),
       datetime.date(2017, 1, 12), datetime.date(2017, 1, 18),
       datetime.date(2017, 1, 20), datetime.date(2017, 1, 23),
       datetime.date(2017, 1, 25), datetime.date(2017, 1, 26),
       datetime.date(2017, 1, 30), datetime.date(2017, 2, 1),
       datetime.date(2017, 2, 2), datetime.date(2017, 2, 6),
       datetime.date(2017, 2, 9), datetime.date(2017, 2, 13),
       datetime.date(2017, 2, 16), datetime.date(2017, 2, 20),
       datetime.date(2017, 2, 23), datetime.date(2017, 2, 27),
       datetime.date(2017, 3, 2), datetime.date(2017, 3, 6),
       datetime.date(2017, 3, 9), datetime.date(2017, 3, 13),
       datetime.date(2017, 3, 16), datetime.date(2017, 3, 22),
       datetime.date(2017, 3, 23), datetime.date(2017, 3, 28),
       datetime.date(2017, 3, 30), datetime.date(2017, 4, 3),
       datetime.date(2017, 4, 6), datetime.date(2017, 4, 10),
       datetime.date(2017, 4, 13), datetime.date(2017, 4, 17),
       datetime.date(2017, 4, 20), datetime.date(2017, 4, 24),
       datetime.date(2017, 4, 27), datetime.date(2017, 5, 1),
       datetime.date(2017, 5, 2), datetime.date(2017, 5, 4)], dtype=object)
>>> plt.plot_date(data[:,0], data[:,1])
[<matplotlib.lines.Line2D object at 0x050E1230>]
>>> plt.show()
>>> plt.plot_date(data[:,0], data[:,1], '--k')
[<matplotlib.lines.Line2D object at 0x093A0F50>]
>>> plt.show()
>>> plt.plot_date(data[:,0], data[:,1])
[<matplotlib.lines.Line2D object at 0x09433E50>]
>>> plt.axhline(y=3.53)
<matplotlib.lines.Line2D object at 0x093A0EB0>
>>> plt.axhline(y=4.03)
<matplotlib.lines.Line2D object at 0x0941AA10>
>>> sd = np.std(data[:,1])
>>> sd
0.64721861646587397
>>> sd2 = sd*2
>>> m = np.mean(data[:,1])
>>> m
3.59075
>>> LCpsd2 = m + sd2
>>> LCmsd2 = m - sd2
>>> plt.axhline(y=LCmsd2, '--r')
  File "<stdin>", line 1
SyntaxError: non-keyword arg after keyword arg
>>> plt.axhline(y=LCmsd2, color = 'r')
<matplotlib.lines.Line2D object at 0x04EA89B0>
>>> plt.axhline(y=LCpsd2, color = 'r')
<matplotlib.lines.Line2D object at 0x09594A70>
>>> plt.show()
>>> r'C:\Users\John\Documents\Kristi\test.csv'r'C:\Users\John\Documents\Kristi\test.csv'r'C:\Users\John\Documents\Kris
