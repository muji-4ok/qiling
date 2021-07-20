#!/usr/bin/env python3
#
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#


from qiling.const import *
from qiling.os.linux.thread import *
from qiling.os.posix.filestruct import *
from qiling.os.filestruct import *
from qiling.os.posix.const import *
from qiling.os.posix.const_mapping import *
from qiling.exception import *


def ql_syscall_sendfile64(ql, sendfile64_out_fd, sendfile64_in_fd, sendfile64_offest, sendfile64_count, *args, **kw):
    if (
        0 <= sendfile64_out_fd < NR_OPEN
        and 0 <= sendfile64_in_fd < NR_OPEN
        and ql.os.fd[sendfile64_out_fd] != 0
        and ql.os.fd[sendfile64_in_fd] != 0
    ):
        ql.os.fd[sendfile64_in_fd].lseek(ql.unpack32(ql.mem.read(sendfile64_offest, 4)))
        buf = ql.os.fd[sendfile64_in_fd].read(sendfile64_count)
        regreturn = ql.os.fd[sendfile64_out_fd].write(buf)
    else:
        regreturn = -1
    return regreturn
