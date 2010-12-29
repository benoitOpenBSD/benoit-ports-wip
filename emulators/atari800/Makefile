# $OpenBSD$

COMMENT =		Atari 800 emulator

DISTNAME =		atari800-2.1.0
CATEGORIES =		emulators games

HOMEPAGE =		http://atari800.sourceforge.net/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =		Yes 
PERMIT_PACKAGE_FTP =		Yes
PERMIT_DISTFILES_CDROM =	Yes 
PERMIT_DISTFILES_FTP =		Yes 

WANTLIB =		c z m X11 ossaudio

MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=atari800/}

WRKBUILD =		${WRKDIR}/${DISTNAME}/src

USE_GMAKE =		Yes
USE_X11 =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS =	--target=x11 \
			${CONFIGURE_SHARED \
			CFLAGS='${CFLAGS} -I${LOCALBASE}/include' \
			LDFLAGS='${LDFLAGS} -L${LOCALBASE}/lib' \
			--with-x

NO_REGRESS =		Yes

A800DOCSDIR =		${PREFIX}/share/doc/atari800

do-install:
		${INSTALL_PROGRAM} ${WRKBUILD}/atari800 ${PREFIX}/bin
		${INSTALL_DATA_DIR} ${A800DOCSDIR}
		${INSTALL_DATA} ${WRKSRC}/DOC/* ${A800DOCSDIR}
		${INSTALL_DATA} ${WRKBUILD}/atari800.man ${PREFIX}/man/man1/atari800.1
                						
.include <bsd.port.mk>
