#include "cpp_impliment.h"

#include <stdio.h>
#include <Python.h>



static PyObject* hello_on_cpp(PyObject* self, PyObject* args){
  printf("hello on c++");
  return Py_BuildValue("s","hello on cpp" );
}

static char hello_on_cpp_docs[] =
    "this cpp on python\n";


static PyMethodDef hello_on_cpp_funcs[] = {
    {"add", (PyCFunction)hello_on_cpp, METH_VARARGS, hello_on_cpp_docs},
    {NULL, NULL, 0, NULL}
};


PyMODINIT_FUNC initaddList(void){
    Py_InitModule3("cpp_start", hello_on_cpp,
                   "cpp on python");
}