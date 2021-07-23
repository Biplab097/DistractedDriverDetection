class Solution {
    
    public TreeNode pruneTree(TreeNode root) {
        return containsOne(root)?root:null;
    }
     
    public boolean containsOne(TreeNode node){
        if(node==null) return false;
        
        boolean left = containsOne(node.left);
        boolean right = containsOne(node.right);
        
        if(left==false) node.left = null;
        if(right==false) node.right = null;
        
        return node.val==1 || left || right;
    }
}
