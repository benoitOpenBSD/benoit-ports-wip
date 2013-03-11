# $OpenBSD: Makefile,v 1.5 2013/03/11 11:42:46 espie Exp $

COMMENT=	character encoding auto-detection in Python

MODPY_EGG_VERSION = 2.1.1
DISTNAME=	chardet-${MODPY_EGG_VERSION}
PKGNAME=	py-chardet-${MODPY_EGG_VERSION}

CATEGORIES=	textproc

HOMEPAGE =	https://github.com/erikrose/chardet

# LGPLv2.1
PERMIT_PACKAGE_CDROM=	Yes

MASTER_SITES =	${MASTER_SITE_PYPI:=c/chardet/}

MODULES=	lang/python

MODPY_SETUPTOOLS = Yes

NO_TEST=	Yes

post-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/py-chardet/html
	cp -R ${WRKSRC}/docs/* \
		${PREFIX}/share/doc/py-chardet/html
	chown -R ${SHAREOWN}:${SHAREGRP} \
		${PREFIX}/share/doc/py-chardet

.include <bsd.port.mk>
