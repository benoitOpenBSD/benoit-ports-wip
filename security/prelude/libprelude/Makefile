# $OpenBSD: Makefile,v 1.28 2010/11/20 17:22:45 espie Exp $

COMMENT=        Prelude framework library

MODPY_EGG_VERSION=1.0.0
DISTNAME=       libprelude-${MODPY_EGG_VERSION}
PKGNAME=        prelude-${DISTNAME}

MASTER_SITES=   http://www.prelude-technologies.com/download/releases/libprelude/

SHARED_LIBS=    prelude 21.1

MODULES=        devel/gettext \
                lang/python

CONFIGURE_STYLE=gnu
USE_GROFF =     Yes

WANTLIB=        c gcrypt tasn1 z gpg-error gnutls

LIB_DEPENDS=    security/libgpg-error \
                security/gnutls

.include <bsd.port.mk>
