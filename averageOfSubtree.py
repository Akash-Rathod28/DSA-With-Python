class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        matching_nodes_count = 0

        def post_order(node):
            nonlocal matching_nodes_count
            if not node:
                return 0, 0

            left_sum, left_count = post_order(node.left)
            right_sum, right_count = post_order(node.right)

            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count

            if total_sum // total_count == node.val:
                matching_nodes_count += 1

            return total_sum, total_count

        post_order(root)
        return matching_nodes_count
