/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
    //func to detech the loop
    bool if_loop(ListNode * head , ListNode * &slow , ListNode * &fast){


        while(fast != NULL && fast -> next != NULL){
            slow = slow -> next;
            fast = fast -> next -> next;
            if(slow == fast) return true;
        }
        return false;
    }
public:
    ListNode *detectCycle(ListNode *head) {
        if((head == NULL) || (head -> next == NULL)) return NULL;
        
        ListNode * slow = head;
        ListNode * fast = head;

        bool ans = if_loop(head , slow , fast);
        if(ans == false) return NULL;

        //getting the starting point
        ListNode * temp = head;
        while(temp != slow){
            temp = temp -> next;
            slow = slow -> next;
        }
        return slow;
        


        
    }
};