
export TX_ROOT	= E:\tx-workspace
export TX_CC 	= keil

export PKG_ROOT	= E:\tx-workspace\packages

scons:=python ${SCONS}\scons.py

all:
	@$(scons) -j4
	
keil:	
	@$(scons) --target=mdk5 -s
	
iar:	
	@$(scons) --target=iar -s	
	
copy:	
	@$(scons) --copy
	
clean:
	@$(scons) -j4 -c
	
buildlib:
	@$(scons) --buildlib=libxx
cleanlib:
	@$(scons) --cleanlib
	