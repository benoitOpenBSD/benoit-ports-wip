# $OpenBSD: Makefile,v 1.8 2013/03/11 11:42:46 espie Exp $

COMMENT =	python package to parse and build CSS

CATEGORIES =	textproc

MODPY_EGG_VERSION =	0.9.10b1
DISTNAME =	cssutils-${MODPY_EGG_VERSION}
PKGNAME =	py-${DISTNAME}

EPOCH =		0

MASTER_SITES =	${MASTER_SITE_PYPI:=c/cssutils/}

EXTRACT_SUFX =	.zip

# LGPLv2.1
PERMIT_PACKAGE_CDROM=	Yes

HOMEPAGE =	http://cthedot.de/cssutils/

MODULES =	lang/python

MODPY_SETUPTOOLS =	Yes

post-install:
	chmod 444 ${WRKINST}/${MODPY_SITEPKG}/${DISTNAME}-py${MODPY_VERSION}.egg-info/*

.include <bsd.port.mk>
