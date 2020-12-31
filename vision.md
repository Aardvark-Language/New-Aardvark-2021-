## Class Sytax:
```js
class MyClass {
  ~id(what) {
  }
  ~ref() {
  }
  ~oninherit(other) {
  }
  ~init() {
  }
  ~delete() {
  }
  ~iteration() {
  }
  funct this.Method_Name() {
  / Method Body \
  }
}
```
### `~id`
This is called to identify this datatype. It will automaticly be given one argument. This function is meant to take in all possible datatypes and tell whether it is part of this class or not. It defaults to `return False`
### `~ref`
called when an instance of this class if refrenced
### `~oninherit`
called when another class inherits this one
### `~init`
initiates a new instance of the class
### `~delete`
called when an instance of this class is being deleted
### `~iteration`
called when an instance of this class is put through a for loop


## Functions
```
funct Function_Name(Args) {
  /Function Body\
}
```


## Statements
#include /includes a module\
#max-mem / sets the maximum allowed memory to its first arg\
#step /steps through the code telling you where it is and explaining\
#timeout /timeouts the program\


## Keywords
continue /continues in background\
return /returns a value\
timeout /timeouts the code after it\
await /lets this line of code run, but continue to do other stuff while waiting\
delete /deletes a variable\


## Numbers
### `^` is exponet
### `*` is multiply 
### `/` is divide
### `-` is minus
### `+` is plus
### `%` is modulo
`a=0` a is set to 0
`a++` a now = 1
`a--` a now = 0 
`a-=2` a now = -2
`a*=5` a now = -10
`a^=2` a now = 100
`a/=5` a now = 20
`a%=5` a now = 0
`a+=5` a now = 5