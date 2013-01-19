# $OpenBSD$

COMMENT =		Pythonic tool for remote execution and deployment.

MODPY_EGG_VERSION =	1.5.2
DISTNAME =		Fabric-${MODPY_EGG_VERSION}
CATEGORIES =		sysutils

HOMEPAGE =		http://www.fabfile.org/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MASTER_SITES =		${MASTER_SITE_PYPI:=F/Fabric/}

MODULES =		lang/python
MODPY_SETUPTOOLS =	Yes

BUILD_DEPENDS =		${RUN_DEPENDS}
RUN_DEPENDS =		security/py-paramiko

# REGRESS_DEPENDS =	devel/py-nose
NO_REGRESS =		Yes

.include <bsd.port.mk>
