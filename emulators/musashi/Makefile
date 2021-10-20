# $OpenBSD$

COMMENT =		portable Motorola M680x0 processor emulation engine

DISTNAME =		musashi-4.10pl20210816
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/kstenerud/Musashi

GH_ACCOUNT =		kstenerud
GH_PROJECT =		Musashi
GH_COMMIT =		fc7a6fc602e2fbcd24851670a5242358765feacf

WANTLIB +=		c

NO_TEST =		Yes

USE_GMAKE =		Yes

do-install:
			${INSTALL_DATA_DIR} ${PREFIX}/share/musashi/example
			cp ${WRKSRC}/*.{o,txt,c,h} ${PREFIX}/share/musashi
			cp -R ${WRKSRC}/example/* ${PREFIX}/share/musashi/example/

.include <bsd.port.mk>
