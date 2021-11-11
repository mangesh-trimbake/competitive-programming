#!/bin/python3

import os
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

# Complete the reversePrint function below.
def reversePrint(head):
    if(head.next is not None):
        reversePrint(head.next)
    print(head.data)

# Complete the reverse function below.
def reverse(head):
    fptr = open(os.environ['OUTPUT_PATH'], 'a')
    print("====")
    # print_singly_linked_list(head,"\n",fptr)
    current = head
    nextto = None
    prev  = None
    while(current is not None):
        nextto = current.next
        current.next = prev
        prev = current
        current = nextto
    
    head = prev
    return head

# Complete the compare_lists function below.
def compare_lists(llist1, llist2):
    while((llist1 is not None) and (llist2) is not None):
        if(llist1.data != llist2.data):
            return 0
        
        llist1 = llist1.next
        llist2 = llist2.next
    if(llist1 is None and llist2 is None):
        return 1
    else:
        return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        result = compare_lists(llist1.head, llist2.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()

