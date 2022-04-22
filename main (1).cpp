#include <iostream>

using namespace std;

class Node
{
   public:
    int data;
    Node* next;
    Node(int dData, Node* n)
    {
        data = dData;
        next = n;
    }



};

class Stack
{
   public:
   int _MAXSIZE;
   int _size;
   Node* head;

   Stack(int _max)
   {
    _MAXSIZE = _max;
    head = nullptr;
   }

   bool push(int data)
   {
    if(head == nullptr)
    {
       head = new Node(data , nullptr);
       _size++;
       return true;
    }
    else
    {
         if(_size < _MAXSIZE)
         {
             Node* tmp = new Node(data , head);
             head = tmp;
             _size++;
             return true;
         } else { return false;}

    }
   }

   bool isEmpty()
   {
        if(_size <= 0)
        {
            return true;
        }
        else{
            return false;
        }
   }

   int pop()
   {
        int tmp = head->data;
        head = head->next;
        _size--;
        return tmp;
   }

   int top()
   {
       return head->data;
   }

   int stackSize()
   {
       return _size;
   }

};


int main()
{
    Stack* x = new Stack(10);


    for(int i = 0; i < 10; i++)
    {
        x->push(i*5);
    }


    cout << x->pop() << endl;
    cout << x->isEmpty() << endl;
    cout << x->stackSize() <<endl;

//0xea60f0

}
