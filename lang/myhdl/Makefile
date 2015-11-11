# $OpenBSD: Makefile,v 1.4 2014/09/27 17:41:20 jasper Exp $

COMMENT=	Python as a hardware description and verification language

MODPY_EGG_VERSION=0.9.0
DISTNAME=	myhdl-${MODPY_EGG_VERSION}
CATEGORIES=	lang

HOMEPAGE=	http://www.myhdl.org/

# LGPLv2.1
PERMIT_PACKAGE_CDROM=	Yes

MASTER_SITES=	${MASTER_SITE_SOURCEFORGE:=myhdl/}

MODULES+=	lang/python

MODPY_SETUPTOOLS =	Yes

USE_GMAKE =		Yes
TEST_DEPENDS =		devel/py-test

post-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/examples/myhdl/
	cd ${WRKSRC}/example/ && umask 022 && pax -rw . \
		${PREFIX}/share/examples/myhdl/

do-test: fake
	cd ${WRKSRC}/myhdl/test/core && \
		env PYTHONPATH="${WRKINST}${MODPY_LIBDIR}/site-packages/" \
		${GMAKE}

.include <bsd.port.mk>
