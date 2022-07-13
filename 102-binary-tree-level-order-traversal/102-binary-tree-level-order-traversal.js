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
 * @return {number[][]}
 */
var levelOrder = function(root) {
    if(root === null) return [];
  var level = 0;
  var queue = [[ root, level ]];
  
  var mainArray = []
  
  while(queue.length > 0){
    var [current, level] = queue.pop();
    if(mainArray[level]) {
      mainArray[level].push(current.val);
    } else {
      mainArray.push([ current.val ]);
    }
    
    if(current.right !== null) queue.push([current.right, level+1]);
    if(current.left !== null) queue.push([current.left, level+1]);
  }
  
  return mainArray;
};