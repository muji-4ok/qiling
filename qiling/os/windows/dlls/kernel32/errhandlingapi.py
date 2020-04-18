#!/usr/bin/env python3
#
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
# Built on top of Unicorn emulator (www.unicorn-engine.org)

import struct
import time
from qiling.os.windows.const import *
from qiling.os.const import *
from qiling.os.windows.fncc import *
from qiling.os.windows.utils import *
from qiling.os.windows.thread import *
from qiling.os.windows.handle import *
from qiling.exception import *


# LPTOP_LEVEL_EXCEPTION_FILTER SetUnhandledExceptionFilter(
#   LPTOP_LEVEL_EXCEPTION_FILTER lpTopLevelExceptionFilter
# );
@winapi(cc=STDCALL, params={
    "lpTopLevelExceptionFilter": DWORD
})
def hook_SetUnhandledExceptionFilter(self, address, params):
    addr = params["lpTopLevelExceptionFilter"]
    handle = self.handle_manager.search("TopLevelExceptionHandler")
    if handle is None:
        handle = Handle(name="TopLevelExceptionHandler", obj=addr)
        self.handle_manager.append(handle)
    else:
        handle.obj = addr
    return 0


# _Post_equals_last_error_ DWORD GetLastError();
@winapi(cc=STDCALL, params={})
def hook_GetLastError(self, address, params):
    return self.last_error 


# void SetLastError(
#  DWORD dwErrCode
# );
@winapi(cc=STDCALL, params={
    "dwErrCode": UINT
})
def hook_SetLastError(self, address, params):
    self.last_error  = params['dwErrCode']
    return 0


# LONG UnhandledExceptionFilter(
#   _EXCEPTION_POINTERS *ExceptionInfo
# );
@winapi(cc=STDCALL, params={
    "ExceptionInfo": POINTER
})
def hook_UnhandledExceptionFilter(self, address, params):
    ret = 1
    return ret


# UINT SetErrorMode(
#   UINT uMode
# );
@winapi(cc=STDCALL, params={
    "uMode": UINT
})
def hook_SetErrorMode(self, address, params):
    # TODO maybe this need a better implementation
    return 0


# __analysis_noreturn VOID RaiseException(
#   DWORD           dwExceptionCode,
#   DWORD           dwExceptionFlags,
#   DWORD           nNumberOfArguments,
#   const ULONG_PTR *lpArguments
# );
@winapi(cc=STDCALL, params={
    "dwExceptionCode": DWORD,
    "dwExceptionFlags": DWORD,
    "nNumberOfArguments": DWORD,
    "lpArguments": POINTER
})
def hook_RaiseException(self, address, params):
    address = self.handle_manager.search("TopLevelExceptionHandler").obj
    old_pc = self.ql.reg.pc
    # TODO we should jump on the code
    # self.ql.stack_write(0, address)

    return 0


# PVOID AddVectoredExceptionHandler(
#   ULONG                       First,
#   PVECTORED_EXCEPTION_HANDLER Handler
# );
@winapi(cc=STDCALL, params={
    "First": UINT,
    "Handler": HANDLE
})
def hook_AddVectoredExceptionHandler(self, address, params):
    addr = params["Handler"]
    handle = self.handle_manager.search("VectoredHandler")
    if handle is None:
        handle = Handle(name="VectoredHandler", obj=addr)
        self.handle_manager.append(handle)
    else:
        handle.obj = addr
    return 0


# ULONG RemoveVectoredExceptionHandler(
#   PVOID Handle
# );
@winapi(cc=STDCALL, params={
    "Handler": HANDLE
})
def hook_RemoveVectoredExceptionHandler(self, address, params):
    handle = self.handle_manager.search("VectoredHandler")
    self.handle_manager.delete(handle.id)
    return 0
