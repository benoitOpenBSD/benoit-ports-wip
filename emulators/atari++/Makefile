
COMMENT =		Unix based emulator of the Atari eight bit computers

DISTNAME =		atari++_1.85
PKGNAME =		${DISTNAME:S/_/-/}
CATEGORIES =		emulators

HOMEPAGE =		http://www.xl-project.com/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# TPL
PERMIT_PACKAGE =	Yes

WANTLIB +=		c m z pthread SDL
WANTLIB +=		${COMPILER_LIBCXX} ICE SM X11 Xext Xv curses

# tar: Unable to link file atari++/winmain.cpp to itself
SITES =			http://www.xl-project.com/download/
TAR =			${LOCALBASE}/bin/gtar

BUILD_DEPENDS =		archivers/gtar

LIB_DEPENDS =		devel/sdl

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS = 	CC=${CC} CXX=${CXX} \
			CFLAGS="${CFLAGS}" \
			CXXFLAGS="${CXXFLAGS}"

USE_GMAKE =		Yes

WRKDIST =		${WRKDIR}/atari++

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM}	${WRKDIST}/atari++ ${PREFIX}/bin

.include <bsd.port.mk>
