# $OpenBSD: Makefile,v 1.23 2010/11/20 17:22:45 espie Exp $

COMMENT=	Prelude manager

DISTNAME=	prelude-manager-1.0.0

MASTER_SITES=	http://www.prelude-technologies.com/download/releases/prelude-manager/

WANTLIB += c gcrypt gnutls gpg-error m prelude preludedb pthread tasn1 z
WANTLIB += xml2 preludedb

MODULES=	devel/gettext

CONFIGURE_STYLE=gnu
USE_GROFF =	Yes

LIB_DEPENDS=	textproc/libxml \
		security/prelude/libpreludedb

# XXX check on update whether this is still necessary
post-extract:
	${INSTALL} -m 555 ${FILESDIR}/libgnutls-config ${WRKDIR}/bin

.include <bsd.port.mk>
