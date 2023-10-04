#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted linked list
 * @head: head node
 * @number: integer
 * Return: Address of new node or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	if (*head == NULL || (*head)->n >= new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (current->next != NULL && current->next->n < new_node->n)
		current = current->next;
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
