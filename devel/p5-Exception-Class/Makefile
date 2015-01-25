# $OpenBSD: Makefile,v 1.19 2013/03/11 14:49:15 benoit Exp $

COMMENT=	module to declare real exception classes in perl

MODULES=	cpan
DISTNAME =	Exception-Class-1.39
CATEGORIES=	devel

# perl
PERMIT_PACKAGE_CDROM=	Yes

BUILD_DEPENDS=	${RUN_DEPENDS}
RUN_DEPENDS=	devel/p5-Class-Data-Inheritable>=0.02 \
		devel/p5-Devel-StackTrace>=2.00

.include <bsd.port.mk>
