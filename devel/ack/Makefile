
COMMENT =		the Amsterdam Compiler Kit

DISTNAME =		ack-20261102
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE =	Yes

SITES =			${SITES_GITHUB}

HOMEPAGE =		https://github.com/davidgiven/ack

GH_ACCOUNT =		davidgiven
GH_PROJECT =		ack
GH_COMMIT =		c9bccd0f07212a4ea98ef04bec2db82306886e6e

WANTLIB +=		c

COMPILER =		ports-gcc
COMPILER_LANGS =	c

MODULES =		gcc \
			devel/cmake \
			lang/lua

USE_GMAKE =		Yes
MAKE_FLAGS =		BUILDDIR=${WRKSRC}/ack-build PREFIX=/usr/local/ack

CFLAGS +=		-DUNREACHABLE_CODE="__builtin_unreachable()" \
			-DNORETURN=_Noreturn
        
BUILD_DEPENDS =		devel/libconfig \
			devel/luaposix

NO_TEST =		Yes

do-install:
			${INSTALL_DATA_DIR} ${PREFIX}/ack
			${INSTALL_DATA_DIR} ${PREFIX}/ack/{bin,lib,share}
			${INSTALL_PROGRAM} ${WRKSRC}/ack-build/staging/bin/* ${PREFIX}/ack/bin/
			cp -R ${WRKSRC}/ack-build/staging/lib/* ${PREFIX}/ack/lib/
			cp -R ${WRKSRC}/ack-build/staging/share/* ${PREFIX}/ack/share/
			
.include <bsd.port.mk>
