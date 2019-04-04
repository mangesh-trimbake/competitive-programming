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

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')

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
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode
        
def print_singly_linked_list(head,s,fptr):
    printval = head
    while printval is not None:
        
        data = str(printval.dataval)
        print("d=",data)
        fptr.write(data+s)
        printval = printval.nextval



def insertNodeAtPosition(head, data, position):
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # print_singly_linked_list(head," ",fptr)

    NewNode = Node(data)
    if head is None:
        head = NewNode
        return head
    laste = head
    if position==0:
        NewNode.nextval = head
        return head
    p = 0 
    while(laste.nextval and p<position-1):
        # print(laste.dataval)
        laste = laste.nextval
        p = p+1
    # print(p,laste.dataval)
    nextto = laste.nextval
    # print("next",nextto.dataval)
    laste.nextval=NewNode
    NewNode.nextval = nextto
    print_singly_linked_list(head," ",fptr)
    return head


def reversePrint(head):
    fptr = open(os.environ['OUTPUT_PATH'], 'a')
    print("====")
    # print_singly_linked_list(head,"\n",fptr)
    current = head
    nextto = None
    prev  = None
    while(current is not None):
        nextto = current.nextval
        current.nextval = prev
        prev = current
        current = nextto
    
    head = prev
    
    print_singly_linked_list(head,"\n",fptr)

        


if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        reversePrint(llist.head)

