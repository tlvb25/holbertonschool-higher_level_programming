#include "lists.h"

/**
 * add_dnodeint_end -
 *
 * Return: 
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
        dlistint_t *last = *head;
        
        dlistint_t *newNode = malloc(sizeof(dlistint_t));
        if (!newNode)
        {
                return (NULL);
        }
        newNode->n = n;
        newNode->next = NULL;
        
        if(*head == NULL)
        {
                *head = newNode;
                return (newNode);
        }

        while (last->next)
        {
                last = last->next;
        }

        last->next = newNode;

        newNode->prev = last;
        
        return (newNode);
}
