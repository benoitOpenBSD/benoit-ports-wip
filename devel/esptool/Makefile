# $OpenBSD$

COMMENT =	creation and handling of firmware for the ESP8266

V =		0.0.2
PKGNAME =	esptool-${V}
DISTNAME =	esptool-ck-${V}
CATEGORIES =	devel

HOMEPAGE =	https://github.com/tommie/esptool-ck

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

WANTLIB =		c

MASTER_SITES =          ${MASTER_SITES_GITHUB}
GH_ACCOUNT =            tommie
GH_PROJECT =            esptool-ck
GH_TAGNAME =            v$V

USE_GMAKE =		Yes
MAKE_FLAGS =		CC="${CC}" CFLAGS="${CFLAGS}"

do-install:
		${INSTALL_PROGRAM} ${WRKSRC}/esptool ${PREFIX}/bin
		${INSTALL_DATA_DIR} ${PREFIX}/share/doc/esptool
		${INSTALL_DATA} ${WRKSRC}/LICENSE ${WRKSRC}/README \
			${PREFIX}/share/doc/esptool

NO_TEST =		Yes

.include <bsd.port.mk>
