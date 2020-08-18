/*
 * Copyright (c) 2006-2020, SZ-ZZS Development Team
 *
 *                            _ooOoo_
 *                           o8888888o
 *                           88" . "88
 *                           (| -_- |)
 *                           O\  =  /O
 *                        ____/`---'\____
 *                      .'  \\|     |//  `.
 *                     /  \\|||  :  |||//  \
 *                    /  _||||| -:- |||||-  \
 *                    |   | \\\  -  /// |   |
 *                    | \_|  ''\---/''  |   |
 *                    \  .-\__  `-`  ___/-. /
 *                  ___`. .'  /--.--\  `. . __
 *               ."" '<  `.___\_<|>_/___.'  >'"".
 *              | | :  `- \`.;`\ _ /`;.`/ - ` : | |
 *              \  \ `-.   \_ __\ /__ _/   .-` /  /
 *         ======`-.____`-.___\_____/___.-`____.-'======
 *                            `=---='
 *        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 *                      Buddha Bless, No Bug !
 * Change Logs:
 * Date           Author       Notes
 * 2020-08-18     Urey       the first version
 */


#include "tx_api.h"
#include "board.h"

#define DEMO_STACK_SIZE         1024
#define DEMO_BYTE_POOL_SIZE     2048


/* Define the ThreadX object control blocks...  */

TX_THREAD               thread_0;
TX_BYTE_POOL            byte_pool_0;


/* Define the counters used in the demo application...  */

ULONG                   thread_0_counter;


/* Define thread prototypes.  */

void    thread_0_entry(ULONG thread_input);

/* Define main entry point.  */
extern int hw_board_init(void);
int main()
{
    hw_board_init();

    /* Enter the ThreadX kernel.  */
    tx_kernel_enter();
}


/* Define what the initial system looks like.  */

void    tx_application_define(void *first_unused_memory)
{

CHAR    *pointer = TX_NULL;


    /* Create a byte memory pool from which to allocate the thread stacks.  */
    tx_byte_pool_create(&byte_pool_0, "byte pool 0", first_unused_memory, DEMO_BYTE_POOL_SIZE);

    /* Put system definition stuff in here, e.g. thread creates and other assorted
       create information.  */

    /* Allocate the stack for thread 0.  */
    tx_byte_allocate(&byte_pool_0, (VOID **) &pointer, DEMO_STACK_SIZE, TX_NO_WAIT);

    /* Create the main thread.  */
    tx_thread_create(&thread_0, "thread 0", thread_0_entry, 0,
            pointer, DEMO_STACK_SIZE,
            1, 1, TX_NO_TIME_SLICE, TX_AUTO_START);


}


/* Define the test threads.  */
void    thread_0_entry(ULONG thread_input)
{
    /* This thread simply sits in while-forever-sleep loop.  */
    while(1)
    {
        P20 = 0;
        /* Sleep for 10 ticks.  */
        tx_thread_sleep(50);

        P20 = 1;
        /* Sleep for 10 ticks.  */
        tx_thread_sleep(50);
        /* Increment the thread counter.  */
        thread_0_counter++;
    }
}

