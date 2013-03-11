# $OpenBSD: Makefile,v 1.11 2013/03/11 10:50:26 espie Exp $

COMMENT =		Python easy_install replacement

MODPY_EGG_VERSION =	1.3.1
DISTNAME =		pip-${MODPY_EGG_VERSION}
PKGNAME =		py-${DISTNAME}
CATEGORIES =		devel

MAINTAINER =		Wen Heping <wenheping@gmail.com>

HOMEPAGE =		http://www.pip-installer.org/

# MIT
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITE_PYPI:=p/pip/}

MODULES =		lang/python
MODPY_SETUPTOOLS =	Yes
NO_TEST =		Yes

FLAVORS =		python3
FLAVOR ?=

# XXX http://marc.info/?l=openbsd-ports&m=135557010512004&w=2

.include <bsd.port.mk>
