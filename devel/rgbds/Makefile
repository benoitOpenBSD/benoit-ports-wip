# $OpenBSD$

COMMENT =		rednex Game Boy Development System

DISTNAME =		rgbds-0.3.3
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# MIT / ISC / BSD
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/rednex/rgbds

GH_ACCOUNT =		rednex
GH_PROJECT =		rgbds
GH_TAGNAME =		v0.3.3

WANTLIB +=		c m png z

LIB_DEPENDS =		graphics/png

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/rgbasm ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/rgbfix ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/rgbgfx ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/rgblink ${PREFIX}/bin/

.include <bsd.port.mk>
