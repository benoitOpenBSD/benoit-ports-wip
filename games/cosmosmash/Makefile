# $OpenBSD: Makefile,v 1.20 2010/11/26 07:20:12 espie Exp $

COMMENT=	astrosmash clone for X

DISTNAME=	cosmosmash-1.4.6

CATEGORIES=	games

HOMEPAGE=	http://sarrazip.com/dev/cosmosmash.html

# GPLv2
PERMIT_PACKAGE_CDROM=   Yes

WANTLIB += SDL SDL_image SDL_mixer c m pthread stdc++ flatzebra-0.1>=1

MASTER_SITES=	http://sarrazip.com/dev/

LIB_DEPENDS=	devel/flatzebra>=0.1.5
RUN_DEPENDS=	devel/desktop-file-utils

USE_GROFF =	Yes

CONFIGURE_STYLE= gnu

.include <bsd.port.mk>
