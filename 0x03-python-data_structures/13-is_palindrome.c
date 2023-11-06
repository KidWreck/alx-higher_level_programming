#include "main.h"

/**
 * is_palindrome - check
 * @head: head
 * Return: 1 if True, 0 if False
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux(head, *head));
}

/**
 * aux - helper
 * @head: head
 * @end: end
 * Return: 1 if True, 0 if False
 */
int aux(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux(head, ens->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
