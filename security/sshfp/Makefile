
COMMENT =		Generate RFC-4255 SSHFP DNS records

DISTNAME =		sshfp-1.1.3
CATEGORIES =		security

HOMEPAGE =		http://www.xelerance.com/software/sshfp/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2+
PERMIT_PACKAGE_CDROM =	Yes

# https://github.com/xelerance/sshfp
SITES =			ftp://ftp.xelerance.com/sshfp/

MODULES =		lang/python

BUILD_DEPENDS=		:py-dnspython-*:net/py-dnspython

NO_BUILD =		Yes
NO_TEST =		Yes

pre-configure:
		${SUBST_CMD} ${WRKSRC}/sshfp

do-install:
		 ${INSTALL_SCRIPT} ${WRKSRC}/sshfp ${PREFIX}/bin
		 ${INSTALL_MAN_DIR} ${PREFIX}/man/man1
		 ${INSTALL_MAN} ${WRKSRC}/sshfp.1 ${PREFIX}/man/man1

.include <bsd.port.mk>
