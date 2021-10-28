package main

import "fmt"

func mergeSortUtil(a, aux []int, left, right int) {
	if left >= right {
		return
	}
	if left+1 == right && a[left] > a[right] {
		a[right], a[left] = a[left], a[right]
		return
	}
	m := (left + right) / 2
	mergeSortUtil(a, aux, left, m)
	mergeSortUtil(a, aux, m + 1, right)
	first, second := left, m + 1
	i := left
	for first <= m && second <= right {
		if a[first] < a[second] {
			aux[i] = a[first]
			first += 1
		} else {
			aux[i] = a[second]
			second += 1
		}
		i += 1
	}
	for first <= m {
		aux[i] = a[first]
		first += 1
		i += 1
	}
	for second <= right {
		aux[i] = a[second]
		second += 1
		i += 1
	}
	for i := left;i <= right; i++ {
		a[i] = aux[i]
	}
}

func mergeSort(a []int) []int {
	aux := make([]int, len(a), len(a))
	mergeSortUtil(a, aux, 0, len(a) - 1)
	return a
}

func main() {
	fmt.Println(mergeSort([]int{3, 1, 5, 6, 9, 8, 4, 7, 2}))
}
