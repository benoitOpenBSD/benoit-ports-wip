
COMMENT =		z80 CPU emulation library

DISTNAME =		libz80ex-v1.1.22-200603
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

SHARED_LIBS =		libz80ex 1.1.22

# GPL-2.0
PERMIT_PACKAGE =	Yes

HOMEPAGE =		https://github.com/wyan/libz80ex

SITES =			${SITES_GITHUB}

GH_ACCOUNT =            wyan
GH_PROJECT =            libz80ex
GH_COMMIT =             c84c78a355f6e7f5fa97434c8486c66a7dee965a

COMPILER=               base-clang ports-gcc
COMPILER_LANGS =	c

USE_GMAKE =		Yes
AKE_FLAGS =		CFLAGS="${CFLAGS}" \
			CXXFLAGS="${CXXFLAGS}" \
			CXX="${CXX}"

NO_TEST =		Yes

.include <bsd.port.mk>
