package main

import (
	"fmt"
	"sync"
)

var lock = &sync.Mutex{}

type singleton struct{}

var singletonInstance *singleton

func getSingletonInstance() *singleton {
	lock.Lock()
	defer lock.Unlock()

	if singletonInstance == nil {
		singletonInstance = &singleton{}
	}
	return singletonInstance
}

func main() {
	singleton1 := getSingletonInstance()
	singleton2 := getSingletonInstance()
	fmt.Printf("singleton1 pointer: %p\nsingleton2 pointer: %p\n", singleton1, singleton2)
}
