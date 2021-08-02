package main

import "fmt"

const MaxSize = 4

/*
	Implement following Array interface
	Get, Set, SetAll operations must be dont in constant time
*/
type Array interface {
	Get(int) (int, error)
	Set(int, int) error
	SetAll(int) error
}

var (
	_ Array = &ArrayImpl{}
)

type ArrayImpl struct {
	array           []int
	version         int
	elementVersions []int
	setAllVal       int
}

func NewArrayImpl() *ArrayImpl {
	return &ArrayImpl{
		array:           make([]int, MaxSize),
		elementVersions: make([]int, MaxSize),
		version:         0,
		setAllVal:       0,
	}
}

func (a *ArrayImpl) checkBounds(index int) error {
	if index < 0 || index >= len(a.array) {
		return fmt.Errorf("check bounds")
	}
	return nil
}

func (a *ArrayImpl) Get(index int) (int, error) {
	if err := a.checkBounds(index); err != nil {
		return 0, err
	}
	if a.elementVersions[index] > a.version {
		return a.array[index], nil
	}
	return a.setAllVal, nil
}

func (a *ArrayImpl) Set(index, val int) error {
	if err := a.checkBounds(index); err != nil {
		return err
	}
	a.array[index] = val
	a.elementVersions[index] = a.version + 1
	return nil
}

func (a *ArrayImpl) SetAll(val int) error {
	a.version += 1
	a.setAllVal = val
	return nil
}

func main() {
	array := NewArrayImpl()
	array.Set(1, 2)
	array.Set(1, 3)
	array.SetAll(7)
	fmt.Println(array.Get(1))
	array.Set(1, 5)
	fmt.Println(array.Get(1))
	fmt.Println(array.Get(2))
	array.Set(3, 9)
	fmt.Println(array.Get(3))
	fmt.Println(array.Get(2))
	fmt.Println(array.Get(1))
	array.SetAll(-1)
	fmt.Println(array.Get(3))
	fmt.Println(array.Get(2))
	fmt.Println(array.Get(1))
}
