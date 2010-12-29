
COMMENT=	Busybox-like tool to the BSD

DISTNAME=	beastiebox-090222

CATEGORIES=	sysutils 

HOMEPAGE=	http://www.beastiebox.org/

MAINTAINER=	Benoit Lecocq <blq@arcane-labs.net>

# cvs -d :pserver:anonymous@beastiebox.cvs.sourceforge.net:/cvsroot/beastiebox login
# cvs -d :pserver:anonymous@beastiebox.cvs.sourceforge.net:/cvsroot/beastiebox co beastiebox
MASTER_SITES=	http://www.arcane-labs.fr/download/

# BSD
PERMIT_PACKAGE_CDROM=	Yes
PERMIT_PACKAGE_FTP=	Yes
PERMIT_DISTFILES_CDROM=	Yes
PERMIT_DISTFILES_FTP=	Yes

WANTLIB=		c 

WRKDIST=	${WRKDIR}/beastiebox

NO_REGRESS=	Yes

.include <bsd.port.mk>
