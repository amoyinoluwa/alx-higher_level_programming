#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: list to be checked
 * Return: 1 or 0
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_ptr;
	listint_t *fast_ptr;

	slow_ptr = fast_ptr = list;

	if (list == NULL)
		return (0);

	while (slow_ptr && fast_ptr && fast_ptr->next)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
		if (fast_ptr == slow_ptr)
			return (1);
	}
	return (0);
}
