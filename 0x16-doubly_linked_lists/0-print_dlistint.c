#include "lists.h"

/**
 * print_dlistint - print the data within nodes of linked list
 * @h: linked list to print 
 * 
 * Return: the data and number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	
	unsigned int count = 0;


	while (h)
	{
		printf("%d\n", h->n);
		count++;
		
		h = h->next;
	}
	return (count);
}
