#!/usr/bin/env python2.7
#
# Compute source files and include dirs for arduino toolchain.
# (c) 2015 Edd Barrett <edd@openbsd.org>

import sys
import os

LOCAL = "/usr/local/share/arduino/"
ASUPPORT = "arduino-support/"

def subst_f(e):
    return e.replace(LOCAL, ASUPPORT)

def _make_assign(make_var, itr):
    ls = [make_var + " ="] + list(itr)
    return " \\\n\t".join(ls) + "\n"

class CompilationInfo(object):
    def __init__(self, cxx_src, c_src, inc_dirs):
        self.cxx_src = set(cxx_src)
        self.c_src = set(c_src)
        self.inc_dirs = set(inc_dirs)

    def __add__(self, other):
        return CompilationInfo(self.cxx_src | other.cxx_src,
                               self.c_src | other.c_src,
                               self.inc_dirs | other.inc_dirs)
    def subst(self):
        r_cxx_src = set(map(subst_f, self.cxx_src))
        r_c_src = set(map(subst_f, self.c_src))
        r_inc_dirs = set(map(subst_f, self.inc_dirs))
        return CompilationInfo(r_cxx_src, r_c_src, r_inc_dirs)

    @classmethod
    def empty(cls):
        return cls([], [], [])

    # generate make source code assigning a make var
    def cxx_src_mk(self, var):
        return _make_assign(var, self.cxx_src)

    def c_src_mk(self, var):
        return _make_assign(var, self.c_src)

    def inc_dir_mk(self, var):
        return _make_assign(var, self.inc_dirs)

def intermediate_inc_dirs(stop_path, path):
    result = [path]
    while path != stop_path:
        path = os.path.dirname(path)
        result.append(path)
    return result

def collect_files(path, root=None):
    if root is None:
        root = path

    # we don't want examples included
    if os.path.basename(path) == "examples":
        return [], [], []

    cxx_src = []
    c_src = []
    inc_dirs = []

    ls = os.listdir(path)
    for f in ls:
        fpath = os.path.join(path, f)
        if os.path.isfile(fpath):
            if f.endswith(".cpp"):
                cxx_src.append(fpath)
            elif f.endswith(".c"):
                c_src.append(fpath)
            elif f.endswith(".h"):
                inc_dir = os.path.dirname(fpath)
                more_inc_dirs = intermediate_inc_dirs(root, inc_dir)
                inc_dirs.extend(more_inc_dirs)
        elif os.path.isdir(fpath):
            # recurse
            n_cxx_src, n_c_src, n_inc_dirs = collect_files(fpath, root)
            cxx_src.extend(n_cxx_src)
            c_src.extend(n_c_src)
            inc_dirs.extend(n_inc_dirs)

    return cxx_src, c_src, inc_dirs

def collect_libs(ad_base):
    # name * arch -> CompilationInfo
    lib_tab = {}
    lib_names = set()

    search =  {
        "common":   os.path.join(ad_base, "libraries"),
        "avr":      os.path.join(ad_base, "avr", "libraries"),
        "sam":      os.path.join(ad_base, "sam", "libraries"),
    }

    for arch, path in search.iteritems():
        ls = os.listdir(path)

        for fln in ls:
            full_path = os.path.join(path, fln)
            if os.path.isdir(full_path):
                cxx_src, c_src, inc_dirs = collect_files(full_path)
                lib_names |= set([fln])
                lib_tab[fln, arch] = \
                    CompilationInfo(cxx_src, c_src, inc_dirs)
            else:
                assert False # shouldn't happen
    return lib_tab, lib_names

def collect_cores(ad_base):
    core_tab = {}
    for arch in "avr", "sam":
        core_path = os.path.join(ad_base, arch, "cores", "arduino")
        cxx_src, c_src, inc_dirs = collect_files(core_path)
        core_tab[arch] = CompilationInfo(cxx_src, c_src, inc_dirs)
    return core_tab

MAKE_HEADER = "# Autogenerated! Do not manually edit.\n\n"

def emit_make_frag(lib_tab, lib_names, core_tab):
    with open("alibs.mk", "w") as mf:
        w = mf.write
        w(MAKE_HEADER)

        w("# Available libraries:\n")
        for lib in sorted(lib_names):
            w("#\t%s\n" % lib)
        w("\n")

        for lib in sorted(lib_names):
            for arch in ["avr", "sam"]:
                common_ci = lib_tab.get((lib, "common"), CompilationInfo.empty())
                plat_ci = lib_tab.get((lib, arch), CompilationInfo.empty())

                ci = (common_ci + plat_ci).subst()

                var_prefix = "%s_%s_" % (lib, arch)
                w("# %s for %s\n" % (lib, arch))
                w(ci.cxx_src_mk("%sCXX_SRC" % var_prefix))
                w(ci.c_src_mk("%sC_SRC" % var_prefix))
                w(ci.inc_dir_mk("%sINC_DIRS" % var_prefix))
                w("\n")

    with open("acores.mk", "w") as mf:
        w = mf.write
        w(MAKE_HEADER)

        for core_name, ci in core_tab.iteritems():
            ci = ci.subst()

            w("# %s core\n" % core_name)
            w(ci.cxx_src_mk("%s_CORE_CXX_SRC" % core_name))
            w(ci.c_src_mk("%s_CORE_C_SRC" % core_name))
            w(ci.inc_dir_mk("%s_CORE_INC_DIRS" % core_name))
            w("\n")

def main(ad_base):
    lib_tab, lib_names = collect_libs(ad_base)
    core_tab = collect_cores(ad_base)
    emit_make_frag(lib_tab, lib_names, core_tab)

ARDUINO_BASE = "/usr/local/share/arduino/"
if __name__ == "__main__":
    main(ARDUINO_BASE)
