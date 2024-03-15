package main

import (
	"fmt"
	"os"
)

// func getCurrentProcessCmd() (string, error) {
// 	pid := os.Getpid()

// 	cmdlineFilePath := filepath.Join("/proc", strconv.Itoa(pid), "cmdline")
// 	cmdlineBytes, err := ioutil.ReadFile(cmdlineFilePath)
// 	if err != nil {
// 		return "", err
// 	}

// 	// return cmdline in string
// 	cmdline := strings.Join(strings.Split(string(cmdlineBytes), "\x00"), " ")
// 	return cmdline, nil
// }

func getCmd() (cmd string) {
	for _, arg := range os.Args {
		cmd += fmt.Sprintf("%s ", arg)
	}
	return cmd
}

func main() {
	cmd := getCmd()
	// cmd2, _ := getCurrentProcessCmd()
	fmt.Printf("%s\n", cmd)
}
