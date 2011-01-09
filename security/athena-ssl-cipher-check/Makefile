# $OpenBSD$

COMMENT =		an SSL Cipher scanner

DISTNAME =		athena-ssl-cipher-check_v062
PKGNAME =		${DISTNAME:S/_/-/}
CATEGORIES =		security

HOMEPAGE =		http://dmcdonald.net/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE_CDROM=   Yes
PERMIT_PACKAGE_FTP=     Yes
PERMIT_DISTFILES_CDROM= Yes
PERMIT_DISTFILES_FTP=   Yes

MASTER_SITES =		${HOMEPAGE}

MODULES =		java
MODJAVA_VER =		1.3+

NO_BUILD =		Yes
NO_REGRESS =		Yes

do-install:
			${INSTALL_DATA} ${WRKBUILD}/${DISTNAME}.jar ${PREFIX}/bin
#			${INSTALL_MAN} ${WRKSRC}/xmake.1     ${PREFIX}/man/man1
			
.include <bsd.port.mk>
