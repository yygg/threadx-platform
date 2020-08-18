import os

# toolchains options
ARCH        ='arm'
CPU         ='cortex-m0'
CROSS_TOOL  ='gcc'

if os.getenv('TX_ROOT'):
    TX_ROOT = os.getenv('TX_ROOT')
else:
    TX_ROOT = '../..'

if os.getenv('TX_CC'):
    CROSS_TOOL = os.getenv('TX_CC')

if  CROSS_TOOL == 'gcc':
    PLATFORM    = 'gcc'
    EXEC_PATH   = r'E:\embTools\gcc\arm-2019.q4\bin'
elif CROSS_TOOL == 'keil':
    PLATFORM    = 'armcc'
    EXEC_PATH   = 'D:/Keil'    
else:
    print 'Please make sure your toolchains is GNU GCC!'
    exit(0)

BUILD = 'release'
# BUILD = 'debug'

if PLATFORM == 'gcc':
    # toolchains
    PREFIX  = 'arm-none-eabi-'
    CC      = PREFIX + 'gcc'
    CXX     = PREFIX + 'g++'
    AS      = PREFIX + 'gcc'
    AR      = PREFIX + 'ar'
    LINK    = PREFIX + 'ld'
    TARGET_EXT = 'elf'
    SIZE    = PREFIX + 'size'
    OBJDUMP = PREFIX + 'objdump'
    OBJCPY  = PREFIX + 'objcopy'

    DEVICE  = ' -mcpu=cortex-m0 -mthumb'
    CFLAGS  = DEVICE + ' -c -g -Wall'
    AFLAGS  = DEVICE + ' -c -g -x assembler-with-cpp'
    LFLAGS  = ' -A cortex-m0 -ereset_handler -T ./Board/link.lds'
    CPATH   = ''
    LPATH   = ''

    if BUILD == 'debug':
        CFLAGS += ' -O0 -gdwarf-2'
        AFLAGS += ' -gdwarf-2'
    else:
        CFLAGS += ' -O2'

    CXXFLAGS = CFLAGS

    DUMP_ACTION = OBJDUMP + ' -D -S $TARGET > threadx.asm\n'
    POST_ACTION = OBJCPY + ' -O binary $TARGET threadx.bin\n' + SIZE + ' $TARGET \n'
    
    
#------- Keil settings ---------------------------------------------------------
elif PLATFORM == 'armcc':
    # toolchains
    CC = 'armcc'
    CXX= 'armcc'
    AS = 'armasm'
    AR = 'armar'
    LINK = 'armlink'
    TARGET_EXT = 'axf'
    EXEC_PATH += '/arm/armcc/bin/'

    DEVICE = ' --cpu Cortex-M0'
    CFLAGS = DEVICE + ' --apcs=interwork --diag_suppress=870 --split_sections'
    AFLAGS = DEVICE + ' -Iplatform'
    LFLAGS = DEVICE + ' --strict'
    LFLAGS += ' --info sizes --info totals --info unused --info veneers'
    LFLAGS += ' --list threadx.map'
    LFLAGS += ' --scatter  board/link.sct'
    LFLAGS += ' --entry Reset_Handler'
    
    CFLAGS += ' --c99'
    
    if BUILD == 'debug':
        CFLAGS += ' -g -O0'
        AFLAGS += ' -g'
    else:
        CFLAGS += ' -O2'
    CXXFLAGS = CFLAGS
    
    POST_ACTION = 'fromelf --bin $TARGET --output threadx.bin \n'
    POST_ACTION += 'fromelf -z $TARGET\n'
