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
  var levels = [];
  fillLevels(root, levels, 0);
  
  var averages = [];
  for(let level of levels){
    averages.push(avg(level));
  }
  return averages;
}

const fillLevels = (node, levels, levelNum) => {
  if(node === null) return [];
  
  if(levels.length === levelNum){
    levels[levelNum] = [node.val];
  } else {
    levels[levelNum].push(node.val);
  }
  
  fillLevels(node.left, levels, levelNum+1);
  fillLevels(node.right, levels, levelNum+1);
}

const avg = (level) => {
  var average = 0;
  for(let num of level){
    average += num
  }
  return average / level.length;
};