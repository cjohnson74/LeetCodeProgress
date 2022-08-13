/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {Node} node
 * @return {Node}
 */
var cloneGraph = function(node) {
    var oldToNew = {};
    
    var dfs = (node) => {
        if (node.val in oldToNew) return oldToNew[node.val];
        
        var copy = new Node(node.val);
        oldToNew[node.val] = copy;
        
        for (neighbor of node.neighbors) {
            copy.neighbors.push(dfs(neighbor));
        }
        return copy;
    }

    if (!node) return;
    return dfs(node);
};