/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var rangeSumBST = function(root, low, high) {
    var sum = 0;
    if (root == null) return sum;
    var stack = [root];
    
    while (stack.length > 0) {
        var currNode = stack.pop();
        
        if (currNode.val >= low && currNode.val <= high) {
            sum += currNode.val;
            console.log(currNode.val)
        }
        
        if (currNode.left != null) stack.push(currNode.left);
        if (currNode.right != null) stack.push(currNode.right);
    }
    
    return sum;
};