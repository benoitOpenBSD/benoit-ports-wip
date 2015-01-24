# $OpenBSD: Makefile,v 1.8 2015/01/21 14:41:37 sthen Exp $

COMMENT =	summarize HTML pages

MODULES =	cpan
DISTNAME =	HTML-Summary-0.019
CATEGORIES =	textproc

# Perl
PERMIT_PACKAGE_CDROM =	Yes

# XXX Need to create port www/p5-HTML-TreeBuilder
RUN_DEPENDS =		converters/p5-Jcode \
			www/p5-HTML-TreeBuilder

.include <bsd.port.mk>
