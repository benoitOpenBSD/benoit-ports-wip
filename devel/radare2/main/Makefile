# $OpenBSD: Makefile,v 1.2 2011/11/07 22:06:47 edd Exp $

COMMENT =		reverse engineers disassembler and debugger

DISTNAME =		radare2-${V}

# In radare, all libs have the same version
LIBV =			2.0	# 0.9.6
.for _lib in r_anal r_asm r_bin r_bp r_cmd r_config r_cons r_core r_db \
	r_debug r_diff r_egg r_flags r_fs r_hash r_io r_lang r_lib \
	r_magic r_parse r_reg r_search r_sign r_socket r_syscall \
	r_util r_crypto
SHARED_LIBS+=		${_lib} ${LIBV}
.endfor

WANTLIB =		c m pthread

CONFIGURE_ARGS +=	--with-libversion=${LIBV} \
			--mandir=${PREFIX}/man

.include <bsd.port.mk>
