#include "lists.h"
/**
 * insert_node - inserts a node into a sorted list
 * @head: head of linked list
 * @number: number to insert
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *num;

	current = malloc(sizeof(listint_t));
	if (current == NULL)
	{
		free(current);
		return (NULL);
	}
	current->n = number;
	current->next = NULL;
	if (*head == NULL || current->n <= (*head)->n)
	{
		current->next = *head;
		*head = current;
		return (current);
	}
	num = *head;
	while (num->next)
	{
		if (current->n <= num->next->n)
		{
			current->next = num->next;
			num->next = current;
			return (current);
		}
		num = num->next;
	}
	num->next = current;
	return (current ? current : NULL);
}
