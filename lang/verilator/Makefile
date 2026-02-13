COMMENT=	very fast free Verilog HDL simulator

V =		5.044
DISTNAME =	verilator-${V}
CATEGORIES=	lang devel

HOMEPAGE=	https://www.veripool.org/wiki/verilator/Intro

# LGPLv3 or Perl
PERMIT_PACKAGE=	Yes

SITES=			https://github.com/verilator/verilator/archive/refs/tags/
DISTFILES=		v${V}.tar.gz

WANTLIB=		c m ${COMPILER_LIBCXX}

COMPILER =		base-clang ports-gcc base-gcc

BUILD_DEPENDS +=	devel/bison \
			devel/help2man

MAKE_FLAGS=		VERILATOR_ROOT=${PREFIX}/share/verilator/ \
			COPT="${CFLAGS}"

AUTOCONF_VERSION =	2.72
AUTOMAKE_VERSION =	1.17
CONFIGURE_STYLE =	gnu

MAKE_ENV +=		AUTOCONF_VERSION=${AUTOCONF_VERSION} \
			AUTOMAKE_VERSION=${AUTOMAKE_VERSION} \
			YACC="${LOCALBASE}/bin/bison" \
			LEX="${LOCALBASE}/bin/flex"

CONFIGURE_STYLE =	gnu
CONFIGURE_ENV +=	YACC="${LOCALBASE}/bin/bison" \
			LEX="${LOCALBASE}/bin/flex"

USE_GMAKE=		Yes

TEST_TARGET=		test
TEST_FLAGS=		VERILATOR_ROOT=${WRKSRC}

pre-configure:
	cd ${WRKSRC} && ${LOCALBASE}/bin/autoconf-${AUTOCONF_VERSION}

.include <bsd.port.mk>
