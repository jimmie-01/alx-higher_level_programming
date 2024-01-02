#include "lists.h"

/**
 * check_cycle - This function checks if a linked list contains a cycle
 * @list: linked list
 *
 * Return: 1 if the list has a cycle, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *quiet = list;
	listint_t *swift = list;

	if (!list)
		return (0);
	while (quiet && swift && swift->next)
	{
		quiet = quiet->next;
		swift = swift->next->next;
		if (quiet == swift)
			return (1);
	}
	return (0);
}

