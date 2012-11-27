# $OpenBSD: Makefile,v 1.1.1.1 2011/10/14 16:32:54 jasper Exp $

COMMENT=	elegant and simple HTTP library for Python

MODPY_EGG_VERSION=0.14.2
DISTNAME=	kennethreitz-requests-v${MODPY_EGG_VERSION}-0-63243b1e3b
PKGNAME=	py-requests-${MODPY_EGG_VERSION}

CATEGORIES=	www

HOMEPAGE=	http://python-requests.org/

# ISC
PERMIT_PACKAGE_CDROM=	Yes
PERMIT_PACKAGE_FTP=	Yes
PERMIT_DISTFILES_CDROM= Yes
PERMIT_DISTFILES_FTP=	Yes

MASTER_SITES=	http://www.arcane-labs.net/download/OpenBSD/ \
		http://distfiles.nl/
EXTRACT_SUFX=	.zip

MODULES=	lang/python

MODPY_SETUPTOOLS= Yes
#MODPY_ADJ_FILES=test_requests.py

WRKDIST= 	${WRKDIR}/requests-${MODPY_EGG_VERSION}/

pre-configure:
	${SUBST_CMD} ${WRKSRC}/setup.py

.include <bsd.port.mk>
