# $OpenBSD$

COMMENT =		portable Motorola M680x0 processor emulation engine

DISTNAME =		musashi-4.10pl20200614
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/kstenerud/Musashi

GH_ACCOUNT =		kstenerud
GH_PROJECT =		Musashi
GH_COMMIT =		66d00ece8a994c73031d71e3d67f3f6fd5cd6a27

WANTLIB +=		c

NO_TEST =		Yes

USE_GMAKE =		Yes

do-install:
			${INSTALL_DATA_DIR} ${PREFIX}/share/musashi
			cp ${WRKSRC}/*.{o,txt} ${PREFIX}/share/musashi
			cp -R ${WRKSRC}/example/ ${PREFIX}/share/musashi

.include <bsd.port.mk>
