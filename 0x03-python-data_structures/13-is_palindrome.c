#include "lists.h"

/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: head of linked list
 * Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i, *data, *data_new, ptr1, ptr2;

	current = *head;

	if (current == NULL)
		return (1);

	data = malloc(1000 * sizeof(int));
	i = 0;

	while (current)
	{
		data[i] = current->n;
		current = current->next;
		i++;
	}
	data_new = realloc(data, i * sizeof(int));

	ptr1 = 0;
	ptr2 = i - 1;

	while (ptr1 < ptr2)
	{
		if (data_new[ptr1] == data_new[ptr2])
		{
			ptr1++;
			ptr2--;
		}
		else
		{
			free(data_new);
			return (0);
		}
	}
	free(data_new);
	return (1);
}
