# $OpenBSD$

COMMENT =		library for support of the Expert Witness Compression Format

VERSION =		beta-20111015
DISTNAME =		libewf-${VERSION}
CATEGORIES =		security

SHARED_LIBS +=		ewf	0.0 # 2.0

HOMEPAGE =              http://sourceforge.net/projects/libewf/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# LGPLv3
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=libewf/}

WANTLIB =		c crypto ssl z

LIB_DEPENDS =		devel/uuid

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS=         ${CONFIGURE_SHARED} \
			--enable-python

USE_LIBTOOL =		Yes
USE_GROFF =		Yes

WRKDIST =		${WRKDIR}/libewf-20111015

NO_REGRESS =		Yes

.include <bsd.port.mk>
