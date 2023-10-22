
COMMENT=	very fast free Verilog HDL simulator

DISTNAME =	verilator-4.032
CATEGORIES=	lang devel

HOMEPAGE=	https://www.veripool.org/wiki/verilator/Intro

# LGPLv3 or Perl
PERMIT_PACKAGE=	Yes

SITES =			https://www.veripool.org/ftp/
EXTRACT_SUFX=		.tgz

WANTLIB=		c m ${COMPILER_LIBCXX}

COMPILER =		base-clang ports-gcc base-gcc

BUILD_DEPENDS +=	devel/bison

CONFIGURE_STYLE=	gnu
MAKE_FLAGS=		VERILATOR_ROOT=${PREFIX}/share/verilator/ \
			COPT="${CFLAGS}"

USE_GMAKE=		Yes

TEST_TARGET=		test
TEST_FLAGS=		VERILATOR_ROOT=${WRKSRC} VERILATOR_MAKE=${MAKE_PROGRAM}

.include <bsd.port.mk>
