# Should work on all archs with Ada and LLVM.
# But... version 3.0.0 doesn't work with LLVM 16.
# mcode backend only works on amd64 and i386.
# XXX: Recheck next update
ONLY_FOR_ARCHS =	amd64 i386

COMMENT =	VHDL 2008/93/87 simulator
CATEGORIES =	lang

SHARED_LIBS +=	ghdl-3_0_0                0.0 # 0.0
SHARED_LIBS +=	ghdlvpi                   0.0 # 0.0
SHARED_LIBS +=	ghw                       0.0 # 0.0

GH_ACCOUNT =	ghdl
GH_PROJECT =	ghdl
GH_TAGNAME =	v3.0.0

HOMEPAGE =	https://ghdl.github.io/ghdl/

# GPLv2+
PERMIT_PACKAGE =	Yes

WANTLIB += c m pthread z

# Requires Ada
COMPILER =	ports-gcc
COMPILER_LANGS =	c

# libgdhl-3_0_0.so links libgnat-8.so
LIB_DEPENDS =	lang/gcc/${MODGCC4_VERSION},-ada

CONFIGURE_STYLE =	simple
# XXX: Not yet, see top comment.
#CONFIGURE_ARGS =	--with-llvm-config="/usr/bin/llvm-config"

USE_GMAKE =	Yes
MAKE_FLAGS =	CC="${CC}" ADA_FLAGS="${CFLAGS}"

do-gen:
	sed -i -e 's,LIBghdl_VERSION,${LIBghdl-3_0_0_VERSION},g' \
		-e 's,LIBghdlvpi_VERSION,${LIBghdlvpi_VERSION},g' \
		-e 's,LIBghw_VERSION,${LIBghw_VERSION},g' \
		${WRKSRC}/Makefile.in

.include <bsd.port.mk>
