# $OpenBSD: Makefile,v 1.22 2010/11/20 17:22:45 espie Exp $

COMMENT=	Prelude Management Console

MODPY_EGG_VERSION=1.0.0
DISTNAME=	prewikka-1.0.0
PKGNAME=	prelude-${DISTNAME}

MODULES=	lang/python

MASTER_SITES=	http://www.prelude-technologies.com/download/releases/prewikka/

BUILD_DEPENDS=	devel/gettext>=0.17 \
		devel/py-cheetah

RUN_DEPENDS=	security/prelude/manager	\
		devel/py-cheetah	\
		graphics/py-cairo

NO_REGRESS=	Yes
VERSION=	${DISTNAME:S/prewikka-//}
SUBST_VARS+=	VERSION

pre-install:
	${SUBST_CMD} -c ${FILESDIR}/siteconfig.py \
		${WRKSRC}/prewikka/siteconfig.py

.include <bsd.port.mk>
