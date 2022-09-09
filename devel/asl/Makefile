# $OpenBSD$

COMMENT =		the macroassembler as

DISTNAME =		asl-1.42-220824
PKGNAME =		asl-1.42.220824
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2 / GPLv3
PERMIT_PACKAGE =	Yes

# MASTER_SITES =		http://john.ccac.rwth-aachen.de:8000/ftp/as/source/c_version/
MASTER_SITES =		https://www.arcane-labs.net/download/OpenBSD/

HOMEPAGE =		http://john.ccac.rwth-aachen.de:8000/as/

WANTLIB +=		c m

MAKE_FLAGS =		CC="${CC}" CFLAGS="${CFLAGS}"

USE_GMAKE =		Yes

# DEBUG_PACKAGES =	${BUILD_PACKAGES}

pre-build:
	@cp ${FILESDIR}/Makefile.def ${WRKSRC}

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
