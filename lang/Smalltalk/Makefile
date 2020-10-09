# $OpenBSD$

COMMENT =	by the Bluebook implementation of Smalltalk-80 

DISTNAME =	Smalltalk-200717
CATEGORIES =	lang

HOMEPAGE =	https://github.com/dbanay/Smalltalk

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# MIT
PERMIT_PACKAGE =	Yes

MASTER_SITES =          ${MASTER_SITES_GITHUB}

GH_ACCOUNT =            dbanay
GH_PROJECT =            Smalltalk
GH_COMMIT =		f647e589cfa84551899b61b48a638dae2d4e77d9

WANTLIB +=		${COMPILER_LIBCXX} c m SDL2

LIB_DEPENDS =		devel/sdl2

USE_GMAKE =		Yes
                        
do-build:
			cd ${WRKSRC}/linux && ${SETENV} ${MAKE_ENV} ${MAKE_PROGRAM}

do-install:
			${INSTALL_PROGRAM} ${WRKSRC}/linux/Smalltalk ${PREFIX}/bin/
			${INSTALL_DATA_DIR} ${PREFIX}/share/Smalltalk/files
			${INSTALL_DATA} ${WRKSRC}/files/* ${PREFIX}/share/Smalltalk/files

do-test:
			cd ${WRKSRC}/linux && ./Smalltalk -directory ../files

.include <bsd.port.mk>
