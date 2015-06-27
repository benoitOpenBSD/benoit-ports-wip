# $OpenBSD: Makefile,v 1.11 2015/01/21 14:41:37 sthen Exp $

COMMENT= 		POE Filter for parsing XML

DISTNAME =		POE-Filter-XML-1.140700
CATEGORIES=		textproc

# GPLv2
PERMIT_PACKAGE_CDROM=	Yes

MODULES=		cpan

# Need to create devel/p5-MooseX-InsideOut
RUN_DEPENDS =		devel/p5-POE \
			devel/p5-MooseX-NonMoose \
			textproc/p5-XML-SAX>=0.16 \
			textproc/p5-XML-LibXML \
			textproc/p5-XML-SAX-Expat-Incremental

.include <bsd.port.mk>
