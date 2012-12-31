# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_normalize_numexp', [dirname(__file__)])
        except ImportError:
            import _normalize_numexp
            return _normalize_numexp
        if fp is not None:
            try:
                _mod = imp.load_module('_normalize_numexp', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _normalize_numexp = swig_import_helper()
    del swig_import_helper
else:
    import _normalize_numexp
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _normalize_numexp.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _normalize_numexp.SwigPyIterator_value(self)
    def incr(self, n = 1): return _normalize_numexp.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _normalize_numexp.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _normalize_numexp.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _normalize_numexp.SwigPyIterator_equal(self, *args)
    def copy(self): return _normalize_numexp.SwigPyIterator_copy(self)
    def next(self): return _normalize_numexp.SwigPyIterator_next(self)
    def __next__(self): return _normalize_numexp.SwigPyIterator___next__(self)
    def previous(self): return _normalize_numexp.SwigPyIterator_previous(self)
    def advance(self, *args): return _normalize_numexp.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _normalize_numexp.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _normalize_numexp.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _normalize_numexp.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _normalize_numexp.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _normalize_numexp.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _normalize_numexp.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _normalize_numexp.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class IntVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _normalize_numexp.IntVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _normalize_numexp.IntVector___nonzero__(self)
    def __bool__(self): return _normalize_numexp.IntVector___bool__(self)
    def __len__(self): return _normalize_numexp.IntVector___len__(self)
    def pop(self): return _normalize_numexp.IntVector_pop(self)
    def __getslice__(self, *args): return _normalize_numexp.IntVector___getslice__(self, *args)
    def __setslice__(self, *args): return _normalize_numexp.IntVector___setslice__(self, *args)
    def __delslice__(self, *args): return _normalize_numexp.IntVector___delslice__(self, *args)
    def __delitem__(self, *args): return _normalize_numexp.IntVector___delitem__(self, *args)
    def __getitem__(self, *args): return _normalize_numexp.IntVector___getitem__(self, *args)
    def __setitem__(self, *args): return _normalize_numexp.IntVector___setitem__(self, *args)
    def append(self, *args): return _normalize_numexp.IntVector_append(self, *args)
    def empty(self): return _normalize_numexp.IntVector_empty(self)
    def size(self): return _normalize_numexp.IntVector_size(self)
    def clear(self): return _normalize_numexp.IntVector_clear(self)
    def swap(self, *args): return _normalize_numexp.IntVector_swap(self, *args)
    def get_allocator(self): return _normalize_numexp.IntVector_get_allocator(self)
    def begin(self): return _normalize_numexp.IntVector_begin(self)
    def end(self): return _normalize_numexp.IntVector_end(self)
    def rbegin(self): return _normalize_numexp.IntVector_rbegin(self)
    def rend(self): return _normalize_numexp.IntVector_rend(self)
    def pop_back(self): return _normalize_numexp.IntVector_pop_back(self)
    def erase(self, *args): return _normalize_numexp.IntVector_erase(self, *args)
    def __init__(self, *args): 
        this = _normalize_numexp.new_IntVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _normalize_numexp.IntVector_push_back(self, *args)
    def front(self): return _normalize_numexp.IntVector_front(self)
    def back(self): return _normalize_numexp.IntVector_back(self)
    def assign(self, *args): return _normalize_numexp.IntVector_assign(self, *args)
    def resize(self, *args): return _normalize_numexp.IntVector_resize(self, *args)
    def insert(self, *args): return _normalize_numexp.IntVector_insert(self, *args)
    def reserve(self, *args): return _normalize_numexp.IntVector_reserve(self, *args)
    def capacity(self): return _normalize_numexp.IntVector_capacity(self)
    __swig_destroy__ = _normalize_numexp.delete_IntVector
    __del__ = lambda self : None;
IntVector_swigregister = _normalize_numexp.IntVector_swigregister
IntVector_swigregister(IntVector)

class DoubleVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _normalize_numexp.DoubleVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _normalize_numexp.DoubleVector___nonzero__(self)
    def __bool__(self): return _normalize_numexp.DoubleVector___bool__(self)
    def __len__(self): return _normalize_numexp.DoubleVector___len__(self)
    def pop(self): return _normalize_numexp.DoubleVector_pop(self)
    def __getslice__(self, *args): return _normalize_numexp.DoubleVector___getslice__(self, *args)
    def __setslice__(self, *args): return _normalize_numexp.DoubleVector___setslice__(self, *args)
    def __delslice__(self, *args): return _normalize_numexp.DoubleVector___delslice__(self, *args)
    def __delitem__(self, *args): return _normalize_numexp.DoubleVector___delitem__(self, *args)
    def __getitem__(self, *args): return _normalize_numexp.DoubleVector___getitem__(self, *args)
    def __setitem__(self, *args): return _normalize_numexp.DoubleVector___setitem__(self, *args)
    def append(self, *args): return _normalize_numexp.DoubleVector_append(self, *args)
    def empty(self): return _normalize_numexp.DoubleVector_empty(self)
    def size(self): return _normalize_numexp.DoubleVector_size(self)
    def clear(self): return _normalize_numexp.DoubleVector_clear(self)
    def swap(self, *args): return _normalize_numexp.DoubleVector_swap(self, *args)
    def get_allocator(self): return _normalize_numexp.DoubleVector_get_allocator(self)
    def begin(self): return _normalize_numexp.DoubleVector_begin(self)
    def end(self): return _normalize_numexp.DoubleVector_end(self)
    def rbegin(self): return _normalize_numexp.DoubleVector_rbegin(self)
    def rend(self): return _normalize_numexp.DoubleVector_rend(self)
    def pop_back(self): return _normalize_numexp.DoubleVector_pop_back(self)
    def erase(self, *args): return _normalize_numexp.DoubleVector_erase(self, *args)
    def __init__(self, *args): 
        this = _normalize_numexp.new_DoubleVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _normalize_numexp.DoubleVector_push_back(self, *args)
    def front(self): return _normalize_numexp.DoubleVector_front(self)
    def back(self): return _normalize_numexp.DoubleVector_back(self)
    def assign(self, *args): return _normalize_numexp.DoubleVector_assign(self, *args)
    def resize(self, *args): return _normalize_numexp.DoubleVector_resize(self, *args)
    def insert(self, *args): return _normalize_numexp.DoubleVector_insert(self, *args)
    def reserve(self, *args): return _normalize_numexp.DoubleVector_reserve(self, *args)
    def capacity(self): return _normalize_numexp.DoubleVector_capacity(self)
    __swig_destroy__ = _normalize_numexp.delete_DoubleVector
    __del__ = lambda self : None;
DoubleVector_swigregister = _normalize_numexp.DoubleVector_swigregister
DoubleVector_swigregister(DoubleVector)

class StringVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _normalize_numexp.StringVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _normalize_numexp.StringVector___nonzero__(self)
    def __bool__(self): return _normalize_numexp.StringVector___bool__(self)
    def __len__(self): return _normalize_numexp.StringVector___len__(self)
    def pop(self): return _normalize_numexp.StringVector_pop(self)
    def __getslice__(self, *args): return _normalize_numexp.StringVector___getslice__(self, *args)
    def __setslice__(self, *args): return _normalize_numexp.StringVector___setslice__(self, *args)
    def __delslice__(self, *args): return _normalize_numexp.StringVector___delslice__(self, *args)
    def __delitem__(self, *args): return _normalize_numexp.StringVector___delitem__(self, *args)
    def __getitem__(self, *args): return _normalize_numexp.StringVector___getitem__(self, *args)
    def __setitem__(self, *args): return _normalize_numexp.StringVector___setitem__(self, *args)
    def append(self, *args): return _normalize_numexp.StringVector_append(self, *args)
    def empty(self): return _normalize_numexp.StringVector_empty(self)
    def size(self): return _normalize_numexp.StringVector_size(self)
    def clear(self): return _normalize_numexp.StringVector_clear(self)
    def swap(self, *args): return _normalize_numexp.StringVector_swap(self, *args)
    def get_allocator(self): return _normalize_numexp.StringVector_get_allocator(self)
    def begin(self): return _normalize_numexp.StringVector_begin(self)
    def end(self): return _normalize_numexp.StringVector_end(self)
    def rbegin(self): return _normalize_numexp.StringVector_rbegin(self)
    def rend(self): return _normalize_numexp.StringVector_rend(self)
    def pop_back(self): return _normalize_numexp.StringVector_pop_back(self)
    def erase(self, *args): return _normalize_numexp.StringVector_erase(self, *args)
    def __init__(self, *args): 
        this = _normalize_numexp.new_StringVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _normalize_numexp.StringVector_push_back(self, *args)
    def front(self): return _normalize_numexp.StringVector_front(self)
    def back(self): return _normalize_numexp.StringVector_back(self)
    def assign(self, *args): return _normalize_numexp.StringVector_assign(self, *args)
    def resize(self, *args): return _normalize_numexp.StringVector_resize(self, *args)
    def insert(self, *args): return _normalize_numexp.StringVector_insert(self, *args)
    def reserve(self, *args): return _normalize_numexp.StringVector_reserve(self, *args)
    def capacity(self): return _normalize_numexp.StringVector_capacity(self)
    __swig_destroy__ = _normalize_numexp.delete_StringVector
    __del__ = lambda self : None;
StringVector_swigregister = _normalize_numexp.StringVector_swigregister
StringVector_swigregister(StringVector)

NORMALIZENUMEXP_NAME = _normalize_numexp.NORMALIZENUMEXP_NAME
NORMALIZENUMEXP_VERSION = _normalize_numexp.NORMALIZENUMEXP_VERSION
NORMALIZENUMEXP_COPYRIGHT = _normalize_numexp.NORMALIZENUMEXP_COPYRIGHT
class NormalizeNumexp(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NormalizeNumexp, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NormalizeNumexp, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _normalize_numexp.new_NormalizeNumexp(*args)
        try: self.this.append(this)
        except: self.this = this
    def normalize(self, *args): return _normalize_numexp.NormalizeNumexp_normalize(self, *args)
    __swig_destroy__ = _normalize_numexp.delete_NormalizeNumexp
    __del__ = lambda self : None;
NormalizeNumexp_swigregister = _normalize_numexp.NormalizeNumexp_swigregister
NormalizeNumexp_swigregister(NormalizeNumexp)



