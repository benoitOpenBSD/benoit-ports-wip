
COMMENT =		a Z80 CP/M 2.2 emulator

DISTNAME =		runCPM
PKGNAME =		runCPM-v6.6-240820
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# MIT
PERMIT_PACKAGE =	Yes

SITES =			${SITES_GITHUB}

HOMEPAGE =		https://github.com/MockbaTheBorg/RunCPM

GH_ACCOUNT =		MockbaTheBorg
GH_PROJECT =		RunCPM
GH_COMMIT =		f87f6eaf79781e376d5f199192d16698ef714eb8

WANTLIB +=		c m curses

USE_GMAKE =		Yes

NO_TEST =		Yes
	
do-build:
	cd ${WRKBUILD}/RunCPM && ${GMAKE} posix build

do-install:
	${INSTALL_DATA_DIR} ${PREFIX}/RunCPM
	${INSTALL_DATA_DIR} ${PREFIX}/RunCPM/Docs
	${INSTALL_PROGRAM} ${WRKBUILD}/RunCPM/RunCPM ${PREFIX}/RunCPM/
	cp -R ${WRKSRC}/CCP/* ${PREFIX}/RunCPM/
	cd ${PREFIX}/RunCPM && unzip ${WRKSRC}/DISK/A0.ZIP
	cp -R ${WRKSRC}/Docs/* ${PREFIX}/RunCPM/Docs

.include <bsd.port.mk>
