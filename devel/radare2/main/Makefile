# $OpenBSD: Makefile,v 1.5 2016/04/04 22:57:45 naddy Exp $

COMMENT =		reverse engineers disassembler and debugger

DISTNAME =		radare2-${V}

# In radare, all libs have the same version
LIBV =			2.0	# 0.10.2
.for _lib in r_anal r_asm r_bin r_bp r_config r_cons r_core r_crypto r_db \
	r_debug r_egg r_flags r_fs r_hash r_io r_lang \
	r_magic r_parse r_reg r_search r_socket r_syscall \
	r_util
SHARED_LIBS+=		${_lib} ${LIBV}
.endfor

EXTRACT_SUFX =		.tar.xz

WANTLIB =		c crypto m pthread ssl

CONFIGURE_ARGS +=	--with-libversion=${LIBV} \
			--mandir=${PREFIX}/man

.include <bsd.port.mk>

WARNING: didn't find any library to match SHARED_LIBS r_cmd
WARNING: didn't find any library to match SHARED_LIBS r_diff
WARNING: didn't find any library to match SHARED_LIBS r_lib
WARNING: didn't find any library to match SHARED_LIBS r_line
WARNING: didn't find any library to match SHARED_LIBS r_print
WARNING: didn't find any library to match SHARED_LIBS r_sign
WARNING: didn't find any library to match SHARED_LIBS r_th
