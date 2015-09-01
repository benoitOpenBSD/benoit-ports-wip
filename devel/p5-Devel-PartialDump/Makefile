# $OpenBSD: Makefile,v 1.7 2015/01/21 14:27:57 sthen Exp $

COMMENT=		partial dumping of data structures

DISTNAME =		Devel-PartialDump-0.18

CATEGORIES=		devel

# perl
PERMIT_PACKAGE_CDROM=   Yes

MODULES=		cpan

# XXX Need p5-Class-Tiny
RUN_DEPENDS=		devel/p5-Moose \
			devel/p5-Sub-Exporter \
			devel/p5-namespace-clean \
			devel/p5-Class-Tiny

TEST_DEPENDS=		devel/p5-Devel-GlobalDestruction \
			devel/p5-Class-Load \
			devel/p5-Module-Runtime \
			devel/p5-MRO-Compat \
			devel/p5-Test-use-ok

.include <bsd.port.mk>
