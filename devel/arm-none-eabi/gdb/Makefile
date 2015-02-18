# $OpenBSD: Makefile,v 1.8 2011/11/11 18:33:03 jasper Exp $

COMMENT=	gdb for arm-none-eabi cross-development

VERSION=	7.8
DISTNAME=	gdb-${VERSION}

HOMEPAGE=	https://www.gnu.org/software/gdb/

WANTLIB=	c expat m ncurses z

MASTER_SITES=	${MASTER_SITE_GNU:=gdb/}
DIST_SUBDIR=	gdb

USE_GMAKE=	Yes

CFLAGS+=	-Dunix

CONFIGURE_ARGS+=--enable-multilib	\
		--enable-thumb		\
		--enable-interwork

TEST_DEPENDS=	devel/dejagnu

.include <bsd.port.mk>
