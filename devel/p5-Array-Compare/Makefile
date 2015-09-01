# $OpenBSD: Makefile,v 1.16 2014/03/23 13:59:37 jasper Exp $

COMMENT =	Perl module for comparing arrays

MODULES =	cpan
DISTNAME =	Array-Compare-2.11
CATEGORIES =	devel

# perl
PERMIT_PACKAGE_CDROM =	Yes

CPAN_AUTHOR =	DAVECROSS

# XXX Need p5-Types-Standard
BUILD_DEPENDS =	${RUN_DEPENDS}
RUN_DEPENDS =	devel/p5-Moose
TEST_DEPENDS =	devel/p5-Test-NoWarnings \
		devel/p5-Test-Pod \
		devel/p5-Test-Pod-Coverage

.include <bsd.port.mk>
