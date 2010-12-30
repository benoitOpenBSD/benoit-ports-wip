# $OpenBSD: Makefile,v 1.19 2010/11/20 17:22:45 espie Exp $

COMMENT=	Prelude log analyzer

DISTNAME=	prelude-lml-1.0.0

WANTLIB=	c gcrypt gnutls gpg-error m tasn1 z pcre prelude

MODULES=	devel/gettext

MASTER_SITES=	http://www.prelude-technologies.com/download/releases/prelude-lml/

CONFIGURE_STYLE=gnu

LIB_DEPENDS=	devel/pcre \
		security/prelude/libprelude

CONFIGURE_ARGS=	--disable-unsupported-rulesets

.include <bsd.port.mk>
