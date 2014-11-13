# $OpenBSD: Makefile,v 1.10 2011/09/16 12:00:08 espie Exp $

COMMENT=	web framework for python

VERSION=	0.37
DISTNAME=	web.py-${VERSION}
PKGNAME=	py-webpy-${VERSION}
CATEGORIES=	www

MASTER_SITES=	${HOMEPAGE}/static/
HOMEPAGE=	http://webpy.org

# Public Domain, except wsgiserver
PERMIT_PACKAGE_CDROM =	Yes

MODULES=	lang/python

SUBST_VARS=	VERSION

TEST_DEPENDS= databases/py-sqlite2 \
		${BASE_PKGPATH}

do-test:
	cd ${WRKSRC} && ${MODPY_BIN} ./web/test.py 
	cd ${WRKSRC} && ${MODPY_BIN} ./web/db.py SqliteTest

.include <bsd.port.mk>
