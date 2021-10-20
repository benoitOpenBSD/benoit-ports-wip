# $OpenBSD$

COMMENT =		a Z80 CP/M 2.2 emulator

DISTNAME =		runCPM
PKGNAME =		runCPM-v5.7-210928
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# MIT
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/MockbaTheBorg/RunCPM

GH_ACCOUNT =		MockbaTheBorg
GH_PROJECT =		RunCPM
GH_COMMIT =		0459e2344770409c47522c06c11898741f834cb1

WANTLIB +=		c m curses

USE_GMAKE =		Yes

NO_TEST =		Yes
	
do-build:
	cd ${WRKBUILD}/RunCPM && ${GMAKE} posix build

do-install:
	${INSTALL_DATA_DIR} ${PREFIX}/RunCPM/A/0
	${INSTALL_DATA_DIR} ${PREFIX}/RunCPM/Docs
	${INSTALL_PROGRAM} ${WRKBUILD}/RunCPM/RunCPM ${PREFIX}/RunCPM/
	cp -R ${WRKSRC}/CCP/* ${PREFIX}/RunCPM/
	cd ${PREFIX}/RunCPM/A/0 && unzip ${WRKSRC}/DISK/A.ZIP
	cp -R ${WRKSRC}/Docs/* ${PREFIX}/RunCPM/Docs

.include <bsd.port.mk>
