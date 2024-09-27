
COMMENT =		a ZX Second-Emulator And Released for UniX

DISTNAME =		zesarux
PKGNAME =		zesarux-v11.0-240927
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE =	Yes

SITES =			${SITES_GITHUB}

HOMEPAGE =		https://github.com/chernandezba/zesarux

GH_ACCOUNT =		chernandezba
GH_PROJECT =		zesarux
GH_COMMIT =		a0b95f6fa5cd5ffd4d508cbfc48318afef69129c

WANTLIB +=		c m curses

#USE_GMAKE =		Yes

#NO_TEST =		Yes
	
do-build:
	cd ${WRKBUILD}/RunCPM && ${GMAKE} posix build

.include <bsd.port.mk>
