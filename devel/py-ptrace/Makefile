
COMMENT=		debugger using ptrace written in Python. 

V=			0.6
DISTNAME=		python-ptrace-$V
PKGNAME=		py-ptrace-$V
CATEGORIES=		devel

HOMEPAGE=		http://python-ptrace.hachoir.org/trac

MAINTAINER=		Benoit Lecocq <blq@arcane-labs.net>

# GPLv2
PERMIT_PACKAGE_CDROM=	Yes
PERMIT_PACKAGE_FTP=	Yes
PERMIT_DISTFILES_CDROM=	Yes
PERMIT_DISTFILES_FTP=	Yes

MASTER_SITES=		http://pypi.python.org/packages/source/p/python-ptrace/

MODULES=		lang/python

pre-configure:
			@${SUBST_CMD} ${WRKSRC}/setup.py

.include <bsd.port.mk>
