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
 * @return {number[]}
 */
var averageOfLevels = function(root) {
  if(root === null) return [];
  var queue = [{ node: root, levelNum: 0 }]
  var mainArray = [];
  var answer = [];
  
  while(queue.length > 0){
    const { node, levelNum } = queue.shift();
    if(mainArray.length === levelNum){
      mainArray.push([node.val]);
    } else {
      mainArray[levelNum].push(node.val);
    }
    
    if(node.left !== null) queue.push({ node: node.left, levelNum: levelNum+1 });
    if(node.right !== null) queue.push({ node: node.right, levelNum: levelNum+1 })
  }
  
  for(let level of mainArray){
    answer.push(averageLevel(level));
  }
  return answer;
};

const averageLevel = (level) => {
  var sum = 0;
  var divisor = level.length;
  for(let num of level){
    sum += num;
  }
  return sum / divisor;
};