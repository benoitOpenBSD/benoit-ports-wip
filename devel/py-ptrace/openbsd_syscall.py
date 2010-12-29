# OpenBSD kernel syscall list from OpenBSD 4.5-beta
#
# List extracted from:
#    /usr/include/sys/syscall.h
SYSCALL_NAMES = {
    0: "syscall",
    1: "exit",
    2: "fork",
    3: "read",
    4: "write",
    5: "open",
    6: "close",
    7: "wait4",
#   8:  compat_43 ocreat
    9: "link",
    10: "unlink",
#   11: obsolete execv
    12: "chdir",
    13: "fchdir",
    14: "mknod",
    15: "chmod",
    16: "chown",
    17: "break",
#   18: compat_25 ogetfsstat
#   19:  compat_43 olseek
    20: "getpid",
    21: "mount",
    22: "unmount",
    23: "setuid",
    24: "getuid",
    25: "geteuid",
    26: "ptrace",
    27: "recvmsg",
    28: "sendmsg",
    29: "recvfrom",
    30: "accept",
    31: "getpeername",
    32: "getsockname",
    33: "access",
    34: "chflags",
    35: "fchflags",
    36: "sync",
    37: "kill",
#   38:  compat_43 stat43
    39: "getppid",
#   40: compat_43 lstat43
    41: "dup",
    42: "opipe",
    43: "getegid",
    44: "profil",
    45: "ktrace",
    46: "sigaction",
    47: "getgid",
    48: "sigprocmask",
    49: "getlogin",
    50: "setlogin",
    51: "acct",
    52: "sigpending",
    53: "osigaltstack",
    54: "ioctl",
    55: "reboot",
    56: "revoke",
    57: "symlink",
    58: "readlink",
    59: "execve",
    60: "umask",
    61: "chroot",
#   62: compat_43 fstat43
#   63: compat_43 ogetkerninfo
#   64: compat_43 ogetpagesize
#   65: compat_25 omsync
    66: "vfork",
#   67: obsolete vread 
#   68: obsolete vwrite
    69: "sbrk",
    70: "sstk",
#   71: compat_43 ommap
#   72:  obsolete vadvise
    73: "munmap",
    74: "mprotect",
    75: "madvise",
#   76: obsolete vhangup
#   77: obsolete vlimit
    78: "mincore",
    79: "getgroups",
    80: "setgroups",
    81: "getpgrp",
    82: "setpgid",
    83: "setitimer",
#   84: compat_43 owait
#   85: compat_25 swapon
    86: "getitimer",
#   87: compat_43 ogethostname
#   88: compat_43 osethostname
#   89: compat_43 ogetdtablesize
    90: "dup2",
    92: "fcntl",
    93: "select",
    95: "fsync",
    96: "setpriority",
    97: "socket",
    98: "connect",
#   99: compat_43 oaccept
    100: "getpriority",
#   101: compat_43 osend
#   102: compat_43 orecv
    103: "sigreturn",
    104: "bind",
    105: "setsockopt",
    106: "listen",
#   107: obsolete vtimes
#   108: compat_43 osigvec
#   109: compat_43 psigblock
#   110: compat_43 osigsetmask
    111: "sigsuspend",
#   112: compat_43 osigstack
#   113: compat_43 orecvmsg
#   114: compat_43 osendmsg
#   115: obsolete vtrace
    116: "gettimeofday",
    117: "getrusage",
    118: "getsockopt",
#   119: obsolete resuba
    120: "readv",
    121: "writev",
    122: "settimeofday",
    123: "fchown",
    124: "fchmod",
#   125:  compat_43 orecvfrom
    126: "setreuid",
    127: "setregid",
    128: "rename",
#   129: compat_43 otruncate
#   130: compat_43 oftruncate
    131: "flock",
    132: "mkfifo",
    133: "sendto",
    134: "shutdown",
    135: "socketpair",
    136: "mkdir",
    137: "rmdir",
    138: "utimes",
#   139: obsolete 4.2 sigreturn
    140: "adjtime",
#   141: compat_43 ogetpeername
#   142: compat_43 ogethostid
#   143: compat_43 osethostid
#   144: compat_43 ogetrlimit
#   145: compat_43 osetrlimit
#   146: compat_43 okillpg
    147: "setsid",
    148: "quotactl",
#   149: compat_43 oquota
#   150: compat_43 ogetsockname
    155: "nfssvc",
#   156: compat_43 ogetdirentries
#   157: compat_25 ostatfs
#   158: compat_25 ostatfs
    161: "getfh",
#   162: compat_09 ogetdomainname
#   163: compat_09 osetdomainname
    165: "sysarch",
#   169: compat_10 osemsys
#   170: compat_10 omsgsys
#   171: compat_10 oshmsys
    173: "pread",
    174: "pwrite",
    181: "setgid",
    182: "setegid",
    183: "seteuid",
    184: "lfs_bmapv",
    185: "lfs_markv",
    186: "lfs_segclean",
    187: "lfs_segwait",
#   188: compat_35 stat35
#   189: compat_35 fstat35 
#   190: compat_35 lstat35
    191: "pathconf",
    192: "fpathconf",
    193: "swapctl",
    194: "getrlimit",
    195: "setrlimit",
    196: "getdirentries",
    197: "mmap",
    198: "__syscall",
    199: "lseek",
    200: "truncate",
    201: "ftruncate",
    202: "__sysctl",
    203: "mlock",
    204: "munlock",
    206: "futimes",
    207: "getpgid",
    208: "xfspioctl",
#   220: compat_23 semctl23
    221: "semget",
#   222: compat_35 semop 
#   223: obsolete sys_semconfig
#   224: compat_23 msgctl23
    225: "msgget",
    226: "msgsnd",
    227: "msgrcv",
    228: "shmat",
#   229: compat_23 shmctl23
    230: "shmdt",
#   231: compat_35 shmget
    232: "clock_gettime",
    233: "clock_settime",
    234: "clock_getres",
    240: "nanosleep",
    250: "minherit",
    251: "rfork",
    252: "poll",
    253: "issetugid",
    254: "lchown",
    255: "getsid",
    256: "msync",
#   257: compat_35 semctl35
#   258: compat_35 shmctl35
#   259: compat_35 msgctl35
#   260: compat_o43 getfsstat
#   261: compat_o43 statfs
#   262: compat_o43 fstatfs
    263: "pipe",
    264: "fhopen",
#   265: compat_35 fhstat
#   266: compat_o43 fhstatfs
    267: "preadv",
    268: "pwritev",
    269: "kqueue",
    270: "kevent",
    271: "mlockall",
    272: "munlockall",
    273: "getpeereid",
    281: "getresuid",
    282: "setresuid",
    283: "getresgid",
    284: "setresgid",
#   285: obsolete sys_omquery
    286: "mquery",
    287: "closefrom",
    288: "sigaltstack",
    289: "shmget",
    289: "preadv",
    290: "semop",
    291: "stat",
    292: "fstat",
    293: "lstat",
    294: "fhstat",
    295: "__semctl",
    296: "shmctl",
    297: "msgctl",
    298: "sched_yield",
    299: "getthrid",
    300: "thrsleep",
    301: "thrwakeup",
    302: "threxit",
    303: "thrsigdivert",
    304: "__getcwd",
    305: "adjfreq",
    306: "getfsstat",
    307: "statfs",
    308: "fstatfs",
    309: "fhstatfs",
}
