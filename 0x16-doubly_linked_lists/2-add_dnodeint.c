#include "lists.h"

/**
 * add_dnodeint -
 *
 * Return:
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *ptr = *head;
	dlistint_t *newNode = malloc(sizeof(dlistint_t));
	
	if (newNode == NULL)
	{
		return (NULL);
	}
	/* put data in newNode */
	newNode->n = n;
	/* Make next of new node as head and previous as NULL */
	newNode->next = ptr;
	newNode->prev = NULL;
	/* Change prev of head node to new node */
	ptr->prev = newNode;
	/* Move the head to point to the new node */
	ptr = newNode;

	return (newNode);
}
