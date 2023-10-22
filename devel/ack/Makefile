
COMMENT =		the Amsterdam Compiler Kit

DISTNAME =		ack-20210504
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE =	Yes

SITES =			${SITES_GITHUB}

HOMEPAGE =		https://github.com/davidgiven/ack

GH_ACCOUNT =		davidgiven
GH_PROJECT =		ack
GH_COMMIT =		8b53004031c3b44063c2260ebf352eaae643b23f

WANTLIB +=		c

USE_GMAKE =		Yes
MAKE_FLAGS =		BUILDDIR=${WRKSRC}/ack-build PREFIX=/usr/local/ack

NO_TEST =		Yes

do-install:
			${INSTALL_DATA_DIR} ${PREFIX}/ack
			${INSTALL_DATA_DIR} ${PREFIX}/ack/{bin,lib,share}
			${INSTALL_PROGRAM} ${WRKSRC}/ack-build/staging/bin/* ${PREFIX}/ack/bin/
			cp -R ${WRKSRC}/ack-build/staging/lib/* ${PREFIX}/ack/lib/
			cp -R ${WRKSRC}/ack-build/staging/share/* ${PREFIX}/ack/share/
			
.include <bsd.port.mk>
