# $OpenBSD$

COMMENT =	ANother Tool for Language Recognition

DISTNAME =	antlr-3.1.3
PKGNAME =	${DISTNAME}

CATEGORIES =	lang java

HOMEPAGE =	http://www.antlr.org/

MAINTAINER =	Benoit Lecocq <blq@arcane-labs.net>

# BSD
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM = Yes
PERMIT_DISTFILES_FTP =	Yes

MASTER_SITES =	http://www.antlr.org/download/

BUILD_DEPENDS =	archivers/zip \
		archivers/gtar

MODULES =	java
MODJAVA_VER =	1.5+

TAR =		${LOCALBASE}/bin/gtar

NO_BUILD =	Yes
NO_REGRESS =	Yes

JAVA_HOME =	${LOCALBASE}/jdk-1.6.0
JAVA_BIN =	${LOCALBASE}/jdk-1.6.0/bin

do-install:
		${INSTALL_DATA_DIR} ${PREFIX}/${DISTNAME}

.include <bsd.port.mk>
