#!/usr/bin/env python3
#
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#

# cols = ("arm64", "x8664")

from qiling.const import QL_ARCH
from qiling.os.posix.posix import SYSCALL_PREF


def map_syscall(ql, syscall_num):
    for k, v in syscall_table.items():
        if ql.archtype == QL_ARCH.X8664:
            if syscall_num >= 0x2000000 and syscall_num <= 0x3000000:
                syscall_num = syscall_num - 0x2000000

            if v[0] == syscall_num:
                return f"{SYSCALL_PREF}{k}"

        elif ql.archtype == QL_ARCH.ARM64:
            if syscall_num >= 0xFFFFFFFFFFFFFF00:
                syscall_num = syscall_num - 0xFFFFFFFFFFFFFF00

            if v[1] == syscall_num:
                return f"{SYSCALL_PREF}{k}"


syscall_table = {
    "kernelrpc_mach_vm_allocate_trap": (0x100000A, -1),
    "kernelrpc_mach_vm_deallocate_trap": (0x100000C, -1),
    "kernelrpc_mach_vm_map_trap": (0x100000F, -1),
    "kernelrpc_mach_port_deallocate_trap": (0x1000012, -1),
    "kernelrpc_mach_port_mod_refs_trap": (0x1000013, -1),
    "kernelrpc_mach_port_construct_trap": (0x1000018, -1),
    "mach_reply_port": (0x100001A, -1),
    "thread_self_trap": (0x100001B, -1),
    "task_self_trap": (0x100001C, -1),
    "host_self_trap": (0x100001D, -1),
    "mach_msg_trap": (0x100001F, -1),
    "thread_fast_set_cthread_self64": (0x3000003, -1),
    # FIXME: Lets fix this later
    # "kernelrpc_mach_vm_allocate_trap": (-1, 9),
    # "kernelrpc_mach_vm_deallocate_trap": (-1, 11),
    # "kernelrpc_mach_vm_protect_trap": (-1, 13),
    # "kernelrpc_mach_vm_map_trap": (-1, 14),
    # "kernelrpc_mach_port_destroy_trap": (-1, 16),
    # "kernelrpc_mach_port_deallocate_trap": (-1, 17),
    # "kernelrpc_mach_port_mod_refs_trap": (-1, 18),
    # "kernelrpc_mach_port_move_member_trap": (-1, 19),
    # "kernelrpc_mach_port_insert_right_trap": (-1, 20),
    # "kernelrpc_mach_port_insert_member_trap": (-1, 21),
    # "kernelrpc_mach_port_extract_member_trap": (-1, 22),
    # "kernelrpc_mach_port_construct_trap": (-1, 23),
    # "kernelrpc_mach_port_destruct_trap": (-1, 24),
    "nosys": (379, -1),
    "exit": (1, 1),
    "fork": (2, 2),
    "read": (3, 3),
    "write_nocancel": (397, 397),
    "write": (4, 4),
    "open": (5, 5),
    "close": (6, 6),
    "wait4": (7, 7),
    "link": (9, -1),
    "unlink": (10, 10),
    "chdir": (12, 12),
    "fchdir": (13, -1),
    "mknod": (14, -1),
    "chmod": (15, 15),
    "chown": (16, -1),
    "getfsstat": (18, 347),
    "getpid": (20, -1),
    "setuid": (23, -1),
    "getuid": (24, -1),
    "geteuid": (25, 25),
    "ptrace": (26, -1),
    "recvmsg": (27, 27),
    "sendmsg": (28, 28),
    "recvfrom": (29, 29),
    "accept": (30, 30),
    "getpeername": (31, 31),
    "getsockname": (32, 32),
    "access_macos": (33, 33),
    "chflags": (34, 34),
    "fchflags": (35, 35),
    "sync": (36, -1),
    "kill": (37, 37),
    "getppid": (39, 39),
    "dup": (41, -1),
    "pipe": (42, -1),
    "getegid": (43, 43),
    "profil": (44, -1),
    "sigaction": (46, 46),
    "getgid": (47, 47),
    "sigprocmask": (48, -1),
    "getlogin": (49, 49),
    "setlogin": (50, 50),
    "acct": (51, 51),
    "sigpending": (52, -1),
    "sigaltstack": (53, 53),
    "ioctl": (54, 54),
    "reboot": (55, 55),
    "revoke": (56, 56),
    "symlink": (57, 57),
    "readlink": (58, 58),
    "execve": (59, 59),
    "umask": (60, -1),
    "chroot": (61, 61),
    "msync": (65, 65),
    "vfork": (66, -1),
    "munmap": (73, 73),
    "mprotect": (74, 74),
    "madvise": (75, 75),
    "mincore": (78, 78),
    "getgroups": (79, 79),
    "setgroups": (80, 80),
    "getpgrp": (81, 81),
    "setpgid": (82, 82),
    "setitimer": (83, 83),
    "int": (224, -1),
    "getitimer": (86, 86),
    "getdtablesize": (89, 89),
    "dup2": (90, 90),
    "fcntl64_macos": (92, 92),
    "select": (93, 93),
    "fsync": (95, 95),
    "setpriority": (96, 96),
    "socket": (97, 97),
    "connect": (98, 98),
    "getpriority": (100, 100),
    "bind": (104, 104),
    "setsockopt": (105, 105),
    "listen": (106, 106),
    "sigsuspend": (111, 111),
    "gettimeofday": (116, -1),
    "getrusage": (117, 117),
    "getsockopt": (118, 118),
    "readv": (120, 120),
    "writev": (121, 121),
    "settimeofday": (122, 122),
    "fchown": (123, 123),
    "fchmod": (124, 124),
    "setreuid": (126, 126),
    "setregid": (127, 127),
    "rename": (128, 128),
    "flock": (131, 131),
    "mkfifo": (132, 132),
    "sendto": (133, 133),
    "shutdown": (134, 134),
    "socketpair": (135, 135),
    "mkdir": (136, 136),
    "rmdir": (137, 137),
    "utimes": (138, 138),
    "futimes": (139, 139),
    "adjtime": (140, 140),
    "gethostuuid": (142, 142),
    "setsid": (147, 147),
    "getpgid": (151, 151),
    "setprivexec": (152, 152),
    "pread": (153, 153),
    "pwrite": (154, 154),
    "nfssvc": (155, 155),
    "statfs": (157, 345),
    "fstatfs": (158, 346),
    "unmount": (159, 159),
    "getfh": (161, 161),
    "quotactl": (165, 165),
    "mount": (167, 167),
    "csops": (169, 169),
    "waitid": (173, 173),
    "add_profil": (176, -1),
    "setgid": (181, 181),
    "setegid": (182, 182),
    "seteuid": (183, 183),
    "sigreturn": (184, 184),
    "fdatasync": (187, 187),
    "stat": (188, 338),
    "fstat": (189, 339),
    "lstat": (190, 340),
    "pathconf": (191, 191),
    "fpathconf": (192, 192),
    "getrlimit": (194, 194),
    "setrlimit": (195, 195),
    "getdirentries": (196, 196),
    "mmap2": (197, 197),
    "lseek": (199, 199),
    "truncate": (200, 200),
    "ftruncate": (201, 201),
    "mlock": (203, 203),
    "munlock": (204, 204),
    "undelete": (205, 205),
    "ATsocket": (206, -1),
    "ATgetmsg": (207, -1),
    "ATputmsg": (208, -1),
    "ATPsndreq": (209, -1),
    "ATPsndrsp": (210, -1),
    "ATPgetreq": (211, -1),
    "ATPgetrsp": (212, -1),
    "mkcomplex": (216, -1),
    "statv": (217, -1),
    "lstatv": (218, -1),
    "fstatv": (219, -1),
    "getattrlist": (220, 220),
    "setattrlist": (221, 221),
    "getdirentriesattr": (222, 222),
    "exchangedata": (223, 223),
    "searchfs": (225, 225),
    "delete": (226, 226),
    "copyfile": (227, 227),
    "fgetattrlist": (228, 228),
    "fsetattrlist": (229, 229),
    "poll": (230, 230),
    "watchevent": (231, 231),
    "waitevent": (232, 232),
    "modwatch": (233, 233),
    "getxattr": (234, 234),
    "fgetxattr": (235, 235),
    "setxattr": (236, 236),
    "fsetxattr": (237, 237),
    "removexattr": (238, 238),
    "fremovexattr": (239, 239),
    "listxattr": (240, 240),
    "flistxattr": (241, 241),
    "fsctl": (242, 242),
    "initgroups": (243, 243),
    "posix_spawn": (244, 244),
    "ffsctl": (245, 245),
    "nfsclnt": (247, 247),
    "fhopen": (248, 248),
    "minherit": (250, 250),
    "semsys": (251, 251),
    "msgsys": (252, 252),
    "shmsys": (253, 253),
    "semctl": (254, 254),
    "semget": (255, 255),
    "semop": (256, 256),
    "msgctl": (258, 258),
    "msgget": (259, 259),
    "msgsnd": (260, 260),
    "msgrcv": (261, 261),
    "shmat": (262, 262),
    "shmctl": (263, 263),
    "shmdt": (264, 264),
    "shmget": (265, 265),
    "shm_open": (266, 266),
    "shm_unlink": (267, 267),
    "sem_open": (268, 268),
    "sem_close": (269, 269),
    "sem_unlink": (270, 270),
    "sem_wait": (271, 271),
    "sem_trywait": (272, 272),
    "sem_post": (273, 273),
    "sem_getvalue": (274, -1),
    "sem_init": (275, -1),
    "sem_destroy": (276, -1),
    "open_extended": (277, 277),
    "umask_extended": (278, 278),
    "stat_extended": (279, 279),
    "lstat_extended": (280, 280),
    "fstat_extended": (281, 281),
    "chmod_extended": (282, 282),
    "fchmod_extended": (283, 283),
    "access_extended": (284, 284),
    "settid": (285, 285),
    "gettid": (286, 286),
    "setsgroups": (287, 287),
    "getsgroups": (288, 288),
    "setwgroups": (289, 289),
    "getwgroups": (290, 290),
    "mkfifo_extended": (291, 291),
    "mkdir_extended": (292, 292),
    "identitysvc": (293, 293),
    "shared_region_check_np": (294, 294),
    "shared_region_map_np": (295, -1),
    "vm_pressure_monitor": (296, 296),
    "psynch_rw_longrdlock": (297, 297),
    "psynch_rw_yieldwrlock": (298, 298),
    "psynch_rw_downgrade": (299, 299),
    "psynch_rw_upgrade": (300, 300),
    "psynch_mutexwait": (301, 301),
    "psynch_mutexdrop": (302, 302),
    "psynch_cvbroad": (303, 303),
    "psynch_cvsignal": (304, 304),
    "psynch_cvwait": (305, 305),
    "psynch_rw_rdlock": (306, 306),
    "psynch_rw_wrlock": (307, 307),
    "psynch_rw_unlock": (308, 308),
    "psynch_rw_unlock2": (309, 309),
    "getsid": (310, 310),
    "settid_with_pid": (311, 311),
    "aio_fsync": (313, 313),
    "user_ssize_t": (314, -1),
    "aio_suspend": (315, 315),
    "aio_cancel": (316, 316),
    "aio_error": (317, 317),
    "aio_read": (318, 318),
    "aio_write": (319, 319),
    "lio_listio": (320, 320),
    "iopolicysys": (322, 322),
    "mlockall": (324, 324),
    "munlockall": (325, 325),
    "issetugid": (327, 327),
    "pthread_kill": (328, 328),
    "pthread_sigmask": (329, 329),
    "sigwait": (330, 330),
    "disable_threadsignal": (331, 331),
    "pthread_markcancel": (332, 332),
    "pthread_canceled": (333, 333),
    "semwait_signal": (334, 334),
    "proc_info": (336, 336),
    "sendfile": (337, 337),
    "stat64": (338, -1),
    "fstat64": (339, -1),
    "lstat64": (340, -1),
    "stat64_extended": (341, 341),
    "lstat64_extended": (342, 342),
    "fstat64_extended": (343, 343),
    "getdirentries64": (344, 344),
    "statfs64": (345, -1),
    "fstatfs64": (346, -1),
    "getfsstat64": (347, -1),
    "pthread_chdir": (348, 348),
    "pthread_fchdir": (349, 349),
    "audit": (350, 350),
    "auditon": (351, 351),
    "getauid": (353, 353),
    "setauid": (354, 354),
    "getaudit": (355, -1),
    "setaudit": (356, -1),
    "getaudit_addr": (357, 357),
    "setaudit_addr": (358, 358),
    "auditctl": (359, 359),
    "bsdthread_create": (360, 360),
    "bsdthread_terminate": (361, 361),
    "kqueue": (362, 362),
    "kevent": (363, 363),
    "lchown": (364, 364),
    "stack_snapshot": (365, 365),
    "bsdthread_register": (366, 366),
    "workq_open": (367, 367),
    "workq_kernreturn": (368, 368),
    "kevent64": (369, 369),
    "old_semwait_signal": (370, 370),
    "old_semwait_signal_nocancel": (371, 371),
    "thread_selfid": (372, 372),
    "mac_execve": (380, 380),
    "mac_syscall": (381, 381),
    "mac_get_file": (382, 382),
    "mac_set_file": (383, 383),
    "mac_get_link": (384, 384),
    "mac_set_link": (385, 385),
    "mac_get_proc": (386, 386),
    "mac_set_proc": (387, 387),
    "mac_get_fd": (388, 388),
    "mac_set_fd": (389, 389),
    "mac_get_pid": (390, 390),
    "mac_get_lcid": (391, -1),
    "mac_get_lctx": (392, -1),
    "mac_set_lctx": (393, -1),
    "setlcid": (394, -1),
    "getlcid": (395, -1),
    "read_nocancel": (396, 396),
    "open_nocancel": (398, 398),
    "close_nocancel": (399, 399),
    "wait4_nocancel": (400, 400),
    "recvmsg_nocancel": (401, 401),
    "sendmsg_nocancel": (402, 402),
    "recvfrom_nocancel": (403, 403),
    "accept_nocancel": (404, 404),
    "msync_nocancel": (405, 405),
    "fcntl_nocancel": (406, 406),
    "select_nocancel": (407, 407),
    "fsync_nocancel": (408, 408),
    "connect_nocancel": (409, 409),
    "sigsuspend_nocancel": (410, 410),
    "readv_nocancel": (411, 411),
    "writev_nocancel": (412, 412),
    "sendto_nocancel": (413, 413),
    "pread_nocancel": (414, 414),
    "pwrite_nocancel": (415, 415),
    "waitid_nocancel": (416, 416),
    "poll_nocancel": (417, 417),
    "msgsnd_nocancel": (418, 418),
    "msgrcv_nocancel": (419, 419),
    "sem_wait_nocancel": (420, 420),
    "aio_suspend_nocancel": (421, 421),
    "sigwait_nocancel": (422, 422),
    "semwait_signal_nocancel": (423, 423),
    "mac_mount": (424, 424),
    "mac_get_mount": (425, 425),
    "mac_getfsstat": (426, 426),
    "fsgetpath": (427, 427),
    "audit_session_self": (428, 428),
    "audit_session_join": (429, 429),
    # "thread_self_trap": (-1, 26),
    "semaphore_wait_signal_trap": (-1, 36),
    "semaphore_timedwait_signal_trap": (-1, 38),
    "kernelrpc_mach_port_guard_trap": (-1, 40),
    "kernelrpc_mach_port_unguard_trap": (-1, 41),
    "task_for_pid": (-1, 44),
    "pid_for_task": (-1, 45),
    "macx_swapoff": (-1, 48),
    "macx_backing_store_recovery": (-1, 52),
    "syscall_thread_switch": (-1, 60),
    "swapon": (-1, 85),
    "mach_timebase_info": (-1, 88),
    "mk_timer_destroy": (-1, 91),
    "setquota": (-1, 148),
    "quota": (-1, 149),
    "csops_audittoken": (-1, 170),
    "kdebug_trace_string": (-1, 178),
    "kdebug_trace64": (-1, 179),
    "kdebug_trace": (-1, 180),
    "chud": (-1, 185),
    "sysctl": (-1, 202),
    "open_dprotected_np": (-1, 216),
    "sysctlbyname": (-1, 274),
    "psynch_cvclrprepost": (-1, 312),
    "aio_return": (-1, 314),
    "process_policy": (-1, 323),
    "ledger": (-1, 373),
    "kevent_qos": (-1, 374),
    "fileport_makeport": (-1, 430),
    "fileport_makefd": (-1, 431),
    "audit_session_port": (-1, 432),
    "pid_suspend": (-1, 433),
    "pid_resume": (-1, 434),
    "pid_hibernate": (-1, 435),
    "pid_shutdown_sockets": (-1, 436),
    "shared_region_map_and_slide_np": (-1, 438),
    "kas_info": (-1, 439),
    "memorystatus_control": (-1, 440),
    "guarded_open_np": (-1, 441),
    "guarded_close_np": (-1, 442),
    "guarded_kqueue_np": (-1, 443),
    "change_fdguard_np": (-1, 444),
    "proc_rlimit_control": (-1, 446),
    "connectx": (-1, 447),
    "disconnectx": (-1, 448),
    "peeloff": (-1, 449),
    "socket_delegate": (-1, 450),
    "telemetry": (-1, 451),
    "proc_uuid_policy": (-1, 452),
    "memorystatus_get_level": (-1, 453),
    "system_override": (-1, 454),
    "vfs_purge": (-1, 455),
    "sfi_ctl": (-1, 456),
    "sfi_pidctl": (-1, 457),
    "coalition": (-1, 458),
    "coalition_info": (-1, 459),
    "necp_match_policy": (-1, 460),
    "getattrlistbulk": (-1, 461),
    "openat": (-1, 463),
    "openat_nocancel": (-1, 464),
    "renameat": (-1, 465),
    "faccessat": (-1, 466),
    "fchmodat": (-1, 467),
    "fchownat": (-1, 468),
    "fstatat": (-1, 470),
    "linkat": (-1, 471),
    "unlinkat": (-1, 472),
    "readlinkat": (-1, 473),
    "symlinkat": (-1, 474),
    "mkdirat": (-1, 475),
    "getattrlistat": (-1, 476),
    "proc_trace_log": (-1, 477),
    "bsdthread_ctl": (-1, 478),
    "openbyid_np": (-1, 479),
    "recvmsg_x": (-1, 480),
    "sendmsg_x": (-1, 481),
    "thread_selfusage": (-1, 482),
    "csrctl": (483, 483),
    "guarded_open_dprotected_np": (-1, 484),
    "guarded_write_np": (-1, 485),
    "guarded_pwrite_np": (-1, 486),
    "guarded_writev_np": (-1, 487),
    "rename_ext": (-1, 488),
    "mremap_encrypted": (-1, 489),
    "netagent_trigger": (-1, 490),
    "stack_snapshot_with_config": (-1, 491),
    "microstackshot": (-1, 492),
    "grab_pgo_data": (-1, 493),
    "work_interval_ctl": (-1, 499),
    "abort_with_payload": (521, -1),
    "terminate_with_payload": (520, -1),
    "getentropy": (500, -1),
}
