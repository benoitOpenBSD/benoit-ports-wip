# $OpenBSD: Makefile,v 1.4 2013/03/11 10:50:26 espie Exp $

COMMENT=	extensions to the Python unit testing framework

MODPY_EGG_VERSION = 0.9.29
DISTNAME=	testtools-${MODPY_EGG_VERSION}
PKGNAME=	py-${DISTNAME}

CATEGORIES=	devel

HOMEPAGE=	http://pypi.python.org/pypi/testtools

# MIT
PERMIT_PACKAGE_CDROM=	Yes

MASTER_SITES=	${MASTER_SITE_PYPI:=t/testtools/}

MODULES=	lang/python

MODPY_SETUPTOOLS =	Yes

NO_TEST=	Yes

.include <bsd.port.mk>
