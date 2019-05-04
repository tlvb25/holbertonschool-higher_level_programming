#include "lists.h"

/**
 * free_dlistint -
 *
 * Return: 
 */
void free_dlistint(dlistint_t *head)
{
        dlistint_t *current;

        while ((current = head) != NULL)
	{
		head = head->next;
		free(current);
	}
}
