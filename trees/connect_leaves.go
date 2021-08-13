package main

import "fmt"

/*

	type Node struct{
		left   *Node
		right  *Node
		next   *Node
	}

	Given a binary tree.
	Connect all leaf nodes of tree  all together with next pointer,
	nodes should be connected in Top-To-Bottom Left-To-Right fashion

	input tree:

					3

				/		\
						 6
			  4			/  \

			/ 	       5    7
		   2     		  /	   \
		  /				 8	    10
		 1					\
							 9


	output: 5 -> 1 -> 10 -> 9
*/

type Node struct {
	value int
	left  *Node
	right *Node
	next  *Node
}

func isLeaf(node *Node) bool {
	if node == nil {
		return false
	}

	if node.left == nil && node.right == nil {
		return true
	}

	return false
}

func connectLeaves(root *Node) *Node {
	queue := []*Node{root}
	leaves := make([]*Node, 0)

	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		if isLeaf(cur) {
			leaves = append(leaves, cur)
		}
		if cur.left != nil {
			queue = append(queue, cur.left)
		}
		if cur.right != nil {
			queue = append(queue, cur.right)
		}
	}

	for i := 0; i < len(leaves)-1; i++ {
		leaves[i].next = leaves[i+1]
	}
	return leaves[0]
}

func connectLeaves2(root *Node) *Node {
	if isLeaf(root) {
		return nil
	}
	var (
		curLevelStart = root
		result        *Node
		curLeaf       *Node
	)

	for curLevelStart != nil {
		var (
			nextLevelStart *Node
			NextLevelEnd   *Node
		)

		for cur := curLevelStart; cur != nil; cur = cur.next {
			// find out first next level pointer and current next level pointer
			if NextLevelEnd == nil {
				NextLevelEnd = cur.left
			}
			if NextLevelEnd == nil {
				NextLevelEnd = cur.right
			}
			if nextLevelStart == nil {
				nextLevelStart = cur.left
			}
			if nextLevelStart == nil {
				nextLevelStart = cur.right
			}
			if isLeaf(cur) {
				if curLeaf == nil {
					curLeaf = cur
					result = curLeaf
				} else {
					curLeaf.next = cur
					curLeaf = curLeaf.next
				}
			} else {
				if cur.left != nil {
					if cur.left != NextLevelEnd {
						NextLevelEnd.next = cur.left
						NextLevelEnd = NextLevelEnd.next
					}
				}
				if cur.right != nil {
					if cur.right != NextLevelEnd {
						NextLevelEnd.next = cur.right
						NextLevelEnd = NextLevelEnd.next
					}
				}
			}
		}
		curLevelStart = nextLevelStart
	}
	return result
}

func main() {
	node1 := Node{
		value: 1,
	}
	node2 := Node{
		value: 2,
	}
	node3 := Node{
		value: 3,
	}
	node4 := Node{
		value: 4,
	}
	node5 := Node{
		value: 5,
	}
	node6 := Node{
		value: 6,
	}
	node7 := Node{
		value: 7,
	}
	node8 := Node{
		value: 8,
	}
	node9 := Node{
		value: 9,
	}
	node10 := Node{
		value: 10,
	}
	node3.left = &node4
	node4.left = &node2
	node2.left = &node1
	node3.right = &node6
	node6.left = &node5
	node6.right = &node7
	node7.left = &node8
	node8.right = &node9
	node7.right = &node10
	//start := connectLeaves(&node3)
	//for ; start != nil; start = start.next {
	//	fmt.Printf("%d ", start.value)
	//}
	fmt.Println("")
	start := connectLeaves2(&node3)
	for ; start != nil; start = start.next {
		fmt.Printf("%d ", start.value)
	}
	fmt.Println("")
}
