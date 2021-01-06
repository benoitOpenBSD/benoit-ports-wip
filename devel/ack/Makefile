# $OpenBSD$

COMMENT =		the Amsterdam Compiler Kit

DISTNAME =		ack-20201009
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/davidgiven/ack

GH_ACCOUNT =		davidgiven
GH_PROJECT =		ack
GH_COMMIT =		7c51d86c4ebb688f32f7886a5c4fdd9b8129f05d

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
