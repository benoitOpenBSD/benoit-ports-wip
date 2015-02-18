# $OpenBSD: Makefile,v 1.6 2011/11/11 18:33:03 jasper Exp $

COMMENT=	binutils for arm-none-eabi cross-development

VERSION=	2.24
DISTNAME=	binutils-${VERSION}

HOMEPAGE=	https://www.gnu.org/software/binutils/

WANTLIB=	c z

MASTER_SITES=	${MASTER_SITE_GNU:=binutils/}
DIST_SUBDIR=	binutils

USE_LIBTOOL=	No

CONFIGURE_ARGS+=--enable-commonbfdlib=no \
		--enable-interwork	 \
		--enable-multilib

.include <bsd.port.mk>
