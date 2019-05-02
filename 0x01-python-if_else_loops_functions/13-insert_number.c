#include "lists.h"

/**
 * add_nodeint - function that adds a new node to the begining of list
 * @head: the double pointer to the head node of the list
 * @n: the integer value passed to the function
 *
 * Return: new_node
 */
listint_t *insert_nodeint(listint_t **head, int number)
{
	/* new node to inserted at end of list */
	listint_t *new_node;

	/* allocates memory for new_node ptr */
	new_node = malloc(sizeof(listint_t));

	/* checks if either the new node and the passed-in head ptr are null */
	if (!new_node || !head)
		return (NULL);

	/* stores the passed-in integer into the new_node */
	new_node->n = n;

	/* makes new_node point to the same node that head points to */
	new_node->next = *head;

	/*set head ptr to now point to the new_node which is now the first node */
	*head = new_node;

	return (new_node);
}