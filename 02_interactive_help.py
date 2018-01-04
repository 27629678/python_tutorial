dir() # short for directory
# ['__builtins__', '__doc__', '__name__', '__package__', 'a', 'b', 'c', 'd']

dir(__builtins__)
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BufferError', 'BytesWarnin
# g', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'Floatin
# gPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'Indentat
# ionError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError',
#  'None', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWar
# ning', 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StandardError', 'StopIteration', 'Syntax
# Error', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'True', 'TypeError', 'UnboundLocal
# Error', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'Unicod
# eWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__debu
# g__', '__doc__', '__import__', '__name__', '__package__', 'abs', 'all', 'any', 'apply', 'basestring'
# , 'bin', 'bool', 'buffer', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'cmp', 'coerce',
# 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval
# ', 'execfile', 'exit', 'file', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasa
# ttr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'intern', 'isinstance', 'issubclass', 'iter', 'le
# n', 'license', 'list', 'locals', 'long', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct',
#  'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'raw_input', 'reduce', 'reload', 'repr'
# , 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', '
# tuple', 'type', 'unichr', 'unicode', 'vars', 'xrange', 'zip']

help(pow)
# pow(x, y[, z]) -> number

# With two arguments, equivalent to x**y.  With three arguments,
# equivalent to (x**y) % z, but may be more efficient (e.g. for longs).

help('modules')

# Please wait a moment while I gather a list of all available modules...

# BaseHTTPServer      argparse            imageop             sets
# Bastion             array               imaplib             setuptools
# CGIHTTPServer       ast                 imghdr              sgmllib
# Canvas              asynchat            imp                 sha
# ConfigParser        asyncore            importlib           shelve
# Cookie              atexit              imputil             shlex
# Dialog              audiodev            inspect             shutil
# DocXMLRPCServer     audioop             io                  signal
# FileDialog          base64              itertools           site
# FixTk               bdb                 itsdangerous        smtpd
# HTMLParser          binascii            jinja2              smtplib
# MimeWriter          binhex              json                sndhdr
# Queue               bisect              keyword             socket
# ScrolledText        bsddb               lib2to3             sqlite3
# SimpleDialog        bz2                 linecache           sre
# SimpleHTTPServer    cPickle             locale              sre_compile
# SimpleXMLRPCServer  cProfile            logging             sre_constants
# SocketServer        cStringIO           macpath             sre_parse
# StringIO            calendar            macurl2path         ssl
# Tix                 cgi                 mailbox             stat
# Tkconstants         cgitb               mailcap             statvfs
# Tkdnd               chunk               markupbase          string
# Tkinter             click               markupsafe          stringold
# UserDict            cmath               marshal             stringprep
# UserList            cmd                 math                strop
# UserString          code                md5                 struct
# _LWPCookieJar       codecs              mhlib               subprocess
# _MozillaCookieJar   codeop              mimetools           sunau
# __builtin__         collections         mimetypes           sunaudio
# __future__          colorsys            mimify              symbol
# _abcoll             commands            mmap                symtable
# _ast                compileall          modulefinder        sys
# _bisect             compiler            msilib              sysconfig
# _bsddb              contextlib          msvcrt              tabnanny
# _codecs             cookielib           multifile           tarfile
# _codecs_cn          copy                multiprocessing     telnetlib
# _codecs_hk          copy_reg            mutex               tempfile
# _codecs_iso2022     csv                 netrc               test
# _codecs_jp          ctypes              new                 textwrap
# _codecs_kr          curses              nntplib             this
# _codecs_tw          datetime            nt                  thread
# _collections        dbhash              ntpath              threading
# _csv                decimal             nturl2path          time
# _ctypes             difflib             numbers             timeit
# _ctypes_test        dircache            opcode              tkColorChooser
# _elementtree        dis                 operator            tkCommonDialog
# _functools          distutils           optparse            tkFileDialog
# _hashlib            doctest             os                  tkFont
# _heapq              dumbdbm             os2emxpath          tkMessageBox
# _hotshot            dummy_thread        parser              tkSimpleDialog
# _io                 dummy_threading     pdb                 toaiff
# _json               easy_install        pickle              token
# _locale             email               pickletools         tokenize
# _lsprof             encodings           pip                 trace
# _md5                ensurepip           pipes               traceback
# _msi                errno               pkg_resources       ttk
# _multibytecodec     exceptions          pkgutil             tty
# _multiprocessing    filecmp             platform            turtle
# _osx_support        fileinput           plistlib            types
# _pyio               flask               popen2              unicodedata
# _random             fnmatch             poplib              unittest
# _sha                formatter           posixfile           urllib
# _sha256             fpformat            posixpath           urllib2
# _sha512             fractions           pprint              urlparse
# _socket             ftplib              profile             user
# _sqlite3            functools           pstats              uu
# _sre                future_builtins     pty                 uuid
# _ssl                gc                  py_compile          warnings
# _strptime           genericpath         pyclbr              wave
# _struct             getopt              pydoc               weakref
# _subprocess         getpass             pydoc_data          webbrowser
# _symtable           gettext             pyexpat             werkzeug
# _testcapi           glob                quopri              whichdb
# _threading_local    gzip                random              winsound
# _tkinter            hashlib             re                  wsgiref
# _warnings           heapq               repr                xdrlib
# _weakref            hmac                rexec               xml
# _weakrefset         hotshot             rfc822              xmllib
# _winreg             htmlentitydefs      rlcompleter         xmlrpclib
# abc                 htmllib             robotparser         xxsubtype
# aifc                httplib             runpy               zipfile
# antigravity         idlelib             sched               zipimport
# anydbm              ihooks              select              zlib

# Enter any module name to get more help.  Or, type "modules spam" to search
# for modules whose descriptions contain the word "spam".