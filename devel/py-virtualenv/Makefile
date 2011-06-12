# $OpenBSD$

COMMENT =		tool to create isolated Python environments

MODPY_EGG_VERSION =	1.6.1
DISTNAME =		virtualenv-${MODPY_EGG_VERSION}
PKGNAME =		py-${DISTNAME}

CATEGORIES =		devel

HOMEPAGE =		http://www.virtualenv.org/

# MIT
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MASTER_SITES =		${MASTER_SITE_PYPI:=v/virtualenv/}

MODULES =		lang/python

MODPY_SETUPTOOLS =	Yes

NO_REGRESS =		Yes

.include <bsd.port.mk>
