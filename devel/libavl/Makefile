# $OpenBSD: Makefile,v 1.7 2013/03/11 10:50:09 espie Exp $

COMMENT=	library for balanced binary trees

VERSION =	2.0.3
DISTNAME=	avl-${VERSION}
PKGNAME=	libavl-${VERSION}
CATEGORIES=	devel

HOMEPAGE =	http://adtinfo.org/

MAINTAINER=	Kevin Lo <kevlo@openbsd.org>

# GPLv3
PERMIT_PACKAGE =   Yes

MASTER_SITES=   ${MASTER_SITE_GNU:=avl/}

BUILD_DEPENDS =	print/texlive/base \
		graphics/ImageMagick

USE_GMAKE =	Yes

.include <bsd.port.mk>
