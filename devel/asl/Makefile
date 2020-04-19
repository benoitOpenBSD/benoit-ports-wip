# $OpenBSD$

COMMENT =		the macroassembler as

DISTNAME =		asl-1.42-200412
PKGNAME =		asl-1.42-current
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2 / GPLv3
PERMIT_PACKAGE =	Yes

# http://john.ccac.rwth-aachen.de:8000/ftp/as/source/c_version/asl-current.tar.gz
# http://john.ccac.rwth-aachen.de:8000/ftp/as/source/c_version/asl-1.41r8.tar.gz
# MASTER_SITES =		http://john.ccac.rwth-aachen.de:8000/ftp/as/source/c_version/
# Add Makefile.def and patch stdinc.h & sysdefs.h
MASTER_SITES =		https://www.arcane-labs.net/download/OpenBSD/

HOMEPAGE =		http://john.ccac.rwth-aachen.de:8000/as/

WANTLIB +=		c m

MAKE_FLAGS =		CC="${CC}" CFLAGS="${CFLAGS}"

USE_GMAKE =		Yes

DEBUG_PACKAGES =	${BUILD_PACKAGES}

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/asl ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/plist ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/alink ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/pbind ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/p2hex ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/p2bin ${PREFIX}/bin/
#	${INSTALL_DATA_DIR} ${PREFIX}/share/asl/doc
	${INSTALL_DATA_DIR} ${PREFIX}/include/asl
	cp -R ${WRKDIST}/include/* ${PREFIX}/include/asl/

do-test:
	@cd ${WRKSRC}/tests && ${SETENV} sh ./testall

.include <bsd.port.mk>
