
COMMENT =		OS9 6809 Emulator

DISTNAME =		OS9Emu-20201213
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# XXX
PERMIT_PACKAGE =	Yes

HOMEPAGE =		https://github.com/jamieleecho/OS9Emu

GH_ACCOUNT =		jamieleecho
GH_PROJECT =		OS9Emu
GH_COMMIT =		e7e7e65506008a086772cc1ee0e34d233cc5ae43

WANTLIB +=		c ${COMPILER_LIBCXX}

USE_GMAKE =		Yes

WRKSRC =		${WRKDIST}/OS9

ALL_TARGET =		os9emu

do-install:
			${INSTALL_PROGRAM} ${WRKDIST}/OS9/os9emu ${PREFIX}/bin/

NO_TEST =		Yes

.include <bsd.port.mk>
