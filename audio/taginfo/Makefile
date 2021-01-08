# $OpenBSD$

COMMENT=	quick implementation of the TagLib API
DISTNAME=	taginfo-1.2
CATEGORIES=	audio

HOMEPAGE= 	http://grecni.com/software/taginfo/

MAINTAINER=	Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_DISTFILES =	Yes

WANTLIB=	stdc++ m z

MASTER_SITES=	http://grecni.com/software/taginfo/

EXTRACT_SUFX=	.tar.bz2

LIB_DEPENDS=	audio/taglib

do-install:
		${INSTALL_PROGRAM} ${WRKBUILD}/taginfo ${PREFIX}/bin

NO_TEST =	Yes

ALL_TARGET=	main
        
.include <bsd.port.mk>
