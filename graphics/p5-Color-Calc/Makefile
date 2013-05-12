# $OpenBSD: Makefile,v 1.6 2013/03/11 11:10:54 espie Exp $

COMMENT=	simple calculations with RGB colors

MODULES=	cpan
DISTNAME =	Color-Calc-1.073
CATEGORIES=	graphics

MAINTAINER=	Simon Bertrang <simon@openbsd.org>

# Perl
PERMIT_PACKAGE_CDROM=	Yes

RUN_DEPENDS=	devel/p5-Params-Validate \
		graphics/p5-Graphics-ColorNames-WWW
BUILD_DEPENDS =	${RUN_DEPENDS}
TEST_DEPENDS =	devel/p5-Test-NoWarnings

.include <bsd.port.mk>
