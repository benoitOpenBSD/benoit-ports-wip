# $OpenBSD: Makefile,v 1.9 2011/09/16 10:31:23 espie Exp $

COMMENT =	Python interface to memcached

MODPY_EGG_VERSION = 1.48
DISTNAME =	python-memcached-${MODPY_EGG_VERSION}
PKGNAME =	${DISTNAME:S/python-/py-/}
CATEGORIES =	misc

HOMEPAGE =	http://www.tummy.com/Community/software/python-memcached/

MAINTAINER =	Ben Lovett <ben@tilderoot.com>

# Python
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =	ftp://ftp.tummy.com/pub/python-memcached/

MODULES =	lang/python

MODPY_SETUPTOOLS =	Yes

NO_TEST =	Yes

pre-install:
	@perl -pi -e "s,#!.*python,#!${MODPY_BIN}," ${WRKSRC}/memcache.py

post-install:
	@rm -rf ${WRKSRC}/python_memcached.egg-info

.include <bsd.port.mk>
