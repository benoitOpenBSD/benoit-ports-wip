# $OpenBSD$

COMMENT =		???

DISTNAME =		zdoom-2.3.1-src
PKGNAME =		${DISTNAME:S/-src//}
CATEGORIES =		games

HOMEPAGE =		http://zdoom.org/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

#
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

#WANTLIB =		???

MASTER_SITES =		http://zdoom.org/files/zdoom/2.3/

EXTRACT_SUFX =		.7z

EXTRACT_SUFX ?=		.7z
#EXTRACT_CASES +=        *.7z) 7z x ${FULLDISTDIR}/$$archive | tar xf -;;
EXTRACT_CASES +=	*.7z) 7z x ${FULLDISTDIR}/$$archive;;
BUILD_DEPENDS +=        archivers/p7zip

MODULES =		devel/cmake

USE_GROFF =		Yes
USE_GMAKE =		Yes

CONFIGURE_STYLE =	cmake

NO_REGRESS =		Yes

WRKDIST =		${WRKDIR}

.include <bsd.port.mk>
