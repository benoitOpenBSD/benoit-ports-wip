# $OpenBSD: Makefile,v 1.4 2011/09/16 09:24:55 espie Exp $

COMMENT=		Python module dependency analysis tool

MODPY_EGG_VERSION=	0.9.1
DISTNAME=		modulegraph-${MODPY_EGG_VERSION}
PKGNAME=		py-${DISTNAME}

CATEGORIES=		devel

HOMEPAGE=		http://pypi.python.org/pypi/modulegraph/

# MIT
PERMIT_PACKAGE_CDROM=   Yes
PERMIT_PACKAGE_FTP=     Yes
PERMIT_DISTFILES_CDROM= Yes
PERMIT_DISTFILES_FTP=   Yes

MODULES=		lang/python

MODPY_SETUPTOOLS=	Yes

BUILD_DEPENDS =		textproc/py-sphinx
RUN_DEPENDS=		devel/py-altgraph
REGRESS_DEPENDS=	${RUN_DEPENDS}

MASTER_SITES=		${MASTER_SITE_PYPI:=m/modulegraph/}

post-build:
			cd ${WRKSRC}/doc && \
			 ${LOCALBASE}/bin/sphinx-build -N -b html . _build/html

post-install:
			${INSTALL_DATA_DIR} ${PREFIX}/share/doc/py-modulegraph 
			cd ${WRKSRC}/doc/_build/html && \
			 pax -rw * ${PREFIX}/share/doc/py-modulegraph

.include <bsd.port.mk>
