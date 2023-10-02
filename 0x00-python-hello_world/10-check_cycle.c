#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list has a cycle
 *
 * @list: linked list
 *
 * Return: 0 if there is no cycle and 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slower_pace = list;
	listint_t *faster_pace = list;

	while (faster_pace && faster_pace->next)
	{
		slower_pace = slower_pace->next;
		faster_pace = faster_pace->next->next;

		if (slower_pace == faster_pace)
			return (1);
	}

	return (0);
}
