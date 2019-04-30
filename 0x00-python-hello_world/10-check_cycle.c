#include "lists.h"
/**
 * check_cycle - function that detects if list has cycle (loop)
 * @list: linked list passed-in to check
 *
 * Return: 0 if no cycle 1 if there is
 */
int check_cycle(listint_t *list)
{
        listint_t *slow=list;
        listint_t *fast=list;
        
        while(slow && fast && fast->next!=NULL) 
        {
            
            slow = slow->next;               /* Slow pointer moves by 1 step */
            fast = fast->next->next;        /* Fast pointer moves by two steps */
            
            if(slow==fast) /* If they meet then there is a loop */
                return (1);
        }
        return (0); /* No loop */
}
