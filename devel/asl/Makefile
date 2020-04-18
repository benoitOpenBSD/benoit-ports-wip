# $OpenBSD$

COMMENT =		the macroassembler as

DISTNAME =		asl-1.42-200412
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

WANTLIB +=		c

MAKE_FLAGS =		CC="${CC}" CFLAGS="${CFLAGS}"

USE_GMAKE =		Yes

NO_TEST =		Yes

#do-install:
#	${INSTALL_PROGRAM} ${WRKSRC}/asl ${PREFIX}/bin/
#	${INSTALL_PROGRAM} ${WRKSRC}/asl ${PREFIX}/bin/
#	${INSTALL_DATA_DIR} ${PREFIX}/share/asl/test
#	cp -R ${WRKDIST}/test/* ${PREFIX}/share/asl/test

.include <bsd.port.mk>
