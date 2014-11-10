#	$OpenBSD$

COMMENT=	random number test suite
DISTNAME=	dieharder-3.31.1
CATEGORIES=	math
EXTRACT_SUFX=	.tgz
HOMEPAGE=	http://www.phy.duke.edu/~rgb/General/dieharder.php
MASTER_SITES=	http://www.phy.duke.edu/~rgb/General/dieharder/
MAINTAINER=	Jonathan Gray <jsg@openbsd.org>

SHARED_LIBS +=  dieharder	0.0

# GPLv2+ with "Beverage" Modification
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB=		c gsl gslcblas m
LIB_DEPENDS=		devel/gsl

USE_LIBTOOL=		Yes
CONFIGURE_STYLE=	gnu
CONFIGURE_ENV+=		CPPFLAGS="-I${LOCALBASE}/include" \
			LDFLAGS="-L${LOCALBASE}/lib"

.include <bsd.port.mk>
