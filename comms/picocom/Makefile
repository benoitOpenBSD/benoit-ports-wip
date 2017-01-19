# $OpenBSD: Makefile,v 1.7 2016/10/01 11:54:14 naddy Exp $

COMMENT =		minimal dumb-terminal emulation program

DISTNAME =		picocom-2.2
CATEGORIES =		comms

HOMEPAGE =		https://github.com/npat-efault/picocom
MAINTAINER =		Kyle Isom <kyle@tyrfingr.is>

# GPLv2+
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB += c

#MASTER_SITES =		${MASTER_SITE_GOOGLECODE:=picocom/}
GH_TAGNAME =            2.2
GH_ACCOUNT =            npat-efault
GH_PROJECT =            picocom

MAKE_FLAGS =		CC="${CC}" CFLAGS="${CFLAGS}"
MAKE_ENV =		LDFLAGS="${LDFLAGS}"

NO_TEST =		Yes

do-install:
	${INSTALL_DATA} ${WRKSRC}/picocom.1 ${PREFIX}/man/man1/picocom.1
	${INSTALL_PROGRAM} ${WRKDIST}/picocom ${PREFIX}/bin/picocom


.include <bsd.port.mk>
