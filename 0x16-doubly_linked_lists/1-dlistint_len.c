#include "lists.h"

/**
 * dlistint_len - prints number nodes in linked list
 * @h: the linked list passed into function
 * 
 * Return: the number of nodes
 */
size_t dlistint_len(const dlistint_t *h)
{
	const dlistint_t *last;
	unsigned int count = 0;


	while (h)
	{
		count++;
		last = h;
		h = h->next;
	}
	return (count);
}
