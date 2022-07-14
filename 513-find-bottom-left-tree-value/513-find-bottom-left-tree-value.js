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
 * @return {number}
 */
var findBottomLeftValue = function(root) {
    var queue = [ root ];
  let current = null;
  
  while(queue.length > 0){
    current = queue.shift();
    if(current.right) queue.push(current.right);
    if(current.left) queue.push(current.left); 
  }
  return current.val;
};