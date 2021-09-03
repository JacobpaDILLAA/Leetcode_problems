def merge(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    start = None
    if l1.val < l2.val:
        start = l1
        start.next = merge(l1.next, l2)
    else:
        start = l2
        start.next = merge(l1, l2.next)
    return start


def two_sum(target, nums):
    if len(nums) < 2:
        pass
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] - target is nums[j]:
                return [i, j]


def max_depth(root):
    if root is None:
        return -1
    left = max_depth(root.left)
    right = max_depth(root.right)
    return max(left, right) + 1


def cycle(head):
    if head is None or head.next is None:
        return False
    slow = head
    fast = head.next

    while slow is not fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next

    return True


def reverse(head):
    if head is None:
        return None
    prev = None
    cur = head
    while cur is not None:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev


def invert(root):
    if root is None:
        return None
    left = invert(root.left)
    right = invert(root.right)
    left.root = right
    right.root = left

    return root


def symmetric(root):
    if root is None:
        return True
    left = symmetric(root.left)
    right = symmetric(root.right)
    if left.val is not right.val:
        return False
    return True


def merge_tree(t1, t2):
    if not t1:
        return t2
    if not t2:
        return t1

    t1.val += t2.val

    t1.left = merge_tree(t1.left, t2.left)
    t1.right = merge_tree(t1.right, t2.right)
    return t1


def intersection(h1, h2):
    myset = set()
    while h1:
        myset.add(h1)
        h1 = h1.next
    while h2:
        if h2 in myset:
            return h2
        h2 = h2.next
    return None


def zeros(nums):
    i = count = 0
    while count < len(nums):
        if nums[i] == 0:
            nums.append(nums.pop(i))
        else:
            i += 1
        count += 1
    return nums


def single_num(nums):
    mylist = []
    for num in nums:
        if num not in mylist:
            mylist.append(num)
        else:
            mylist.remove(num)
    return mylist.pop()


def valid(s):
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] is not top:
                return False
        else:
            stack.append(char)
    return not stack


def Min_path(grid):
    m = len(grid)
    n = len(grid[0])

    for i in range(1, m):
        grid[i][0] += grid[i-1][0]

    for j in range(1, n):
        grid[0][j] += grid[0][j-1]

    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])

    return grid[-1][-1]


def two_num(l1, l2):
    temp = cur = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        cur.next = ListNode(carry % 10)
        cur = cur.next
        carry //= 10
    return temp.next


def rob(nums):
    last, now = 0,0
    for num in nums:
        last, now = now, max(last + num, now)
    return now


def num(l1, l2):
    temp = cur = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += 1
            l1 = l1.next
        if l2:
            carry += 1
            l2 = l2.next
        cur.next = ListNode(carry % 10)
        