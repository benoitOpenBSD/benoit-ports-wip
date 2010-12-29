# $OpenBSD$

COMMENT =		Sixth Edition UNIX shell

DISTNAME =		osh-20090527
CATEGORIES =		shells

HOMEPAGE =		http://v6shell.org/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

WANTLIB =		c

MASTER_SITES =		http://v6shell.org/src/

NO_REGRESS =		Yes

#ALL_TARGET =		oshall

do-install:
	${INSTALL_DATA_DIR}  ${PREFIX}/man/man1
	${INSTALL_MAN} ${WRKSRC}/*.1 ${PREFIX}/man/man1
	${INSTALL_PROGRAM_DIR}  ${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKSRC}/{osh,sh6,glob6,fd2,if,goto} ${PREFIX}/bin

.include <bsd.port.mk>
