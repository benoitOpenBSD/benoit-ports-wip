# $OpenBSD$

COMMENT =		Python Interface to the Google API

MODPY_EGG_VERSION =	0.6
DISTNAME =		pygoogle-${MODPY_EGG_VERSION}
PKGNAME =		py-google-${MODPY_EGG_VERSION}
CATEGORIES =		net

HOMEPAGE =		http://pygoogle.sourceforge.net/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# Python license
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

#WANTLIB =		???

MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=pygoogle/}

MODULES =		lang/python
#MODPY_SETUPTOOLS =	Yes

RUN_DEPENDS =		devel/py-SOAPpy

NO_REGRESS =		Yes

.include <bsd.port.mk>
