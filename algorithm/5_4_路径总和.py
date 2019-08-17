/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
        if (root == null) {
            return false;
        }
        return hasPath(root, sum, root.val);
        
    }
    
    public static boolean hasPath(TreeNode root, int sum, int cur) {
        if (root.left == null && root.right == null) {
            if (cur == sum) {
                return true;
            } else {
                return false;
            }
        }
        boolean l = false;
        if (root.left != null) {
            l = hasPath(root.left, sum, cur + root.left.val);
        }
        boolean r = false;
        if (root.right != null) {
            r = hasPath(root.right, sum, cur + root.right.val);
        }
        return l || r;
    }
}
