#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - This Function Run an infinite while loop.
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates five zombie processes.
 *
 * Return: Always 0.
 */
int main(void)
{
	pid_t one;
	char two = 0;

	while (two < 5)
	{
		one = fork();
		if (one > 0)
		{
			printf("Zombie process created, PID: %d\n", one);
			sleep(1);
			two++;
		}
		else
			exit(0);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}