// import java.util.Stack;
// public class usingpackage {
//     public static void main(String[] args) {
//         Stack<Integer> stack = new Stack<>();
//         stack.push(819);
//         stack.push(688);
//         stack.push(989);
//         // Display the stack
//         System.out.println("Stack: " + stack);
//         // peek the top element
//         System.out.println("Top element: " + stack.peek());
//         // pop the top element
//         System.out.println("Popped element: " + stack.pop());
//         // Display the stack after pop
//         System.out.println("Stack after pop: " + stack);
//         //to check if stack is empty
//         System.out.println("Is stack empty? " + stack.isEmpty());
//         //search for an element
//         System.out.println("Search for 688: " + stack.search(688));
//     }
// }

import java.util.Stack;

public class usingpackage {
    public static boolean isBalanced(String input) {
        Stack<Character> stack = new Stack<>();
        for (char c : input.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else if (c == ')' || c == '}' || c == ']') {
                if (stack.isEmpty()) {
                    return false;
                }
                char top = stack.peek();
                if ((c == ')' && top == '(') || (c == '}' && top == '{') || (c == ']' && top == '[')) {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
    
    public static void main(String[] args) {
        String input = "((()))";
        System.out.println(isBalanced(input));  // Output: true
    }
}
class stacknode{
    int data;
    stacknode next;
    stacknode(int data){
        this.data=data;
        this.next=null;
    }
}
class mystack{
    stacknode top;
    mystack(){
        this.top=null;
    }
    void push(int data){
        stacknode newnode=new stacknode(data);
        if(top==null){
            top=newnode;
        }else{
            newnode.next=top;
            top=newnode;
        }
    }
    int pop(){
        if(top==null){
            System.out.println("Stack is empty");
            return -1;
        }else{
            int popped=top.data;
            top=top.next;
            return popped;
        }
    }
    int peek(){
        if(top==null){
            System.out.println("Stack is empty");
            return -1;
        }else{
            return top.data;
        }
    }
    boolean isEmpty(){
        return top==null;
    }

    
}