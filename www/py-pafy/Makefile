# $OpenBSD: Makefile,v 1.97 2014/09/03 06:03:40 dcoppa Exp $

COMMENT =	Retrieve YouTube content and metadata

MODPY_EGG_VERSION = 0.3.62

DISTNAME =	Pafy-${MODPY_EGG_VERSION}
PKGNAME =	py-pafy-${MODPY_EGG_VERSION}
CATEGORIES =	www

HOMEPAGE =	https://github.com/np1/pafy

#MAINTAINER =	James Lecocq <james@james.cx>

# Public Domain
PERMIT_PACKAGE_CDROM =		Yes

MASTER_SITES =	${MASTER_SITE_PYPI:=P/Pafy/}

MODULES =	lang/python

MODPY_SETUPTOOLS = Yes

NO_TEST =	Yes

PKG_ARCH =	*


.include <bsd.port.mk>
