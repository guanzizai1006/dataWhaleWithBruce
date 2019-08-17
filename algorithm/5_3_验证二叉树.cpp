// 记录比较结果
    private static boolean res = true;
    // 记录上个节点的值
    private static long max = Long.MIN_VALUE; 

    private  static void test(TreeNode root) {
        if (!res || root == null) return;
        test(root.left);

        if (root.val > max) max = root.val;
        else { res = false; return;}

        test(root.right);
    }


    public static boolean isValidBST(TreeNode root) {
        if (root == null) return true;
        test(root);
        return res;
    }
	
	