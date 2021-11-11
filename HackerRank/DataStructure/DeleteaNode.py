#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)




# Complete the insertNodeAtPosition function below.
def insertNodeAtPosition(head, data, position):
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # print_singly_linked_list(head," ",fptr)

    NewNode = SinglyLinkedListNode(data)
    if head is None:
        head = NewNode
        return head
    laste = head
    if position==0:
        NewNode.next = head
        return head
    p = 0 
    while(laste.next and p<position-1):
        # print(laste.dataval)
        laste = laste.next
        p = p+1
    # print(p,laste.dataval)
    nextto = laste.next
    # print("next",nextto.dataval)
    laste.next=NewNode
    NewNode.next = nextto
    print_singly_linked_list(head," ",fptr)
    return head
    
# Complete the deleteNode function below.
def deleteNode(head, position):
    if position==0:
        head = head.next
        return head
    p = 0 
    laste = head
    while(laste.next and p<position-1):
        # print(laste.dataval)
        laste = laste.next
        p = p+1
    # print(p,laste.dataval)
    nextto = laste.next
    # print("next",nextto.dataval)
    laste.next=nextto.next
    
    # print_singly_linked_list(head," ",fptr)
    return head

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = deleteNode(llist.head, position)

    print_singly_linked_list(llist1, ' ', fptr)
    fptr.write('\n')

    fptr.close()
