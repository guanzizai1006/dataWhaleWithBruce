int minDepth(TreeNode * root)
    {
        if(root == NULL)
            return 0;
        if(root->left == NULL && root->right == NULL)
            return 1;
        int left = minDepth(root->left) + 1;
        int right = minDepth(root->right) + 1;
        if(left == 1)          //等于1说明没有左子树有右子树，为避免干扰结果，另其为一个最大数
            left = INT_MAX;
        if(right == 1)         //等于1说明没有右子树有左子树，为避免干扰结果，另其为一个最大数
            right = INT_MAX;
        return left > right ? right : left;    //返回二者之中较小数
    }
	