/*
 * Contains notes and implementations of different data structures
 * Start @ main to begin
 */

#include <iostream>

using namespace std;

// Node class to represent nodes of linked lists, utilizing heaps
class Node {
public:
    int data;
    Node *next;

    // default constructor
    Node() {
        data = 0;
        next = NULL;
    }

    // parameterised constructor
    Node(int data) {
        this->data = data;
        this->next = NULL;
    }
};

// class to represent Linked Lists using the Node class above, utilizing heaps
class LinkedList {
    Node *head;

public:
    // default constructor
    LinkedList(){
        head = NULL;
    }

    // function to insert a node at the end of a linked list
    void insertNode(int data) {
        Node *newNode = new Node(data);

        // check if list is empty, if so, assign to head
        if (head == NULL) {
            head = newNode;
            return;
        }

        // if list not empty, traverse and add to end of list
        Node *temp = head;
        while (temp->next != NULL) {    // stopping at last element in the list, not at NULL
            temp = temp->next;
        }
        temp->next = newNode;
    }

    // function to delete a node at an index
    void deleteNode(int index) {

        // if list is empty, can't delete nodes
        if (head == NULL) {
            cout << "List empty" << endl;
            return;
        }

        // if first index, aka head, change head to next
        if (index == 0) {
            Node *temp = head;
            head = head->next;
            delete temp;        // delete node off of the heap
            return;
        }


        // check to see if index is out of range
        if (index >= getLength()) {     // index cant be same or above length, ex. list[3] as last element means there are 4 elements, index has to be length - 1 at max
            cout << "index " << index << " out of range" << endl;
            return;
        } else {    // if index within range
            Node *curr = head;
            Node *prev;
            int count = 0;

            while (count != index) {       // traverse until index is found
                prev = curr;
                curr = curr->next;
                count++;
            }

            prev->next = curr->next;    // once found, set prev node of index to next node of index
            delete curr;    // delete node off of the heap
        }
    }

    // function to print entire linked list
    void printList() {
        Node *temp = head;

        // check to see if linked list is empty
        if (head == NULL) {
            cout << "list empty" << endl;
            return;
        }

        // traverse through linked list
        while (temp != NULL) {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }

    // returns length of linked list
    int getLength() {
        Node *temp = head;
        int length = 0;
        while (temp != NULL) {
            length++;
            temp = temp->next;
        }
        return length;
    }
};


int main() {
    // main will contain the data structures and how they are used
    // data structure implementations/classes are above

    /////////////////////////////////////////////////////////////////////////////////////////////////////////////

    // BACKGROUND INFO, read to get a basic understanding of what data structures are

    /* LINEAR vs N0N-LINEAR data structures
     *
     * linear data structures combine elements to form a specific order
     * examples include arrays, queues, stacks, linked lists
     *
     * non-linear data structures represent data as a hierarchical relationship between elements
     * examples include graphs, family of trees, and table of contents
     */

    /* BUILT-IN vs DERIVED data types
     *
     * built-in data types are "built in" and supported by many programming languages
     * examples are integer, boolean, character, float
     *
     * derived data types are implemented independently within a language, they combine built in data types and associate operations on them
     * examples are arrays, stacks, queues, lists
     *
     */

    /* BASIC OPERATIONS of data structures
     *
     * dependent on the data structure, can choose data structures based on optimization of use case and what each use case will require/use more
     *
     * examples are:
     *      traversing, searching, insertion, deletion, sorting, merging
     *
     */

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    // ARRAYS
    // fixed size sequenced collection of variables of the same data type
    // adjacent memory locations to store values

    // declare array
    int numbers[5];

    // showing operations
    for (int i = 0; i < sizeof(numbers)/sizeof(numbers[0]); i++) {      // traversing, using length of array which == total bytes allocated / data type byte size; ex array size of:: 20 bytes / 4 bytes per int == 5 ints total
        numbers[i] = i + 1;     // updating/inserting
        cout << numbers[i] << " ";  // searching
    }
    cout << endl;

    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    // LINKED LIST
    // linear set of data elements, referred to as nodes
    // each node consists of data and pointer to next node
    // list is dynamic, can be resized

    // typical notation for optimized linked lists
    // insertion == O(1)
    // deletion == O(n)
    // searching == O(n)


    // declare linked list
    LinkedList linkedList;

    // adding values
    for (int i = 0; i < 5; i++){
        linkedList.insertNode(i);
    }

    linkedList.printList();

    // insertion
    linkedList.insertNode(10);
    cout << "after insertion" << endl;
    linkedList.printList();

    // deletion
    linkedList.deleteNode(3);       // testing out of range
    cout << "after deletion" << endl;
    linkedList.printList();

    return 0;
}
